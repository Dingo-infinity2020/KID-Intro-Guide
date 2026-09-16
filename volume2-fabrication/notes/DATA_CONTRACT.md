# Volume 2 Data Contract

第二册从 v0.2 开始把“工艺记录”和“低温结果”当作同一个数据系统，而不是几份彼此独立的表格。目标不是建立复杂数据库，而是先保证任何一个异常 resonance 都能反查到它对应的版图、薄膜、工艺、物理位置和 cooldown。

## 1. 推荐的主键层级

建议所有模板尽量复用下面这些 ID：

`project_id -> batch_id -> wafer_id -> die_id -> resonator_id`

测量侧再增加：

`metrology_run_id`、`package_id`、`cooldown_id`、`measurement_id`

设计/工艺侧至少保留：

`gds_revision`、`process_revision`、`film_run_id`。

不要依赖“文件夹名字看起来能猜出来”。这些字段应该直接写进数据文件。

## 2. 最小可连接关系

一条 resonator 记录至少应该能够连接：

`resonator_id`
→ `die_id / physical x,y`
→ `design_f0`
→ `measured_f0, Qi, Qc`
→ `wafer_id / batch_id`
→ `film_run_id`
→ `gds_revision / process_revision`
→ `package_id / cooldown_id`

如果某一步暂时没有数据，保留字段并写空值；不要删除列。

从 v0.2.1 起，`wafer_metrology_map.csv` 也显式保留可选的 `die_id` 和 `resonator_id`。对于 linewidth、gap 或其他能够明确落到某个 resonator 的测量，应填写它们；对于 blanket-film witness、全局 coupon 或无法唯一映射到单个 resonator 的测量，可以留空。这样既能保存 wafer-level 数据，也不会为了“凑主键”伪造映射。

## 3. Join 规则：ID 优先，不默认猜坐标

进入定量分析时，默认以 `resonator_id` 做一对一 join。

- 同一张表中重复的非空 `resonator_id` 应视为数据错误，除非先显式聚合；
- 不同表中缺失的 ID 应统计为 `UNMATCHED`，不要悄悄丢掉；
- `x_mm / y_mm` 首先用来做 sanity check、wafer map 和空间诊断，不默认作为“最近邻自动配对”依据；
- 如果以后确实需要 coordinate-based matching，应把 tolerance、坐标变换和匹配置信度写进独立步骤，而不是藏在分析脚本里。

这样可以避免一个很危险的问题：两张图看起来位置很接近，脚本却把错误的 metrology 点配给了错误的 resonator。

## 4. 单位约定

为了避免后续脚本反复猜单位，v0.2 模板采用显式单位后缀：

- 坐标：`*_mm`
- 薄膜厚度：`*_nm`
- 关键线宽/间距：`*_um`
- 方阻：`*_ohm_sq`
- 温度：`*_K`
- 频率：`*_Hz`
- 品质因数：无量纲
- 相对偏差：`*_frac`

不要只写 `thickness=40`、`f0=2.5` 这种没有单位的值。

## 5. 缺失值与状态

CSV 中缺失值建议留空，不要用 `0` 代替未知量。

状态字段使用少量稳定词汇，例如：

- `PASS`
- `FAIL`
- `REVIEW`
- `NOT_MEASURED`
- `UNMATCHED`
- `COLLISION_CANDIDATE`

自由文本异常说明放在 `notes`，不要把所有信息都塞进状态字段。

## 6. 坐标约定

所有 wafer/die map 必须在第一次使用时固定：

- 原点在哪里；
- +x / +y 指向哪里；
- 正面观察还是背面观察；
- die 翻转/旋转后如何换算；
- GDS coordinate 与显微镜/探针台 coordinate 的关系。

推荐把这个定义同时写进 `run_manifest.yaml` 和图片/报告标题中。

## 7. 原始表和派生表要分开

`wafer_metrology_map.csv` 与 `resonator_map.csv` 应尽量保存接近原始测量/拟合输出的量，不要在里面覆盖式写入“修正后的答案”。

定量反馈脚本产生的派生量，例如：

- `predicted_systematic_frac`
- `residual_frac`
- `recommended_design_f0_Hz`
- `design_correction_Hz`

应放在单独的 `joined_feedback.csv` / `next_design.csv` 中，并保留生成它们时使用的模型参数。这样换一个 sensitivity model 时，可以重新生成派生结果而不污染原始数据。

## 8. 模型参数也需要 provenance

像 kinetic-inductance fraction `alpha_k`、`Rsq` reference、linewidth sensitivity、collision margin 这类量不能只存在于代码常数里。至少要知道：

- 数值是多少；
- 单位/定义是什么；
- 来源是解析模型、EM 仿真、哪一批 measured data，还是暂时的教学假设；
- 是否在独立 batch 上验证过。

当前 `examples/analyze_fabrication_feedback.py` 故意要求把关键系数作为命令行输入，而不在同一批数据上自动拟合。这样做是为了把“应用一个已声明模型”和“从数据学习模型”严格分开。

## 9. 推荐文件角色

- `run_manifest.yaml`：一批样品的身份与 revision 总表；
- `film_batch_card.md`：一次超导薄膜 run 的材料证据；
- `wafer_metrology_map.csv`：按物理坐标保存 thickness / Rsq / CD / defect 等数据；
- `resonator_map.csv`：把 design resonator、physical pixel 和低温 fit 结果连接起来；
- `first_cooldown_report.md`：把第一次低温测试收敛成可反馈的结论；
- `joined_feedback.csv`：metrology 与 resonance join 后的逐 resonator 派生量；
- `next_design.csv`：在模型已经跨 batch 验证之后，供下一版设计审核的 correction proposal。

## 10. 一个重要原则

这些模板不是为了“记录得更正式”。它们真正的验收标准是：

> 当某个 `resonator_id` 的 `f0`、`Qi` 或 `Qc` 异常时，能否在几分钟内找到同位置的 film/CD/defect 数据，并知道它来自哪一版 GDS、哪一次薄膜、哪一种封装和哪一次 cooldown？

第二个验收标准则是：

> 换一个模型参数或加入下一批数据时，能否重新计算 predictor / residual，而不需要手工复制粘贴或覆盖原始 CSV？

能同时做到这两点，fabrication feedback 才真正从文字原则变成可计算、可复现的数据链。
