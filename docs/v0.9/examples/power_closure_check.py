"""Minimal modal power-closure checker for the v0.9 workflow."""
from math import fsum

reflected = {"TE11-X": 0.08, "TE11-Y": 0.01, "TM01": 0.03}
transmitted = {}
absorbed = 0.879
closure = fsum(reflected.values()) + fsum(transmitted.values()) + absorbed
error = abs(1.0 - closure)

print(f"closure={closure:.6f}")
print(f"closure_error={100*error:.3f}%")
if error < 0.005:
    print("PASS: normal project sanity gate")
elif error < 0.01:
    print("WARNING: inspect mesh/ports/reference planes")
else:
    print("FAIL: fix numerical accounting before judging performance")
