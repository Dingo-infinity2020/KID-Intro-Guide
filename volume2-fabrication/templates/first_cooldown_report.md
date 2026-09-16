# First Cooldown Report

## Identity

- `project_id`:
- `batch_id`:
- `wafer_id`:
- `die_id`:
- `gds_revision`:
- `process_revision`:
- `film_run_id`:
- `package_id`:
- `cooldown_id`:
- measurement date:
- data root / immutable archive:
- analysis commit:

## 1. Cryogenic / readout configuration

- base-stage temperature range:
- magnetic shielding / field note:
- RF chain revision:
- sweep band:
- attenuation / gain configuration identifier:
- VNA / readout backend:
- package / lid / connector revision:
- deviations from planned configuration:

## 2. Resonance inventory

- design resonance count:
- detected resonance count:
- confidently mapped count:
- unmatched count:
- collision candidates:
- obvious spurious / package-mode candidates:
- unusable frequency intervals:

Detection yield:

`Y_det = N_matched / N_design =`

Attach / link:

- full raw `S21` sweep:
- resonance table:
- designed-vs-measured frequency plot:
- frequency-error histogram:
- spatial frequency-error map:

## 3. Frequency diagnosis

- median / mean `delta_f_frac`:
- spread metric:
- whole-wafer systematic offset?:
- center-edge trend?:
- directional gradient?:
- local outlier cluster?:
- correlation checked against `thickness / Rsq / CD / etch` map?:

Do not write only “frequency is low/high”. State which evidence supports material, geometry, EM-model, mapping, or package hypotheses.

## 4. Coupling diagnosis

- `Qc` target range:
- measured distribution:
- systematic shift?:
- coupling-region CD checked?:
- feedline / package EM mismatch suspected?:
- background / asymmetric-fit sensitivity checked?:

## 5. Internal-loss diagnosis

- `Qi` summary at defined power / temperature:
- spatial clustering?:
- selected power sweeps:
- selected temperature sweeps:
- TLS-like power dependence?:
- heating / nonlinearity / bifurcation evidence?:
- package-revision dependence?:
- film / surface / etch / magnetic hypotheses still open?:

## 6. Package / spurious modes

- broad baseline structures:
- reference / empty-package comparison:
- repeatable features across dies?:
- candidate cavity / slotline / connector features:
- resonators excluded from fitting because of package background:

## 7. Join with fabrication evidence

For every major anomaly, point to the evidence used for comparison:

| anomaly / resonator group | fabrication / metrology evidence | supports | does not distinguish | next cheapest test |
|---|---|---|---|---|
| | | | | |

## 8. Batch conclusion

Write no more than a few testable conclusions:

1. Design assumptions verified:
2. Fabrication variables with evidence of correlation:
3. Important hypotheses not yet distinguished:
4. Variables that should **not** be changed next run because evidence is insufficient:
5. One or two highest-information changes for the next controlled split:

## 9. Disposition

- status: `PASS / REVIEW / FAIL`
- science-use status:
- fabrication-learning status:
- next GDS change request:
- next process split:
- linked issue / notebook / report:
