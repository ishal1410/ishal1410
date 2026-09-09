"""Generate the profile README's SVG assets.

Run: python scripts/build_assets.py
The stats card is refreshed daily by .github/workflows/assets.yml, so its
counts cannot quietly go stale into a false claim.

Visual system, frozen here so every asset reads as one page:

  Palette   near-monochrome with one accent: ink, panel, rule, paper, two
            greys, and warm gold used only where something is signalled.
  Type      Georgia for display, system sans for body, mono for metadata.
            The serif is the deliberate anti-template choice.
  Shape     one radius family, one hairline weight, a 56-unit page margin.
  Motif     a measurement tick, a short rule crossed by a mark at a measured
            point. It comes from the through-line in this work: a model
            proposes and code checks the result.
"""

import json
import os
import pathlib
import urllib.error
import urllib.request

USER = "ishal1410"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

INK = "#0A0A0C"
PANEL = "#141417"
RULE = "#26262C"
PAPER = "#F4F2EE"
GRAY = "#9B9BA4"
DIM = "#83848E"  # 4.95:1 on PANEL, 5.33:1 on INK; #5E5F68 was 2.90:1
GOLD = "#E0B252"

SERIF = "Georgia,'Times New Roman',serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

# Jupyter counts every embedded plot image as source, so one notebook repo can
# outweigh a year of hand-written services. Excluded so the bar describes the
# work rather than the plots. The card states this on its face.
LANGUAGE_NOISE = {"Jupyter Notebook"}

# A restrained ramp instead of language brand colours. The legend names every
# language, so hue carries no information here, and seven brand colours fought
# everything else on the page.
RAMP = ["#E0B252", "#C9A268", "#A99175", "#87807A", "#6A6873", "#514F58", "#3A3941"]

# Three measured facts, each from a repository on this account. They are what
# makes this hero unusable on anyone elses profile.
EVIDENCE = [
    ("3,632 / 3,632", "IRS returns, total revenue rebuilt", "ninetyninety"),
    ("177", "tests, none spending an API call", "depositcheck"),
    ("95.33% / 75.00%", "in-set and cross-dataset", "deepfake-detection"),
]


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={"Accept": "application/vnd.github+json",
                 "User-Agent": f"{USER}-profile-assets"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def tick(x, y, w=54, color=GOLD):
    """The motif: a hairline rule crossed by a mark at a measured point."""
    return (f'<g><line x1="{x}" y1="{y}" x2="{x + w}" y2="{y}" stroke="{RULE}" '
            f'stroke-width="2"/><line x1="{x + 14}" y1="{y - 7}" x2="{x + 14}" '
            f'y2="{y + 7}" stroke="{color}" stroke-width="2"/></g>')


def hero_svg():
    w, h = 1200, 440
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="ht hd">',
        '<title id="ht">Vishal Patel, backend and machine learning engineer</title>',
        '<desc id="hd">Name and role beside three measured results from this '
        "account: 3,632 of 3,632 IRS returns reconciled in ninetyninety, 177 "
        "tests that spend no API call in depositcheck, and 95.33 percent in-set "
        "against 75.00 percent cross-dataset accuracy in the deepfake detection "
        "project.</desc>",
        f'<rect width="{w}" height="{h}" rx="20" fill="{INK}"/>',
        f'<line x1="672" y1="70" x2="672" y2="{h - 34}" stroke="{RULE}" '
        'stroke-width="2"/>',
        tick(56, 92),
        f'<text x="130" y="98" font-family="{MONO}" font-size="18" fill="{GRAY}" '
        'letter-spacing="4">BACKEND AND MACHINE LEARNING</text>',
        f'<text x="56" y="196" font-family="{SERIF}" font-size="76" fill="{PAPER}">'
        "Vishal Patel</text>",
        f'<text x="56" y="252" font-family="{SANS}" font-size="23" fill="{GRAY}">'
        "I build production services and the models</text>",
        f'<text x="56" y="286" font-family="{SANS}" font-size="23" fill="{GRAY}">'
        "behind them, then measure whether they hold.</text>",
        f'<text x="56" y="352" font-family="{MONO}" font-size="18" fill="{DIM}">'
        "github.com/ishal1410</text>",
        f'<text x="736" y="98" font-family="{MONO}" font-size="18" fill="{GRAY}" '
        'letter-spacing="4">MEASURED, NOT CLAIMED</text>',
    ]
    y = 160
    for value, label, source in EVIDENCE:
        out += [
            f'<text x="736" y="{y}" font-family="{SERIF}" font-size="36" '
            f'fill="{PAPER}">{esc(value)}</text>',
            f'<text x="736" y="{y + 30}" font-family="{SANS}" font-size="20" '
            f'fill="{GRAY}">{esc(label)}</text>',
            f'<text x="736" y="{y + 58}" font-family="{MONO}" font-size="18" '
            f'fill="{GOLD}">{esc(source)}</text>',
        ]
        y += 96
    out.append("</svg>")
    return "\n".join(out)


SECTIONS = [
    ("recent", "01", "Recent"),
    ("live", "02", "Live"),
    ("backend", "03", "Backend and infrastructure"),
    ("research", "04", "Machine learning and research"),
    ("tools", "05", "Tools"),
    ("stack", "06", "Stack"),
]


def section_svg(number, title):
    w, h = 1200, 92
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">'
        f'<title id="t">{esc(title)}</title>'
        f'<desc id="d">Section heading: {esc(title)}.</desc>'
        f'<rect width="{w}" height="{h}" rx="14" fill="{PANEL}"/>'
        f"{tick(48, 46)}"
        f'<text x="130" y="40" font-family="{MONO}" font-size="18" fill="{GOLD}">'
        f"{number}</text>"
        f'<text x="130" y="72" font-family="{SERIF}" font-size="34" fill="{PAPER}">'
        f"{esc(title)}</text>"
        "</svg>\n"
    )


def collect():
    repos = [r for r in api(f"users/{USER}/repos?per_page=100") if not r["fork"]]
    totals = {}
    for r in repos:
        for lang, size in api(f"repos/{USER}/{r['name']}/languages").items():
            if lang in LANGUAGE_NOISE:
                continue
            totals[lang] = totals.get(lang, 0) + size
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    return len(repos), sum(r["stargazers_count"] for r in repos), ranked


def stats_svg(repo_count, stars, ranked):
    top = ranked[:6]
    other = sum(v for _, v in ranked[6:])
    if other:
        top.append(("Other", other))
    total = sum(v for _, v in top) or 1

    w, h = 1200, 304
    bx, by, bw, bh = 56, 150, 1088, 14

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="st sd">',
        '<title id="st">Public code on this account</title>',
        f'<desc id="sd">{repo_count} public repositories, {stars} stars, and the '
        "share of each language across them, notebook bytes excluded.</desc>",
        f'<rect width="{w}" height="{h}" rx="20" fill="{PANEL}"/>',
        tick(56, 62),
        f'<text x="130" y="68" font-family="{MONO}" font-size="18" fill="{GRAY}" '
        'letter-spacing="4">PUBLIC CODE ON THIS ACCOUNT</text>',
    ]
    for i, (value, label) in enumerate(
        [(str(repo_count), "repositories"), (str(stars), "stars"),
         (str(len(ranked)), "languages")]
    ):
        x = 56 + i * 200
        out += [
            f'<text x="{x}" y="124" font-family="{SERIF}" font-size="40" '
            f'fill="{PAPER}">{esc(value)}</text>',
            f'<text x="{x}" y="124" dx="{14 + 22 * len(value)}" '
            f'font-family="{SANS}" font-size="19" fill="{DIM}">'
            f"{esc(label)}</text>",
        ]

    out.append(f'<clipPath id="bc"><rect x="{bx}" y="{by}" width="{bw}" '
               f'height="{bh}" rx="7"/></clipPath>')
    out.append('<g clip-path="url(#bc)">')
    x = bx
    # Whole pixels: at one decimal, any repository growing anywhere nudged every
    # segment and the daily refresh committed a diff nobody could see.
    for i, (lang, size) in enumerate(top):
        seg = bw * size / total
        out.append(f'<rect x="{round(x)}" y="{by}" width="{round(seg)}" '
                   f'height="{bh}" fill="{RAMP[i % len(RAMP)]}"/>')
        x += seg
    out.append("</g>")

    col = bw / len(top)
    for i, (lang, size) in enumerate(top):
        cx = round(bx + i * col)
        out += [
            f'<rect x="{cx}" y="{by + 42}" width="18" height="4" rx="2" '
            f'fill="{RAMP[i % len(RAMP)]}"/>',
            f'<text x="{cx}" y="{by + 78}" font-family="{SANS}" font-size="20" '
            f'fill="{PAPER}">{esc(lang)}</text>',
            f'<text x="{cx}" y="{by + 104}" font-family="{MONO}" font-size="20" '
            f'fill="{DIM}">{100 * size / total:.1f}%</text>',
        ]
    out.append(f'<text x="56" y="{h - 22}" font-family="{MONO}" font-size="18" '
               f'fill="{DIM}">Notebook bytes excluded; Jupyter counts embedded '
               "plot images as source.</text>")
    out.append("</svg>")
    return "\n".join(out)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "hero.svg").write_text(hero_svg(), encoding="utf-8")
    for slug, number, title in SECTIONS:
        (OUT / f"section-{slug}.svg").write_text(section_svg(number, title),
                                                 encoding="utf-8")
    try:
        repo_count, stars, ranked = collect()
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        # A rate limit must not overwrite a good card with an empty one.
        print(f"skipped stats.svg: {exc}")
        return
    (OUT / "stats.svg").write_text(stats_svg(repo_count, stars, ranked),
                                   encoding="utf-8")
    print(f"hero + {len(SECTIONS)} sections + stats.svg "
          f"({repo_count} repos, {stars} stars, {len(ranked)} languages)")


if __name__ == "__main__":
    main()
