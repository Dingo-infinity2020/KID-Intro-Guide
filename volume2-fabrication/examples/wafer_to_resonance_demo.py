#!/usr/bin/env python3
"""Synthetic wafer-to-resonance feedback demo for KID Volume 2.

This is a teaching example, not a fabrication recipe and not a claim about a
specific laboratory process. The numbers are deliberately synthetic.

The demo connects:
  wafer metrology -> simple frequency-shift surrogate -> collision audit
  -> model-based pre-compensation for the next design revision.

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


def build_records(seed: int = RNG_SEED):
    """Create a deterministic synthetic 8x8 wafer/resonator data set."""
    rng = random.Random(seed)
    rows = []

    for row in range(NSIDE):
        for col in range(NSIDE):
            pixel_id = row * NSIDE + col
            x_norm = (col - (NSIDE - 1) / 2) / ((NSIDE - 1) / 2)
            y_norm = (row - (NSIDE - 1) / 2) / ((NSIDE - 1) / 2)

            # Synthetic spatial structure + small random component.
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

            rsq_ohm = R_SQ_NOM_OHM * (1.0 + rsq_frac)
            linewidth_um = LINEWIDTH_NOM_UM + linewidth_delta_um

            # Film term follows the small-signal relation used in the guide:
            # df/f ~= -(alpha/2) dLk/Lk, with Lk,sq proportional to Rsq here.
            frac_shift_film = -0.5 * ALPHA_K * (
                (rsq_ohm - R_SQ_NOM_OHM) / R_SQ_NOM_OHM
            )

            # The linewidth coefficient is a placeholder surrogate that, in a
            # real project, must come from EM/LC sensitivity or measured data.
            frac_shift_cd = WIDTH_SENSITIVITY * (
                (linewidth_um - LINEWIDTH_NOM_UM) / LINEWIDTH_NOM_UM
            )

            frac_shift_unmodeled = rng.gauss(0.0, 0.00012)
            frac_shift_total = (
                frac_shift_film + frac_shift_cd + frac_shift_unmodeled
            )

            target_hz = F_START_HZ + pixel_id * DESIGN_SPACING_HZ
            design_hz_before = target_hz
            measured_hz_before = design_hz_before * (1.0 + frac_shift_total)

            # If the systematic predictor is repeatable, compensate the next
            # design so the expected fabricated frequency lands on target.
            predicted_frac_shift = frac_shift_film + frac_shift_cd
            design_hz_after = target_hz / (1.0 + predicted_frac_shift)
            measured_hz_after = design_hz_after * (1.0 + frac_shift_total)

            rows.append(
                {
                    "pixel_id": f"P{pixel_id:03d}",
                    "row": row,
                    "col": col,
                    "x_norm": x_norm,
                    "y_norm": y_norm,
                    "rsq_ohm_sq": rsq_ohm,
                    "linewidth_um": linewidth_um,
                    "frac_shift_film": frac_shift_film,
                    "frac_shift_cd": frac_shift_cd,
                    "frac_shift_unmodeled": frac_shift_unmodeled,
                    "predicted_frac_shift": predicted_frac_shift,
                    "target_hz": target_hz,
                    "design_hz_before": design_hz_before,
                    "measured_hz_before": measured_hz_before,
                    "design_hz_after": design_hz_after,
                    "measured_hz_after": measured_hz_after,
                    "qr": Q_R,
                }
            )

    return rows


def detect_collisions(rows, frequency_key):
    """Find adjacent measured resonances closer than a configurable margin."""
    ordered = sorted(rows, key=lambda r: r[frequency_key])
    collisions = []
    involved = set()

    for left, right in zip(ordered, ordered[1:]):
        f_left = left[frequency_key]
        f_right = right[frequency_key]
        separation_hz = f_right - f_left
        linewidth_hz = max(f_left / left["qr"], f_right / right["qr"])
        threshold_hz = COLLISION_MARGIN_LINEWIDTHS * linewidth_hz

        if separation_hz < threshold_hz:
            collisions.append(
                {
                    "left_pixel": left["pixel_id"],
                    "right_pixel": right["pixel_id"],
                    "separation_hz": separation_hz,
                    "threshold_hz": threshold_hz,
                }
            )
            involved.add(left["pixel_id"])
            involved.add(right["pixel_id"])

    return collisions, involved


def write_wafer_csv(rows, path):
    fields = [
        "pixel_id",
        "row",
        "col",
        "x_norm",
        "y_norm",
        "rsq_ohm_sq",
        "linewidth_um",
        "frac_shift_film",
        "frac_shift_cd",
        "predicted_frac_shift",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_resonator_csv(rows, path):
    fields = [
        "pixel_id",
        "target_hz",
        "design_hz_before",
        "measured_hz_before",
        "design_hz_after",
        "measured_hz_after",
        "frac_shift_unmodeled",
        "qr",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def ppm_error(row, measured_key):
    return 1e6 * (row[measured_key] - row["target_hz"]) / row["target_hz"]


def build_summary(rows):
    before_collisions, before_involved = detect_collisions(
        rows, "measured_hz_before"
    )
    after_collisions, after_involved = detect_collisions(
        rows, "measured_hz_after"
    )

    before_ppm = [ppm_error(r, "measured_hz_before") for r in rows]
    after_ppm = [ppm_error(r, "measured_hz_after") for r in rows]

    summary = {
        "n_resonators": len(rows),
        "before_collision_pairs": len(before_collisions),
        "before_collision_resonators": len(before_involved),
        "after_collision_pairs": len(after_collisions),
        "after_collision_resonators": len(after_involved),
        "before_mean_error_ppm": statistics.mean(before_ppm),
        "before_std_error_ppm": statistics.pstdev(before_ppm),
        "after_mean_error_ppm": statistics.mean(after_ppm),
        "after_std_error_ppm": statistics.pstdev(after_ppm),
        "before_max_abs_error_mhz": max(
            abs(r["measured_hz_before"] - r["target_hz"]) for r in rows
        )
        / 1e6,
        "after_max_abs_error_mhz": max(
            abs(r["measured_hz_after"] - r["target_hz"]) for r in rows
        )
        / 1e6,
    }

    # Deterministic smoke-test conditions for CI.
    if not summary["after_std_error_ppm"] < summary["before_std_error_ppm"]:
        raise RuntimeError("Expected pre-compensation to reduce synthetic scatter.")
    if not summary["after_collision_pairs"] <= summary["before_collision_pairs"]:
        raise RuntimeError("Expected pre-compensation not to increase collisions.")

    return summary, before_collisions, after_collisions


def write_summary(summary, before_collisions, after_collisions, path):
    lines = [
        "KID Volume 2 synthetic wafer-to-resonance demo",
        "================================================",
        "",
        "These values are synthetic teaching data, not measured device results.",
        "",
        f"resonators: {summary['n_resonators']}",
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
                "  "
                f"{item['left_pixel']} / {item['right_pixel']}: "
                f"{item['separation_hz']/1e3:.1f} kHz "
                f"(threshold {item['threshold_hz']/1e3:.1f} kHz)"
            )

    if after_collisions:
        lines.extend(["", "after collision pairs:"])
        for item in after_collisions:
            lines.append(
                "  "
                f"{item['left_pixel']} / {item['right_pixel']}: "
                f"{item['separation_hz']/1e3:.1f} kHz "
                f"(threshold {item['threshold_hz']/1e3:.1f} kHz)"
            )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("build/example-wafer-loop"),
        help="output directory",
    )
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    rows = build_records()
    summary, before_collisions, after_collisions = build_summary(rows)

    write_wafer_csv(rows, args.out / "wafer_metrology_map.csv")
    write_resonator_csv(rows, args.out / "resonator_map.csv")
    write_summary(
        summary,
        before_collisions,
        after_collisions,
        args.out / "summary.txt",
    )

    print((args.out / "summary.txt").read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
