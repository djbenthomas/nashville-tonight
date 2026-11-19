#!/usr/bin/env python3
"""Nashville Tonight — short sales pitch, printable/shareable PDF (light)."""
import os
import segno
from weasyprint import HTML

BASE = os.path.expanduser('~/.openclaw/workspace-dale/nashville-tonight')
QR = os.path.join(BASE, 'qr-pitch.png')
OUT = os.path.join(BASE, 'Nashville-Tonight-Pitch.pdf')
URL = 'https://djbenthomas.github.io/nashville-tonight/'

segno.make(URL, error='m').save(QR, scale=10, border=1)

HTML_DOC = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@page {{ size: Letter; margin: 0.5in 0.6in; }}
* {{ box-sizing:border-box }}
body {{ font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; color:#1a1614; font-size:9.3pt; line-height:1.4; }}
.brand {{ font-size:7.6pt; letter-spacing:.3em; text-transform:uppercase; color:#b58427; }}
h1 {{ font-family:Georgia,serif; font-weight:400; font-size:19pt; line-height:1.08; margin:5pt 0 4pt; }}
h1 em {{ color:#b58427; font-style:italic; }}
.kick {{ font-size:8.6pt; color:#6b6158; margin:0; }}
.hdr {{ display:flex; justify-content:space-between; gap:16pt; border-bottom:2pt solid #1a1614; padding-bottom:8pt; }}
.hdr .qr {{ text-align:center; font-size:6.8pt; color:#8a7a66; }}
.hdr .qr img {{ width:1.15in; height:1.15in; display:block; margin:0 auto 2pt; }}
h2 {{ font-family:Georgia,serif; font-weight:400; font-size:11.4pt; margin:9pt 0 3pt; }}
h2 .n {{ color:#c9a227; font-size:8pt; margin-right:5pt; }}
p {{ margin:0 0 5pt; }}
ul {{ margin:3pt 0 6pt 12pt; padding:0; }}
li {{ margin-bottom:2.2pt; }}
.cols {{ display:flex; gap:14pt; }}
.cols > div {{ flex:1; }}
.q {{ background:#faf7f0; border-left:2pt solid #c9a227; padding:5pt 8pt; margin:3pt 0; font-size:8.8pt; }}
.q b {{ display:inline; }}
.quote {{ font-family:Georgia,serif; font-style:italic; font-size:10.4pt; border-left:2pt solid #1a1614; padding-left:9pt; margin:8pt 0; }}
.box {{ background:#faf7f0; border-left:2.5pt solid #c9a227; padding:7pt 9pt; margin-top:6pt; font-size:8.6pt; }}
.foot {{ margin-top:9pt; border-top:.7pt solid #ddd3c4; padding-top:5pt; font-size:7.8pt; color:#6b6158; display:flex; justify-content:space-between; }}
</style></head><body>

<div class="hdr">
  <div>
    <div class="brand">Nashville Tonight</div>
    <h1>Somebody's standing on Broadway at 9pm.<br><em>Nobody's telling them where to go.</em></h1>
    <p class="kick">The 60-second version. I want the holes poked in it before I print ten thousand magnets.</p>
  </div>
  <div class="qr">
    <img src="file://{QR}" alt="QR">
    Live now
  </div>
</div>

<h2><span class="n">01</span>The problem</h2>
<p>There is no real directory for live music downtown. Google gives you a list of bars — it doesn't tell
you that one room has a fiddle and a steel guitar and the one three doors down is a rock band with a
cowboy hat on. Locals know. Tourists guess. Everybody ends up in the loudest room with the worst music,
and the rooms that actually book real country don't get found.</p>

<h2><span class="n">02</span>The product</h2>
<p>One page. No app, no login. Scan, answer three questions:</p>
<div class="q"><b>1. What night are you out?</b> &nbsp;Tonight, or plan the rest of the week.</div>
<div class="q"><b>2. What do you want to hear?</b> &nbsp;Real country, classic country, bluegrass, roots, rock, two-step.</div>
<div class="q"><b>3. What kind of night is it?</b> &nbsp;Sit and listen, honky tonk, dance floor — or a party bar, clearly labeled.</div>
<p>You get a short list of rooms, walking distance, described honestly — plus one tap that hides the
bachelorette scene: <strong>"skip the party bars."</strong> The promise is the whole product:
<em>for people who came for the music.</em></p>

<h2><span class="n">03</span>How people find it</h2>
<div class="cols">
  <div>
    <ul>
      <li><strong>Fridge magnets with a QR code</strong> — thousands. "More info →". Magnets get taken home, and that's the point: locals keep them and use them every weekend.</li>
      <li><strong>Cards and flyers</strong> for the two-day tourists — honky tonk doorways, boot shops, hotels.</li>
      <li><strong>Window stickers</strong> on the doors of rooms that want to be found.</li>
      <li>Every batch has its own code, so we know which location and which hand produced the scans.</li>
    </ul>
  </div>
  <div>
    <div class="box"><strong>Why magnets:</strong> tourists leave in 48 hours, locals go out every weekend. A magnet is repeat traffic; a flyer in a trash can is not.</div>
    <div class="box"><strong>Why not an app:</strong> nobody installs an app to find a bar tonight. QR + web page is zero friction, any phone, two seconds.</div>
  </div>
</div>

<h2><span class="n">04</span>Who it's for</h2>
<p>The 30+ crowd who came for the music, and the locals tired of paying a cover to hear a rock band call
itself country. The Instagram account — <strong>Keeping Nashville Country</strong> — is the audience
engine: same voice, same taste, one post a day about who's actually playing it.</p>

<h2><span class="n">05</span>How it makes money</h2>
<ul>
  <li><strong>Featured night — $75/week:</strong> pinned to the top of their night.</li>
  <li><strong>Partner — $450/month:</strong> featured every night they're open, plus drink specials on the printed magnet/flyer.</li>
  <li><strong>Print sponsorship — $250 per 1,000:</strong> a logo on the back of the run. Works for boot shops, hotels, liquor brands, ride-share.</li>
  <li><strong>Drink specials — free, all tiers:</strong> the easiest "yes" in the pitch, and the reason people open the page twice.</li>
</ul>
<p>Free listings stay free. Nobody buys a better description — a party bar is listed as a party bar
whether they pay or not. That's what makes the recommendations worth trusting, and it's the reason a bar
manager will believe the rest of it.</p>

<div class="quote">"Nashville invented this music. We're just making sure people can find it on a Friday night."</div>

<h2><span class="n">06</span>Where it is right now</h2>
<div class="cols">
  <div>
    <ul>
      <li><strong>Live:</strong> 23 rooms, filterable by night, music and vibe — djbenthomas.github.io/nashville-tonight</li>
      <li><strong>Sponsorship tiers + print PDF:</strong> /partners.html</li>
      <li><strong>Flyer:</strong> print-ready, QR already points at it</li>
    </ul>
  </div>
  <div>
    <ul>
      <li><strong>Next:</strong> magnets, Instagram launch, first five venue partners</li>
      <li><strong>Not built yet, on purpose:</strong> accounts, reviews, ticketing — the second it becomes a platform, it stops shipping</li>
    </ul>
  </div>
</div>

<div class="box">
  <strong>What I want from you:</strong> tell me what's wrong with it, and what you'd do first. If it's a
  good idea I'd rather hear where it breaks now — before the magnets get printed.
</div>

<div class="foot">
  <div>Benny Thomas · AS·U·LIKE·IT Entertainment · (661) 533-0100 · djbenthomas@gmail.com</div>
  <div>djbenthomas.github.io/nashville-tonight</div>
</div>

</body></html>"""

HTML(string=HTML_DOC).write_pdf(OUT)
print('wrote', OUT, os.path.getsize(OUT), 'bytes')
