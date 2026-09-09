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
meander 双频角色、sheet impedance、fill factor、quarter-wave backshort、圆波导模态、双偏振、IDC/Qc、solver 分工与 full-wave power closure。

### v0.8 — 理论闭环复习与手写笔记册
一页式主因果链、9 张核心笔记卡、公式阶梯、数学—物理—工程三问法、15 道闭卷自测、150 GHz Al LEKID 综合题与详细答案章。

### v0.9 — 150 GHz 双偏振 LEKID 项目验证矩阵
- Claim–Observable–Method–Acceptance–Evidence 验证结构；
- Nominal Design Ledger / geometry gate；
- Sonnet GHz resonance/current/Qc/IDC gate；
- CST/HFSS TE11-X/Y + TM01 modal power closure；
- co-pol / cross-pol / higher-mode conversion 分解；
- B0/B1 band/angle/polarization comparison matrix；
- mesh/frequency/adaptive convergence；
- superconducting material sensitivity 与 manufacturing tolerance；
- cryogenic VNA / optical loading / polarization calibration；
- traceability matrix / run manifest / evidence level / stop rule；
- pre-fabrication 与 post-fabrication release checklist。

## 下一阶段

### v1.0 — 阵列与频分复用
- resonance placement 与 frequency-spacing policy；
- fabrication scatter 与 resonance collision / yield；
- feedline loading、total bandwidth 与 resonator count；
- readout power / dynamic range / crest factor；
- tone comb、channelization、DDC 与 calibration data products。

### v1.1+ — RFSoC / FPGA / GPU 实时读出
- automatic notch identification；
- tone tracking；
- FPGA channelizer / DDC；
- 100G / GPU 后端；
- array health monitoring；
- instrument-level sensitivity / yield closure。
