# Quantitative examples

This directory contains small runnable examples that connect Volume 2 concepts to data handling. They are teaching models, not fabrication recipes and not claims about a specific laboratory process.

## `wafer_to_resonance_demo.py`

Runs a deterministic synthetic 8×8 KID-array example:

`wafer Rsq/CD map -> simple frequency-shift surrogate -> measured resonance map -> collision audit -> next-design pre-compensation`

Run:

```bash
cd volume2-fabrication
python3 examples/wafer_to_resonance_demo.py
```

or choose an output directory:

```bash
python3 examples/wafer_to_resonance_demo.py --out build/example-wafer-loop
```

It writes:

- `wafer_metrology_map.csv`
- `resonator_map.csv`
- `summary.txt`

The demo deliberately separates two types of model input:

1. a film term whose sign follows the small-signal kinetic-inductance relation used in Chapter 3;
2. a linewidth sensitivity coefficient that is explicitly a placeholder surrogate.

In a real project, the placeholder coefficient and the synthetic spatial distributions must be replaced by EM/LC sensitivities and measured process statistics.

With the fixed seed in the current example, the synthetic 64-resonator array has about 860 ppm frequency-error standard deviation before compensation and about 111 ppm afterward; the demo collision count drops from two adjacent collision pairs to zero under its deliberately chosen collision rule. These numbers are regression targets for the example only, not KID design specifications.

## Why keep this example small?

The goal is to make the complete logic auditable before adding a larger notebook or data stack. The script uses only Python's standard library, so CI can execute it without installing scientific packages. Later v0.2 work can add plotting and measured-data adapters without changing the underlying data contract.
