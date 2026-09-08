"""Numerical companion to KID Intro Guide v0.8 capstone review.

Computes the 150 GHz photon -> Al pair-breaking threshold -> resonator Q ->
fixed-tone IQ shift example used in the workbook chapter.
"""

from math import atan2, degrees

H = 6.62607015e-34
KB = 1.380649e-23
EV = 1.602176634e-19

nu_opt = 150e9
Tc = 1.2
f0_dark = 2.5e9
Qi = 1.0e5
Qc = 5.0e4
delta_f0 = -15e3

E_gamma = H * nu_opt
Delta0 = 1.764 * KB * Tc
nu_pb = 2.0 * Delta0 / H

Qr = 1.0 / (1.0 / Qi + 1.0 / Qc)
linewidth = f0_dark / Qr
d = Qr / Qc
S_dark = complex(1.0 - d, 0.0)

f0_light = f0_dark + delta_f0
f_tone = f0_dark
x = (f_tone - f0_light) / f0_light
y = 2.0 * Qr * x
S_light = 1.0 - d / (1.0 + 1j * y)

print("=== KID v0.8 capstone chain ===")
print(f"E_gamma = {E_gamma:.6e} J = {E_gamma / EV * 1e3:.6f} meV")
print(f"Delta0   = {Delta0 / EV * 1e3:.6f} meV")
print(f"2Delta0  = {2 * Delta0 / EV * 1e3:.6f} meV")
print(f"nu_pb    = {nu_pb / 1e9:.6f} GHz")
print(f"pair breaking allowed at 150 GHz? {nu_opt > nu_pb}")
print()
print(f"Qr       = {Qr:.6f}")
print(f"linewidth= {linewidth / 1e3:.6f} kHz")
print(f"d=Qr/Qc  = {d:.9f}")
print(f"S21 dark = {S_dark.real:.9f} {S_dark.imag:+.9f}j")
print()
print(f"f0 light = {f0_light / 1e9:.9f} GHz")
print(f"y        = {y:.9f}")
print(f"S21 light= {S_light.real:.9f} {S_light.imag:+.9f}j")
print(f"|S21|    = {abs(S_light):.9f}")
print(f"phase    = {degrees(atan2(S_light.imag, S_light.real)):.6f} deg")
