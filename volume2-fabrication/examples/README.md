# Quantitative examples

This directory contains small runnable examples that connect Volume 2 concepts to data handling. They are teaching models, not fabrication recipes and not claims about a specific laboratory process.

## 1. `wafer_to_resonance_demo.py`

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

- `wafer_metrology_map.csv` — same column contract as `templates/wafer_metrology_map.csv`;
- `resonator_map.csv` — same column contract as `templates/resonator_map.csv`;
- `synthetic_truth.csv` — demo-only hidden model components, deliberately kept outside the raw-data contract;
- `summary.txt` — deterministic regression summary.

The demo deliberately separates two types of model input:

1. a film term whose sign follows the small-signal kinetic-inductance relation used in Chapter 3;
2. a linewidth sensitivity coefficient that is explicitly a placeholder surrogate.

In a real project, the placeholder coefficient and the synthetic spatial distributions must be replaced by EM/LC sensitivities and measured process statistics.

With the fixed seed in the current example, the synthetic 64-resonator array has about 860 ppm frequency-error standard deviation before compensation and about 111 ppm afterward; the demo collision count drops from two adjacent collision pairs to zero under its deliberately chosen collision rule. These numbers are regression targets for the example only, not KID design specifications.

## 2. `analyze_fabrication_feedback.py`

This is the first measured-data adapter. It consumes the same two CSV contracts that the synthetic demo emits, joins them by `resonator_id`, applies *explicitly supplied* sensitivities, and writes derived feedback tables without modifying the raw inputs.

Example using the synthetic data:

```bash
python3 examples/analyze_fabrication_feedback.py \
  --metrology build/example-wafer-loop/wafer_metrology_map.csv \
  --resonators build/example-wafer-loop/resonator_map.csv \
  --out build/example-feedback-analysis \
  --alpha-k 0.45 \
  --rsq-reference-ohm-sq 0.45 \
  --linewidth-sensitivity 0.08 \
  --collision-margin-linewidths 5
```

Outputs:

- `joined_feedback.csv` — one row per successfully joined resonator, including measured error, model prediction and residual;
- `next_design.csv` — model-based correction proposal;
- `analysis_summary.txt` — join coverage, scatter statistics, correlations and current collision count.

The adapter intentionally does **not** fit `alpha_k` or linewidth sensitivity from the same batch it is evaluating. Coefficients are command-line inputs whose provenance should be recorded separately. This keeps a crucial distinction visible:

`apply a stated model != learn a model from the same data`

For real data, `next_design.csv` should be treated as a proposal until the systematic component has been shown to repeat on an independent batch.

## 3. Join behavior

The current adapter is deliberately conservative:

- primary join key: `resonator_id`;
- duplicate non-empty `resonator_id`: error;
- unmatched IDs: counted and reported;
- incomplete numeric rows: excluded and counted;
- coordinate-nearest-neighbor matching: **not performed automatically**.

This is intentional. Silent coordinate matching is convenient but can create a very convincing analysis of the wrong resonator.

## Why keep these examples small?

The goal is to make the complete logic auditable before adding a larger notebook or data stack. Both scripts use only Python's standard library, so CI can execute them without installing scientific packages. Plotting can be added later on top of the stable CSV contract rather than becoming another incompatible analysis path.
