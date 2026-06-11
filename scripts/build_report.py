#!/usr/bin/env python3
"""Build a self-contained HTML report from findings.json + annotated screenshots."""
import argparse
import base64
import json
import re
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("findings")
    ap.add_argument("--annotated", required=True, help="dir with screen-N.png")
    ap.add_argument("--template", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    data = json.load(open(args.findings))
    adir = Path(args.annotated)
    images = []
    for p in sorted(adir.glob("screen-*.png"),
                    key=lambda p: int(re.search(r"\d+", p.stem).group())):
        b64 = base64.b64encode(p.read_bytes()).decode()
        images.append(f"data:image/png;base64,{b64}")
    if not images:
        sys.exit(f"ERROR: no screen-*.png in {adir}")

    def safe(obj):
        # keep inline <script type=application/json> blocks unterminated
        return json.dumps(obj).replace("</", "<\\/")

    html = Path(args.template).read_text()
    html = (html.replace("{{TITLE}}",
                         f"UX audit — {data.get('meta', {}).get('audit_id', 'report')}")
                .replace("{{FINDINGS_JSON}}", safe(data))
                .replace("{{IMAGES_JSON}}", safe(images)))
    Path(args.out).write_text(html)
    print(f"wrote {args.out} ({len(html) // 1024} KB, {len(images)} screens)")


if __name__ == "__main__":
    main()
