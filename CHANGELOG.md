# Changelog

## v0.7 — 2026-09-07

- 新增“LEKID 电磁设计”完整章节；
- 建立同一 meander 在 150 GHz absorber 与 GHz resonator 中的双频电磁图景；
- 引入 fill factor / effective sheet impedance / absorber volume 的工程权衡；
- 用 transmission-line toy model 解释 quarter-wave backshort，并讨论 $X_s$、vacuum gap 与 waveguide mode 导致的最佳厚度偏移；
- 推导圆波导 TE11/TM01/TE21 cutoff，加入 D=1.6 mm 数值例子：约 109.8 / 143.4 / 182.2 GHz；
- 解释 TE11 两重简并与 polarization mode basis；
- 加入 co-pol/cross-pol、hairpin end-turn、双偏振 bandshape symmetry；
- 加入 IDC/TLS、coupling capacitor 与 `Qc` 的器件设计直觉；
- 区分 optical cross-pol 与 microwave resonator crosstalk；
- 建立 Sonnet vs CST/HFSS solver responsibility matrix 与 full-wave modal power closure；
- 新增 `waveguide_modes_demo.py` 与 `backshort_toy_model.py`；
- 修复 Markdown 历史控制字符/损坏的 `\frac` / `\rightarrow`；
- 本地两次 XeLaTeX 编译、81 页逐页渲染视觉审查；首轮审查发现的新章流程图箭头/标签重叠已重做；
- 正式 PDF 81 页，并按项目规则作为普通 Git 文件保存。

详见 [`docs/v0.7/CHANGELOG.md`](docs/v0.7/CHANGELOG.md)。

## v0.6 — 2026-09-07

- 新增“光学响应、噪声与 NEP”完整章节；
- 建立 `P_abs → Γ_qp → Nqp → f0/Qi → I/Q` 的 responsivity 链；
- 引入 quasiparticle lifetime 与 resonator ring-down 的级联动态响应；
- 区分 PSD / ASD，并定义 input-referred NEP；
- 系统介绍 photon shot / bunching、GR、TLS、amplifier/readout noise；
- 增加 150 GHz Al LEKID、1 pW absorbed loading 数值例子；
- 新增 optical responsivity 与 noise budget 两个 Python 示例；
- 正式 PDF 67 页并作为普通 Git 文件保存。

详见 [`docs/v0.6/CHANGELOG.md`](docs/v0.6/CHANGELOG.md)。

## v0.5 — 2026-09-07

- 新增微波谐振器与 IQ 读出完整章节；
- 推导 `Qi/Qc/Qr`、linewidth 与 ring-down；
- 推导 ideal notch `S21` 与 IQ circle；
- 引入 fixed-tone readout、cable delay、complex gain、asymmetry 与 resonance fitting；
- 新增两个 Python 教学示例。

详见 [`docs/v0.5/CHANGELOG.md`](docs/v0.5/CHANGELOG.md)。

## v0.4 — 2026-09-06

- 新增“复电导与 Mattis–Bardeen”章节；
- 建立 `Nqp → σ1/σ2 → Rs/Xs → Qi/f0 → S21` 闭环；
- 引入 `LATEST_VERSION` 与固定版本发布规则。

详见 [`docs/v0.4/CHANGELOG.md`](docs/v0.4/CHANGELOG.md)。

## v0.3 — 2026-09-04

- 新增 Cooper pair、BCS 能隙、准粒子、thermal excitation、generation-recombination 与 lifetime。

详见 [`docs/v0.3/CHANGELOG.md`](docs/v0.3/CHANGELOG.md)。

## v0.2 — 2026-09-04

- 重做流程图语义；
- 新增动能电感专题章与 London / sheet kinetic inductance / `α`。

详见 [`docs/v0.2/CHANGELOG.md`](docs/v0.2/CHANGELOG.md)。

## v0.1 — 2026-09-03

- 建立 KID 总体路线与“光子到 `S21`”基础链。
