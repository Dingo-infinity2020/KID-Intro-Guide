# KID Intro Guide v0.7

v0.7 extends the guide from detector responsivity/NEP into practical LEKID electromagnetic design.

## Main additions

- the same meander as a 150 GHz absorber and a GHz kinetic inductor;
- fill factor, effective sheet impedance, absorber volume and optical-matching tradeoffs;
- quarter-wave backshort as an impedance-matching problem rather than a fixed geometric recipe;
- circular-waveguide TE11/TM01/TE21 cutoff calculations, TE11 degeneracy and polarization-basis bookkeeping;
- co-pol/cross-pol metrics and the role of hairpin end-turns;
- IDC, coupling capacitor and Qc design intuition;
- separation of optical cross-polarization from microwave resonator crosstalk;
- Sonnet vs CST/HFSS responsibilities and full-wave power-closure checks;
- mapping to the current 150 GHz dual-polarization LEKID validation workflow.

## Files

- `KID入门讲义_v0.7.pdf` - reviewed 81-page reading version.
- `KID入门讲义_v0.7.tex` - authoritative XeLaTeX source.
- `KID入门讲义_v0.7.md` - editable content source.
- `CHANGELOG.md` - version-specific change record.
- `examples/` - runnable Python exercises inherited from v0.5/v0.6 plus the new waveguide/backshort examples.

Build with XeLaTeX twice. The repository-level `LATEST_VERSION` and GitHub Actions should point to `v0.7` after release.
