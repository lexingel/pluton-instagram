"""Claude sabah görevi: o günün PNG'lerini JPEG'e çevirir, manifest ile birlikte GitHub'a yükler.
Kullanım: python3 push_day.py <YYYY-MM-DD> <posts.json>
posts.json: [{"png": "/mnt/.../x.png", "file": "1-sabah.jpg", "caption": "...", "time": "08:00"}, ...]
Ortam: GH_PAT (yalnızca bu depoya yazma izinli anahtar), GH_REPO (kullanıcı/depo)
"""
import base64, io, json, os, sys, urllib.request
from PIL import Image

day, spec = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
repo, tok = os.environ["GH_REPO"], os.environ["GH_PAT"]

def put(path, data: bytes, msg):
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    h = {"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"}
    sha = None
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=h)) as r:
            sha = json.load(r)["sha"]
    except urllib.error.HTTPError as e:
        if e.code != 404: raise
    body = {"message": msg, "content": base64.b64encode(data).decode()}
    if sha: body["sha"] = sha
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=h, method="PUT")
    with urllib.request.urlopen(req) as r:
        print("yüklendi:", path, r.status)

manifest = []
for p in spec:
    buf = io.BytesIO()
    Image.open(p["png"]).convert("RGB").save(buf, "JPEG", quality=92, optimize=True)
    put(f"posts/{day}/{p['file']}", buf.getvalue(), f"{day} {p['file']}")
    manifest.append({"file": p["file"], "caption": p["caption"],
                     "publish_at": f"{day}T{p['time']}:00+03:00", "status": "pending"})
# manifest en son yüklenir ki yayıncı eksik görsel görmesin
put(f"posts/{day}/manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2).encode(), f"{day} manifest")
