#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOC_DIR="$ROOT/docs/v0.2"
TEX="KID入门讲义_v0.2.tex"

cd "$DOC_DIR"
xelatex -interaction=nonstopmode -halt-on-error "$TEX"
xelatex -interaction=nonstopmode -halt-on-error "$TEX"

echo "Built: $DOC_DIR/KID入门讲义_v0.2.pdf"
