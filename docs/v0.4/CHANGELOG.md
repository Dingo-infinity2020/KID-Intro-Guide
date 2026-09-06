# v0.4 Changelog — 2026-09-06

## 新增章节

新增第 5 章：**复电导与 Mattis–Bardeen：把准粒子真正连接到 $L_k$ 与 $Q_i$**。

主要新增内容：

- 引入复电导 `σ = σ1 - iσ2`，明确 `σ1` 的耗散含义与 `σ2` 的感性/超流含义；
- 用平均耗散功率说明为什么 `σ1` 直接对应微波损耗；
- 介绍 Mattis–Bardeen 理论的输入、输出及标准积分的物理含义；
- 给出 KID 常用的低温、低频近似与 `σ1 ↑ / σ2 ↓` 的基本趋势；
- 从体电导推导表面阻抗 `Zs = Rs + iXs`；
- 在薄膜均匀电流近似下推导 `Z□ ≈ 1/(tσ)`；
- 得到 `Lk,□ ≈ 1/(ω t σ2)`；
- 建立 `δf0/f0 ≈ (α/2) δσ2/σ2`；
- 建立简化导体损耗关系 `1/Qi,qp ≈ α σ1/σ2`；
- 加入正常态 sheet resistance 与零温 sheet kinetic inductance 的估算关系：`Lk,□(0) ≈ ħ R□,n /(πΔ0)`；
- 专门区分 GHz readout 与 150 GHz optical absorber 两个频率区间，强调材料参数不能跨频段无条件复用；
- 增加 Mattis–Bardeen 的适用边界：TLS、非平衡准粒子、强读出、磁通俘获、无序/DOS broadening 与非局域效应。

## 图示与视觉审查

- 新增复电导分流图；
- 新增 `σ1/σ2` 随温度变化的定性示意图，并明确标注“非定量 MB 曲线”；
- 新增 `Nqp → σ → Zs → Qi/f0 → S21` 的闭环图；
- 新增 GHz readout / Al pair-breaking / 150 GHz optical band 的频率轴示意；
- 全文重新渲染，共 47 页；
- 逐页检查新增流程图的箭头锚点、框体间距、文字重叠与公式裁切。

## 仓库维护

从 v0.4 起固定以下发布规则：

1. 每个版本目录同时保存 `.tex`、`.md`、正式 `.pdf`、`README.md` 和 `CHANGELOG.md`；
2. `LATEST_VERSION` 记录当前最新版；
3. 根目录 README / ROADMAP / CHANGELOG 与构建脚本同步更新；
4. GitHub Actions 从 `LATEST_VERSION` 自动选择最新版并实际执行两次 XeLaTeX 编译；
5. 最新 PDF 必须作为普通仓库文件存在，而不只作为 Actions artifact。
