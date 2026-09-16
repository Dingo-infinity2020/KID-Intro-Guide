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

## 3. 单位约定

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

## 4. 缺失值与状态

CSV 中缺失值建议留空，不要用 `0` 代替未知量。

状态字段使用少量稳定词汇，例如：

- `PASS`
- `FAIL`
- `REVIEW`
- `NOT_MEASURED`
- `UNMATCHED`
- `COLLISION_CANDIDATE`

自由文本异常说明放在 `notes`，不要把所有信息都塞进状态字段。

## 5. 坐标约定

所有 wafer/die map 必须在第一次使用时固定：

- 原点在哪里；
- +x / +y 指向哪里；
- 正面观察还是背面观察；
- die 翻转/旋转后如何换算；
- GDS coordinate 与显微镜/探针台 coordinate 的关系。

推荐把这个定义同时写进 `run_manifest.yaml` 和图片/报告标题中。

## 6. 推荐文件角色

- `run_manifest.yaml`：一批样品的身份与 revision 总表；
- `film_batch_card.md`：一次超导薄膜 run 的材料证据；
- `wafer_metrology_map.csv`：按物理坐标保存 thickness / Rsq / CD / defect 等数据；
- `resonator_map.csv`：把 design resonator、physical pixel 和低温 fit 结果连接起来；
- `first_cooldown_report.md`：把第一次低温测试收敛成可反馈的结论。

## 7. 一个重要原则

这些模板不是为了“记录得更正式”。它们真正的验收标准是：

> 当某个 `resonator_id` 的 `f0`、`Qi` 或 `Qc` 异常时，能否在几分钟内找到同位置的 film/CD/defect 数据，并知道它来自哪一版 GDS、哪一次薄膜、哪一种封装和哪一次 cooldown？

能做到这一点，fabrication feedback 才从文字原则变成可计算的数据链。
