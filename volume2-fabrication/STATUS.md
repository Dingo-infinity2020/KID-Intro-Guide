# Volume 2 Status

## v0.1 milestone candidate

第二册已经从“架构验证”推进到第一轮完整正文：第 0–9 章都已经有可连续阅读的内容，并继续保持独立分册、单章快速编译和与第一册 v0.10 解耦的维护方式。

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
- 普通章节 push 的增量编译，以及 Markdown/模板修改的 TeXLive 跳过逻辑。

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

### 当前维护策略

开发分支普通 push 只编译本次修改的章节；只改 Markdown/模板时应直接跳过 TeXLive。整册编译保留给结构变更、手工 milestone，以及 PR 从 draft 切换到 ready-for-review 等检查点。

这样继续扩一章时，不需要反复重新编译第一册 144 页，也不需要每次都完整重编第二册。

### v0.1 milestone 尚需完成

1. 验证 Markdown-only push 确实不启动 TeXLive；
2. 对最新整册执行编译日志审计：页数、Overfull、bookmark/math-token、undefined refs/citations、missing characters；
3. 下载 CI PDF，逐页渲染并做视觉 QA；
4. 将最终审计结果写入仓库，并同步 Draft PR #6 描述；
5. 实际进入目标微纳平台培训后，再依据 material policy / tool capability / SOP 编号修正平台相关内容；公开讲义仍不复制危险化学或设备操作 recipe。
