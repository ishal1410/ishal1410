"""Capture the live apps and compose them into one showcase board.

Run: python scripts/build_showcase.py
Needs Playwright (pip install playwright && playwright install chromium).

Deliberately not part of the daily workflow. It drives four real deployments,
one of which sleeps on a free tier, so it runs when the work changes rather
than on a timer. Screenshots are the strongest proof on the page and they
should be captured on purpose, not silently replaced by a cron job.

Output is PNG rather than SVG because the board is four raster screenshots;
an SVG would only wrap them in base64 and grow.
"""

import base64
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHOTS = ROOT / "assets" / "shots"
OUT = ROOT / "assets" / "showcase.png"

# Same palette as build_assets.py. Repeated rather than shared because the
# board is composed in HTML instead of drawn as SVG, and two short constant
# blocks beat a module that exists only to hold seven colours.
INK = "#0A0A0C"
PANEL = "#141417"
RULE = "#26262C"
PAPER = "#F4F2EE"
GRAY = "#9B9BA4"
GOLD = "#E0B252"

APPS = [
    ("depositcheck", "DepositCheck", "Do these photos belong to that address?",
     "depositcheck-liart.vercel.app", "https://depositcheck-liart.vercel.app"),
    ("ninetyninety", "NinetyNinety", "A bank export becomes a Form 990-EZ draft",
     "ishal1410.github.io/ninetyninety", "https://ishal1410.github.io/ninetyninety/"),
    ("glowread", "GlowRead", "Read your skin like an instrument",
     "glowread.vercel.app", "https://glowread.vercel.app"),
    ("jdecode", "JDecode", "Which keywords your resume is missing",
     "jdecode.vercel.app", "https://jdecode.vercel.app"),
]


def capture(page_factory):
    SHOTS.mkdir(parents=True, exist_ok=True)
    for slug, _, _, _, url in APPS:
        pg = page_factory()
        try:
            pg.goto(url, wait_until="networkidle", timeout=60000)
        except Exception as exc:  # a sleeping free tier still renders on load
            print(f"  {slug}: {type(exc).__name__}, falling back to load")
            pg.goto(url, wait_until="load", timeout=60000)
        pg.wait_for_timeout(2500)
        pg.screenshot(path=str(SHOTS / f"{slug}.png"))
        print(f"  captured {slug}")
        pg.close()


def board_html():
    cards = []
    for slug, name, line, host, _ in APPS:
        # Inlined, not linked. A page built with set_content has an opaque
        # origin and silently refuses to load file:// images, which composes a
        # board of broken-image icons that still screenshots cleanly.
        b64 = base64.b64encode((SHOTS / f"{slug}.png").read_bytes()).decode()
        src = f"data:image/png;base64,{b64}"
        cards.append(f"""
        <figure class="card">
          <div class="chrome">
            <span class="dot"></span><span class="dot"></span><span class="dot"></span>
            <span class="host">{host}</span>
          </div>
          <div class="shot"><img src="{src}" alt="{name}"></div>
          <figcaption>
            <span class="name">{name}</span>
            <span class="line">{line}</span>
          </figcaption>
        </figure>""")
    return f"""<body>
    <style>
      * {{ box-sizing: border-box; margin: 0; }}
      body {{ width: 2400px; background: {INK}; padding: 72px;
             font-family: -apple-system, 'Segoe UI', Roboto, sans-serif; }}
      .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 56px; }}
      .card {{ background: {PANEL}; border: 2px solid {RULE}; border-radius: 20px;
              overflow: hidden; }}
      .chrome {{ display: flex; align-items: center; gap: 12px;
                padding: 18px 24px; border-bottom: 2px solid {RULE}; }}
      .dot {{ width: 13px; height: 13px; border-radius: 50%; background: {RULE}; }}
      .host {{ margin-left: 14px; color: {GRAY}; font-size: 20px;
              font-family: ui-monospace, Menlo, Consolas, monospace; }}
      .shot {{ height: 640px; overflow: hidden; }}
      .shot img {{ width: 100%; display: block; }}
      figcaption {{ display: flex; align-items: baseline; gap: 18px;
                   padding: 26px 28px; border-top: 2px solid {RULE}; }}
      .name {{ color: {PAPER}; font-family: Georgia, serif; font-size: 34px; }}
      .line {{ color: {GRAY}; font-size: 22px; }}
      .foot {{ display: flex; align-items: center; gap: 20px; padding: 46px 4px 0; }}
      .tick {{ width: 54px; height: 2px; background: {RULE}; position: relative; }}
      .tick::after {{ content: ''; position: absolute; left: 14px; top: -7px;
                     width: 2px; height: 16px; background: {GOLD}; }}
      .footnote {{ color: {GRAY}; font-size: 22px;
                  font-family: ui-monospace, Menlo, Consolas, monospace;
                  letter-spacing: 3px; }}
    </style>
    <div class="grid">{''.join(cards)}</div>
    <div class="foot"><span class="tick"></span>
      <span class="footnote">FOUR DEPLOYMENTS, CAPTURED LIVE</span></div>
  </body>"""


def main():
    recapture = "--skip-capture" not in sys.argv
    with sync_playwright() as p:
        b = p.chromium.launch()
        if recapture:
            print("capturing live apps")
            capture(lambda: b.new_page(viewport={"width": 1440, "height": 900},
                                       device_scale_factor=2))
        missing = [s for s, *_ in APPS if not (SHOTS / f"{s}.png").exists()]
        if missing:
            raise SystemExit(f"no screenshot for: {', '.join(missing)}")
        pg = b.new_page(viewport={"width": 2400, "height": 1200},
                        device_scale_factor=1)
        pg.set_content(board_html())
        pg.wait_for_load_state("networkidle")
        pg.wait_for_timeout(1500)
        broken = pg.evaluate(
            "Array.from(document.images).filter(i => !i.naturalWidth).length")
        if broken:
            raise SystemExit(f"{broken} screenshot(s) failed to load into the board")
        pg.locator("body").screenshot(path=str(OUT))
        b.close()
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
