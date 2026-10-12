# Plüton PDRM – haftalık tema motoru
import datetime, asyncio

FOOT = "@plutonpdrm · @plutongelisimmerkezi_ · plutonpdrm.com.tr"

# Her tema: soft (SABAH) + bold (ÖĞLEN/AKŞAM) paleti, yerleşim ve dekor.
THEMES = [
 dict(name="Pastel & Petrol", layout="classic", decor="circles",
  soft=dict(bg="#FBF4EA",tx="#33404A",sub="#6B7780",kick="#7FA38E",acc="#D98C6C",d1="#DDE9E0",d2="#F8E1D2",row="#FFFFFF",dot="#DDE9E0",dotx="#33404A",tip="#FFFFFF",tipx="#33404A",tipl="#D98C6C",bar="#F4B393",foot="#7A868F",i=["#F4B393","#F2C9B2","#7FA38E","#DDE9E0"],hf="Lora",h2i=True),
  bold=dict(bg="#1F5E5B",tx="#FFFFFF",sub="#CFE5E2",kick="#FFD166",acc="#FFD166",d1="#27716D",d2="#FF8A65",row="rgba(255,255,255,.12)",dot="#FF8A65",dotx="#FFFFFF",tip="#FFD166",tipx="#1F5E5B",tip2="#FF8A65",tipx2="#FFFFFF",foot="#CFE5E2",i=["#FFD166","#FF8A65","#FFFFFF","#27716D"],hf="Poppins",h2i=False)),
 dict(name="Lavanta & Mürdüm", layout="centered", decor="blobs",
  soft=dict(bg="#F4EFF9",tx="#3B3355",sub="#6E6688",kick="#8E6CC2",acc="#8E6CC2",d1="#E4D9F3",d2="#FCE1EA",row="#FFFFFF",dot="#E4D9F3",dotx="#3B3355",tip="#FFFFFF",tipx="#3B3355",tipl="#C2678E",bar="#F2A7C3",foot="#7D7598",i=["#B79CE0","#F2A7C3","#8E6CC2","#E4D9F3"],hf="Lora",h2i=True),
  bold=dict(bg="#3B2F5C",tx="#FFFFFF",sub="#D9D2EC",kick="#9FE0D0",acc="#FFB4A2",d1="#4A3C72",d2="#9FE0D0",row="rgba(255,255,255,.10)",dot="#9FE0D0",dotx="#3B2F5C",tip="#FFB4A2",tipx="#3B2F5C",tip2="#9FE0D0",tipx2="#3B2F5C",foot="#CFC7E6",i=["#FFB4A2","#9FE0D0","#FFFFFF","#4A3C72"],hf="Lora",h2i=True)),
 dict(name="Gün Batımı & Lacivert", layout="side", decor="rings",
  soft=dict(bg="#FFF2E8",tx="#2E4057",sub="#5E6C7E",kick="#E07A5F",acc="#E07A5F",d1="#FAD7C0",d2="#DCE8DF",row="#FFFFFF",dot="#FAD7C0",dotx="#2E4057",tip="#2E4057",tipx="#FFFFFF",tipl="#F6BD60",bar="#E07A5F",foot="#6F7C8C",i=["#E07A5F","#F6BD60","#2E4057","#FAD7C0"],hf="Poppins",h2i=False),
  bold=dict(bg="#C8553D",tx="#FFFFFF",sub="#FBE3D9",kick="#FFE5A0",acc="#FFE5A0",d1="#D4694F",d2="#2E4057",row="rgba(255,255,255,.15)",dot="#2E4057",dotx="#FFFFFF",tip="#2E4057",tipx="#FFFFFF",tip2="#FFE5A0",tipx2="#2E4057",foot="#FBE3D9",i=["#FFE5A0","#2E4057","#FFFFFF","#D4694F"],hf="Poppins",h2i=False)),
 dict(name="Okyanus & Limon", layout="framed", decor="dots",
  soft=dict(bg="#EDF5FB",tx="#22394D",sub="#55697B",kick="#3A86C8",acc="#3A86C8",d1="#D3E7F5",d2="#FFF1BF",row="#FFFFFF",dot="#FFF1BF",dotx="#22394D",tip="#FFF1BF",tipx="#22394D",tipl="#3A86C8",bar="#F4D35E",foot="#5E7385",i=["#3A86C8","#F4D35E","#8CC4EA","#D3E7F5"],hf="Lora",h2i=True),
  bold=dict(bg="#1D3557",tx="#FFFFFF",sub="#C9D8EA",kick="#4CC9F0",acc="#F4D35E",d1="#274472",d2="#4CC9F0",row="rgba(255,255,255,.10)",dot="#4CC9F0",dotx="#1D3557",tip="#F4D35E",tipx="#1D3557",tip2="#4CC9F0",tipx2="#1D3557",foot="#C9D8EA",i=["#F4D35E","#4CC9F0","#FFFFFF","#274472"],hf="Poppins",h2i=False)),
 dict(name="Orman & Hardal", layout="lines", decor="leaves",
  soft=dict(bg="#F5F1E6",tx="#2F3A2F",sub="#5E6A5B",kick="#6B8F47",acc="#B5832A",d1="#E2E9D4",d2="#F3DDB3",row="transparent",dot="#6B8F47",dotx="#FFFFFF",tip="#E2E9D4",tipx="#2F3A2F",tipl="#6B8F47",bar="#B5832A",foot="#6E7766",i=["#6B8F47","#E9B949","#A7C28A","#E2E9D4"],hf="Lora",h2i=True),
  bold=dict(bg="#2F4A3A",tx="#FFFFFF",sub="#D3DFD3",kick="#E9B949",acc="#E9B949",d1="#3A5A47",d2="#E9B949",row="transparent",dot="#E9B949",dotx="#2F4A3A",tip="#F2E8CF",tipx="#2F4A3A",tip2="#E9B949",tipx2="#2F4A3A",foot="#C9D6CB",i=["#E9B949","#A7C28A","#F2E8CF","#3A5A47"],hf="Poppins",h2i=False)),
 dict(name="Gül & Bordo", layout="pill", decor="waves",
  soft=dict(bg="#FDF1F0",tx="#4A2E35",sub="#7A5E64",kick="#C55A72",acc="#C55A72",d1="#F7D5DB",d2="#E3ECF4",row="#FFFFFF",dot="#F7D5DB",dotx="#4A2E35",tip="#FFFFFF",tipx="#4A2E35",tipl="#C55A72",bar="#F2A1B0",foot="#8A6E74",i=["#F2A1B0","#C55A72","#9DB8D2","#F7D5DB"],hf="Lora",h2i=True),
  bold=dict(bg="#7A2E45",tx="#FFFFFF",sub="#F3D9DF",kick="#FFC9B9",acc="#FFC9B9",d1="#8C3A53",d2="#F6A6B2",row="rgba(255,255,255,.12)",dot="#FFC9B9",dotx="#7A2E45",tip="#FFC9B9",tipx="#7A2E45",tip2="#F6A6B2",tipx2="#4A1E2C",foot="#F3D9DF",i=["#FFC9B9","#F6A6B2","#FFFFFF","#8C3A53"],hf="Poppins",h2i=False)),
]

def theme_for(date: datetime.date):
    # 5 Ekim 2026 haftası (ISO 41) = tema 1 (Lavanta & Mürdüm); her pazartesi bir sonrakine geçer.
    y, w, _ = date.isocalendar()
    weeks = (datetime.date.fromisocalendar(y, w, 1) - datetime.date(2026, 10, 5)).days // 7
    return THEMES[(weeks + 1) % len(THEMES)]

def _decor(kind, p):
    d1, d2 = p["d1"], p["d2"]
    if kind == "circles":
        return f'<div class="dc" style="background:{d1};width:640px;height:640px;top:-220px;right:-240px;border-radius:50%"></div><div class="dc" style="background:{d2};width:300px;height:300px;bottom:-150px;right:-120px;border-radius:50%"></div>'
    if kind == "blobs":
        return f'<div class="dc" style="background:{d1};width:620px;height:560px;top:-240px;left:-180px;border-radius:58% 42% 63% 37%/45% 55% 45% 55%"></div><div class="dc" style="background:{d2};width:360px;height:320px;bottom:-190px;right:-200px;border-radius:40% 60% 35% 65%/55% 40% 60% 45%;opacity:.9"></div>'
    if kind == "rings":
        return f'<svg class="dc" style="top:-260px;right:-260px" width="720" height="720"><circle cx="360" cy="360" r="340" fill="{d1}"/><circle cx="360" cy="360" r="250" fill="none" stroke="{d2}" stroke-width="18" opacity=".7"/><circle cx="360" cy="360" r="160" fill="none" stroke="{d2}" stroke-width="18" opacity=".5"/></svg><svg class="dc" style="bottom:-140px;right:-140px" width="300" height="300"><circle cx="150" cy="150" r="140" fill="none" stroke="{d2}" stroke-width="22"/></svg>'
    if kind == "dots":
        dots = "".join(f'<circle cx="{x*34+10}" cy="{y*34+10}" r="5" fill="{d2}"/>' for x in range(6) for y in range(4))
        return f'<div class="dc" style="background:{d1};width:560px;height:560px;top:-230px;right:-200px;border-radius:50%"></div><svg class="dc" style="top:240px;right:70px;opacity:.6" width="200" height="130">{dots}</svg>'
    if kind == "leaves":
        return f'<div class="dc" style="background:{d1};width:600px;height:600px;top:-240px;right:-230px;border-radius:50%"></div><svg class="dc" style="bottom:-30px;right:-40px" width="300" height="300" viewBox="0 0 300 300"><path d="M150 300 C 150 200, 170 120, 260 60" stroke="{d2}" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M190 170 C 170 110, 220 70, 270 80 C 270 140, 230 180, 190 170Z" fill="{d2}"/><path d="M165 230 C 110 220, 90 170, 110 130 C 160 145, 175 190, 165 230Z" fill="{d2}" opacity=".75"/></svg>'
    if kind == "waves":
        return f'<svg class="dc" style="top:0;left:0" width="1080" height="260" viewBox="0 0 1080 260" preserveAspectRatio="none"><path d="M0 0 H1080 V120 C 900 210, 760 40, 560 120 S 220 230, 0 140Z" fill="{d1}"/></svg><svg class="dc" style="bottom:0;right:0" width="300" height="160" viewBox="0 0 420 220" preserveAspectRatio="none"><path d="M420 0 V220 H0 C 90 200, 120 120, 220 120 S 360 60, 420 0Z" fill="{d2}" opacity=".85"/></svg>'
    return ""

def build(content, variant, theme, evening=False):
    """content: kicker,h1,h2,icon(svg; renk için class i1..i4 / s1..s4),items[(başlık, alt satır|"")],tipl,tipt"""
    p = theme[variant]; L = theme["layout"]; soft = variant == "soft"
    tip, tipx = (p.get("tip2", p["tip"]), p.get("tipx2", p["tipx"])) if evening else (p["tip"], p["tipx"])
    tipl = p.get("tipl", tipx)
    shadow = "0 8px 24px rgba(0,0,0,.07)" if soft and p["row"] != "transparent" else "none"
    ic = "".join(f".i{n+1}{{fill:{c}}}.s{n+1}{{stroke:{c};fill:none}}" for n, c in enumerate(p["i"]))
    def num(i):
        return f'<div class="num">{i+1:02d}</div>' if L == "lines" else f'<div class="dot">{i+1}</div>'
    rows = "".join(f'<div class="row">{num(i)}<div><div class="it">{t}</div>{f"<div class=sub>{s}</div>" if s else ""}</div></div>' for i, (t, s) in enumerate(content["items"]))
    head = f'<h1>{content["h1"]}</h1><h2>{content["h2"]}</h2>'
    icon = f'<div class="icon">{content["icon"]}</div>'
    hero = f'<div class="hero"><div>{head}</div>{icon}</div>' if L == "side" else icon + head
    tipbox = f'<div class="tip"><div class="tl">{content["tipl"]}</div><div class="tt">{content["tipt"]}</div></div>' if content.get("tipt") else ""
    hf = p["hf"]; h2style = "italic" if p["h2i"] else "normal"
    lay = {
      "classic": "",
      "centered": ".main{text-align:center;align-items:center}.icon{display:flex;justify-content:center}.rows,.tip{width:100%;text-align:left}.foot{left:0;right:0;text-align:center}",
      "side": ".hero{display:flex;align-items:center;justify-content:space-between;gap:20px}.hero .icon{margin:0;transform:scale(1.3);transform-origin:right center}.rows{gap:22px!important;margin-top:44px!important}.row{padding:30px 34px!important}.it{font-size:32px!important}.sub{font-size:26px!important}.tip{padding:34px 38px!important;margin-top:30px!important}.tt{font-size:32px!important}.hero h1{font-size:82px}.hero h2{font-size:%s}" % ("72px" if soft else "80px"),
      "framed": f".frame{{position:absolute;inset:36px;border:3px solid {p['kick']};border-radius:44px;opacity:.45}}.wrap{{padding:84px 100px 0}}.foot{{left:100px;bottom:66px}}",
      "lines": f".row{{background:none!important;border-radius:0!important;box-shadow:none!important;border-bottom:2px solid {p['sub']}55;padding:20px 4px!important}}.rows{{gap:4px!important}}.num{{font-family:{hf};font-weight:700;font-size:54px;color:{p['acc']};width:90px;flex:none;line-height:1}}",
      "pill": ".row{border-radius:999px!important;padding:18px 40px 18px 22px!important}.tip{border-radius:36px!important}",
    }[L]
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{position:relative;background:{p['bg']};color:{p['tx']};font-family:Poppins}}
.dc{{position:absolute}}
.wrap{{position:absolute;inset:0;padding:70px 88px 0;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;align-items:center;position:relative}}
.kick{{font-weight:500;font-size:24px;letter-spacing:5px;color:{p['kick']}}}
.wm{{font-family:{hf};font-weight:700;font-size:34px}} .wm b{{color:{p['acc']}}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:120px}}
.icon{{margin:0 0 26px}}
h1{{font-family:{hf};font-weight:700;font-size:{'90px' if hf=='Lora' else '86px'};line-height:1.06}}
h2{{font-family:{hf};font-style:{h2style};font-weight:{'600' if hf=='Lora' else '700'};font-size:{'76px' if hf=='Lora' else '86px'};line-height:1.1;color:{p['acc']}}}
.rows{{margin-top:36px;display:flex;flex-direction:column;gap:18px}}
.row{{display:flex;align-items:center;gap:26px;padding:22px 30px;background:{p['row']};border-radius:{'24px' if soft else '18px'};box-shadow:{shadow}}}
.dot{{flex:none;width:58px;height:58px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;background:{p['dot']};color:{p['dotx']}}}
.it{{font-weight:500;font-size:32px;line-height:1.25}}
.sub{{font-size:24px;margin-top:4px;line-height:1.3;color:{p['sub']}}}
.tip{{margin-top:26px;padding:26px 34px;background:{tip};color:{tipx};border-radius:{'24px' if soft else '18px'};box-shadow:{shadow};{f"border-left:10px solid {p['bar']};" if soft and 'bar' in p and tip in ('#FFFFFF',) else ''}}}
.tl{{font-weight:700;font-size:21px;letter-spacing:4px;margin-bottom:8px;color:{tipl if soft else tipx};opacity:{1 if soft else .85}}}
.tt{{font-weight:500;font-size:30px;line-height:1.35}}
.foot{{position:absolute;left:88px;bottom:50px;font-size:22px;letter-spacing:.5px;color:{p['foot']}}}
{ic}
{lay}
</style></head><body>{_decor(theme['decor'], p)}{'<div class="frame"></div>' if L=='framed' else ''}
<div class="wrap"><div class="top"><div class="kick">{content['kicker']}</div><div class="wm">Plüton <b>PDRM</b></div></div>
<div class="main">{hero}<div class="rows">{rows}</div>{tipbox}</div></div>
<div class="foot">{FOOT}</div></body></html>"""

async def render(jobs):
    """jobs: [(png_path, html)]"""
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for path, html in jobs:
            await pg.set_content(html); await pg.wait_for_timeout(300)
            await pg.screenshot(path=path)
        await b.close()

SOLEMN = dict(bg="#1C2126",tx="#F2F2F2",sub="#B9C0C7",kick="#C9B27C",acc="#C9B27C",d1="#262C32",d2="#2E353C",foot="#9AA3AB",i=["#C9B27C","#E6E6E6","#7E8891","#2E353C"])

def build_special(content, theme, solemn=False):
    """Özel gün postu. content: kicker (ör. "29 EKİM"), h1, h2, icon (svg; class i1..i4/s1..s4), msg (2–3 satırlık kısa mesaj, <br> serbest), sign (ör. "Plüton PDRM ailesi olarak")"""
    p = SOLEMN if solemn else theme["bold"]
    hf = "Lora" if solemn else p["hf"]
    ic = "".join(f".i{n+1}{{fill:{c}}}.s{n+1}{{stroke:{c};fill:none}}" for n, c in enumerate(p["i"]))
    decor = (f'<div class="dc" style="border:2px solid {p["acc"]};opacity:.35;inset:44px;border-radius:8px"></div>' if solemn
             else _decor(theme["decor"], p))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{position:relative;background:{p['bg']};color:{p['tx']};font-family:Poppins}}
.dc{{position:absolute}}
.wrap{{position:absolute;inset:0;padding:80px 96px 0;display:flex;flex-direction:column;align-items:center;text-align:center}}
.wm{{font-family:{hf};font-weight:700;font-size:34px}} .wm b{{color:{p['acc']}}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;padding-bottom:110px}}
.kick{{font-weight:600;font-size:30px;letter-spacing:8px;color:{p['kick']};margin-bottom:34px}}
.icon svg{{width:300px;height:300px}} .icon{{margin-bottom:40px}}
h1{{font-family:{hf};font-weight:700;font-size:{'88px' if hf=='Lora' else '84px'};line-height:1.08}}
h2{{font-family:{hf};font-style:{'italic' if (hf=='Lora' and not solemn) else 'normal'};font-weight:{'600' if hf=='Lora' else '700'};font-size:{'74px' if hf=='Lora' else '80px'};line-height:1.12;color:{p['acc']}}}
.line{{width:120px;height:4px;border-radius:2px;background:{p['acc']};margin:40px auto 36px;opacity:.8}}
.msg{{font-size:32px;line-height:1.5;color:{p['sub']};max-width:860px}}
.sign{{margin-top:30px;font-family:{hf};font-style:italic;font-size:30px;color:{p['tx']}}}
.foot{{position:absolute;left:0;right:0;bottom:58px;text-align:center;font-size:22px;letter-spacing:.5px;color:{p['foot']}}}
{ic}
</style></head><body>{decor}
<div class="wrap"><div class="wm">Plüton <b>PDRM</b></div>
<div class="main"><div class="kick">{content['kicker']}</div><div class="icon">{content['icon']}</div>
<h1>{content['h1']}</h1><h2>{content['h2']}</h2><div class="line"></div>
<div class="msg">{content['msg']}</div>{f'<div class="sign">{content["sign"]}</div>' if content.get('sign') else ''}</div></div>
<div class="foot">{FOOT}</div></body></html>"""

# Resmi oranlara göre Türk bayrağı (Wikimedia yapısı) — milli günlerde ikon olarak kullanılabilir, elle çizmeyin.
FLAG = '<svg viewBox="0 -30000 90000 60000"><path fill="#E30A17" d="m0-30000h90000v60000H0z"/><path fill="#fff" d="m41750 0 13568-4408-8386 11541V-7133l8386 11541zm925 8021a15000 15000 0 1 1 0-16042 12000 12000 0 1 0 0 16042z"/></svg>'
