# Plüton PDRM – Günlük Instagram postları (rutin talimatı)

You are preparing today's Instagram posts (images + captions) for Plüton PDRM, a psychological counseling & guidance center (Plüton Psikolojik Danışmanlık ve Rehberlik Merkezi) in Narlıdere, İzmir, Türkiye: 3 daily posts, plus a 4th "özel gün" post on special days. You then upload them to this repository (`lexingel/pluton-instagram`), from which a GitHub Actions workflow publishes them to Instagram at their scheduled times. Work unattended: never ask questions, make reasonable choices. All post content is in Turkish.

## 0. Setup (every run)
- Work in a scratch folder, e.g. `/tmp/posts`. Keep this repository clean except for what `scripts/push_day.py` adds.
- Fonts: `mkdir -p ~/.fonts && cp fonts/*.ttf ~/.fonts/ && fc-cache -f` (the repo ships Lora and Poppins; Google Fonts/CDNs may be blocked).
- Rendering library: `scripts/pluton.py` (do not modify its THEMES). Use it via `sys.path.insert(0, "<repo>/scripts"); import pluton`.
- Playwright: use Python Playwright with the preinstalled Chromium if present (`PLAYWRIGHT_BROWSERS_PATH` / `/opt/pw-browsers`); if `playwright` is missing, `pip install playwright` (add `--break-system-packages` if pip requires it). Only if no Chromium exists at all, try `python -m playwright install chromium`. If rendering is impossible, stop and report the error in the summary email (step 6).
- Pillow is needed for JPEG conversion (`pip install pillow` if missing).

## 1. The 3 daily posts
1. SABAH – "Günaydın" post: warm, short good-morning message for parents/families + one small practical suggestion for the day.
2. ÖĞLEN – informative post (topic area chosen by rotation below).
3. AKŞAM – informative post (a different topic area and a different angle from the noon post).

## 2. Topic rotation (so posts don't repeat)
Compute N = today's day-of-year (Europe/Istanbul date).
Noon topic area = AREAS[N mod 16], evening topic area = AREAS[(N + 7) mod 16]:
AREAS = [DEHB, Kaygı/Anksiyete, Disleksi, Öğrenme güçlüğü, Sınav kaygısı, Sınav başarısı & çalışma alışkanlıkları, Kariyer planlama (ergen/genç), Spor psikolojisi, Gelişim takibi & testler, Okul öncesi dönem gelişimi, Akran uyumu & sosyal beceriler, Ekran bağımlılığı & dijital denge, Akran zorbalığı, Aile iletişimi & ebeveynlik, Ergenlik dönemi, Duygu düzenleme & öfke]
Evening post angle rotates by weekday: Mon/Thu = pratik ebeveyn ipuçları; Tue/Fri = güncel gelişme (do a quick web search for recent Turkish/international news or research on the topic from the last few months, and base the post on it; cite sources in the summary email, not in the caption); Wed/Sat = mit mi gerçek mi / sık sorulan soru; Sun = merkez tanıtımı (gently introduce a related Plüton service, workshop, or the "Okullar İçin" school program — informative, not salesy).
The noon post is always an informative "what to know / signs / what to do" style post on its area.

## 3. ÖZEL GÜNLER – 4th post on special days
Check today's Europe/Istanbul date against the lists below. If it matches, ALSO produce a 4th post. At most one özel gün post per day; if two match, choose the higher priority (resmi/milli > dini bayram > okul > farkındalık).

Fixed every year (MM-DD):
- 01-01 Yeni Yıl (umut, yeni başlangıçlar)
- 03-08 Dünya Kadınlar Günü
- 03-18 Çanakkale Zaferi ve Şehitleri Anma Günü — SOLEMN
- 03-20 Dünya Mutluluk Günü
- 03-21 Dünya Down Sendromu Günü (farkındalık, kapsayıcılık)
- 04-02 Dünya Otizm Farkındalık Günü
- 04-07 Dünya Sağlık Günü
- 04-23 Ulusal Egemenlik ve Çocuk Bayramı
- 05-01 Emek ve Dayanışma Günü (short, neutral)
- 05-15 Dünya Aileler Günü
- 05-19 Atatürk'ü Anma, Gençlik ve Spor Bayramı
- 07-15 Demokrasi ve Milli Birlik Günü — SOLEMN (neutral, respectful)
- 08-12 Uluslararası Gençlik Günü
- 08-30 Zafer Bayramı
- 10-10 Dünya Ruh Sağlığı Günü
- 10-11 Dünya Kız Çocukları Günü
- 10-29 Cumhuriyet Bayramı
- 11-10 Atatürk'ü Anma Günü — SOLEMN (time 09:05)
- 11-20 Dünya Çocuk Hakları Günü
- 11-24 Öğretmenler Günü
- 12-03 Dünya Engelliler Günü

Movable (compute or verify):
- Anneler Günü = 2nd Sunday of May; Babalar Günü = 3rd Sunday of June.
- Okulda Şiddet ve Zorbalıkla Mücadele Uluslararası Günü (UNESCO) = 1st Thursday of November.
- Ramazan Bayramı & Kurban Bayramı: post on the FIRST bayram day only. Known: Ramazan Bayramı 1. gün 2027-03-09; Kurban Bayramı 1. gün 2027-05-16. For later years, search Diyanet dates (when the date is not listed here and today is within ~2 weeks of the expected period).
- Karne günleri (MEB 2026–2027): 1. dönem sonu 2027-01-22; ders yılı sonu 2027-06-25 (supportive message: karne bir değerlendirme, çocuğun değeri değil). For later school years, search the MEB çalışma takvimi.
- Okulların ilk günü (2027–2028 and later): search the MEB takvimi when in late August/September.
- LGS and YKS: if it is June, search the official exam dates; on the day BEFORE each exam add an encouraging "sınava bir gün kala" post (calm, no pressure).

Özel gün post rules:
- Image: `pluton.build_special(content, theme)`; for SOLEMN days `pluton.build_special(content, theme, solemn=True)`. content keys: kicker (date in caps, e.g. "29 EKİM"), h1, h2, icon, msg (2–3 short lines; use <br> to balance), sign (e.g. "Plüton PDRM ailesi olarak" / for solemn days just "Plüton PDRM"). For milli/resmi days use `pluton.FLAG` as the icon (never hand-draw the flag). Otherwise draw a simple original icon (heart, star, sun, balloons, book, apple, puzzle piece for otizm, etc.) colored with classes i1..i4/s1..s4. Never depict Atatürk or any real person — text and flag only.
- Caption: 40–80 words, warm and sincere; for solemn days respectful, calm, no celebratory emojis (🇹🇷 is fine). Connect gently to children/families/well-being when natural. Same content rules as below.
- On SOLEMN days keep the SABAH günaydın post calm and low-key (no celebratory wording/emojis).
- Time: 10:00 (milli bayramlar & dini bayramlar), 09:05 (10 Kasım), 10:30 otherwise.

## 4. Caption tone: "samimi giriş + bilgilendirici gövde"
Open with a warm, relatable line or question a parent would ask; then clear, expert-voiced information; measured emojis (🌿 💛 🔹 style, not excessive); bullet items with 🔹. Reference example (DEHB):
"""
🌿 Yaramazlık değil, farklı işleyen bir dikkat.

"Neden bir türlü yerinde duramıyor?" diye düşündüğünüz oluyor mu? DEHB, çocuğun dikkat ve hareket düzenlemesini etkileyen nörogelişimsel bir durumdur.

Dikkat edilebilecek işaretler:
🔹 Dikkati sürdürmekte güçlük
🔹 Yerinde duramama
🔹 Sırasını beklemekte zorlanma

Bu işaretler tek başına tanı anlamına gelmez; uzman değerlendirmesi yol gösterir. Sorularınız için bize mesaj atabilirsiniz. 💛

#dehb #çocukgelişimi #dikkateksikliği #ebeveynlik #plütonpdrm
📲 @plutonpdrm | @plutongelisimmerkezi_
"""
Caption length: günaydın ~40–70 words; informative ~80–150 words. Every caption must stay under 2,000 characters (Instagram limit 2,200).

## Content rules (strict)
- NEVER use the words "terapi" or "oyun grubu" anywhere (image or caption).
- No links in captions and no references to blog posts or "linkteki yazı" — each post must stand alone.
- Max 5 hashtags per caption (Instagram limit); always include #plütonpdrm.
- End each caption with: 📲 @plutonpdrm | @plutongelisimmerkezi_
- No invented statistics or numbers; only cite widely established guidance (e.g., WHO) or facts you verified via search. Soft, non-alarmist; "signs don't always mean a problem, expert evaluation helps" framing where relevant. No diagnoses, no medical claims.
- No photos or drawings of real people or known characters; simple original illustrations only (shapes, sun, stars, plants, hearts, icons).

## 5. Image production — weekly theme rotation
- 1080×1350 PNG, rendered with `scripts/pluton.py`: `theme = pluton.theme_for(<today's Europe/Istanbul date>)`.
  - SABAH: `pluton.build(content, "soft", theme)`
  - ÖĞLEN: `pluton.build(content, "bold", theme)`
  - AKŞAM: `pluton.build(content, "bold", theme, evening=True)`
  - ÖZEL GÜN: `pluton.build_special(content, theme[, solemn=True])`
  - Render: `asyncio.run(pluton.render([(png_path, html), ...]))`
- content dict keys (daily posts): kicker (small letter-spaced label, e.g. "GÜNAYDIN", "BİLGİ · DEHB", "EBEVEYN İPUCU · SPOR PSİKOLOJİSİ", "MİT Mİ GERÇEK Mİ?", "GÜNCEL · …", "PLÜTON'DAN · …"), h1 (short headline line 1), h2 (accent line 2), icon (inline SVG ~230×230), items (up to 3 tuples (title, short subline or "")), tipl (tip box label, e.g. "BUGÜNÜN ÖNERİSİ" / "UNUTMAYIN" / "BU AKŞAM"), tipt (tip text; use <br> to balance two lines).
- Icons: draw a fresh, simple, original inline SVG per post — different for noon vs evening. Color icon parts ONLY via classes i1..i4 (fill) and s1..s4 (stroke, fill none); plain #fff is fine for small details. Give each icon svg a viewBox.
- Do not change THEMES. Per post you may adjust wording/length, <br> breaks, or add small inline style tweaks to fix layout problems.
- After rendering, view each PNG and fix overflow, overlap (decor shapes must not cover text or the footer), cut-off text, large empty areas, orphan single-word lines, or broken Turkish characters, then re-render.

## 6. Upload for automatic publishing + summary
1. Write a spec JSON, e.g. `/tmp/posts/spec.json`:
   `[{"png": "/tmp/posts/1.png", "file": "1-sabah-gunaydin.jpg", "caption": "...", "time": "08:00"}, {"png": ..., "file": "2-oglen-<konu-slug>.jpg", "time": "12:30"}, {"png": ..., "file": "3-aksam-<konu-slug>.jpg", "time": "19:30"}]` (+ the özel gün post with its time and file `4-ozel-<slug>.jpg`). Use ASCII slugs.
2. Run `python3 scripts/push_day.py <YYYY-MM-DD> /tmp/posts/spec.json` from the repo root. It converts to JPEG, writes `posts/<date>/manifest.json` and pushes directly to `main` (the publisher only reads `main`; do NOT use a claude/ branch or open a PR for this). If it fails, retry once; if it still fails, report it in the summary.
3. Summary email: if the Gmail connector is available, send ONE email to semihnazli@gmail.com, subject `Plüton – <tarih> postları`, plain-text body in Turkish:
   - first line: whether upload succeeded and that posts will publish automatically at their times; if it's a special day, say so at the top;
   - this week's theme name;
   - each post: topic, time, and the full caption;
   - how to cancel a post: in GitHub `posts/<tarih>/manifest.json`, change that post's `"status": "pending"` to `"status": "cancelled"`;
   - a "Kaynaklar" list for any web sources used.
   Do not attach images (they are visible in the repository under `posts/<tarih>/`).
4. End the session with the same summary as your final message.
