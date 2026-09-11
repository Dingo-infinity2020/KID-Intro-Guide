"""Toy B0/B1 robust-claim example used by the v0.9 validation chapter."""
import numpy as np

f = np.linspace(149.0, 151.0, 401)
A_b0 = 0.838 + 0.018*np.cos(np.pi*(f-150.0))
A_b1 = 0.899 + 0.010*np.cos(np.pi*(f-150.0))
mean_b0 = np.trapezoid(A_b0, f)/(f[-1]-f[0])
mean_b1 = np.trapezoid(A_b1, f)/(f[-1]-f[0])
gain = mean_b1 - mean_b0
solver_uncertainty = 0.006
tolerance_uncertainty = 0.012
margin = solver_uncertainty + tolerance_uncertainty
print(f"mean_A_B0={mean_b0:.4f}")
print(f"mean_A_B1={mean_b1:.4f}")
print(f"improvement={gain:.4f}")
print(f"solver+tolerance uncertainty={margin:.4f}")
print("ROBUST CLAIM" if gain > margin else "CLAIM NOT YET ROBUST")
