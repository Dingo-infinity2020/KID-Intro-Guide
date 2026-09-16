# Volume 2 Status

## v0.1 content checkpoint

第二册已经完成从“架构验证”向“加工知识主线”的第一轮推进。当前仍保持独立分册和单章快速编译，不触碰第一册 v0.10。

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
- 独立 GitHub Actions workflow。

### 已形成第一版实质正文

- 第 0 章：从版图到芯片的完整出生流程；
- 第 1 章：洁净室、污染与工艺纪律；
- 第 2 章：基底、介电参与度、界面/TLS 与 surface history；
- 第 3 章：超导薄膜、`Rsq / Tc / thickness / Lk_square` 与 frequency scatter；
- 第 4 章：光刻、critical dimension、CD bias、linewidth/gap variation 与 frequency collision；
- 第 5 章：subtractive etch、lift-off、over-etch、residue、edge damage 与 final-geometry acceptance。

其中第 2、4、5 章已经把工艺现象明确接回 `f0 / Qi / Qc / collision / yield`，并补入 substrate/interface-loss、linewidth-scatter 和 etch-edge/residue 的文献证据链。

### 当前维护策略

开发分支普通 push 只编译被修改的章节；只改 Markdown/模板则跳过 TeX。整册编译只保留给结构变更、手工 milestone，以及 PR 从 draft 切换到 ready-for-review 等检查点。

这样继续扩一章时，不需要反复重新编译第一册 144 页，也不需要每次都完整重编第二册。

### 下一阶段

1. 扩写第 6 章：dicing、封装、wire bond、grounding、slotline / cavity mode；
2. 扩写第 7 章：room-temperature metrology 与 fabrication acceptance gate；
3. 扩写第 8 章：第一次 cooldown 的 `f0, Qi, Qc` 诊断树；
4. 把真实平台培训得到的 material policy / tool capability / SOP 编号回填到第 1–5 章，但不在公开讲义中复制危险化学 recipe；
5. 在 v0.1 milestone 时再执行一次整册 PDF、渲染和视觉 QA。
