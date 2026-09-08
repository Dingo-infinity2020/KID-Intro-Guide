"""Toy model: resistive/complex sheet in front of a grounded dielectric spacer.

This is intentionally a first-order normal-incidence transmission-line model.
It explains why a quarter-wave backshort can create impedance matching and why
sheet reactance can shift the optimum spacer thickness.  It is NOT a substitute
for a full-wave waveguide/horn/LEKID simulation.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

C0 = 299_792_458.0
Z0 = 376.730313668


def absorption(
    frequency_hz: float,
    thickness_m: np.ndarray,
    n_spacer: float,
    sheet_impedance_ohm: complex,
) -> np.ndarray:
    """Return A=1-|Gamma|^2 for a sheet shunting a PEC-backed dielectric stub."""
    beta = 2.0 * np.pi * n_spacer * frequency_hz / C0
    zd = Z0 / n_spacer

    # Short-circuited lossless transmission-line input impedance.
    z_stub = 1j * zd * np.tan(beta * thickness_m)

    # Sheet and grounded stub are parallel admittances at the illuminated plane.
    y_sheet = 1.0 / sheet_impedance_ohm
    y_stub = 1.0 / z_stub
    z_in = 1.0 / (y_sheet + y_stub)

    gamma = (z_in - Z0) / (z_in + Z0)
    return 1.0 - np.abs(gamma) ** 2


def main() -> None:
    nu = 150e9
    n_si = 3.4
    quarter_wave = C0 / (4.0 * n_si * nu)
    print(f"150 GHz, n = {n_si:.2f}")
    print(f"Quarter-wave spacer = {quarter_wave * 1e6:.2f} um")

    d_um = np.linspace(20.0, 300.0, 2000)
    d_m = d_um * 1e-6

    cases = [
        (Z0 + 0j, "Zs = Z0"),
        (250.0 + 0j, "Zs = 250 ohm"),
        (Z0 + 1j * 120.0, "Zs = Z0 + j120 ohm"),
    ]

    fig, ax = plt.subplots(figsize=(7.2, 4.8))
    for zs, label in cases:
        a = absorption(nu, d_m, n_si, zs)
        idx = int(np.nanargmax(a))
        print(f"{label:22s}: max A={a[idx]:.4f} at d={d_um[idx]:.2f} um")
        ax.plot(d_um, a, label=label)

    ax.axvline(quarter_wave * 1e6, linestyle="--", linewidth=1.0, label="lambda/(4n)")
    ax.set_xlabel("Spacer / backshort distance d (um)")
    ax.set_ylabel("Absorption A")
    ax.set_ylim(0.0, 1.05)
    ax.set_title("PEC-backed sheet absorber: transmission-line toy model")
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig("backshort_toy_model.png", dpi=180)
    print("Saved backshort_toy_model.png")


if __name__ == "__main__":
    main()
