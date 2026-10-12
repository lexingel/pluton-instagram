"""Plüton PDRM – Instagram otomatik yayıncı (GitHub Actions içinde çalışır).

posts/<YYYY-MM-DD>/manifest.json dosyalarını okur; saati gelmiş ve
"pending" durumdaki postları Instagram API ile yayınlar, durumu manifest'e yazar.

Ortam değişkenleri (GitHub Secrets / workflow):
  IG_USER_ID   – Instagram profesyonel hesap ID'si
  IG_TOKEN     – erişim anahtarı
  API_HOST     – graph.instagram.com (Instagram girişi) veya graph.facebook.com (Facebook sayfası girişi)
  BASE_URL     – görsellerin herkese açık kök adresi (ör. https://raw.githubusercontent.com/<kullanıcı>/<repo>/main)
  MAX_LATE_MIN – saatinden bu kadar dakika geç kalan post atlanır (varsayılan 180)
"""
import datetime as dt, glob, json, os, sys, time, urllib.parse, urllib.request

API = os.environ.get("API_HOST", "graph.facebook.com")
VER = os.environ.get("API_VERSION", "v21.0")
UID, TOKEN = os.environ["IG_USER_ID"], os.environ["IG_TOKEN"]
BASE = os.environ["BASE_URL"].rstrip("/")
MAX_LATE = dt.timedelta(minutes=int(os.environ.get("MAX_LATE_MIN", "180")))
DRY = os.environ.get("DRY_RUN") == "1"


def call(method, path, **params):
    params["access_token"] = TOKEN
    url = f"https://{API}/{VER}/{path}"
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(url + "?" + data.decode())
    else:
        req = urllib.request.Request(url, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{e.code} {e.read().decode()[:500]}")


def publish(image_url, caption):
    c = call("POST", f"{UID}/media", image_url=image_url, caption=caption)
    cid = c["id"]
    for _ in range(20):  # konteyner hazır olana kadar bekle
        s = call("GET", cid, fields="status_code").get("status_code")
        if s == "FINISHED":
            break
        if s == "ERROR":
            raise RuntimeError(f"konteyner hatası: {cid}")
        time.sleep(5)
    return call("POST", f"{UID}/media_publish", creation_id=cid)["id"]


def main():
    now = dt.datetime.now(dt.timezone.utc)
    changed, failed = False, False
    for mf in sorted(glob.glob("posts/*/manifest.json")):
        posts = json.load(open(mf, encoding="utf-8"))
        folder = os.path.dirname(mf)
        for p in posts:
            if p.get("status") != "pending":
                continue
            at = dt.datetime.fromisoformat(p["publish_at"])
            if at > now:
                continue
            if now - at > MAX_LATE:
                p["status"] = "skipped_late"; changed = True
                print(f"ATLANDI (geç): {mf} {p['file']}"); continue
            url = f"{BASE}/{folder}/{urllib.parse.quote(p['file'])}"
            print(f"YAYINLANIYOR: {url}")
            if DRY:
                continue
            try:
                p["media_id"] = publish(url, p["caption"])
                p["status"] = "published"
                p["published_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
                print("  OK", p["media_id"])
            except Exception as e:
                p["error"] = str(e)[:500]; p["attempts"] = p.get("attempts", 0) + 1
                if p["attempts"] >= 3:
                    p["status"] = "failed"
                print("  HATA", e); failed = True
            changed = True
        if changed:
            json.dump(posts, open(mf, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
