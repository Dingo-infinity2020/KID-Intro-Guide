# Volume 2 Status

## v0.1 architecture checkpoint

当前目标是先验证“分册 + 单章快速编译”的维护方式，再进入设备/SOP 与文献调研。

已建立：

- 第 0–9 章独立 TeX 文件；
- 全书 `main.tex` 与单章 `chapter-preview.tex`；
- `make chapter CH=...` 快速构建；
- 工艺知识地图；
- 工艺—KID 参数矩阵；
- 微纳加工设备学习清单；
- 独立 GitHub Actions workflow。

下一阶段优先完成第 0、1、3 章，并基于实际加工平台资料校正设备与流程描述。
