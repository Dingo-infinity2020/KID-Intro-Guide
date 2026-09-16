#!/usr/bin/env python3
"""Compare fabrication-feedback model behavior across independent batches.

The input is one or more ``joined_feedback.csv`` files. The tool summarizes
model residuals and predictor-vs-measurement agreement without declaring a
universal PASS/FAIL threshold; acceptable repeatability is project-specific.
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics
from pathlib import Path


FIELDS = [
    "label", "batch_id", "wafer_id", "n_resonators",
    "measured_mean_ppm", "measured_std_ppm",
    "predicted_mean_ppm", "predicted_std_ppm",
    "residual_mean_ppm", "residual_std_ppm", "residual_rmse_ppm",
    "corr_predicted_measured", "slope_measured_vs_predicted",
    "intercept_measured_ppm",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    required = {"measured_delta_f_frac", "predicted_systematic_frac", "residual_frac"}
    if not rows:
        raise ValueError(f"{path} is empty")
    missing = sorted(required - set(rows[0]))
    if missing:
        raise ValueError(f"{path} missing columns: {missing}")
    return rows


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2:
        return None
    mx, my = statistics.mean(xs), statistics.mean(ys)
    dx = [x - mx for x in xs]
    dy = [y - my for y in ys]
    denom = math.sqrt(sum(x*x for x in dx) * sum(y*y for y in dy))
    if denom == 0.0:
        return None
    return sum(x*y for x, y in zip(dx, dy)) / denom


def regression(xs: list[float], ys: list[float]) -> tuple[float | None, float | None]:
    if len(xs) < 2:
        return None, None
    mx, my = statistics.mean(xs), statistics.mean(ys)
    denom = sum((x - mx) ** 2 for x in xs)
    if denom == 0.0:
        return None, None
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / denom
    return slope, my - slope * mx


def summarize(label: str, path: Path) -> dict[str, object]:
    rows = read_csv(path)
    measured, predicted, residual = [], [], []
    for row in rows:
        try:
            measured.append(1.0e6 * float(row["measured_delta_f_frac"]))
            predicted.append(1.0e6 * float(row["predicted_systematic_frac"]))
            residual.append(1.0e6 * float(row["residual_frac"]))
        except (TypeError, ValueError):
            continue
    if len(measured) < 2:
        raise ValueError(f"{path} has fewer than two complete numeric rows")
    corr = pearson(predicted, measured)
    slope, intercept = regression(predicted, measured)
    batch_ids = sorted({(r.get("batch_id") or "").strip() for r in rows if (r.get("batch_id") or "").strip()})
    wafer_ids = sorted({(r.get("wafer_id") or "").strip() for r in rows if (r.get("wafer_id") or "").strip()})
    return {
        "label": label,
        "batch_id": ";".join(batch_ids),
        "wafer_id": ";".join(wafer_ids),
        "n_resonators": len(measured),
        "measured_mean_ppm": statistics.mean(measured),
        "measured_std_ppm": statistics.pstdev(measured),
        "predicted_mean_ppm": statistics.mean(predicted),
        "predicted_std_ppm": statistics.pstdev(predicted),
        "residual_mean_ppm": statistics.mean(residual),
        "residual_std_ppm": statistics.pstdev(residual),
        "residual_rmse_ppm": math.sqrt(statistics.mean([x*x for x in residual])),
        "corr_predicted_measured": corr,
        "slope_measured_vs_predicted": slope,
        "intercept_measured_ppm": intercept,
    }


def fmt(value: object, digits: int = 3) -> str:
    if value is None:
        return "NA"
    if isinstance(value, float):
        return f"{value:.{digits}f}"
    return str(value)


def parse_item(text: str) -> tuple[str, Path]:
    if "=" not in text:
        raise argparse.ArgumentTypeError("use LABEL=PATH")
    label, raw_path = text.split("=", 1)
    label = label.strip()
    if not label:
        raise argparse.ArgumentTypeError("label must not be empty")
    return label, Path(raw_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--joined", action="append", type=parse_item, required=True, metavar="LABEL=PATH")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if len(args.joined) < 2:
        parser.error("provide at least two --joined LABEL=PATH inputs")
    labels = [label for label, _ in args.joined]
    if len(set(labels)) != len(labels):
        parser.error("labels must be unique")

    summaries = [summarize(label, path) for label, path in args.joined]
    args.out.mkdir(parents=True, exist_ok=True)

    with (args.out / "batch_summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(summaries)

    lines = [
        "# Fabrication-feedback cross-batch comparison",
        "",
        "This report compares the same stated predictor across batches. It deliberately does not define a universal acceptance threshold.",
        "",
        "| label | batch | N | measured std (ppm) | residual std (ppm) | corr(pred, meas) | slope meas/pred | residual mean (ppm) |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for row in summaries:
        lines.append(
            f"| {row['label']} | {row['batch_id'] or '-'} | {row['n_resonators']} | "
            f"{fmt(row['measured_std_ppm'], 1)} | {fmt(row['residual_std_ppm'], 1)} | "
            f"{fmt(row['corr_predicted_measured'], 3)} | {fmt(row['slope_measured_vs_predicted'], 3)} | "
            f"{fmt(row['residual_mean_ppm'], 1)} |"
        )
    lines.extend([
        "",
        "## How to read this table",
        "",
        "A predictor is more credible when its sign and scale remain useful on an independent batch, its residual distribution stays centered and substantially narrower than the raw measured error, and unexplained spatial structure does not simply migrate elsewhere. These are evidence checks, not proof of root cause.",
        "",
        "Before writing any correction into a new GDS, also inspect the residual maps and confirm that process/tool/revision changes have not invalidated the model provenance.",
    ])
    (args.out / "repeatability_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"BATCH_COMPARISON_PASS batches={len(summaries)} out={args.out}")


if __name__ == "__main__":
    main()
