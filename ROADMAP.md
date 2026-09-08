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
完成：
- 一页式 `hν → pair breaking → Nqp → σ1/σ2 → Lk/Qi → f0/S21 → IQ → responsivity/noise → NEP` 总因果链；
- 9 张核心笔记卡；
- 5 组公式阶梯；
- “数学—物理—工程”三问法；
- 15 道闭卷概念自测；
- 150 GHz、Tc=1.2 K、f0=2.5 GHz 的 Al LEKID 综合闭环题；
- 独立详细答案章，逐题给出推导步骤、单位检查、物理解释、工程意义和常见误区；
- `capstone_chain_demo.py` 与 `iq_circle_workbook.py` 两个复习脚本。

## 下一阶段

### v0.9 — 当前 150 GHz 双偏振 LEKID 的完整验证矩阵

目标是把 v0.1–v0.8 的理论逐项变成当前项目可执行、可复现、可对照实验的验证项：
- 设计参数表与 nominal geometry；
- Sonnet：`f0/Qc/current/IDC/coupler`；
- CST：TE11-X/Y、TM01、mode closure、co/cross-pol absorption；
- B0/B1 backshort 的 bandwidth / angle / polarization symmetry 比较；
- superconducting material model sensitivity；
- optical `P_abs` → responsivity / NEP 的端到端映射；
- mesh/frequency/adaptive convergence 与 reproducibility；
- 将模拟指标对应到未来 cryogenic VNA / optical load / polarization test；
- 形成“理论预测—仿真—加工—低温测量—光学标定”闭环表格与验收门槛。

### v1.0+ — 阵列与实时读出

- FDM / resonance placement / collision budget；
- tone tracking 与自动 notch identification；
- RFSoC FPGA channelization / DDC；
- 100G / GPU 后端与实时数据产品；
- 大阵列 calibration / health monitoring；
- instrument-level sensitivity and yield budget。
