"""First-order tolerance budget: sigma_M^2 = sum((dM/dp_i sigma_i)^2)."""
from math import sqrt

terms = {
    "linewidth": (2.0e-4, 2.0),
    "film_thickness": (7.0e-4, 5.0),
    "backshort_depth": (3.0e-4, 10.0),
    "lateral_offset": (1.5e-4, 10.0),
}
contributions = {k: abs(sens*sigma) for k, (sens, sigma) in terms.items()}
sigma_M = sqrt(sum(v*v for v in contributions.values()))
for name, value in sorted(contributions.items(), key=lambda kv: kv[1], reverse=True):
    print(f"{name:18s}: {value:.5f}")
print(f"combined_sigma_M: {sigma_M:.5f}")
