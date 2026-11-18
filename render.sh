#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
page_url=$(python3 -c 'from pathlib import Path; print(Path("page.html").resolve().as_uri())')
profile=$(mktemp -d /tmp/cr-XXXXXX)
trap 'rm -rf -- "$profile"' EXIT

TMPDIR=/tmp /home/hatch/workspace/.browser-cache/chrome-linux64/chrome \
  --headless=new --disable-dev-shm-usage --disable-gpu --no-sandbox --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=1024,1024 \
  --disable-background-networking --no-first-run \
  --user-data-dir="$profile" --screenshot=entry.png "$page_url"
