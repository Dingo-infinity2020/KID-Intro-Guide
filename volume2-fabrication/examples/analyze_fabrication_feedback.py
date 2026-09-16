#!/usr/bin/env python3
"""Join KID metrology and resonance maps into a transparent feedback report.

The script intentionally does not fit hidden coefficients. The user supplies
film and geometry sensitivities from physics, EM/LC simulation, or a separately
validated batch. This keeps the distinction between "apply a stated model" and
"learn a model from the same data" explicit.

Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
import csv
import math
import statistics
from pathlib import Path
from typing import Iterable


JOINED_FIELDS = [
    "project_id", "batch_id", "wafer_id", "die_id", "resonator_id",
    "x_mm", "y_mm", "design_f0_Hz", "measured_f0_Hz", "Qr",
    "Rsq_ohm_sq", "linewidth_design_um", "linewidth_meas_um",
    "rsq_delta_frac", "linewidth_delta_frac", "measured_delta_f_frac",
    "predicted_film_frac", "predicted_cd_frac", "predicted_systematic_frac",
    "residual_frac", "recommended_design_f0_Hz", "design_correction_Hz",
]

NEXT_DESIGN_FIELDS = [
    "resonator_id", "current_design_f0_Hz", "predicted_systematic_frac",
    "recommended_design_f0_Hz", "design_correction_Hz",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def number(row: dict[str, str], key: str) -> float | None:
    value = (row.get(key) or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def require_columns(rows, required: Iterable[str], label: str) -> None:
    if not rows:
        raise ValueError(f"{label} is empty")
    available = set(rows[0])
    missing = [name for name in required if name not in available]
    if missing:
        raise ValueError(f"{label} is missing required columns: {missing}")


def unique_map(rows, key: str, label: str):
    mapping = {}
    duplicates = []
    for row in rows:
        value = (row.get(key) or "").strip()
        if not value:
            continue
        if value in mapping:
            duplicates.append(value)
        mapping[value] = row
    if duplicates:
        sample = sorted(set(duplicates))[:5]
        raise ValueError(f"duplicate {key} in {label}: {sample}")
    return mapping


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2 or len(xs) != len(ys):
        return None
    mean_x = statistics.mean(xs)
    mean_y = statistics.mean(ys)
    dx = [value - mean_x for value in xs]
    dy = [value - mean_y for value in ys]
    denominator = math.sqrt(
        sum(value * value for value in dx) * sum(value * value for value in dy)
    )
    if denominator == 0.0:
        return None
    return sum(x * y for x, y in zip(dx, dy)) / denominator


def format_optional(value: float | None, digits: int = 4) -> str:
    return "NA" if value is None else f"{value:.{digits}f}"


def detect_collisions(rows, margin_linewidths: float):
    usable = []
    for row in rows:
        frequency_hz = number(row, "measured_f0_Hz")
        q_r = number(row, "Qr")
        resonator_id = (row.get("resonator_id") or "").strip()
        if frequency_hz is not None and q_r is not None and q_r > 0.0:
            usable.append((frequency_hz, q_r, resonator_id))

    usable.sort()
    collisions = []
    for left, right in zip(usable, usable[1:]):
        f_left, q_left, id_left = left
        f_right, q_right, id_right = right
        separation_hz = f_right - f_left
        threshold_hz = margin_linewidths * max(
            f_left / q_left, f_right / q_right
        )
        if separation_hz < threshold_hz:
            collisions.append({
                "left_resonator": id_left,
                "right_resonator": id_right,
                "separation_hz": separation_hz,
                "threshold_hz": threshold_hz,
            })
    return collisions


def join_feedback(
    metrology_rows,
    resonator_rows,
    alpha_k: float,
    rsq_reference_ohm_sq: float,
    linewidth_sensitivity: float,
):
    require_columns(
        metrology_rows,
        [
            "resonator_id", "Rsq_ohm_sq", "linewidth_design_um",
            "linewidth_meas_um",
        ],
        "metrology CSV",
    )
    require_columns(
        resonator_rows,
        ["resonator_id", "design_f0_Hz", "measured_f0_Hz", "Qr"],
        "resonator CSV",
    )

    metrology = unique_map(metrology_rows, "resonator_id", "metrology CSV")
    resonators = unique_map(resonator_rows, "resonator_id", "resonator CSV")
    unmatched_metrology = set(metrology) - set(resonators)
    unmatched_resonators = set(resonators) - set(metrology)
    common_ids = sorted(set(metrology) & set(resonators))

    joined = []
    excluded_incomplete = []
    for resonator_id in common_ids:
        metrology_row = metrology[resonator_id]
        resonator_row = resonators[resonator_id]

        design_hz = number(resonator_row, "design_f0_Hz")
        measured_hz = number(resonator_row, "measured_f0_Hz")
        rsq_ohm_sq = number(metrology_row, "Rsq_ohm_sq")
        linewidth_design_um = number(metrology_row, "linewidth_design_um")
        linewidth_meas_um = number(metrology_row, "linewidth_meas_um")

        if (
            design_hz is None or design_hz <= 0.0 or measured_hz is None
            or rsq_ohm_sq is None or linewidth_design_um is None
            or linewidth_design_um == 0.0 or linewidth_meas_um is None
        ):
            excluded_incomplete.append(resonator_id)
            continue

        measured_delta_frac = (measured_hz - design_hz) / design_hz
        rsq_delta_frac = (
            rsq_ohm_sq - rsq_reference_ohm_sq
        ) / rsq_reference_ohm_sq
        linewidth_delta_frac = (
            linewidth_meas_um - linewidth_design_um
        ) / linewidth_design_um

        predicted_film_frac = -0.5 * alpha_k * rsq_delta_frac
        predicted_cd_frac = linewidth_sensitivity * linewidth_delta_frac
        predicted_systematic_frac = predicted_film_frac + predicted_cd_frac
        residual_frac = measured_delta_frac - predicted_systematic_frac
        denominator = 1.0 + predicted_systematic_frac
        if denominator == 0.0:
            excluded_incomplete.append(resonator_id)
            continue
        recommended_design_hz = design_hz / denominator

        joined.append({
            "project_id": resonator_row.get("project_id", ""),
            "batch_id": resonator_row.get("batch_id", ""),
            "wafer_id": resonator_row.get("wafer_id", ""),
            "die_id": resonator_row.get("die_id", ""),
            "resonator_id": resonator_id,
            "x_mm": resonator_row.get("x_mm") or metrology_row.get("x_mm", ""),
            "y_mm": resonator_row.get("y_mm") or metrology_row.get("y_mm", ""),
            "design_f0_Hz": design_hz,
            "measured_f0_Hz": measured_hz,
            "Qr": number(resonator_row, "Qr") or "",
            "Rsq_ohm_sq": rsq_ohm_sq,
            "linewidth_design_um": linewidth_design_um,
            "linewidth_meas_um": linewidth_meas_um,
            "rsq_delta_frac": rsq_delta_frac,
            "linewidth_delta_frac": linewidth_delta_frac,
            "measured_delta_f_frac": measured_delta_frac,
            "predicted_film_frac": predicted_film_frac,
            "predicted_cd_frac": predicted_cd_frac,
            "predicted_systematic_frac": predicted_systematic_frac,
            "residual_frac": residual_frac,
            "recommended_design_f0_Hz": recommended_design_hz,
            "design_correction_Hz": recommended_design_hz - design_hz,
        })

    return joined, excluded_incomplete, unmatched_metrology, unmatched_resonators


def write_outputs(
    joined,
    resonator_rows,
    excluded_incomplete,
    unmatched_metrology,
    unmatched_resonators,
    args,
) -> str:
    if len(joined) < 2:
        raise ValueError(
            "Need at least two complete resonator joins for summary statistics."
        )

    args.out.mkdir(parents=True, exist_ok=True)
    with (args.out / "joined_feedback.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=JOINED_FIELDS)
        writer.writeheader()
        writer.writerows(joined)

    with (args.out / "next_design.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=NEXT_DESIGN_FIELDS)
        writer.writeheader()
        for row in joined:
            writer.writerow({
                "resonator_id": row["resonator_id"],
                "current_design_f0_Hz": row["design_f0_Hz"],
                "predicted_systematic_frac": row["predicted_systematic_frac"],
                "recommended_design_f0_Hz": row["recommended_design_f0_Hz"],
                "design_correction_Hz": row["design_correction_Hz"],
            })

    measured_errors = [float(row["measured_delta_f_frac"]) for row in joined]
    predictions = [float(row["predicted_systematic_frac"]) for row in joined]
    residuals = [float(row["residual_frac"]) for row in joined]
    rsq_deltas = [float(row["rsq_delta_frac"]) for row in joined]
    linewidth_deltas = [float(row["linewidth_delta_frac"]) for row in joined]
    collisions = detect_collisions(
        resonator_rows, args.collision_margin_linewidths
    )

    lines = [
        "KID Volume 2 fabrication-feedback analysis",
        "==========================================",
        "",
        f"joined_resonators={len(joined)}",
        f"excluded_incomplete={len(excluded_incomplete)}",
        f"unmatched_metrology={len(unmatched_metrology)}",
        f"unmatched_resonators={len(unmatched_resonators)}",
        f"measured_error_mean_ppm={statistics.mean(measured_errors) * 1e6:.1f}",
        f"measured_error_std_ppm={statistics.pstdev(measured_errors) * 1e6:.1f}",
        f"predicted_systematic_std_ppm={statistics.pstdev(predictions) * 1e6:.1f}",
        f"residual_mean_ppm={statistics.mean(residuals) * 1e6:.1f}",
        f"residual_std_ppm={statistics.pstdev(residuals) * 1e6:.1f}",
        "corr_error_rsq_delta=" + format_optional(
            pearson(measured_errors, rsq_deltas)
        ),
        "corr_error_linewidth_delta=" + format_optional(
            pearson(measured_errors, linewidth_deltas)
        ),
        f"current_collision_pairs={len(collisions)}",
        "",
        f"alpha_k={args.alpha_k:g}",
        f"rsq_reference_ohm_sq={args.rsq_reference_ohm_sq:g}",
        f"linewidth_sensitivity={args.linewidth_sensitivity:g}",
        f"collision_margin_linewidths={args.collision_margin_linewidths:g}",
        "",
        "Coefficients are inputs, not fitted by this script.",
        "Validate them on independent batches before using next_design.csv",
        "as a design decision.",
    ]
    summary = "\n".join(lines) + "\n"
    (args.out / "analysis_summary.txt").write_text(summary, encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Join KID fabrication metrology and resonance maps without fitting "
            "hidden model coefficients."
        )
    )
    parser.add_argument("--metrology", type=Path, required=True)
    parser.add_argument("--resonators", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--alpha-k", type=float, required=True)
    parser.add_argument("--rsq-reference-ohm-sq", type=float, required=True)
    parser.add_argument("--linewidth-sensitivity", type=float, required=True)
    parser.add_argument("--collision-margin-linewidths", type=float, default=5.0)
    args = parser.parse_args()

    if args.rsq_reference_ohm_sq <= 0.0:
        parser.error("--rsq-reference-ohm-sq must be positive")
    if args.collision_margin_linewidths <= 0.0:
        parser.error("--collision-margin-linewidths must be positive")

    metrology_rows = read_csv(args.metrology)
    resonator_rows = read_csv(args.resonators)
    joined, excluded, unmatched_metrology, unmatched_resonators = join_feedback(
        metrology_rows,
        resonator_rows,
        args.alpha_k,
        args.rsq_reference_ohm_sq,
        args.linewidth_sensitivity,
    )
    summary = write_outputs(
        joined, resonator_rows, excluded,
        unmatched_metrology, unmatched_resonators, args,
    )
    print(summary, end="")


if __name__ == "__main__":
    main()
