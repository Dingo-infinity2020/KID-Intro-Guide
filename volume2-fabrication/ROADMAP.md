# Volume 2 Roadmap

## v0.1 — 完整开发里程碑（PASS）

目标：先搭出“一个 KID 芯片怎样出生”的完整因果链，而不是马上堆工艺名词。

- [x] 独立目录、单章编译入口、整册入口
- [x] 第 0–9 章第一轮完整正文
- [x] 工艺 → 材料/几何 → KID 参数 → 可观测量矩阵
- [x] 微纳设备学习清单
- [x] SECUF F1 公开设备能力与章节映射
- [x] 首批 fabrication / array-yield 文献种子
- [x] process traveler 模板
- [x] substrate / surface、薄膜、光刻、etch / lift-off 第一轮扩写
- [x] dicing / packaging / metrology / first cooldown 第一轮扩写
- [x] Design for Fabrication 第一轮扩写
- [x] 普通章节增量构建
- [x] Markdown-only 修改跳过 TeXLive
- [x] full-build 严格日志门禁
- [x] 58 页 milestone PDF 全书编译与 58/58 页渲染检查
- [x] `V0.1_MILESTONE_AUDIT.md`

平台现场培训/SOP 修订不作为 v0.1 完成的前置条件；它属于下一阶段的现实约束回填。

## v0.2 — 平台实测约束与定量案例

重点从“概念正确”推进到“能拿真实数据验证”：

- 根据实际现场培训补充目标平台的 material policy、tool capability、可测 readback 与 SOP 编号；
- 不复制危险或可直接绕过培训的 recipe 参数；
- 建立 Al film batch card 的真实示例：`thickness / Rsq / Tc / uniformity`；
- 加入 CD / gap / etch / surface witness 的 wafer-map 示例；
- 用真实或公开数据演示 `film/CD variation -> f0 scatter -> collision/yield`；
- 给第 2–7 章补更多“测量结果怎样读”的定量 worked example。

出口：读者不只知道要测什么，还能看懂一套 fabrication metrology 数据怎样进入 KID 模型。

## v0.3 — First Cooldown 数据闭环

重点补齐：

- design-frequency ↔ physical-pixel ↔ measured-resonance mapping；
- resonance inventory 与自动化表格模板；
- `f0 / Qi / Qc` wafer map；
- power sweep、temperature sweep 的最小诊断流程；
- package / spurious mode / collision 的对照案例；
- fabrication traveler、film/CD map 与 cooldown result 的统一 sample ID；
- 从一次 cooldown 形成“下一批只改什么”的实验设计案例。

出口：读者能把一片新芯片的第一次低温测试整理成可追溯 fabrication feedback report。

## v0.4 — Array DfM 与可计算 tolerance loop

- sensitivity matrix / tolerance budget；
- spatially correlated fabrication variation；
- Monte Carlo frequency-collision yield；
- resonator ordering / spacing / trimming 策略；
- machine-readable local design rules；
- test coupon / controlled split / pre-fabrication review；
- fabrication statistics -> next GDS 的自动化接口。

出口：从“讲工艺”升级到“用平台统计数据设计更鲁棒的阵列”。

## v1.0 — 稳定教学版

形成可供第一次进入微纳平台前预习、加工过程中记录、低温测试后回溯使用的闭环手册；与第一册共同构成“器件物理/设计 + 加工/实验反馈”的两册体系。

## 构建策略

为避免再次出现第一册后期“改一小段也重编整本”的维护负担：

- 普通开发 push：只编译本次修改的 chapter；
- 只改 notes/templates/Markdown：不启动 TeXLive；
- 修改 `main.tex` / `preamble.tex` / build workflow：做一次 full build；
- Draft PR 的普通同步更新：不重复 full build；
- PR `ready for review`、重新打开或手工 `workflow_dispatch`：做 full build；
- full build 自动检查 Overfull、PDF-string/bookmark 警告、undefined refs/citations、missing characters；Underfull 仅报告不失败。
