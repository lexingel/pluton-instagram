"""Claude sabah görevi: o günün PNG'lerini JPEG'e çevirir, manifest ile birlikte GitHub'a (git push) yükler.

Kullanım: python3 push_day.py <YYYY-MM-DD> <posts.json>
posts.json: [{"png": "/yol/x.png", "file": "1-sabah.jpg", "caption": "...", "time": "08:00"}, ...]
Ortam: GH_PAT (yalnızca bu depoya yazma izinli anahtar), GH_REPO (kullanıcı/depo)
Not: Claude ortamında GitHub REST API kapalı; git üzerinden yüklenir.
"""
import json, os, subprocess, sys, tempfile
from PIL import Image

day, spec = sys.argv[1], json.load(open(sys.argv[2], encoding="utf-8"))
repo, tok = os.environ["GH_REPO"], os.environ["GH_PAT"]
url = f"https://x-access-token:{tok}@github.com/{repo}.git"
work = tempfile.mkdtemp()

def git(*a):
    r = subprocess.run(["git", "-C", work, *a], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit((r.stdout + r.stderr).replace(tok, "***"))
    return r.stdout

subprocess.run(["git", "clone", "-q", "--depth", "1", url, work], check=True, capture_output=True)
git("config", "user.name", "Claude (Plüton)"); git("config", "user.email", "claude@users.noreply.github.com")
folder = os.path.join(work, "posts", day); os.makedirs(folder, exist_ok=True)
manifest = []
for p in spec:
    Image.open(p["png"]).convert("RGB").save(os.path.join(folder, p["file"]), "JPEG", quality=92, optimize=True)
    manifest.append({"file": p["file"], "caption": p["caption"],
                     "publish_at": f"{day}T{p['time']}:00+03:00", "status": "pending"})
json.dump(manifest, open(os.path.join(folder, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
git("add", "posts")
git("commit", "-q", "-m", f"{day} postları")
for i in range(3):  # yayıncı aynı anda durum yazmışsa yeniden dene
    try:
        git("push", "-q", "origin", "HEAD:main"); break
    except SystemExit as e:
        if i == 2 or "403" in str(e) or "denied" in str(e):
            raise
        git("pull", "-q", "--rebase", "origin", "main")
print("yüklendi:", f"posts/{day}", [m["file"] for m in manifest])
