# KID 入门讲义 v0.10 — 修改记录

发布日期：2026-09-10

v0.10 是一次面向“真正第一次接触 KID 的读者”的全书教学化重构，而不是简单增加新章节。它保留 v0.9 的项目验证闭环，同时系统降低前置知识门槛并提高公式、术语和工程结论的可追溯性。

## 主要变化

1. **新手入口重做**：补强第 0 章、全书阅读路线、符号/缩写/术语速查和每章导航，让读者先建立“光 → 超导状态 → 谐振器 → 微波读出”的主链。
2. **核心公式教学化**：共保留 43 组四层解释，统一回答“数学上是什么、物理上为什么、工程上怎么用、适用条件是什么”。
3. **超导与材料链补强**：扩展 BCS 能隙、准粒子、热激发、复电导、薄膜表面阻抗、动能电感及其近似条件。
4. **微波读出链补强**：强化 $Q_i/Q_c/Q_r$、notch、IQ circle、固定 tone 读出、frequency/dissipation response 与 fitting 的联系。
5. **响应度与噪声链补强**：明确 responsivity、PSD/ASD、one-sided/two-sided 约定与 NEP 的输入功率定义。
6. **LEKID 电磁设计教学化**：增加 fill factor、active volume、backshort、圆波导 cutoff、偏振选择性、耦合 $Q$、modal power closure 与 band-weighted absorption 的解释。
7. **公开教材一致性清理**：移除正文中的历史版本标签和私有项目措辞；统一 $N_{qp}$/$n_{qp}$、$\Delta$/$\Delta\nu$、$P_{inc}$/$P_{abs}$/$P_{read}$ 与复数单位约定。
8. **可执行示例**：保留 v0.9 项目验证示例，并加入/更新 resonator、responsivity、noise、waveguide 与 backshort 等 canonical examples。
9. **严格发布门禁**：XeLaTeX 双编译、Overfull hbox、bookmark、undefined refs/citations、missing glyph、Python 示例实际执行、PDF 页面渲染和字体嵌入检查。

## 兼容性

v0.9 的 validation matrix、run manifest 与 pre-fabrication checklist 继续保留，v0.10 不改变它们作为工程证据模板的角色。
