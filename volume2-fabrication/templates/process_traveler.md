# KID Fabrication Process Traveler

> 一批样品一份。目标不是写实验日记，而是让低温测试出现异常时，能沿记录反查到具体 run、recipe、样品和版图版本。

## A. Batch identity

- Batch ID:
- Project / device family:
- GDS / mask version:
- Date started:
- Operator(s):
- Target device:
- Intended cooldown / experiment:

## B. Starting substrate

- Wafer / die ID:
- Material:
- Crystal orientation (if relevant):
- Vendor / lot:
- Nominal thickness:
- Measured thickness / map:
- Surface / oxide condition:
- Initial inspection notes:

## C. Surface preparation / cleaning

| Step | Date/time | Equipment / station | SOP / recipe ID | Purpose | Actual observations | Pass? |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Record explicitly:

- what contamination/layer this step is intended to remove;
- time from final clean to film deposition;
- any unexpected delay, exposure, rinse/dry anomaly or handling event.

## D. Superconducting film deposition

- Material:
- Equipment:
- Run / recipe ID:
- Source / target lot if available:
- Target thickness:
- Thickness monitor reading:
- Deposition rate readback:
- Base pressure readback:
- Substrate rotation/heating:
- Witness sample ID(s):
- Abnormal events:

### Post-deposition metrology

- Thickness / map:
- Sheet resistance `Rsq` / map:
- `Tc` measurement:
- Film stress:
- Roughness / AFM if measured:
- Optical inspection:

## E. Lithography

- Resist:
- Resist lot / age if tracked:
- Spin program / SOP ID:
- Bake program / SOP ID:
- Resist thickness:
- Exposure tool:
- Mask / write-file version:
- Exposure / dose recipe ID:
- Alignment notes:
- Development SOP / recipe ID:
- Post-develop inspection:

### Critical-dimension checks

| Site | Designed linewidth/gap | Measured | Bias | Method |
|---|---:|---:|---:|---|
| meander |  |  |  |  |
| IDC |  |  |  |  |
| coupler |  |  |  |  |
| feedline |  |  |  |  |

## F. Pattern transfer

Choose route: **etch / lift-off / other**

- Equipment:
- Recipe ID:
- Nominal endpoint / target:
- Actual process time / endpoint observation:
- Over-etch / undercut / residue notes:
- Strip / post-clean SOP:
- Witness / test coupon result:

### Inspection

- Shorts found?
- Opens found?
- Fence / redeposition?
- Edge roughness / sidewall concern?
- Representative microscope / SEM image IDs:

## G. Dicing / packaging / wire bond

- Dicing tool / recipe:
- Die IDs produced:
- Edge/chip inspection:
- Package drawing/version:
- Die attach method:
- Chip orientation:
- Connector / PCB version:
- Bond wire material/diameter:
- Signal bond notes:
- Ground bond count / map:
- Rework performed:

## H. Room-temperature release gate

Before cooldown:

- [ ] visual inspection complete
- [ ] no obvious feedline open/short
- [ ] critical dimensions sampled
- [ ] thickness evidence attached
- [ ] `Rsq` evidence attached or explicitly unavailable
- [ ] `Tc` evidence attached or planned
- [ ] package/bond photos archived
- [ ] all data filenames point back to this Batch ID

## I. First cryogenic result

- Cooldown ID:
- Base temperature:
- Readout chain version:
- Designed resonators:
- Resonances found:
- Resonance yield:
- Median / distribution of `f0`:
- Median / distribution of `Qi`:
- Median / distribution of `Qc`:
- Frequency collision count:
- Spurious modes / baseline issues:

## J. Feedback to next design/process

### Observed problem


### Leading hypotheses

1.
2.
3.

### Evidence that supports / rejects each hypothesis


### Next-run change

- design change:
- process change:
- metrology change:
- packaging change:
- readout/test change:

### Do not change yet

List variables intentionally held fixed so the next run remains interpretable.
