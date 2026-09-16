# Volume 2 Status

## v0.1 development milestone — PASS

第二册已经完成第一轮完整正文与 milestone QA：第 0–9 章可以连续阅读，并继续保持独立分册、单章快速编译和与第一册 v0.10 解耦的维护方式。

### 已建立

- 第二册独立目录；
- 第 0–9 章独立 TeX 文件；
- 全书 `main.tex` 与单章 `chapter-preview.tex`；
- `make chapter CH=...` 快速构建；
- 工艺知识地图；
- 工艺—KID 参数矩阵；
- 微纳加工设备学习清单；
- SECUF F1 公开设备能力映射；
- fabrication process traveler；
- 每章 must-answer / exit-competency contract；
- 独立 GitHub Actions workflow；
- 普通章节 push 的增量编译；
- Markdown/模板修改的 TeXLive 跳过逻辑；
- full build 严格日志门禁；
- 58 页整册 CI PDF 与全页视觉 QA。

### 第 0–9 章第一版正文

- 第 0 章：从版图到芯片的完整出生流程；
- 第 1 章：洁净室、污染与工艺纪律；
- 第 2 章：基底、介电参与度、界面/TLS 与 surface history；
- 第 3 章：超导薄膜、`Rsq / Tc / thickness / Lk_square` 与 frequency scatter；
- 第 4 章：光刻、critical dimension、CD bias、linewidth/gap variation 与 frequency collision；
- 第 5 章：subtractive etch、lift-off、over-etch、residue、edge damage 与 final-geometry acceptance；
- 第 6 章：dicing、封装、wire bond、ground return 与 package / slotline / cavity 风险；
- 第 7 章：room-temperature metrology、inspection、coupon 与 fabrication acceptance gate；
- 第 8 章：first cooldown 的 resonance inventory、`f0 / Qi / Qc`、power/temperature sweep 与 fabrication diagnosis；
- 第 9 章：Design for Fabrication，包括 tolerance、systematic/random variation、frequency collision、test structures、controlled split 与下一版 GDS feedback。

这些章节共同维持同一条主线：

`process variable -> real material/geometry -> electromagnetic/superconducting parameter -> f0/Qi/Qc/noise/yield -> next fabrication decision`

### v0.1 QA 摘要

最终审计基准：`014457073b13a775a5eda40676913ccde9adc954`

GitHub Actions run：`35085673096`

- 58 pages；
- Overfull 0；
- bookmark/math-token warning 0；
- undefined refs/citations 0；
- missing characters 0；
- Underfull hbox 12（非致命）；
- fonts embedded PASS；
- `pdftotext` replacement chars 0；
- 58/58 pages rendered；
- visual QA PASS。

完整记录见 `V0.1_MILESTONE_AUDIT.md`。

### 当前维护策略

开发分支普通 push 只编译本次修改的章节；只改 Markdown/模板时直接跳过 TeXLive。整册编译用于结构变更、手工 milestone，以及 PR 从 draft 切换到 ready-for-review 等检查点。full build 同时执行严格 TeX 日志审计。

### 下一阶段

v0.1 之后不再把主要工作定义成“补齐章节”，而转向：

1. 实际进入目标微纳平台培训后，依据 material policy / tool capability / SOP 编号修正平台相关内容；
2. 加入真实或公开数据驱动的定量案例：film/CD wafer map、resonance map、collision/yield、first-cooldown diagnosis；
3. 把 traveler、batch card、metrology report、cooldown report 与 resonator mapping 做成更可直接复用的数据模板；
4. 逐步建立 design tolerance -> fabrication statistics -> low-temperature feedback -> next GDS 的可计算闭环。

公开讲义仍不复制危险化学或设备操作 recipe，实际工艺条件以目标平台培训和 SOP 为准。
