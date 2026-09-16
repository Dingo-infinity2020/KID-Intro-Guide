#!/usr/bin/env python3
"""Synthetic wafer-to-resonance feedback demo for KID Volume 2.

This is a teaching example, not a fabrication recipe and not a claim about a
specific laboratory process. All numbers are deliberately synthetic.

The demo connects:
  wafer metrology -> frequency-shift surrogate -> collision audit
  -> model-based pre-compensation for the next design revision.

The two primary CSV files use the same column contracts as the templates.
Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
import csv
import random
import statistics
from pathlib import Path


NSIDE = 8
F_START_HZ = 2.0e9
DESIGN_SPACING_HZ = 2.0e6
R_SQ_NOM_OHM = 0.45
LINEWIDTH_NOM_UM = 2.0
ALPHA_K = 0.45
WIDTH_SENSITIVITY = 0.08
Q_R = 40_000.0
COLLISION_MARGIN_LINEWIDTHS = 5.0
RNG_SEED = 20260916

PROJECT_ID = "SYNTH_DEMO"
BATCH_ID = "SYNTH_B001"
WAFER_ID = "W01"
DIE_ID = "D01"
METROLOGY_RUN_ID = "MET_SYNTH_001"
GDS_REVISION = "SYNTH_G0"
PACKAGE_ID = "PKG_SYNTH_001"
COOLDOWN_ID = "CD_SYNTH_001"

WAFER_FIELDS = [
    "project_id", "batch_id", "wafer_id", "die_id", "resonator_id",
    "metrology_run_id", "measurement_id", "feature_id", "feature_type",
    "x_mm", "y_mm", "thickness_nm", "Rsq_ohm_sq", "Tc_K",
    "linewidth_design_um", "linewidth_meas_um", "gap_design_um",
    "gap_meas_um", "etch_or_recess_nm", "continuity_status", "defect_class",
    "measurement_method", "tool_id", "status", "notes",
]

RESONATOR_FIELDS = [
    "project_id", "batch_id", "wafer_id", "die_id", "resonator_id",
    "gds_revision", "package_id", "cooldown_id", "x_mm", "y_mm",
    "design_f0_Hz", "measured_f0_Hz", "delta_f_Hz", "delta_f_frac", "Qr",
    "Qi", "Qc", "fit_status", "mapping_status", "collision_status",
    "readout_power_dBm", "stage_temperature_K", "notes",
]

TRUTH_FIELDS = [
    "resonator_id", "row", "col", "frac_shift_film", "frac_shift_cd",
    "frac_shift_unmodeled", "predicted_frac_shift", "design_f0_after_Hz",
    "measured_f0_after_Hz",
]


def build_records(seed=RNG_SEED):
    rng = random.Random(seed)
    rows = []
    for row in range(NSIDE):
        for col in range(NSIDE):
            index = row * NSIDE + col
            resonator_id = f"R{index:03d}"
            x_norm = (col - 3.5) / 3.5
            y_norm = (row - 3.5) / 3.5
            x_mm = col - 3.5
            y_mm = row - 3.5

            rsq_frac = (
                0.0040 * x_norm
                + 0.0015 * (x_norm * x_norm + y_norm * y_norm - 0.65)
                + rng.gauss(0.0, 0.0005)
            )
            linewidth_delta_um = (
                0.025 * y_norm
                + 0.008 * x_norm
                + rng.gauss(0.0, 0.005)
            )
            rsq_ohm_sq = R_SQ_NOM_OHM * (1.0 + rsq_frac)
            linewidth_um = LINEWIDTH_NOM_UM + linewidth_delta_um

            frac_shift_film = -0.5 * ALPHA_K * (
                (rsq_ohm_sq - R_SQ_NOM_OHM) / R_SQ_NOM_OHM
            )
            frac_shift_cd = WIDTH_SENSITIVITY * (
                (linewidth_um - LINEWIDTH_NOM_UM) / LINEWIDTH_NOM_UM
            )
            frac_shift_unmodeled = rng.gauss(0.0, 0.00012)
            frac_shift_total = (
                frac_shift_film + frac_shift_cd + frac_shift_unmodeled
            )

            target_hz = F_START_HZ + index * DESIGN_SPACING_HZ
            measured_hz_before = target_hz * (1.0 + frac_shift_total)
            predicted_frac_shift = frac_shift_film + frac_shift_cd
            design_hz_after = target_hz / (1.0 + predicted_frac_shift)
            measured_hz_after = design_hz_after * (1.0 + frac_shift_total)

            rows.append({
                "resonator_id": resonator_id,
                "row": row,
                "col": col,
                "x_mm": x_mm,
                "y_mm": y_mm,
                "rsq_ohm_sq": rsq_ohm_sq,
                "linewidth_um": linewidth_um,
                "frac_shift_film": frac_shift_film,
                "frac_shift_cd": frac_shift_cd,
                "frac_shift_unmodeled": frac_shift_unmodeled,
                "predicted_frac_shift": predicted_frac_shift,
                "target_hz": target_hz,
                "measured_hz_before": measured_hz_before,
                "design_hz_after": design_hz_after,
                "measured_hz_after": measured_hz_after,
                "qr": Q_R,
            })
    return rows


def detect_collisions(rows, frequency_key):
    ordered = sorted(rows, key=lambda item: item[frequency_key])
    collisions = []
    involved = set()
    for left, right in zip(ordered, ordered[1:]):
        f_left = left[frequency_key]
        f_right = right[frequency_key]
        separation_hz = f_right - f_left
        linewidth_hz = max(f_left / left["qr"], f_right / right["qr"])
        threshold_hz = COLLISION_MARGIN_LINEWIDTHS * linewidth_hz
        if separation_hz < threshold_hz:
            collisions.append({
                "left_resonator": left["resonator_id"],
                "right_resonator": right["resonator_id"],
                "separation_hz": separation_hz,
                "threshold_hz": threshold_hz,
            })
            involved.update((left["resonator_id"], right["resonator_id"]))
    return collisions, involved


def write_wafer_csv(rows, path):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=WAFER_FIELDS)
        writer.writeheader()
        for index, row in enumerate(rows):
            writer.writerow({
                "project_id": PROJECT_ID,
                "batch_id": BATCH_ID,
                "wafer_id": WAFER_ID,
                "die_id": DIE_ID,
                "resonator_id": row["resonator_id"],
                "metrology_run_id": METROLOGY_RUN_ID,
                "measurement_id": f"M{index:03d}",
                "feature_id": f"F{index:03d}",
                "feature_type": "resonator_trace",
                "x_mm": f"{row['x_mm']:.3f}",
                "y_mm": f"{row['y_mm']:.3f}",
                "thickness_nm": "",
                "Rsq_ohm_sq": f"{row['rsq_ohm_sq']:.9g}",
                "Tc_K": "",
                "linewidth_design_um": f"{LINEWIDTH_NOM_UM:.6g}",
                "linewidth_meas_um": f"{row['linewidth_um']:.9g}",
                "gap_design_um": "",
                "gap_meas_um": "",
                "etch_or_recess_nm": "",
                "continuity_status": "PASS",
                "defect_class": "",
                "measurement_method": "synthetic_demo",
                "tool_id": "SYNTHETIC",
                "status": "PASS",
                "notes": "synthetic teaching data",
            })


def write_resonator_csv(rows, collision_resonators, path):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=RESONATOR_FIELDS)
        writer.writeheader()
        for row in rows:
            target_hz = row["target_hz"]
            measured_hz = row["measured_hz_before"]
            delta_hz = measured_hz - target_hz
            resonator_id = row["resonator_id"]
            writer.writerow({
                "project_id": PROJECT_ID,
                "batch_id": BATCH_ID,
                "wafer_id": WAFER_ID,
                "die_id": DIE_ID,
                "resonator_id": resonator_id,
                "gds_revision": GDS_REVISION,
                "package_id": PACKAGE_ID,
                "cooldown_id": COOLDOWN_ID,
                "x_mm": f"{row['x_mm']:.3f}",
                "y_mm": f"{row['y_mm']:.3f}",
                "design_f0_Hz": f"{target_hz:.9f}",
                "measured_f0_Hz": f"{measured_hz:.9f}",
                "delta_f_Hz": f"{delta_hz:.9f}",
                "delta_f_frac": f"{delta_hz / target_hz:.12g}",
                "Qr": f"{row['qr']:.9g}",
                "Qi": "",
                "Qc": "",
                "fit_status": "PASS",
                "mapping_status": "MATCHED",
                "collision_status": (
                    "COLLISION_CANDIDATE"
                    if resonator_id in collision_resonators else "PASS"
                ),
                "readout_power_dBm": "",
                "stage_temperature_K": "",
                "notes": "synthetic teaching data",
            })


def write_truth_csv(rows, path):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRUTH_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "resonator_id": row["resonator_id"],
                "row": row["row"],
                "col": row["col"],
                "frac_shift_film": f"{row['frac_shift_film']:.12g}",
                "frac_shift_cd": f"{row['frac_shift_cd']:.12g}",
                "frac_shift_unmodeled": f"{row['frac_shift_unmodeled']:.12g}",
                "predicted_frac_shift": f"{row['predicted_frac_shift']:.12g}",
                "design_f0_after_Hz": f"{row['design_hz_after']:.9f}",
                "measured_f0_after_Hz": f"{row['measured_hz_after']:.9f}",
            })


def ppm_error(row, measured_key):
    return 1.0e6 * (row[measured_key] - row["target_hz"]) / row["target_hz"]


def build_summary(rows):
    before_collisions, _ = detect_collisions(rows, "measured_hz_before")
    after_collisions, _ = detect_collisions(rows, "measured_hz_after")
    before_ppm = [ppm_error(row, "measured_hz_before") for row in rows]
    after_ppm = [ppm_error(row, "measured_hz_after") for row in rows]
    summary = {
        "n_resonators": len(rows),
        "before_collision_pairs": len(before_collisions),
        "after_collision_pairs": len(after_collisions),
        "before_mean_error_ppm": statistics.mean(before_ppm),
        "before_std_error_ppm": statistics.pstdev(before_ppm),
        "after_mean_error_ppm": statistics.mean(after_ppm),
        "after_std_error_ppm": statistics.pstdev(after_ppm),
        "before_max_abs_error_mhz": max(
            abs(row["measured_hz_before"] - row["target_hz"]) for row in rows
        ) / 1.0e6,
        "after_max_abs_error_mhz": max(
            abs(row["measured_hz_after"] - row["target_hz"]) for row in rows
        ) / 1.0e6,
    }
    if summary["after_std_error_ppm"] >= summary["before_std_error_ppm"]:
        raise RuntimeError("Expected pre-compensation to reduce synthetic scatter.")
    if summary["after_collision_pairs"] > summary["before_collision_pairs"]:
        raise RuntimeError("Expected pre-compensation not to increase collisions.")
    return summary, before_collisions, after_collisions


def write_summary(summary, before_collisions, after_collisions, path):
    lines = [
        "KID Volume 2 synthetic wafer-to-resonance demo",
        "================================================",
        "",
        "These values are synthetic teaching data, not measured device results.",
        "",
        f"resonators={summary['n_resonators']}",
        (
            "before: "
            f"mean_error={summary['before_mean_error_ppm']:.1f} ppm, "
            f"std_error={summary['before_std_error_ppm']:.1f} ppm, "
            f"max_abs_error={summary['before_max_abs_error_mhz']:.3f} MHz, "
            f"collision_pairs={summary['before_collision_pairs']}"
        ),
        (
            "after model-based pre-compensation: "
            f"mean_error={summary['after_mean_error_ppm']:.1f} ppm, "
            f"std_error={summary['after_std_error_ppm']:.1f} ppm, "
            f"max_abs_error={summary['after_max_abs_error_mhz']:.3f} MHz, "
            f"collision_pairs={summary['after_collision_pairs']}"
        ),
        "",
        (
            "collision rule: adjacent measured resonances are flagged when "
            f"separation < {COLLISION_MARGIN_LINEWIDTHS:g} loaded linewidths"
        ),
        "",
        "Important: WIDTH_SENSITIVITY and the synthetic wafer maps are demo",
        "parameters. A real project must replace them with measured or",
        "simulation-derived sensitivities and process statistics.",
    ]
    if before_collisions:
        lines.extend(["", "before collision pairs:"])
        for item in before_collisions:
            lines.append(
                f"  {item['left_resonator']} / {item['right_resonator']}: "
                f"{item['separation_hz'] / 1e3:.1f} kHz "
                f"(threshold {item['threshold_hz'] / 1e3:.1f} kHz)"
            )
    if after_collisions:
        lines.extend(["", "after collision pairs:"])
        for item in after_collisions:
            lines.append(
                f"  {item['left_resonator']} / {item['right_resonator']}: "
                f"{item['separation_hz'] / 1e3:.1f} kHz "
                f"(threshold {item['threshold_hz'] / 1e3:.1f} kHz)"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out", type=Path, default=Path("build/example-wafer-loop"),
        help="output directory",
    )
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    rows = build_records()
    summary, before_collisions, after_collisions = build_summary(rows)
    _, before_collision_resonators = detect_collisions(rows, "measured_hz_before")
    write_wafer_csv(rows, args.out / "wafer_metrology_map.csv")
    write_resonator_csv(
        rows, before_collision_resonators, args.out / "resonator_map.csv"
    )
    write_truth_csv(rows, args.out / "synthetic_truth.csv")
    write_summary(
        summary, before_collisions, after_collisions, args.out / "summary.txt"
    )
    print((args.out / "summary.txt").read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
