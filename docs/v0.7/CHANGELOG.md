# v0.7 changelog - 2026-09-07

## Added

- New Chapter 8: **LEKID electromagnetic design**.
- Explicit two-frequency picture: 150 GHz optical absorber vs GHz resonator.
- First-order fill-factor/effective-sheet-impedance intuition and absorber-volume tradeoffs.
- Quarter-wave backshort transmission-line toy model and explanation of why the optimum shifts away from the naive lambda/4 value.
- Circular-waveguide cutoff derivation for TE11, TM01 and TE21, including the D=1.6 mm numerical example.
- TE11 polarization degeneracy and solver mode-basis bookkeeping.
- Co-pol/cross-pol definitions, hairpin end-turn discussion and dual-polarization symmetry checks.
- IDC/TLS and coupling-capacitor/Qc design guidance.
- Clear distinction between optical cross-polarization and GHz resonator crosstalk.
- Solver responsibility matrix: Sonnet for planar GHz resonator design; CST/HFSS for 3D waveguide/horn/backshort/polarization.
- Full-wave propagating-mode power-closure checklist and band-integrated optical objective.
- Current 150 GHz dual-polarization LEKID five-layer validation matrix.
- `examples/waveguide_modes_demo.py`.
- `examples/backshort_toy_model.py`.

## Validation

- All Python examples executed successfully.
- XeLaTeX compiled twice without fatal errors.
- Final PDF: **81 pages**.
- PDF preflight passed: openable, unencrypted, searchable/non-scanned.
- All 81 pages were rendered and visually reviewed; the new chapter flowchart was revised after the first visual review to remove arrow/label overlap.
