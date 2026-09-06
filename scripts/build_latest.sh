#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/LATEST_VERSION")"
DOC_DIR="$ROOT/docs/$VERSION"
TEX="KID入门讲义_${VERSION}.tex"
PDF="KID入门讲义_${VERSION}.pdf"

if [[ ! -f "$DOC_DIR/$TEX" ]]; then
  echo "Missing source: $DOC_DIR/$TEX" >&2
  exit 1
fi

cd "$DOC_DIR"
xelatex -interaction=nonstopmode -halt-on-error "$TEX"
xelatex -interaction=nonstopmode -halt-on-error "$TEX"

echo "Built: $DOC_DIR/$PDF"
