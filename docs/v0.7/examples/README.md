# v0.7 Python examples

This directory keeps the runnable numerical exercises associated with KID Intro Guide v0.7.

- `resonator_basics.py`: inherited from v0.5; ideal hanger/notch resonator and IQ circle.
- `resonator_fit_demo.py`: inherited from v0.5; synthetic non-ideal complex S21 fitting.
- `optical_responsivity_demo.py`: inherited from v0.6; absorbed power -> quasiparticle -> fractional-frequency response.
- `noise_budget_demo.py`: inherited from v0.6; photon/GR/readout noise and NEP bookkeeping.
- `waveguide_modes_demo.py`: circular-waveguide TE11/TM01/TE21 cutoff calculation; default D=1.6 mm.
- `backshort_toy_model.py`: normal-incidence sheet + grounded-dielectric toy model for quarter-wave backshort matching.

The backshort script is deliberately a teaching model. Real horn/waveguide/LEKID optical design must still be validated with a 3D full-wave solver and a frequency-dependent superconducting material model.
