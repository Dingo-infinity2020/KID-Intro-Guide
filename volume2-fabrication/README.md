# KID 器件加工与实验入门

副标题：**从版图到可测芯片**

这是 KID 入门讲义系列的第二册开发目录。第一册回答“为什么 KID 能工作”，第二册聚焦另一条工程链：

`版图 → 基底/表面 → 超导薄膜 → 光刻 → 图形转移 → 切片/封装 → 工艺表征 → 低温 S21 → 反推加工`

## 当前状态

- v0.1 development milestone：**PASS**
- v0.1 整册：58 页，第 0–9 章第一轮正文完成
- v0.2：开始进入平台实测约束、定量案例和数据闭环
- 第一原则：不写成泛微纳加工教材，所有知识都要回答“它怎样影响 KID 的 `f0`、`Qi`、`Qc`、`Lk`、吸收、噪声、frequency collision 或 yield？”
- 完整 v0.1 QA：见 `V0.1_MILESTONE_AUDIT.md`

## 目录结构

- `main.tex`：整册入口，只在 structural change / milestone / PR / 手工检查时完整编译
- `chapter-preview.tex`：单章快速预览入口
- `chapters/`：分章源文件
- `notes/`：知识地图、工艺—器件参数矩阵、设备学习清单与数据约定
- `references/`：文献与设备/SOP 证据入口
- `templates/`：process traveler、run manifest、film batch card、wafer metrology map、resonator map、first-cooldown report
- `figures/`：图件
- `Makefile`：本地快速构建

## 快速编译

整册：

```bash
cd volume2-fabrication
make full
```

只编译一章，例如超导薄膜：

```bash
make chapter CH=ch03_superconducting_film
```

默认单章为 `ch00_overview`。输出放在 `build/`，不会触碰第一册。

GitHub Actions 的普通章节 push 只编译改动章节；Markdown / 模板修改不会启动 TeXLive。full build 额外检查 Overfull、PDF bookmark/PDF-string 数学警告、undefined refs/citations 和 missing characters。

## 从 v0.2 开始的数据链

第二册不只保存“工艺步骤”，还要求不同阶段能够通过稳定 ID 连接：

`project_id -> batch_id -> wafer_id -> die_id -> resonator_id`

并关联：

`gds_revision / process_revision / film_run_id / metrology_run_id / package_id / cooldown_id`

数据字段与单位约定见 `notes/DATA_CONTRACT.md`。

建议第一批真实器件就开始使用：

- `templates/run_manifest.yaml`：一批样品的身份、revision 与文件入口；
- `templates/film_batch_card.md`：薄膜 run、witness 与材料统计；
- `templates/wafer_metrology_map.csv`：按坐标保存 thickness / Rsq / CD / defect；
- `templates/resonator_map.csv`：连接设计频率、物理像素和低温 `f0/Qi/Qc`；
- `templates/first_cooldown_report.md`：把第一次 cooldown 收敛成下一批可执行的 fabrication feedback。

## 写作约定

每章都优先采用同一条解释顺序：

1. **这道工艺在做什么**；
2. **它改变了哪些材料/几何量**；
3. **这些量如何进入 KID 的物理参数**；
4. **最终会在什么测量量上暴露出来**；
5. **怎样用 witness sample / test coupon / 低温数据把问题定位回工艺步骤**。

涉及设备操作、化学品、真空、高压、高温、等离子体等内容时，本册只讲原理、参数意义、记录方法和诊断思路；具体操作条件必须以所在实验室 SOP 和设备培训为准。
