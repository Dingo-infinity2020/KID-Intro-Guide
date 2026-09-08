"""Circular-waveguide cutoff demo for KID optical coupling.

Educational model used in KID Intro Guide v0.7.
It computes TE11, TM01 and TE21 cutoff frequencies for a circular waveguide
and plots them against waveguide diameter.  The default D=1.6 mm example
matches the 150 GHz dual-polarization LEKID discussion in the guide.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

C0 = 299_792_458.0
ROOTS = {
    "TE11": 1.8412,
    "TM01": 2.4048,
    "TE21": 3.0542,
}


def cutoff_hz(diameter_m: float | np.ndarray, root: float) -> np.ndarray:
    return root * C0 / (np.pi * np.asarray(diameter_m))


def main() -> None:
    diameter0 = 1.6e-3
    print("Circular waveguide, D = 1.6 mm")
    for name, root in ROOTS.items():
        fc = float(cutoff_hz(diameter0, root))
        print(f"  {name:4s}: {fc / 1e9:8.3f} GHz")

    print("\nAt 149-151 GHz:")
    for name, root in ROOTS.items():
        fc = float(cutoff_hz(diameter0, root))
        state = "propagating" if fc < 149e9 else "cut off"
        print(f"  {name:4s}: {state}")

    diameters_mm = np.linspace(1.3, 2.0, 300)
    diameters_m = diameters_mm * 1e-3

    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    for name, root in ROOTS.items():
        ax.plot(diameters_mm, cutoff_hz(diameters_m, root) / 1e9, label=name)

    ax.axhspan(149.0, 151.0, alpha=0.15, label="149-151 GHz band")
    ax.axvline(1.6, linestyle="--", linewidth=1.0, label="D = 1.6 mm")
    ax.set_xlabel("Circular-waveguide diameter D (mm)")
    ax.set_ylabel("Cutoff frequency (GHz)")
    ax.set_title("Circular-waveguide cutoff frequencies")
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig("waveguide_modes_demo.png", dpi=180)
    print("\nSaved waveguide_modes_demo.png")


if __name__ == "__main__":
    main()
