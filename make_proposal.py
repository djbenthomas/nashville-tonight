#!/usr/bin/env python3
"""Nashville Tonight — one-page sponsorship proposal (light, print-friendly)."""
import os
import segno
from weasyprint import HTML

BASE = os.path.expanduser('~/.openclaw/workspace-dale/nashville-tonight')
QR = os.path.join(BASE, 'qr-proposal.png')
OUT = os.path.join(BASE, 'Nashville-Tonight-Partnership.pdf')
URL = 'https://djbenthomas.github.io/nashville-tonight/partners.html'

segno.make(URL, error='m').save(QR, scale=10, border=1)

TIERS = [
    ("Free listing", "$0", "Always free",
     ["Listed with hours, cover, music and crowd",
      "Searchable by night and genre",
      "Drink specials posted weekly — free at every tier"]),
    ("Featured night", "$75 / wk &nbsp;·&nbsp; $250 / mo", "Most rooms start here",
     ["Pinned above free listings on your night",
      "Featured tag + photo on the card",
      "Specials shown inside the card",
      "Schedule kept current for you — send Sunday, live Monday"]),
    ("Partner", "$450 / mo", "Every night you're open",
     ["Everything in Featured, all week",
      "Specials on the printed flyer next to the QR",
      "One feature post a month on Keeping Nashville Country",
      "First right of refusal on the flyer sponsor line"]),
    ("Flyer sponsor", "$250 / 1,000", "For non-bars too",
     ["Logo on the back of the print run",
      "Boot shops, hotels, liquor brands, ride-share",
      "Print and delivery handled — you send the logo"]),
]

rows = ''.join(f"""
      <div class="tier">
        <div class="row"><div class="tname">{n}</div><div class="tprice">{p}</div></div>
        <div class="tsub">{s}</div>
        <ul>{''.join(f'<li>{i}</li>' for i in items)}</ul>
      </div>""" for n, p, s, items in TIERS)

HTML_DOC = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0.55in 0.65in; }}
* {{ box-sizing:border-box }}
body {{ font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; color:#1a1614; font-size:9.6pt; line-height:1.42; }}
h1 {{ font-family:Georgia,serif; font-weight:400; font-size:24pt; margin:0 0 4pt; line-height:1.06; }}
h1 em {{ color:#b58427; font-style:italic; }}
.brand {{ font-size:8pt; letter-spacing:.32em; text-transform:uppercase; color:#b58427; }}
.hdr {{ border-bottom:2.5pt solid #1a1614; padding-bottom:9pt; margin-bottom:12pt; display:flex; justify-content:space-between; gap:18pt; }}
.hdr .right {{ text-align:right; font-size:8.6pt; color:#6b6158; width:2.1in; }}
.hdr .right img {{ width:1.5in; height:1.5in; display:block; margin-left:auto; }}
.sub {{ font-size:10.4pt; color:#4a423a; margin:6pt 0 0; max-width:4.9in; }}
h2 {{ font-family:Georgia,serif; font-weight:400; font-size:12.6pt; margin:12pt 0 5pt; border-bottom:.7pt solid #ddd3c4; padding-bottom:3pt; }}
.cols {{ display:flex; gap:16pt; }}
.cols > div {{ flex:1; }}
ul {{ margin:3pt 0 0 12pt; padding:0; }}
li {{ margin-bottom:2.6pt; }}
.tiers {{ display:flex; gap:9pt; margin-top:6pt; }}
.tier {{ flex:1; border:.7pt solid #ddd3c4; border-radius:5pt; padding:8pt 9pt; }}
.tier:nth-child(2) {{ border:1.4pt solid #b58427; }}
.tname {{ font-weight:700; font-size:9.4pt; }}
.tprice {{ font-family:Georgia,serif; font-size:11pt; text-align:right; }}
.row {{ display:flex; justify-content:space-between; align-items:baseline; gap:6pt; }}
.tsub {{ font-size:7.6pt; color:#8a7a66; text-transform:uppercase; letter-spacing:.08em; margin:2pt 0 4pt; }}
.tier ul {{ margin:0 0 0 10pt; font-size:8.3pt; }}
.tier li {{ margin-bottom:2pt; }}
.note {{ background:#faf7f0; border-left:2.5pt solid #c9a227; padding:8pt 10pt; margin-top:10pt; font-size:8.9pt; }}
.foot {{ margin-top:12pt; border-top:.7pt solid #ddd3c4; padding-top:6pt; font-size:8.2pt; color:#6b6158; display:flex; justify-content:space-between; }}
</style></head><body>

<div class="hdr">
  <div>
    <div class="brand">Nashville Tonight</div>
    <h1>The people are already downtown.<br><em>We tell them where to go.</em></h1>
    <p class="sub">A hand-curated directory of Nashville's live music rooms — by music, by night, by the
    kind of night someone actually wants. Distributed on magnets, flyers and posters with a QR code,
    refreshed weekly — and handed out by the bands themselves.</p>
  </div>
  <div class="right">
    <img src="file://{QR}" alt="QR">
    <div style="margin-top:4pt">Scan to see the directory</div>
  </div>
</div>

<div class="cols">
  <div>
    <h2>How it works</h2>
    <ul>
      <li>Somebody on Broadway at 9pm scans the flyer</li>
      <li>Picks the night, the music, the vibe</li>
      <li>Gets a short list of rooms, described honestly</li>
      <li>Google gives a list of bars. We give an answer.</li>
      <li>It reaches them three ways: magnets (take-home, repeat use), flyers and posters (bars, doorways,
      windows), and counter cards in boot and product stores</li>
      <li>The bands distribute it themselves — every act we list gets magnets and cards for their crowd</li>
    </ul>
  </div>
  <div>
    <h2>Who's reading it</h2>
    <ul>
      <li>Locals and visitors who came for the music</li>
      <li>Skews 30+, stays for a full set, spends money</li>
      <li>Deciding on a phone, on the street, right now</li>
      <li>Every flyer batch has its own QR code — scans are attributable</li>
    </ul>
  </div>
</div>

<h2>Sponsorship tiers</h2>
<div class="tiers">{rows}</div>

<div class="note">
  <strong>Founding partners:</strong> the first five rooms get 30 days featured free and a rate locked for
  six months. Two asks in return — send your specials weekly, and tell us when we've got something wrong
  about your room.
</div>

<div class="note">
  <strong>What this is not:</strong> nobody buys a good description. A party bar is listed as a party bar
  whether they pay or not. No fake reviews, no paid rankings dressed up as editorial picks. 23 rooms,
  hand-checked, each with a "last verified" date.
</div>

<div class="foot">
  <div>djbenthomas.github.io/nashville-tonight &nbsp;·&nbsp; as-ulikeit.com</div>
  <div>(661) 533-0100 &nbsp;·&nbsp; djbenthomas@gmail.com</div>
</div>

</body></html>"""

HTML(string=HTML_DOC).write_pdf(OUT)
print('wrote', OUT, os.path.getsize(OUT), 'bytes')
