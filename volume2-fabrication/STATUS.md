# Volume 2 Status

## v0.1 architecture checkpoint

当前目标是先验证“分册 + 单章快速编译”的维护方式，再进入更深的设备/SOP 与文献调研。

### 已建立

- 第二册独立目录，不触碰第一册 v0.10；
- 第 0–9 章独立 TeX 文件；
- 全书 `main.tex` 与单章 `chapter-preview.tex`；
- `make chapter CH=...` 快速构建；
- 工艺知识地图；
- 工艺—KID 参数矩阵；
- 微纳加工设备学习清单；
- SECUF F1 公开设备能力映射；
- 首批 LEKID fabrication / frequency-scatter 文献；
- fabrication process traveler；
- 每章 must-answer / exit-competency contract；
- 第 0、1、3 章第一版扩写；
- 独立 GitHub Actions workflow。

### 当前可编译版本

- Full PDF：**24 页**
- XeLaTeX full build：**PASS**
- Poppler render：**24 / 24 页**
- 当前视觉检查：未见文字截断、框体越界、黑块或明显破损字形

### 维护策略

开发分支普通 push 只编译被修改的章节；只改 Markdown/模板则跳过 TeX。整册编译只保留给结构变更、手工 milestone，以及 PR 从 draft 切换到 ready-for-review 等检查点。

这正是第二册独立出来的主要收益：以后扩一章，不再因为第一册已经 144 页而反复重编旧内容。

### 下一阶段

优先扩写第 2、4、5 章，并把第一次真实平台培训得到的 SOP/设备信息填回第 1、3–5 章；随后建立 room-temperature acceptance gate 和 first-cooldown diagnosis tree。
