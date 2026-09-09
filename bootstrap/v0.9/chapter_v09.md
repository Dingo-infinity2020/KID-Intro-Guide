# 11. 150 GHz 双偏振 LEKID 项目验证矩阵：从理论预测到可复现证据

v0.1–v0.8 回答“为什么 KID 能工作”。v0.9 进一步回答：**怎样证明当前这个 KID 确实按预期工作，而且结论能够被复查和复现？**

完整证据链：

$$
\boxed{
\text{设计参数}
\to\text{GHz 电磁}
\to\text{150 GHz 光学电磁}
\to\text{数值收敛}
\to\text{加工}
\to\text{低温 }S_{21}
\to\text{光学/偏振标定}
\to\text{端到端结论}
}
$$

每一步都必须回答：**输入是什么、输出是什么、看哪个指标、怎样判断 PASS/FAIL、证据文件在哪里。**

## 11.1 验证不是“仿真跑完了”

$$
\boxed{
\text{Claim}+
\text{Observable}+
\text{Method}+
\text{Acceptance rule}+
\text{Evidence}
=\text{可审计验证}
}
$$

例如“B1 backshort 更宽带”必须进一步写成：固定 absorber/material/solver，只改变 backshort；比较 $A_X(f),A_Y(f)$ 的 band average、minimum、X/Y mismatch 与 leakage，并要求 B1/B0 差异大于 solver convergence 与 manufacturing tolerance 引起的不确定度。

## 11.2 模型职责分层

| 层 | 主要问题 | 输出 |
|---|---|---|
| GHz Sonnet | $f_0,Q_c$、IDC/coupler、current continuity | complex $S_{21}$、current map、parameter sensitivity |
| 150 GHz CST/HFSS | waveguide mode、absorption、polarization、backshort | modal $S$、absorbed power、co/cross-pol、closure |
| material | $T_c,L_{k,\square},Z_s(\omega,T)$ | sheet inductance / surface impedance |
| fabrication | linewidth/thickness/backshort/alignment | tolerance / yield |
| cryogenic | 实物 microwave resonance | $f_0,Q_i,Q_c(T,P)$ |
| optical | 光功率与偏振是否被探测 | responsivity、NEP、polarization response |

原则：**Sonnet 把 GHz resonator 做对；CST/HFSS 把 150 GHz optical coupling 做对；低温测量用来反标真实材料参数与模型偏差。**

## 11.3 Nominal Design Ledger

至少统一记录：waveguide diameter/reference plane、optical band、meander line/pitch/wiggle、film $t/T_c/R_\square/L_{k,\square}$、IDC finger、coupler、substrate、B0/B1 backshort、alignment、solver modes/mesh/version。所有 solver model 都应从同一 nominal ledger 派生。

## 11.4 Gate 0：geometry audit

- conductor continuity；
- 无意外 short/overlap；
- minimum linewidth/gap 满足加工；
- X/Y 对称与 end-turn 方向正确；
- waveguide/pixel/backshort 共轴；
- parameter sweep 不改变 topology；
- CAD/GDS 单位、层、polarity 固定。

$$
\boxed{\text{Geometry PASS}=\text{连通性}+\text{DRC}+\text{拓扑稳定}+\text{版本可追溯}}
$$

## 11.5 Gate 1：GHz Sonnet

必须输出：

1. $S_{21}$ 及 $f_0,Q_r,Q_c$ fit；
2. resonance current map；
3. coupler sweep 对 $Q_c$ 的可控性；
4. IDC tuning 对 $f_0$ 的连续、单调 sensitivity；
5. parasitic-mode / box-mode 检查。

漂亮 notch 但 current map 不经过目标 absorber，不能算目标 KID mode。

## 11.6 Gate 2：150 GHz modal power closure

对入射传播模 $m$：

$$
1=P_{refl}^{(m)}+P_{trans}^{(m)}+P_{abs}^{(m)}+\cdots
$$

当前 $D=1.6$ mm 圆波导在约 150 GHz 需要至少 accounting：TE11-X、TE11-Y、TM01；TE21 仍为 cutoff consistency check。

$$
P_{refl}=|S_{\mathrm{TE11X}\leftarrow m}|^2+|S_{\mathrm{TE11Y}\leftarrow m}|^2+|S_{\mathrm{TM01}\leftarrow m}|^2.
$$

建议项目 sanity gate：closure 误差 <0.5% 正常，0.5–1% warning，>1% 先排查数值问题再谈性能。这个门槛是项目质量规则，不是物理定律。

## 11.7 Gate 3：co-pol / cross-pol / higher-mode conversion 分开

X-pol 入射至少区分 $A_{XX},A_{YX},R_{XX},R_{YX},R_{0X}$。cross-polar absorption、TE11 polarization conversion、TM01 mode conversion 是不同现象，不能用一个模糊的“cross-pol”代替。

## 11.8 Gate 4：B0 vs B1 研究矩阵

必须同时比较：center absorption、band average、minimum absorption、X/Y symmetry、cross-pol、angle robustness、manufacturing tolerance、numerical robustness。

主 claim 应接近：**B1 在 band/angle 指标上提升，且该提升在 symmetry/leakage/tolerance/convergence 约束下仍成立。**

## 11.9 Band-integrated FOM

$$
\bar A_X=\frac1{f_2-f_1}\int_{f_1}^{f_2}A_X(f)df,
\quad
\bar A_Y=\frac1{f_2-f_1}\int_{f_1}^{f_2}A_Y(f)df.
$$

$$
\bar A_{pol}=\frac{\bar A_X+\bar A_Y}{2},
\qquad
\Delta A_{pol}=\frac1{f_2-f_1}\int|A_X-A_Y|df.
$$

不要在结果出来以后再挑最有利的 FOM；主指标应提前写入 validation matrix。

## 11.10 Gate 5：数值收敛

分别检查 mesh、frequency sampling/interpolation、adaptive reproducibility。对指标 $M$：

$$
\epsilon_M^{(k)}=\frac{|M_{k+1}-M_k|}{\max(|M_{k+1}|,\epsilon_0)}.
$$

真正重要的是：

$$
\boxed{|M_{B1}-M_{B0}|\gg\delta M_{solver}+\delta M_{tolerance}}.
$$

## 11.11 Gate 6：材料模型 sensitivity

至少保留三层：PEC geometry sanity；simple $R_s+jX_s$ / $L_{k,\square}$；frequency/temperature dependent superconducting model。对 $L_{k,\square}$、film thickness、$R_\square$ 做上下界 sensitivity，检查 B0/B1 相对结论是否依赖一个过窄材料假设。

## 11.12 Gate 7：制造容差

至少扫描 linewidth、gap、film thickness、substrate、backshort depth、waveguide lateral offset、tilt/rotation、global scale error。可先用

$$
\sigma_M^2\approx\sum_i\left(\frac{\partial M}{\partial p_i}\sigma_{p_i}\right)^2
$$

识别最值得 Monte Carlo 的变量。

## 11.13 Gate 8：cryogenic VNA

测 $S_{21}(f;T,P_{read})$，提取 resonance yield、$f_0,Q_i,Q_c$、$f_0(T),Q_i(T)$、readout nonlinearity 和 collision。再用实测反标 $L_{k,\square}$、$\alpha$ 和 loss model，更新仿真，而不是只说“实测和仿真差了多少 MHz”。

## 11.14 Gate 9：optical loading

目标数据产品：$f_0(P)$、$Q_i(P)$、IQ$(P)$、$\tau(P)$、noise spectrum $S_x(f;P)$。如果 $P_{abs}=\eta_{opt}P_{BB}$，则

$$
\frac{dx}{dP_{BB}}=\eta_{opt}\frac{dx}{dP_{abs}}.
$$

因此 window/filter/waveguide/spillover/polarization chain 都必须在 end-to-end model 中有位置。

## 11.15 Gate 10：polarization calibration

理想旋转响应可写作

$$
R(\theta)=R_0\cos^2(\theta-\theta_0)+R_{leak}.
$$

X/Y 分别拟合 polarization angle、90° orthogonality、co-pol amplitude、leakage、polarization efficiency、responsivity mismatch，并使用与 full-wave 相同的 cross-pol 定义。

## 11.16 Traceability Matrix

| Claim | Observable | Method | PASS rule | Evidence |
|---|---|---|---|---|
| geometry 正确 | continuity/clearance | audit | 无断路短路/DRC 通过 | report + commit |
| GHz resonance 可控 | $f_0,Q_c$, current | Sonnet | 单调、连续、mode identity 正确 | CSV/map/fit |
| modal accounting 正确 | closure | CST | 项目阈值内 | modal CSV + manifest |
| 双偏振可用 | $A_X,A_Y$ | TE11-X/Y | 两偏振达到目标 | curves |
| B1 更宽带 | $\bar A$, min $A$ | B0/B1 | gain > numerical+tolerance uncertainty | comparison notebook |
| 数值收敛 | $\epsilon_M$ | mesh/frequency tiers | 小于 claim margin | convergence report |
| 制造稳健 | worst-case / sigma | tolerance | 达到预定 yield | tolerance report |
| microwave 实物闭合 | $f_0,Q_i,Q_c$ | cryo VNA | 偏差可解释 | fit database |
| optical 实物闭合 | $dx/dP$ | load | trend/scale 可解释 | load curves |
| polarization 实物闭合 | $R(\theta)$ | rotating source | angle/leakage 达标 | fit report |

## 11.17 Run Manifest

每个正式 run 至少记录：run_id、geometry commit、solver/version、frequency、waveguide/mode basis、material model、mesh/adaptive、backshort、outputs、notes。三个月后必须能回答“这条曲线怎么跑出来的”。

## 11.18 数据分层

推荐：`runs/<run_id>/raw/`、`derived/`、`figures/`、`manifest.yaml`。论文 figure 必须能由 raw + fixed script 重建，figure 不能成为唯一数据源。

## 11.19 Stop rule

当 principal metric 已达目标、solver/material/tolerance uncertainty 小于 claim margin、新增自由度改善小于不确定度，或模型已无法区分候选设计时，应停止 nominal optimization，转入更高层级验证或实验。

## 11.20 论文主 claim

建议压缩为：

1. 双偏振直接吸收 LEKID 在目标 band 内提供可用 co-pol absorption 和低 leakage；
2. B1 四重对称/多路径 backshort 相比 B0 改善 band/angle robustness，且不显著破坏 X/Y symmetry；
3. 改善经过 convergence、material 和 tolerance 检查后仍成立，并最终由 microwave/optical measurements 支持。

## 11.21 推荐执行顺序

`geometry freeze → GHz Sonnet → 150 GHz closure → B0/B1+polarization → convergence → material/tolerance → fabricate → cryogenic → optical/polarization → final closure`

不要一开始就并行扫所有参数；只把过了上一 gate 的候选送入下一层。

## 11.22 Pre-fabrication release checklist

- [ ] nominal geometry 有唯一版本；
- [ ] continuity/DRC 通过；
- [ ] GHz $f_0,Q_c$/current map 通过；
- [ ] TE11-X/Y closure 通过；
- [ ] TM01 纳入 modal accounting；
- [ ] B0/B1 FOM 预先定义；
- [ ] mesh/frequency convergence 小于 claim margin；
- [ ] material sensitivity 通过；
- [ ] manufacturing tolerance 通过；
- [ ] GDS/CAD 与 simulation geometry 同源；
- [ ] cryogenic test plan 已准备；
- [ ] optical/polarization fixture 能测论文主 claim。

## 11.23 Post-fabrication closure checklist

- [ ] 批量拟合 $f_0,Q_i,Q_c$；
- [ ] measured/simulated deviation 有归因；
- [ ] $f_0(T),Q_i(T)$ 更新材料模型；
- [ ] optical load 可重复；
- [ ] responsivity/noise 同 operating point；
- [ ] polarization X/Y angle/leakage 完成；
- [ ] B0/B1 使用同一 measurement chain；
- [ ] 不用任意 scale factor 掩盖偏差；
- [ ] figures 可由 raw + script 重建；
- [ ] 结论强度与 evidence level 匹配。

## 11.24 Evidence level

E0 单 nominal simulation；E1 convergence/repeatability；E2 material+tolerance；E3 fabricated cryogenic microwave；E4 optical/polarization measurement；E5 independent repeat / multi-pixel yield。论文措辞应与 evidence level 匹配。

## 11.25 最终闭环

$$
\boxed{
\text{theory}
\to\text{parameterized model}
\to\text{GHz verification}
\to\text{optical modal closure}
\to\text{B0/B1 FOM}
\to\text{uncertainty}
\to\text{fabrication}
\to\text{cryo/optical calibration}
\to\text{traceable claim}
}
$$

v0.9 的核心习惯：**先写 claim，再定义 observable；先过 numerical gate，再比较设计；先量 uncertainty，再谈 improvement；最后让实验反过来更新模型。**
