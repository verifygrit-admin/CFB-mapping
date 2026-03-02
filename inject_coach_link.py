#!/usr/bin/env python3
"""
Inject coach_link values from GrittyOS DB CSV into cfbrecruit-map.html.

Joins on UNITID. Adds "coach_link" field to each school object immediately
after the existing "q_link" field. Also patches makePopup() to render the link.

Usage:
    python inject_coach_link.py
"""

import csv
import re
import shutil
from datetime import datetime

HTML_FILE  = "cfbrecruit-map.html"
CSV_FILE   = r"C:\Users\chris\dev\recruitingq-url-extract\Gritty OS - CFB Recruiting Center - Example 2027 - GrittyOS DB.csv"
UNITID_COL = "UNITID"
COACH_COL  = "Coach Page"

# ── Load CSV → {unitid_str: coach_link} ───────────────────────────────────────

def load_coach_links(csv_path: str) -> dict[str, str]:
    mapping = {}
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            uid   = row.get(UNITID_COL, "").strip()
            coach = row.get(COACH_COL,  "").strip()
            if uid:
                # Only store valid URLs; treat NOT_FOUND as empty
                mapping[uid] = coach if coach.startswith("http") else ""
    return mapping

# ── Inject coach_link into each school object ─────────────────────────────────

def inject_data(html: str, coach_map: dict[str, str]) -> tuple[str, int, int]:
    """
    Replace every occurrence of:
        "q_link": "..."} or "q_link": ""}
    with:
        "q_link": "...","coach_link": "COACH_URL"}

    Matches by unitid so we can look up the right value.
    Returns (updated_html, injected_count, skipped_count).
    """
    injected = skipped = 0

    def replacer(m: re.Match) -> str:
        nonlocal injected, skipped
        uid        = m.group("uid")
        q_val      = m.group("q_val")
        coach_link = coach_map.get(uid, "")
        injected  += 1
        return f'"unitid": "{uid}"{m.group("mid")}"q_link": "{q_val}","coach_link": "{coach_link}"}}'

    # Pattern: capture unitid, everything between unitid and q_link, and q_link value
    pattern = re.compile(
        r'"unitid":\s*"(?P<uid>\d+)"'     # "unitid": "123456"
        r'(?P<mid>.*?)'                    # everything up to q_link (non-greedy)
        r'"q_link":\s*"(?P<q_val>[^"]*)"' # "q_link": "..."
        r'\}',                             # closing brace of object
        re.DOTALL
    )

    updated = pattern.sub(replacer, html)
    return updated, injected, skipped

# ── Patch makePopup() to render the coach link ────────────────────────────────

ORIGINAL_QLINK_LINE = (
    "  const qLink = s.q_link "
    "? `<a href=\"${s.q_link}\" target=\"_blank\" class=\"popup-link\">📋 Recruiting Questionnaire</a>` : '';"
)

PATCHED_QLINK_BLOCK = (
    "  const qLink = s.q_link "
    "? `<a href=\"${s.q_link}\" target=\"_blank\" class=\"popup-link\">📋 Recruiting Questionnaire</a>` : '';\n"
    "  const coachLink = s.coach_link "
    "? `<a href=\"${s.coach_link}\" target=\"_blank\" class=\"popup-link\">🏈 Coaching Staff</a>` : '';"
)

ORIGINAL_QLINK_RENDER = "      ${qLink}"
PATCHED_QLINK_RENDER  = "      ${qLink}\n      ${coachLink}"

def patch_popup(html: str) -> str:
    html = html.replace(ORIGINAL_QLINK_LINE, PATCHED_QLINK_BLOCK, 1)
    html = html.replace(ORIGINAL_QLINK_RENDER, PATCHED_QLINK_RENDER, 1)
    return html

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("inject_coach_link.py")
    print("=" * 60)

    coach_map = load_coach_links(CSV_FILE)
    filled    = sum(1 for v in coach_map.values() if v)
    print(f"CSV loaded       : {len(coach_map)} schools, {filled} with coach links")

    # Backup
    ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = HTML_FILE.replace(".html", f"_backup_{ts}.html")
    shutil.copy2(HTML_FILE, dest)
    print(f"Backup           : {dest}")

    with open(HTML_FILE, encoding="utf-8") as f:
        html = f.read()

    # Sanity check: already injected?
    if '"coach_link"' in html:
        print("WARNING: coach_link already present in HTML — removing old values first.")
        html = re.sub(r',"coach_link":\s*"[^"]*"', "", html)
        html = html.replace(PATCHED_QLINK_BLOCK, ORIGINAL_QLINK_LINE)
        html = html.replace(PATCHED_QLINK_RENDER, ORIGINAL_QLINK_RENDER)

    html, injected, _ = inject_data(html, coach_map)
    html = patch_popup(html)

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    coach_in_html = html.count('"coach_link"')
    print(f"Objects patched  : {injected}")
    print(f"coach_link fields: {coach_in_html}")
    print(f"makePopup patched: {'coachLink' in html}")
    print("Done.")

if __name__ == "__main__":
    main()
