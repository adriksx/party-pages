"""Builds two lively A6 table cards (HTML) with the QR code inlined."""
import re, pathlib

qr = pathlib.Path("/home/claude/qr.svg").read_text()
qr = re.sub(r'width="[^"]+" height="[^"]+"', 'width="100%" height="100%"', qr, count=1)
qr = qr.replace("<path ", '<path fill="#2b2622" ', 1)

# --- reusable decorative SVG bits ---
def flower(c1, c2, size):
    petals = "".join(
        f'<ellipse cx="0" cy="-11" rx="7" ry="11" fill="{c1}" transform="rotate({a})"/>' for a in range(0, 360, 72))
    return f'<svg width="{size}" height="{size}" viewBox="-24 -24 48 48">{petals}<circle r="5.5" fill="{c2}"/></svg>'

def leaf_sprig(color, w, h, flip=False):
    t = 'transform="scale(-1,1) translate(-120,0)"' if flip else ""
    return f'''<svg width="{w}" height="{h}" viewBox="0 0 120 120"><g {t} fill="{color}" stroke="none">
    <path d="M10 110 C 40 80, 70 50, 112 8" stroke="{color}" stroke-width="2.4" fill="none"/>
    <path d="M30 88 c -14 -2 -22 -14 -20 -26 c 12 2 20 12 20 26z"/>
    <path d="M30 88 c 2 -14 14 -20 26 -18 c -2 12 -12 18 -26 18z"/>
    <path d="M55 62 c -14 -2 -22 -14 -20 -26 c 12 2 20 12 20 26z"/>
    <path d="M55 62 c 2 -14 14 -20 26 -18 c -2 12 -12 18 -26 18z"/>
    <path d="M80 37 c -12 -2 -19 -12 -17 -22 c 10 2 17 10 17 22z"/>
    <path d="M80 37 c 2 -12 12 -17 22 -15 c -2 10 -10 15 -22 15z"/>
    </g></svg>'''

CAMERA = '''<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13" r="3.6"/></svg>'''

BASE_CSS = """
@page { size: 105mm 148mm; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
html, body { width: 105mm; height: 148mm }
body { font-family: Montserrat, sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact }
.card { position: relative; width: 105mm; height: 148mm; overflow: hidden; text-align: center }
.abs { position: absolute }
.script { font-family: 'Great Vibes', cursive; font-weight: 400 }
.serif { font-family: 'Cormorant Garamond', serif }
.qrwrap { margin: 0 auto; background: #fff; border-radius: 6mm; padding: 4.2mm; width: 52mm; height: 52mm; position: relative }
.steps { display: flex; justify-content: center; gap: 2.4mm; margin-top: 4.2mm }
.step { width: 27mm; font-size: 2.55mm; line-height: 1.3; font-weight: 500 }
.step b { display: flex; align-items: center; justify-content: center; margin: 0 auto 1.2mm; width: 6.4mm; height: 6.4mm; border-radius: 50%; font-size: 3.1mm; font-weight: 700 }
.step small { display: block; font-weight: 400; opacity: .7; font-size: 2.25mm }
"""

def page(css, body):
    return f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{BASE_CSS}{css}</style></head><body>{body}</body></html>"

# ===== Variant A: blush & sage floral =====
css_a = """
.card { background: radial-gradient(120% 70% at 50% 0%, #fff7f2 0%, #fbe3da 55%, #f6cfc4 100%); color: #3a2c2a }
.eyebrow { margin-top: 15mm; font-size: 2.6mm; letter-spacing: .45em; font-weight: 600; color: #b5654f; text-transform: uppercase }
h1 { font-size: 13mm; line-height: 1; margin-top: 1.5mm; color: #8c3f3a }
.tag { font-size: 6.2mm; font-weight: 600; margin-top: 1mm; color: #3a2c2a }
.tag small { display:block; font-family: Montserrat; font-size: 2.6mm; font-weight: 500; color: #9a6a60; margin-top: .6mm; letter-spacing: .02em }
.qrzone { margin-top: 5mm; position: relative }
.qrwrap { box-shadow: 0 3mm 7mm -2mm rgba(140,63,58,.35); border: .7mm solid #e7b9a8 }
.badge { position: absolute; top: -3.4mm; right: 22mm; width: 11mm; height: 11mm; border-radius: 50%; background: #8c3f3a; color: #fff; display:flex; align-items:center; justify-content:center; transform: rotate(12deg); box-shadow: 0 1.5mm 3mm rgba(0,0,0,.2) }
.step b { background: #8c3f3a; color: #fff }
.foot { position: absolute; bottom: 7mm; left: 0; right: 0; font-size: 2.3mm; color: #9a6a60 }
.foot .script { font-size: 6mm; color: #8c3f3a; display:block; margin-bottom: .6mm }
"""
deco_a = f"""
<div class="abs" style="top:-9mm;left:-10mm">{leaf_sprig('#9bb08f', '30mm', '30mm', flip=True)}</div>
<div class="abs" style="top:-9mm;right:-10mm">{leaf_sprig('#9bb08f', '30mm', '30mm')}</div>
<div class="abs" style="top:3mm;left:4mm">{flower('#f3a9a0', '#f7d58b', '13mm')}</div>
<div class="abs" style="top:11mm;left:3mm">{flower('#fff', '#f3a9a0', '7mm')}</div>
<div class="abs" style="top:3mm;right:4mm">{flower('#e88a87', '#f7d58b', '12mm')}</div>
<div class="abs" style="top:12mm;right:3mm">{flower('#fbd3c8', '#e88a87', '6mm')}</div>
<div class="abs" style="bottom:-10mm;left:-11mm;transform:rotate(180deg)">{leaf_sprig('#9bb08f', '27mm', '27mm')}</div>
<div class="abs" style="bottom:-10mm;right:-11mm;transform:rotate(180deg)">{leaf_sprig('#9bb08f', '27mm', '27mm', flip=True)}</div>
<div class="abs" style="bottom:3mm;left:3mm">{flower('#f3a9a0', '#f7d58b', '9mm')}</div>
<div class="abs" style="bottom:3mm;right:3mm">{flower('#e88a87', '#fff', '8mm')}</div>
"""
body_a = f"""<div class="card">{deco_a}
<p class="eyebrow">Uhvati trenutak</p>
<h1 class="script">Marko &amp; Ana</h1>
<p class="tag serif">Podijelite svoje fotke s nama!<small>Share your photos &amp; videos with us</small></p>
<div class="qrzone"><div class="qrwrap">{qr}</div><div class="badge">{CAMERA}</div></div>
<div class="steps">
 <div class="step"><b>1</b>Skeniraj sa mobitelom<small>Scan with your phone</small></div>
 <div class="step"><b>2</b>Upiši svoje ime<small>Type your name</small></div>
 <div class="step"><b>3</b>Odaberi fotke<small>Pick your photos</small></div>
</div>
<div class="foot"><span class="script">hvala vam!</span>iPhone: videe učitaj kroz Safari</div>
</div>"""

# ===== Variant B: festive confetti / party =====
import random
random.seed(7)
colors = ["#ff6b6b", "#ffd166", "#06d6a0", "#4cc9f0", "#b388ff", "#ff9f1c"]
conf = []
for _ in range(260):
    x, y = random.uniform(0, 105), random.uniform(0, 148)
    if (7 < x < 98 and 11 < y < 139) or (15 < x < 90 and y >= 132):  # keep the middle clean
        continue
    c = random.choice(colors); r = random.uniform(0, 180); s = random.uniform(1.4, 3.2)
    shape = random.choice(["rect", "dot", "squig"])
    if shape == "rect":
        conf.append(f'<div class="abs" style="left:{x:.1f}mm;top:{y:.1f}mm;width:{s*0.7:.1f}mm;height:{s*1.8:.1f}mm;background:{c};border-radius:.4mm;transform:rotate({r:.0f}deg)"></div>')
    elif shape == "dot":
        conf.append(f'<div class="abs" style="left:{x:.1f}mm;top:{y:.1f}mm;width:{s:.1f}mm;height:{s:.1f}mm;background:{c};border-radius:50%"></div>')
    else:
        conf.append(f'<svg class="abs" style="left:{x:.1f}mm;top:{y:.1f}mm;transform:rotate({r:.0f}deg)" width="{s*3:.1f}mm" height="{s*1.6:.1f}mm" viewBox="0 0 30 12"><path d="M2 6 q 4 -6 8 0 t 8 0 t 8 0" stroke="{c}" stroke-width="3" fill="none" stroke-linecap="round"/></svg>')
css_b = """
.card { background: linear-gradient(165deg, #2b1d52 0%, #4a2a7a 45%, #7a3a8c 100%); color: #fff }
.eyebrow { margin-top: 15mm; display:inline-block; font-size: 2.6mm; letter-spacing: .35em; font-weight: 700; color: #2b1d52; background: #ffd166; padding: 1.2mm 3.4mm; border-radius: 99mm; text-transform: uppercase }
h1 { font-size: 15.5mm; line-height: 1; margin-top: 2.2mm; color: #fff; text-shadow: 0 .8mm 0 #ff6b6b }
.tag { font-size: 3.5mm; font-weight: 600; margin-top: 2mm }
.tag small { display:block; font-size: 2.5mm; font-weight: 400; opacity: .75; margin-top: .6mm }
.qrzone { margin-top: 5mm; position: relative }
.qrwrap { box-shadow: 0 0 0 1.4mm #ffd166, 0 0 0 2.8mm #ff6b6b, 0 4mm 9mm rgba(0,0,0,.4) }
.badge { position: absolute; top: -4mm; left: 21mm; width: 11mm; height: 11mm; border-radius: 50%; background: #06d6a0; color: #2b1d52; display:flex; align-items:center; justify-content:center; transform: rotate(-12deg); box-shadow: 0 1.5mm 3mm rgba(0,0,0,.3) }
.steps { margin-top: 6.5mm }
.step b { background: #ffd166; color: #2b1d52 }
.foot { position: absolute; bottom: 8mm; left: 0; right: 0; font-size: 2.3mm; opacity: .8 }
"""
body_b = f"""<div class="card">{''.join(conf)}
<span class="eyebrow">📸 Fotkajte!</span>
<h1 class="script">Marko &amp; Ana</h1>
<p class="tag">Podijelite svoje fotke i videe s nama!<small>Share your photos &amp; videos with us</small></p>
<div class="qrzone"><div class="qrwrap">{qr}</div><div class="badge">{CAMERA}</div></div>
<div class="steps">
 <div class="step"><b>1</b>Skeniraj sa mobitelom<small>Scan with your phone</small></div>
 <div class="step"><b>2</b>Upiši svoje ime<small>Type your name</small></div>
 <div class="step"><b>3</b>Odaberi fotke<small>Pick your photos</small></div>
</div>
<div class="foot">iPhone: videe učitaj kroz Safari · iPhone: use Safari for videos</div>
</div>"""

pathlib.Path("/home/claude/card/A.html").write_text(page(css_a, body_a))
pathlib.Path("/home/claude/card/B.html").write_text(page(css_b, body_b))
print("ok")
