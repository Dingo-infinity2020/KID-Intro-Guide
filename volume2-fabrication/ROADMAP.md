# Volume 2 Roadmap

## v0.1 — 架构与知识地图

目标：先搭出“一个 KID 芯片怎样出生”的完整因果链，而不是马上堆工艺名词。

- [x] 独立目录、单章编译入口、整册入口
- [x] 第 0–9 章骨架
- [x] 工艺 → 材料/几何 → KID 参数 → 可观测量矩阵
- [x] 微纳设备学习清单
- [x] SECUF F1 公开设备能力与章节映射
- [x] 首批 fabrication / array-yield 文献种子
- [x] process traveler 模板
- [x] 第 0、1、3 章第一版正文
- [x] 24 页 v0.1 architecture PDF 全书编译与渲染检查
- [ ] 根据实际现场培训/SOP 修正第 1、3–5 章中的平台相关内容
- [ ] 完成第 2、4、5 章第一轮扩写

## v0.2 — 薄膜、光刻与图形转移

重点补齐：

- substrate / surface preparation
- Al 等超导薄膜沉积与材料表征
- lithography CD / bias / resist profile
- dry/wet etch 与 lift-off 的选择逻辑
- witness sample 和 test coupon

出口：读者能把 `t, Rsq, Tc, linewidth, gap, residue` 与 `Lk, f0, Qi, yield` 对上。

## v0.3 — 封装、表征与低温反馈

重点补齐：

- dicing / cleaning / package / wirebond / grounding
- optical microscope / profilometer / 4-probe / SEM / AFM / Tc measurement
- 冷却前检查与首轮 S21
- resonance map、power sweep、temperature sweep
- failure tree：设计 / 材料 / 加工 / 封装 / 读出如何区分

## v0.4 — Design for Fabrication

- 最小线宽/间距与工艺窗口
- 阵列频率散布与 collision 风险
- tolerance budget
- mask bias / density / dummy / test structures
- fabrication traveler、run manifest 与 acceptance gate

## v1.0 — 稳定教学版

形成可供第一次进入微纳平台前预习、加工过程中记录、低温测试后回溯使用的闭环手册。

## 构建策略

为避免再次出现第一册后期“改一小段也重编整本”的维护负担：

- 普通开发 push：只编译本次修改的 chapter；
- 只改 notes/templates：不编 PDF；
- 修改 `main.tex` / `preamble.tex` / build workflow：做一次 full build；
- Draft PR 的普通同步更新：不重复 full build；
- PR `ready for review`、重新打开或手工 `workflow_dispatch`：做 full build。
