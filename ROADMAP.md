# Roadmap

## 已完成

### v0.1 — 从一个光子到 `S21`

建立 KID 的第一条完整因果链。

### v0.2 — 动能电感

从载流子惯性推到薄膜 sheet kinetic inductance 与 kinetic inductance fraction。

### v0.3 — 超导基础最小知识集

完成 Cooper pair、BCS 能隙、准粒子、热激发、generation-recombination 与 quasiparticle lifetime。

### v0.4 — 复电导与 Mattis–Bardeen

完成 `σ1/σ2`、Mattis–Bardeen、surface impedance、`Lk`、`Qi` 的器件化闭环，并区分 GHz / 150 GHz 两种电磁频率区间。

### v0.5 — 微波谐振器与 I-Q 读出

完成 `Qi/Qc/Qr`、linewidth、ring-down、ideal notch、IQ circle、fixed tone、非理想传输、resonance fitting 与 Python 示例。

### v0.6 — 光学响应、噪声与 NEP

完成：
- absorbed power → quasiparticle generation → steady-state `Nqp`；
- pair-breaking efficiency 与 quasiparticle lifetime；
- frequency / dissipation / complex I-Q responsivity；
- quasiparticle 与 resonator 两个动态时间尺度；
- PSD / ASD 与 input-referred NEP；
- photon shot / bunching、generation-recombination、TLS、amplifier/readout noise；
- 150 GHz Al LEKID 数值例子与 Python noise budget。

## 下一阶段

### v0.7 — LEKID 电磁设计

- meander 作为 absorber + kinetic inductor 的双重角色；
- IDC 的 capacitance、electric-field participation 与 TLS；
- coupling capacitor、`Qc` 与 frequency-division multiplexing constraint；
- 双偏振 direct-absorption LEKID；
- waveguide aperture、polarization purity 与 mode content；
- backshort / cavity / substrate 的吸收机理；
- 线宽、厚度、sheet impedance 与 optical absorption / resonator design 的联合参数化；
- Sonnet / CST / HFSS 各自的角色与边界。

### v0.8+ — 阵列、实验与真实项目闭环

- array / frequency-division multiplexing readout；
- resonator fitting 与自动定标；
- optical efficiency 与黑体标定；
- material parameter extraction；
- Sonnet / CST / cryogenic measurement closure；
- 当前双偏振 150 GHz LEKID 的理论—电磁—加工—实验验证矩阵；
- 从学习问题收敛到可发表的器件研究问题。
