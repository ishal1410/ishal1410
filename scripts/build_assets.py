"""Generate the profile README's SVG assets.

Run: python scripts/build_assets.py
Refreshed daily by .github/workflows/assets.yml so the numbers cannot go stale.

Everything here is drawn from the GitHub API, so the card can only ever state
what the account actually holds. Notebook bytes are excluded from the language
split on purpose; see LANGUAGE_NOISE.
"""

import json
import os
import pathlib
import urllib.error
import urllib.request

USER = "ishal1410"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets"

# Palette, shared by every asset so the page reads as one system.
BG = "#0B0F14"
PANEL = "#111823"
FG = "#E6EDF3"
MUTED = "#8B949E"
DIM = "#6E7B8A"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,monospace"

# Jupyter counts every embedded plot and image as source bytes, so one notebook
# repo can outweigh a year of hand-written services. Excluded so the bar
# describes the work rather than the plots.
LANGUAGE_NOISE = {"Jupyter Notebook"}

LANG_COLOR = {
    "Python": "#3572A5",
    "TypeScript": "#3178C6",
    "JavaScript": "#F1E05A",
    "HTML": "#E34C26",
    "CSS": "#663399",
    "Shell": "#89E051",
    "Dockerfile": "#384D54",
    "HCL": "#844FBA",
    "Makefile": "#427819",
}
FALLBACK = "#6E7B8A"


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-assets",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def collect():
    """Return (repo_count, star_total, [(language, bytes), ...] descending)."""
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

    w, h = 1200, 292
    bar_x, bar_y, bar_w, bar_h = 56, 156, 1088, 22

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="st sd">',
        '<title id="st">Public code on this account</title>',
        f'<desc id="sd">{repo_count} public repositories, {stars} stars, and the '
        "share of each language written across them, notebooks excluded.</desc>",
        f'<rect width="{w}" height="{h}" rx="24" fill="{BG}"/>',
        f'<g font-family="{SANS}">',
        f'<text x="56" y="52" font-size="15" font-family="{MONO}" fill="{DIM}" '
        'letter-spacing="3">PUBLIC CODE ON THIS ACCOUNT</text>',
    ]

    # Stacked in fixed columns for the same reason as the legend below: the
    # inline form needed the pixel width of the number to place its label.
    for i, (value, label) in enumerate(
        [(str(repo_count), "repositories"), (str(stars), "stars"),
         (str(len(ranked)), "languages")]
    ):
        x = 56 + i * 190
        out.append(f'<text x="{x}" y="104" font-size="40" font-weight="700" '
                   f'fill="{FG}">{esc(value)}</text>')
        out.append(f'<text x="{x}" y="130" font-size="17" fill="{MUTED}">'
                   f"{esc(label)}</text>")

    out.append(f'<clipPath id="barclip"><rect x="{bar_x}" y="{bar_y}" '
               f'width="{bar_w}" height="{bar_h}" rx="11"/></clipPath>')
    out.append('<g clip-path="url(#barclip)">')
    x = bar_x
    for lang, size in top:
        seg = bar_w * size / total
        out.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{seg:.1f}" '
                   f'height="{bar_h}" fill="{LANG_COLOR.get(lang, FALLBACK)}"/>')
        x += seg
    out.append("</g>")

    # Fixed columns. Estimating the width of proportional text to place the
    # percentage after the name collided on short names and gapped on long ones.
    col = bar_w / len(top)
    for i, (lang, size) in enumerate(top):
        cx = bar_x + i * col
        out.append(f'<circle cx="{cx + 7:.0f}" cy="{bar_y + 54}" r="7" '
                   f'fill="{LANG_COLOR.get(lang, FALLBACK)}"/>')
        out.append(f'<text x="{cx + 24:.0f}" y="{bar_y + 60}" font-size="19" '
                   f'fill="{FG}">{esc(lang)}</text>')
        out.append(f'<text x="{cx + 24:.0f}" y="{bar_y + 86}" font-size="18" '
                   f'font-family="{MONO}" fill="{DIM}">'
                   f"{100 * size / total:.1f}%</text>")
    out.append(f'<text x="56" y="{h - 24}" font-size="15" font-family="{MONO}" '
               f'fill="{DIM}">Notebook bytes excluded; Jupyter counts embedded '
               "plot images as source.</text>")
    out.append("</g></svg>")
    return "\n".join(out)


SECTIONS = [
    ("recent", "01", "Recent", "#58A6FF"),
    ("live", "02", "Live", "#3FB950"),
    ("backend", "03", "Backend and infrastructure", "#D29922"),
    ("research", "04", "Machine learning and research", "#BC8CFF"),
    ("tools", "05", "Tools", "#39C5CF"),
    ("stack", "06", "Stack", "#F778BA"),
]


def section_svg(number, title, accent):
    w, h = 1200, 104
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
  <title id="t">{esc(title)}</title>
  <desc id="d">Section heading: {esc(title)}.</desc>
  <rect width="{w}" height="{h}" rx="18" fill="{PANEL}"/>
  <path d="M0 18 A18 18 0 0 1 18 0 L18 {h} A18 18 0 0 1 0 {h - 18} Z" fill="{accent}"/>
  <g font-family="{SANS}">
    <text x="48" y="59" font-size="17" font-family="{MONO}" fill="{accent}">{number}</text>
    <text x="94" y="62" font-size="38" font-weight="700" fill="{FG}">{esc(title)}</text>
  </g>
</svg>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, number, title, accent in SECTIONS:
        (OUT / f"section-{slug}.svg").write_text(
            section_svg(number, title, accent), encoding="utf-8"
        )
    try:
        repo_count, stars, ranked = collect()
    except (urllib.error.URLError, urllib.error.HTTPError) as exc:
        # A rate limit must not overwrite a good card with an empty one.
        print(f"skipped stats.svg: {exc}")
        return
    (OUT / "stats.svg").write_text(stats_svg(repo_count, stars, ranked),
                                   encoding="utf-8")
    print(f"stats.svg: {repo_count} repos, {stars} stars, "
          f"{len(ranked)} languages, top={ranked[0][0]}")


if __name__ == "__main__":
    main()
