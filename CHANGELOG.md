# Changelog

## v0.6 — 2026-09-07

- 新增“光学响应、噪声与 NEP”完整章节；
- 建立 `P_abs → Γ_qp → Nqp → f0/Qi → I/Q` 的 responsivity 链；
- 引入 quasiparticle lifetime 与 resonator ring-down 的级联动态响应；
- 区分 PSD / ASD，并定义 input-referred NEP；
- 系统介绍 photon shot / bunching、GR、TLS、amplifier/readout noise；
- 增加 150 GHz Al LEKID、1 pW absorbed loading 数值例子；
- 新增 optical responsivity 与 noise budget 两个 Python 示例；
- GitHub Actions 在独立 TeX Live 2026 环境中完成两次 XeLaTeX 编译，正式 PDF 为 67 页并作为普通 Git 文件保存。

详见 [`docs/v0.6/CHANGELOG.md`](docs/v0.6/CHANGELOG.md)。

## v0.5 — 2026-09-07

- 新增微波谐振器与 IQ 读出完整章节；
- 推导 `Qi/Qc/Qr`、linewidth 与 ring-down；
- 推导 ideal notch `S21` 与 IQ circle；
- 引入 fixed-tone readout 和 frequency/dissipation response；
- 引入 cable delay、complex gain、asymmetry 与 resonance fitting；
- 新增两个 Python 教学示例。

详见 [`docs/v0.5/CHANGELOG.md`](docs/v0.5/CHANGELOG.md)。

## v0.4 — 2026-09-06

- 新增“复电导与 Mattis–Bardeen”完整章节；
- 建立 `Nqp → σ1/σ2 → Rs/Xs → Qi/f0 → S21` 闭环；
- 推导薄膜 `Z□ ≈ 1/(tσ)` 与 `Lk,□ ≈ 1/(ωtσ2)`；
- 建立 `δf0/f0 ≈ (α/2)δσ2/σ2` 与简化的 `1/Qi,qp ≈ ασ1/σ2`；
- 增加 `Lk,□(0) ≈ ħR□,n/(πΔ0)` 工程估算；
- 区分 GHz readout 与 150 GHz optical absorber 的材料电磁模型；
- 本地两次 XeLaTeX 编译并逐页视觉审查，正式 PDF 47 页；
- 引入 `LATEST_VERSION`，根构建脚本与 GitHub Actions 不再硬编码某个版本；
- 固定“每个版本必须提交正式 PDF 到仓库”的发布规则。

详见 [`docs/v0.4/CHANGELOG.md`](docs/v0.4/CHANGELOG.md)。

## v0.3 — 2026-09-04

- 新增超导基础最小知识集；
- 系统解释 Cooper pair、BCS 能隙、准粒子与 pair-breaking threshold；
- 引入热准粒子、generation-recombination 与 quasiparticle lifetime；
- 建立材料 `Tc`、工作温度与 150 GHz pair-breaking 条件的工程联系；
- 讲义扩展至 38 页。

详见 [`docs/v0.3/CHANGELOG.md`](docs/v0.3/CHANGELOG.md)。

## v0.2 — 2026-09-04

- 重做全部核心流程图并统一箭头语义；
- 新增动能电感专题章；
- 从载流子惯性推导 `Lk`；
- 增加能量法交叉验证；
- 引入 London penetration depth、sheet kinetic inductance 与 `α`；
- 建立 `δf0/f0` 与 `δLk/Lk` 的关系；
- 增加 PEC 与真实超导薄膜电磁建模的讨论。

详见 [`docs/v0.2/CHANGELOG.md`](docs/v0.2/CHANGELOG.md)。

## v0.1 — 2026-09-03

- 建立 KID 总体学习路线；
- 完成“从一个光子到 `S21`”的基础物理链；
- 初步介绍 pair breaking、准粒子、动能电感、谐振频移和 I-Q 读出；
- 建立与 150 GHz LEKID 的工程映射。
