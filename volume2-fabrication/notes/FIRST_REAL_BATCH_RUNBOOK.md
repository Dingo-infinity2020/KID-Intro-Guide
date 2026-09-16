# First Real Batch Runbook

这份 runbook 面向第一次把真实 KID wafer / die 数据接入 Volume 2 v0.2 工具链的场景。它不是设备 SOP，也不规定任何实验室的工艺参数；它只规定**数据闭环怎样不丢身份、不偷拟合、不覆盖原始数据**。

## 0. 开始之前

先固定一批数据的最小身份：

- `project_id`
- `batch_id`
- `wafer_id`
- `die_id`
- `gds_revision`
- `process_revision`
- `film_run_id`
- `metrology_run_id`
- `package_id`
- `cooldown_id`

如果某一项当前不存在，允许留空或写 `NOT_ASSIGNED`，但不要用文件夹名称暗示它已经有正式 ID。

## 1. 永远先复制模板，不改模板本体

建议每一批数据建立独立目录，例如：

```text
BATCH_2026_001/
├── raw/
│   ├── wafer_metrology_map.csv
│   └── resonator_map.csv
├── derived/
├── figures/
└── provenance/
```

从仓库复制：

- `templates/wafer_metrology_map.csv`
- `templates/resonator_map.csv`
- `templates/run_manifest.yaml`
- `templates/first_cooldown_report.md`

`raw/` 中的文件一旦进入正式分析，不应被后续脚本原地修改。

## 2. 先检查 ID，再看数值

对每一条准备 join 的 resonator，确认：

`resonator_id -> die_id -> x_mm/y_mm -> design_f0_Hz -> measured_f0_Hz`

是唯一且可追溯的。

出现以下情况时先停下来处理 mapping，而不是继续拟合：

- 同一个 `resonator_id` 出现两次；
- measured notch 无法唯一对应设计器件；
- die 翻转/旋转后坐标约定不清楚；
- wafer metrology 点只是附近 coupon，却被误写成某个 resonator 的直接测量；
- frequency collision 导致两个 resonance 的身份本身不确定。

## 3. 把模型系数当作“有出处的输入”

当前 adapter 需要显式提供：

- `alpha_k`
- `rsq_reference_ohm_sq`
- `linewidth_sensitivity`
- `collision_margin_linewidths`

每次分析同时保存一份 provenance 文本，至少写：

```text
alpha_k_source = ...
rsq_reference_source = ...
linewidth_sensitivity_source = ...
collision_margin_source = ...
analysis_git_commit = ...
analysis_date = ...
```

如果某个 sensitivity 是从当前 batch 自己拟合出来的，就不能再把同一批的 residual reduction 当成独立验证。

## 4. 运行 measured-data adapter

示例：

```bash
python3 examples/analyze_fabrication_feedback.py \
  --metrology BATCH_2026_001/raw/wafer_metrology_map.csv \
  --resonators BATCH_2026_001/raw/resonator_map.csv \
  --out BATCH_2026_001/derived \
  --alpha-k <value> \
  --rsq-reference-ohm-sq <value> \
  --linewidth-sensitivity <value> \
  --collision-margin-linewidths <value>
```

首先检查 `analysis_summary.txt` 中：

- `joined_resonators`
- `excluded_incomplete`
- `unmatched_metrology`
- `unmatched_resonators`

如果 join coverage 本身有问题，不要先讨论 predictor 好不好。

## 5. 自动生成四张标准图

```bash
python3 examples/plot_fabrication_feedback.py \
  --joined BATCH_2026_001/derived/joined_feedback.csv \
  --out BATCH_2026_001/figures
```

至少人工看一遍：

1. `wafer_rsq_map.svg`
2. `frequency_error_map.svg`
3. `predictor_vs_measurement.svg`
4. `residual_map.svg`

优先问四个问题：

- measured error 是否有明显空间结构？
- predictor 是否至少抓住了同方向、同量级的结构？
- residual 是否明显变窄？
- residual map 是否还留下中心-边缘梯度、局部 cluster 或其他系统结构？

## 6. `next_design.csv` 只是 proposal

不要把脚本生成的 `recommended_design_f0_Hz` 直接自动写回 GDS。

进入版图修正前至少确认：

- predictor 的系数有明确 provenance；
- 它不是只在同一批数据上“拟合得很好”；
- correction 对应的是可重复 systematic component，而不是随机 scatter；
- correction 后的 frequency ordering / spacing / collision margin 仍合理；
- 工艺或材料 recipe 没有在下一批之前发生足以使模型失效的改变。

## 7. 第二批开始做 cross-batch comparison

当 Batch B 完成同样分析后：

```bash
python3 examples/compare_fabrication_batches.py \
  --joined batch_A=BATCH_2026_001/derived/joined_feedback.csv \
  --joined batch_B=BATCH_2026_002/derived/joined_feedback.csv \
  --out CROSS_BATCH_2026_001_002
```

重点不是找一个通用 PASS 数字，而是看：

- predictor 与 measured error 的相关方向是否保持；
- slope 是否仍在相似尺度；
- residual mean 是否持续偏向某一侧；
- residual std 是否稳定低于 raw measured scatter；
- residual 的空间结构是否重复出现。

如果模型只能解释 Batch A，到了 Batch B 就失效，那么它更像 batch-specific description，而不是可写入设计规则的 process knowledge。

## 8. 一次完整反馈循环的最小归档

建议至少保留：

```text
raw/wafer_metrology_map.csv
raw/resonator_map.csv
derived/joined_feedback.csv
derived/next_design.csv
derived/analysis_summary.txt
figures/wafer_rsq_map.svg
figures/frequency_error_map.svg
figures/predictor_vs_measurement.svg
figures/residual_map.svg
figures/diagnostic_report.html
provenance/model_inputs.txt
run_manifest.yaml
first_cooldown_report.md
```

真正的目标不是“文件齐全”，而是半年后仍能回答：

> 这次 next-GDS correction 是根据哪一批 wafer、哪一组 metrology、哪一个 cooldown、哪一版分析脚本和哪一组 sensitivity 做出的？

能回答这句话，才算把 fabrication learning 变成了可积累的工程知识。
