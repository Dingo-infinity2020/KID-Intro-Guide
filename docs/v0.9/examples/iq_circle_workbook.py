"""Check the ideal hanger-resonator IQ-circle identity used in v0.8."""

import numpy as np

Qi = 1.0e5
Qc = 5.0e4
f0 = 2.5e9
Qr = 1.0 / (1.0 / Qi + 1.0 / Qc)
d = Qr / Qc

freq = np.linspace(f0 - 8 * f0 / Qr, f0 + 8 * f0 / Qr, 4001)
y = 2.0 * Qr * (freq - f0) / f0
S21 = 1.0 - d / (1.0 + 1j * y)

center = 1.0 - d / 2.0
radius = d / 2.0
circle_residual = (S21.real - center) ** 2 + S21.imag**2 - radius**2

idx0 = int(np.argmin(np.abs(freq - f0)))
print("=== Ideal IQ-circle check ===")
print(f"Qr                 = {Qr:.6f}")
print(f"circle center      = ({center:.9f}, 0)")
print(f"circle radius      = {radius:.9f}")
print(f"S21(f0)            = {S21[idx0].real:.9f} {S21[idx0].imag:+.9f}j")
print(f"expected 1-d       = {1-d:.9f}")
print(f"max circle residual= {np.max(np.abs(circle_residual)):.3e}")
