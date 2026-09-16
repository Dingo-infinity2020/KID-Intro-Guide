# Film Batch Card

> 一张卡对应一次需要独立追溯的超导薄膜 run。不要把设备设定值当作材料实测值；设定、readback、witness measurement 分开记录。

## Identity

- `project_id`:
- `batch_id`:
- `wafer_id`:
- `film_run_id`:
- `process_revision`:
- deposition tool:
- run / recipe identifier:
- date:
- operator / team:

## Substrate before deposition

- substrate material / lot:
- nominal thickness:
- surface preparation identifier:
- time from final surface preparation to load:
- storage / handling note:
- visible anomaly before load:

## Deposition record

- target/source material identifier:
- nominal target thickness:
- tool thickness-monitor readback:
- deposition-rate readback:
- base-pressure readback:
- sample position / holder / rotation state:
- intentional heating or other platform-approved condition:
- interruption / alarm / anomaly:

> 这里记录“设备实际告诉了我们什么”。具体可执行设备参数仍以目标平台 SOP 和培训为准。

## Witness measurements

| witness_id | x_mm | y_mm | thickness_nm | Rsq_ohm_sq | Tc_K | method | measurement_id | notes |
|---|---:|---:|---:|---:|---:|---|---|---|
| | | | | | | | | |

## Wafer-level summary

- thickness mean / std / range:
- Rsq mean / std / range:
- Tc mean / std / range:
- center-to-edge trend:
- directional gradient:
- obvious outlier region:
- map file:

## First engineering interpretation

不要只写“膜很好/不好”。至少回答：

1. `thickness` 和 `Rsq` 的空间变化是否大到可能解释 resonance-frequency scatter？
2. `Rsq` 的变化主要像 thickness variation，还是提示 resistivity/material-state 也在变化？
3. 本批数据是否足以更新 `Lk_square` 的先验范围？
4. 下一步应该优先与哪一张 `CD map / resonance map` 做空间对齐？

## Links to later measurements

- GDS revision:
- die IDs:
- package IDs:
- cooldown IDs:
- resonator-map files:
- related figures / notebook / issue:

## Disposition

- status: `PASS / REVIEW / FAIL / NOT_MEASURED`
- rationale:
- next action:
