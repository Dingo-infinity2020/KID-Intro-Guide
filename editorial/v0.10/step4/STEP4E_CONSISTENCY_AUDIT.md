# v0.10 Step 4-E — Notation and public-textbook consistency audit

- Reader-facing formula guides retained: **43**
- Historical v0.1–v0.9 development labels in body: **0**
- Known private-project markers: **0**
- Conductivity convention in review sections: **$\sigma=\sigma_1-i\sigma_2$**
- RF $S_{21}$ formulas may retain engineering $j$: **intentional**
- $N_{qp}$ (total) vs $n_{qp}$ (density): **defined explicitly**
- $\Delta$ (gap) vs $\Delta\nu$ (bandwidth): **defined explicitly**
- $P_{inc}$ vs $P_{abs}$ vs $P_{read}$: **defined explicitly**
- PSD/ASD and one-sided/two-sided convention warning: **added**

Compilation, cross-reference and example-script gates are filled by CI.

## Compilation / integrity gate

- PDF pages: **144**
- Overfull hbox count: **0**
- Underfull hbox count (reported, not fatal): **37**
- Hyperref math-token bookmark warning: **NO**
- Undefined references: **NO**
- Undefined citations: **NO**
- Missing-character warnings: **NO**
- Step 4-E final formula/editorial gate: **PASS**

## Canonical examples gate

- `python -m py_compile examples/*.py`: **PASS**
- Headless execution of all six canonical examples: **PASS**
