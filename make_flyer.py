#!/usr/bin/env python3
"""Nashville Tonight — printable flyer with QR.

Light background on purpose: black-out flyers cost a fortune at a copy shop.
Letter size, one page, 300 DPI QR.
"""
import os
import segno
from weasyprint import HTML

BASE = os.path.expanduser('~/.openclaw/workspace-dale/nashville-tonight')
QR = os.path.join(BASE, 'qr-flyer.png')
OUT = os.path.join(BASE, 'Nashville-Tonight-Flyer.pdf')
URL = 'https://djbenthomas.github.io/nashville-tonight/?f=flyer1'

segno.make(URL, error='h').save(QR, scale=15, border=1)

HTML_DOC = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color:#141110; background:#f6efe4; }}
.sheet {{ width:8.5in; height:11in; padding:0.55in 0.7in; display:flex; flex-direction:column; }}
.brand {{ font-size:9pt; letter-spacing:.36em; text-transform:uppercase; color:#b58427; }}
h1 {{ font-family: Georgia, 'Times New Roman', serif; font-size:44pt; line-height:1.02; margin:14pt 0 8pt; letter-spacing:-.015em; }}
h1 em {{ color:#b58427; font-style:italic; }}
.sub {{ font-size:13.5pt; line-height:1.45; color:#4a423a; max-width:5.6in; }}
.rule {{ border:0; border-top:2.5pt solid #141110; margin:16pt 0 0; }}
.row {{ display:flex; gap:26pt; margin-top:20pt; align-items:flex-start; }}
.qr {{ text-align:center; }}
.qr img {{ width:2.5in; height:2.5in; display:block; }}
.qr .cap {{ font-size:9.5pt; letter-spacing:.16em; text-transform:uppercase; color:#7a6c5c; margin-top:6pt; }}
.steps {{ flex:1; }}
.step {{ display:flex; gap:10pt; margin-bottom:11pt; }}
.num {{ font-family:Georgia,serif; font-size:15pt; color:#b58427; width:20pt; flex:none; }}
.step b {{ display:block; font-size:12.5pt; margin-bottom:1pt; }}
.step span {{ font-size:10.5pt; color:#5c5147; line-height:1.4; }}
.genres {{ display:flex; gap:8pt; flex-wrap:wrap; margin-top:6pt; }}
.genres div {{ border:1px solid #cfc2ad; border-radius:999px; padding:4pt 10pt; font-size:9pt; letter-spacing:.12em; text-transform:uppercase; color:#5c5147; }}
.box {{ margin-top:auto; border-top:1px solid #cfc2ad; padding-top:12pt; display:flex; justify-content:space-between; gap:16pt; font-size:9.5pt; color:#5c5147; }}
.box b {{ color:#141110; }}
.week {{ margin-top:14pt; }}
.week h2 {{ font-family:Georgia,serif; font-weight:400; font-size:15pt; margin:0 0 5pt; }}
.week p {{ font-size:9.8pt; color:#5c5147; margin:0 0 3pt; line-height:1.4; }}
.sponsor {{ margin-top:10pt; border:1px dashed #cfc2ad; border-radius:6pt; padding:8pt 12pt; font-size:9pt; color:#8a7a66; }}
</style></head><body>
<div class="sheet">

  <div class="brand">Nashville Tonight</div>
  <h1>You're already downtown.<br><em>Here's where to actually go.</em></h1>
  <p class="sub">No app. No sign-up. Scan the code, pick the night and what you want to hear, and you get
  a short list of rooms that are actually playing it — real country, bluegrass, roots, or rock.</p>
  <hr class="rule">

  <div class="row">
    <div class="qr">
      <img src="file://{QR}" alt="QR code for Nashville Tonight">
      <div class="cap">Point your camera here</div>
    </div>
    <div class="steps">
      <div class="step"><div class="num">1</div><div><b>What night are you out?</b><span>Tonight, or plan the rest of the week.</span></div></div>
      <div class="step"><div class="num">2</div><div><b>What do you want to hear?</b><span>Traditional country, classic country, bluegrass, roots, rock, two-step.</span></div></div>
      <div class="step"><div class="num">3</div><div><b>What kind of night?</b><span>Sit and listen, honky tonk, dance floor — or party bar, clearly labeled.</span></div></div>
      <div class="step"><div class="num">★</div><div><b>Skip the party bars</b><span>One tap hides the bachelorette scene. Some nights you want the band, not the yelling.</span></div></div>
      <div class="genres">
        <div>Real country</div><div>Bluegrass</div><div>Roots</div><div>Rock</div>
      </div>
    </div>
  </div>

  <div class="week">
    <h2>Every room is described honestly.</h2>
    <p>Including which ones are tourist traps after 8pm, and which ones you can actually hear the fiddle in.</p>
    <p>Hand-checked, updated weekly, and free. If something's wrong, tell us on the page — we fix it.</p>
  </div>

  <div class="sponsor">
    <b>Sponsor this flyer.</b> 1,000 flyers in downtown hands — bars, boot shops, hotels, ride-shares.
    Ask about featured placements at djbenthomas@gmail.com.
  </div>

  <div class="box">
    <div>nashvilletonight · <b>djbenthomas.github.io/nashville-tonight</b></div>
    <div>Built by <b>AS·U·LIKE·IT Entertainment</b> · Nashville</div>
  </div>

</div>
</body></html>"""

HTML(string=HTML_DOC).write_pdf(OUT)
print('wrote', OUT, os.path.getsize(OUT), 'bytes')
