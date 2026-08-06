#!/usr/bin/env python3
"""Refresh the live radar-stats block in profile/README.md.

Runs every 3 hours from the org .github repo. It pulls the community radar's
published data (a public raw file — no auth needed), recomputes the headline
numbers, and rewrites ONLY the marker-delimited block

    <!-- RADAR:START -->  ...  <!-- RADAR:END -->

leaving the rest of the profile untouched. The commit is made through the
GitHub Contents API using the repo's own GITHUB_TOKEN, so it is a verified
commit and works even under a "require signed commits" ruleset — no personal
access token required.

Zero third-party dependencies (stdlib only), matching the radar's philosophy.
Honest by construction: every figure is a real public GitHub signal and the
prominent link points to the same report anyone can open.
"""
from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

REPO = os.environ.get("GITHUB_REPOSITORY", "AxonOS-org/.github")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
README_PATH = "profile/README.md"

RADAR_RAW = "https://raw.githubusercontent.com/AxonOS-BCI/axonos-community-radar/main/data/radar.json"
REPORT_URL = "https://axonos-bci.github.io/axonos-community-radar/report.html"

START = "<!-- RADAR:START -->"
END = "<!-- RADAR:END -->"
API = "https://api.github.com"
UA = "axonos-profile-radar/1.0"


def k(n):
    n = n or 0
    return (f"{n / 1000:.1f}k".replace(".0k", "k")) if n >= 1000 else str(n)


def badge(label, value, color="0a4a8f"):
    lab = str(label).replace(" ", "_").replace("-", "--")
    val = str(value).replace(" ", "_").replace("-", "--")
    return (f'<img src="https://img.shields.io/badge/{lab}-{val}-{color}?style=flat-square" '
            f'alt="{label}: {value}">')


def load_radar(local=None):
    if local:
        with open(local, encoding="utf-8") as f:
            return json.load(f)
    req = urllib.request.Request(RADAR_RAW, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
        return json.loads(r.read().decode("utf-8"))


def build_block(radar):
    p = radar.get("projects", [])
    c = radar.get("counts", {})
    tot = c.get("total", len(p))
    stars = sum(int(x.get("stars") or 0) for x in p)
    big = sum(1 for x in p if (x.get("stars") or 0) >= 1000)
    active = c.get("active_30d", sum(1 for x in p if x.get("active")))
    builders = len(radar.get("builders", [])) or c.get("builders", 0)
    langs = len({x.get("language") for x in p if x.get("language")})
    top = [x.get("repo") or (x.get("full_name") or "").split("/")[-1]
           for x in sorted(p, key=lambda x: -(x.get("stars") or 0))[:4]]
    ts = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")

    badges = " ".join([
        badge("projects", tot),
        badge("total stars", k(stars)),
        badge("over 1k", big),
        badge("active 30d", active, "0d7a5f"),
        badge("builders", builders),
        badge("languages", langs),
    ])
    top_line = " · ".join(f"`{t}`" for t in top if t)

    return "\n".join([
        "The **AxonOS Community Radar** continuously maps every open-source brain\u2013computer-interface",
        "project, tool and team building in the open \u2014 AxonOS included, ranked by the same public-signal",
        "formula as everyone else, with no boosting.",
        "",
        # No emoji. The profile removes them by hand and this job put one back
        # every three hours, which made a rule enforced downstream into a lie
        # upstream. A rule that a scheduled job undoes is not a rule.
        f'<p align="center"><a href="{REPORT_URL}"><b>The State of Open BCI \u2014 '
        "read the full report \u2192</b></a></p>",
        "",
        f'<p align="center">{badges}</p>',
        "",
        f"<sub>One click for the exhaustive view \u2014 a Gartner-style reach\u00d7engagement quadrant, "
        f"category and evidence breakdowns, and a full table of all {tot} tracked resources. "
        f"Currently leading by reach: {top_line}. "
        f"Auto-refreshed from the radar every 3 hours \u00b7 last update <b>{ts}</b>.</sub>",
    ])


def splice(readme, block):
    if START not in readme or END not in readme:
        return None
    pre = readme.split(START)[0]
    post = readme.split(END, 1)[1]
    return f"{pre}{START}\n{block}\n{END}{post}"


# --------------------------------------------------------------------------- #
# GitHub Contents API (verified commit via the repo's own token)
# --------------------------------------------------------------------------- #
def api(method, url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
        "User-Agent": UA, "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8"))
        except Exception:  # noqa: BLE001
            return e.code, {}


def get_readme():
    code, body = api("GET", f"{API}/repos/{REPO}/contents/{README_PATH}")
    if code != 200:
        print(f"cannot read {README_PATH}: HTTP {code} {body.get('message')}")
        return None, None
    return body.get("sha"), base64.b64decode(body.get("content", "")).decode("utf-8")


def put_readme(content, sha, message):
    payload = {"message": message, "content": base64.b64encode(content.encode()).decode(),
               "branch": "main", "sha": sha}
    code, body = api("PUT", f"{API}/repos/{REPO}/contents/{README_PATH}", payload)
    if code in (200, 201):
        v = (body.get("commit") or {}).get("verification") or {}
        print(f"committed {(body.get('commit') or {}).get('sha', '')[:8]} (verified={v.get('verified')})")
        return True
    print(f"commit FAILED HTTP {code}: {body.get('message')}")
    return False


def main():
    if "--local" in sys.argv:
        radar = load_radar(sys.argv[sys.argv.index("--local") + 1])
        readme = open(README_PATH, encoding="utf-8").read()
        out = splice(readme, build_block(radar))
        if out is None:
            print("markers not found in README")
            return 1
        open(README_PATH, "w", encoding="utf-8").write(out)
        print("local: profile/README.md updated")
        return 0

    if not TOKEN:
        print("Missing GITHUB_TOKEN")
        return 1
    try:
        radar = load_radar()
    except Exception as e:  # noqa: BLE001
        print("cannot fetch radar data:", e)
        return 0  # never fail the profile over a transient fetch
    block = build_block(radar)
    for attempt in range(2):
        sha, readme = get_readme()
        if readme is None:
            return 1
        out = splice(readme, block)
        if out is None:
            print("markers not found in profile/README.md \u2014 add "
                  f"{START} / {END} once, then this refreshes automatically")
            return 0
        if out == readme:
            print("radar block already current \u2014 nothing to commit")
            return 0
        if put_readme(out, sha, "chore(profile): refresh live radar stats [skip ci]"):
            return 0
        print(f"retry {attempt + 1} (likely a concurrent update)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
