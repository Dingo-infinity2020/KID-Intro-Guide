# Roadmap

## 已完成

### v0.1 — 从一个光子到 `S21`
建立 KID 第一条完整因果链。

### v0.2 — 动能电感
从载流子惯性推到 sheet kinetic inductance 与 kinetic inductance fraction。

### v0.3 — 超导基础最小知识集
Cooper pair、BCS 能隙、准粒子、generation-recombination 与 quasiparticle lifetime。

### v0.4 — 复电导与 Mattis–Bardeen
`σ1/σ2`、surface impedance、`Lk`、`Qi`，以及 GHz / 150 GHz 材料响应边界。

### v0.5 — 微波谐振器与 I-Q 读出
`Qi/Qc/Qr`、linewidth、ring-down、IQ circle、fixed tone、非理想传输与 resonance fitting。

### v0.6 — 光学响应、噪声与 NEP
`P_abs → Nqp → responsivity`、detector dynamics、PSD/ASD、NEP 与 photon/GR/TLS/amplifier noise。

### v0.7 — LEKID 电磁设计
完成：
- meander 的 absorber + kinetic-inductor 双重角色；
- fill factor、effective sheet impedance 与 absorber volume；
- quarter-wave backshort 与其偏离理想 λ/4 的原因；
- circular-waveguide TE11/TM01/TE21 cutoff；
- TE11 简并与 polarization mode basis；
- co-pol/cross-pol、hairpin end-turn 与双偏振对称性；
- IDC/TLS、coupling capacitor 与 `Qc`；
- optical cross-pol vs microwave crosstalk；
- Sonnet / CST / HFSS 分工；
- full-wave propagating-mode power closure；
- D=1.6 mm、149–151 GHz 直接数值示例；
- waveguide/backshort Python exercises。

## 下一阶段

### v0.8 — 当前 150 GHz 双偏振 LEKID 的完整验证矩阵

目标不是再增加一层“通用知识”，而是把 v0.1–v0.7 逐项变成当前项目可执行的验证项：
- 设计参数表与 nominal geometry；
- Sonnet：`f0/Qc/current/IDC/coupler`；
- CST：TE11-X/Y、TM01、mode closure、co/cross-pol absorption；
- B0/B1 backshort 的 bandwidth / angle / polarization symmetry 比较；
- superconducting material model sensitivity；
- optical `P_abs` → responsivity / NEP 的端到端映射；
- mesh/frequency/adaptive convergence 与 reproducibility；
- 将模拟指标对应到未来 cryogenic VNA / optical load / polarization test。

### v0.9+ — 阵列与实时读出

- FDM / resonance placement / collision budget；
- tone tracking 与自动 notch identification；
- RFSoC FPGA channelization / DDC；
- 100G / GPU 后端与实时数据产品；
- 大阵列 calibration / health monitoring；
- instrument-level sensitivity and yield budget。
