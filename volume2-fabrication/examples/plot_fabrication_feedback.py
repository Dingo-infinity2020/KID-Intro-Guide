#!/usr/bin/env python3
"""Generate dependency-free SVG diagnostics for KID fabrication feedback.

Input is the ``joined_feedback.csv`` produced by ``analyze_fabrication_feedback.py``.
The script intentionally uses only Python's standard library so the same plots
can be generated in CI, on a clean lab machine, or on a data-taking computer.
"""

from __future__ import annotations

import argparse
import csv
import html
import math
from pathlib import Path


REQUIRED = [
    "resonator_id",
    "x_mm",
    "y_mm",
    "Rsq_ohm_sq",
    "measured_delta_f_frac",
    "predicted_systematic_frac",
    "residual_frac",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"{path} is empty")
    missing = [name for name in REQUIRED if name not in rows[0]]
    if missing:
        raise ValueError(f"{path} is missing required columns: {missing}")
    return rows


def numeric_rows(rows: list[dict[str, str]]) -> list[dict[str, float | str]]:
    usable: list[dict[str, float | str]] = []
    for row in rows:
        try:
            usable.append({
                "resonator_id": (row.get("resonator_id") or "").strip(),
                "x_mm": float(row["x_mm"]),
                "y_mm": float(row["y_mm"]),
                "Rsq_ohm_sq": float(row["Rsq_ohm_sq"]),
                "measured_ppm": 1.0e6 * float(row["measured_delta_f_frac"]),
                "predicted_ppm": 1.0e6 * float(row["predicted_systematic_frac"]),
                "residual_ppm": 1.0e6 * float(row["residual_frac"]),
            })
        except (KeyError, TypeError, ValueError):
            continue
    if len(usable) < 2:
        raise ValueError("Need at least two rows with numeric plotting fields")
    return usable


def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))


def rgb_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> str:
    t = clamp(t, 0.0, 1.0)
    return rgb_hex(
        round(a[0] + (b[0] - a[0]) * t),
        round(a[1] + (b[1] - a[1]) * t),
        round(a[2] + (b[2] - a[2]) * t),
    )


def sequential(value: float, lo: float, hi: float) -> str:
    if not math.isfinite(value) or hi <= lo:
        return "#888888"
    return blend((239, 246, 255), (8, 81, 156), (value - lo) / (hi - lo))


def diverging(value: float, vmax: float) -> str:
    if not math.isfinite(value) or vmax <= 0.0:
        return "#f7f7f7"
    t = clamp(value / vmax, -1.0, 1.0)
    if t < 0:
        return blend((33, 102, 172), (247, 247, 247), t + 1.0)
    return blend((247, 247, 247), (178, 24, 43), t)


def svg_text(x: float, y: float, text: str, size: int = 14, anchor: str = "start", weight: str = "normal") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="sans-serif" '
        f'font-size="{size}" text-anchor="{anchor}" font-weight="{weight}" '
        f'fill="#222">{html.escape(text)}</text>'
    )


def padded_range(values: list[float], frac: float = 0.08) -> tuple[float, float]:
    lo, hi = min(values), max(values)
    if hi == lo:
        pad = abs(lo) * frac or 1.0
        return lo - pad, hi + pad
    pad = (hi - lo) * frac
    return lo - pad, hi + pad


def write_map(rows, key: str, title: str, label: str, path: Path, *, diverge: bool = False) -> None:
    width, height = 820, 640
    left, right, top, bottom = 92, 170, 70, 78
    plot_w = width - left - right
    plot_h = height - top - bottom

    xs = [float(row["x_mm"]) for row in rows]
    ys = [float(row["y_mm"]) for row in rows]
    vals = [float(row[key]) for row in rows]
    x0, x1 = padded_range(xs, 0.04)
    y0, y1 = padded_range(ys, 0.04)
    vmin, vmax = min(vals), max(vals)
    absmax = max(abs(vmin), abs(vmax)) if diverge else 0.0

    def sx(x: float) -> float:
        return left + (x - x0) / (x1 - x0) * plot_w

    def sy(y: float) -> float:
        return top + plot_h - (y - y0) / (y1 - y0) * plot_h

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        svg_text(width / 2, 34, title, 22, "middle", "bold"),
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fafafa" stroke="#555"/>',
    ]

    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        gx = left + frac * plot_w
        gy = top + frac * plot_h
        parts.append(f'<line x1="{gx:.1f}" y1="{top}" x2="{gx:.1f}" y2="{top+plot_h}" stroke="#e5e5e5"/>')
        parts.append(f'<line x1="{left}" y1="{gy:.1f}" x2="{left+plot_w}" y2="{gy:.1f}" stroke="#e5e5e5"/>')

    for row in rows:
        value = float(row[key])
        color = diverging(value, absmax) if diverge else sequential(value, vmin, vmax)
        title_text = f"{row['resonator_id']}: {label}={value:.6g}, x={float(row['x_mm']):.3g} mm, y={float(row['y_mm']):.3g} mm"
        parts.append(
            f'<circle cx="{sx(float(row["x_mm"])):.1f}" cy="{sy(float(row["y_mm"])):.1f}" r="11" '
            f'fill="{color}" stroke="#333" stroke-width="0.7"><title>{html.escape(title_text)}</title></circle>'
        )

    parts.extend([
        svg_text(left + plot_w / 2, height - 28, "x (mm)", 15, "middle"),
        f'<text x="24" y="{top + plot_h/2:.1f}" font-family="sans-serif" font-size="15" text-anchor="middle" fill="#222" transform="rotate(-90 24 {top + plot_h/2:.1f})">y (mm)</text>',
        svg_text(left, top + plot_h + 28, f"{x0:.2f}", 12, "middle"),
        svg_text(left + plot_w, top + plot_h + 28, f"{x1:.2f}", 12, "middle"),
        svg_text(left - 12, top + 5, f"{y1:.2f}", 12, "end"),
        svg_text(left - 12, top + plot_h, f"{y0:.2f}", 12, "end"),
    ])

    lx = left + plot_w + 58
    ly = top + 35
    legend_h = plot_h - 70
    steps = 120
    for i in range(steps):
        frac = i / (steps - 1)
        value = (vmax - frac * (vmax - vmin)) if not diverge else (absmax - frac * 2 * absmax)
        color = diverging(value, absmax) if diverge else sequential(value, vmin, vmax)
        y = ly + i * legend_h / steps
        parts.append(f'<rect x="{lx}" y="{y:.2f}" width="24" height="{legend_h/steps + 1:.2f}" fill="{color}"/>')
    parts.append(f'<rect x="{lx}" y="{ly}" width="24" height="{legend_h}" fill="none" stroke="#555"/>')
    parts.append(svg_text(lx + 12, ly - 12, label, 13, "middle", "bold"))
    if diverge:
        parts.append(svg_text(lx + 34, ly + 4, f"{absmax:.1f}", 11))
        parts.append(svg_text(lx + 34, ly + legend_h / 2 + 4, "0", 11))
        parts.append(svg_text(lx + 34, ly + legend_h + 4, f"{-absmax:.1f}", 11))
    else:
        parts.append(svg_text(lx + 34, ly + 4, f"{vmax:.6g}", 11))
        parts.append(svg_text(lx + 34, ly + legend_h + 4, f"{vmin:.6g}", 11))

    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def write_scatter(rows, path: Path) -> None:
    width, height = 820, 640
    left, right, top, bottom = 92, 70, 70, 82
    plot_w = width - left - right
    plot_h = height - top - bottom

    xs = [float(row["predicted_ppm"]) for row in rows]
    ys = [float(row["measured_ppm"]) for row in rows]
    lo, hi = padded_range(xs + ys, 0.08)

    def sx(x: float) -> float:
        return left + (x - lo) / (hi - lo) * plot_w

    def sy(y: float) -> float:
        return top + plot_h - (y - lo) / (hi - lo) * plot_h

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        svg_text(width / 2, 34, "Predictor vs measured frequency error", 22, "middle", "bold"),
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#fafafa" stroke="#555"/>',
    ]
    for frac in (0.0, 0.25, 0.5, 0.75, 1.0):
        value = lo + frac * (hi - lo)
        gx = sx(value)
        gy = sy(value)
        parts.append(f'<line x1="{gx:.1f}" y1="{top}" x2="{gx:.1f}" y2="{top+plot_h}" stroke="#e5e5e5"/>')
        parts.append(f'<line x1="{left}" y1="{gy:.1f}" x2="{left+plot_w}" y2="{gy:.1f}" stroke="#e5e5e5"/>')
        parts.append(svg_text(gx, top + plot_h + 24, f"{value:.0f}", 11, "middle"))
        parts.append(svg_text(left - 10, gy + 4, f"{value:.0f}", 11, "end"))

    parts.append(
        f'<line x1="{sx(lo):.1f}" y1="{sy(lo):.1f}" x2="{sx(hi):.1f}" y2="{sy(hi):.1f}" '
        'stroke="#777" stroke-width="1.4" stroke-dasharray="6 5"/>'
    )
    for row in rows:
        x = float(row["predicted_ppm"])
        y = float(row["measured_ppm"])
        title_text = f"{row['resonator_id']}: predicted={x:.1f} ppm, measured={y:.1f} ppm"
        parts.append(
            f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="5.5" fill="#2a6fbb" fill-opacity="0.78" stroke="#244" stroke-width="0.5">'
            f'<title>{html.escape(title_text)}</title></circle>'
        )

    parts.extend([
        svg_text(left + plot_w / 2, height - 30, "predicted systematic error (ppm)", 15, "middle"),
        f'<text x="25" y="{top + plot_h/2:.1f}" font-family="sans-serif" font-size="15" text-anchor="middle" fill="#222" transform="rotate(-90 25 {top + plot_h/2:.1f})">measured error (ppm)</text>',
        svg_text(left + 12, top + 24, "dashed: y = x", 12),
        '</svg>',
    ])
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


def write_html(out_dir: Path) -> None:
    cards = [
        ("Wafer Rsq map", "wafer_rsq_map.svg"),
        ("Measured frequency-error map", "frequency_error_map.svg"),
        ("Predictor vs measurement", "predictor_vs_measurement.svg"),
        ("Residual map", "residual_map.svg"),
    ]
    items = "\n".join(
        f'<section><h2>{html.escape(title)}</h2><img src="{filename}" alt="{html.escape(title)}"></section>'
        for title, filename in cards
    )
    document = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>KID fabrication feedback diagnostics</title>
<style>
body{{font-family:system-ui,sans-serif;margin:2rem;max-width:1100px;color:#222}}
section{{margin:2rem 0 3rem}} img{{max-width:100%;border:1px solid #ddd}}
.note{{background:#f4f6f8;padding:1rem 1.2rem;border-left:4px solid #4a718c}}
</style></head><body>
<h1>KID fabrication-feedback diagnostics</h1>
<p class="note">These figures visualize the stated model and the measured inputs. They do not establish fabrication root cause by themselves; use independent batches or controlled splits before applying design compensation.</p>
{items}
</body></html>
"""
    (out_dir / "diagnostic_report.html").write_text(document, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--joined", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rows = numeric_rows(read_rows(args.joined))
    write_map(rows, "Rsq_ohm_sq", "Wafer sheet-resistance map", "Rsq (ohm/sq)", args.out / "wafer_rsq_map.svg")
    write_map(rows, "measured_ppm", "Measured resonance-frequency error", "error (ppm)", args.out / "frequency_error_map.svg", diverge=True)
    write_scatter(rows, args.out / "predictor_vs_measurement.svg")
    write_map(rows, "residual_ppm", "Residual after stated model", "residual (ppm)", args.out / "residual_map.svg", diverge=True)
    write_html(args.out)
    print(f"PLOT_DIAGNOSTICS_PASS rows={len(rows)} out={args.out}")


if __name__ == "__main__":
    main()
