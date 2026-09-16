# 第二册知识地图

这份地图用于控制范围：任何新增知识都应能落在下面至少一条链上，否则优先放到参考资料而不是正文。

## 1. 五层因果链

**A. Process variables**

substrate / cleaning / base pressure / deposition / thickness / resist / exposure / develop / etch / lift-off / dicing / package / bond

↓

**B. Material & geometry**

`Tc, rho, Rsq, t, roughness, stress, interface, linewidth, gap, sidewall, residue`

↓

**C. Electromagnetic / superconducting parameters**

`Lk_square, Lk, Lg, C, Cc, surface impedance, dielectric loss, current density`

↓

**D. Device observables**

`f0, Qi, Qc, Qr, S21, resonance scatter, optical absorption, responsivity, noise`

↓

**E. System outcome**

`yield, frequency collision, calibration stability, mapping speed / detector usability`

## 2. 学习优先级

### P0：第一次加工前必须会

- 洁净室/设备培训与 SOP 边界
- sample ID、traveler、recipe/run 记录
- substrate / film / resist / lithography / etch 的基本语言
- thickness、Rsq、Tc、linewidth/gap 的含义
- optical microscope / profilometer / four-probe 的基本用途
- dicing、wirebond、grounding 的基本风险

### P1：第一批芯片低温测试前应会

- CD bias / thickness uniformity / Rsq map
- test coupon / witness sample
- Qi vs Qc 的诊断含义
- frequency scatter / collision
- package parasitics
- temperature/power sweep

### P2：阵列优化阶段再深入

- microstructure / grain / disorder 的材料物理
- TLS 与界面损耗的更细模型
- statistical process control
- wafer-scale process window
- Monte Carlo tolerance → frequency collision/yield

## 3. 与第一册的接口

第二册不重复推导 BCS、Mattis–Bardeen、谐振器和 NEP，而把第一册中的量作为接口：

- `Rsq, Tc, t → Lk_square`
- `Lk, Lg, C → f0`
- `loss → Qi`
- `Cc / geometry → Qc`
- `geometry + optical boundary → absorption`
- `fabrication scatter → array frequency map / yield`
