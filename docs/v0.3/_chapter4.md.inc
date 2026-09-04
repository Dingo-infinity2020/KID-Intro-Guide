# 第 4 章：超导基础最小知识集 —— Cooper pair、能隙与准粒子

## 学习目标

这一章不试图把 BCS 理论从头推完。目标是建立一套足够支撑 KID 设计的“最小超导语言”。学完后，你应该能回答：

1. 普通金属与超导态在“可激发的低能状态”上有什么本质区别？
2. Cooper pair 为什么不能简单理解成两个紧紧抱在一起的电子？
3. 能隙 $\Delta$、临界温度 $T_c$ 与 pair-breaking 阈值之间是什么关系？
4. 什么是 quasiparticle（准粒子），为什么 KID 真正关心的是 $N_{qp}$？
5. 为什么热准粒子在低温下呈指数压低，而真实器件仍可能存在 excess quasiparticles？
6. pair breaking、recombination（复合）与 quasiparticle lifetime（准粒子寿命）如何决定 KID 的响应速度与灵敏度？

---

## 4.1 为什么现在才补“超导基础”？

前两章我们已经知道：

$$
P_{\rm abs}\rightarrow N_{qp}\rightarrow L_k,Q_i\rightarrow f_0,S_{21}.
$$

第 3 章又从载流子惯性推出了 $L_k$。但这里一直有一个“黑箱”：

$$
\boxed{\text{光子为什么会让 }N_{qp}\text{ 增加？}\qquad N_{qp}\text{ 到底是什么？}}
$$

本章就是打开这个黑箱。对 KID 设计者来说，最重要的不是会写完整 BCS gap equation，而是建立：

$$
\boxed{
T_c\rightarrow\Delta(T)
\rightarrow
\text{准粒子可激发能量}
\rightarrow
N_{qp}(T,P_{\rm abs})
\rightarrow
\tau_{qp}
\rightarrow
L_k,Q_i,S_{21}
}
$$

**物理直觉：**把超导体想成一个“低能激发被能隙挡住的电子系统”。KID 用毫米波/亚毫米波制造少量准粒子，再用 GHz 谐振器灵敏地读出这些准粒子改变了多少复电导。

---

## 4.2 正常金属与超导态：区别不只是“电阻变成零”

### 正常金属

在金属中，电子填充到 Fermi energy（费米能）$E_F$ 附近。只要提供很小的能量，就可以在 $E_F$ 附近制造电子–空穴激发。交流电流中的电子还不断受到晶格、杂质和缺陷散射，因此产生耗散。

可以先记：

$$
\boxed{\text{正常金属在 }E_F\text{ 附近很容易被激发。}}
$$

### 超导态

常规超导体降到 $T_c$ 以下后，费米面附近的一部分电子形成 Cooper pairs，并进入具有宏观相干相位的配对基态。

关键不是“电子从此不碰撞”，而是：

> **体系的低能激发谱被重构，并出现 energy gap（能隙）$\Delta$。**

对 BCS 准粒子：

$$
E=\sqrt{\xi^2+\Delta^2},\qquad \xi=\varepsilon-E_F.
$$

所以当 $\xi=0$ 时，正常态可以有趋近零的激发能量，而超导态的准粒子最小激发能量是 $\Delta$。

---

## 4.3 Cooper pair：KID 需要掌握到什么程度？

最简单的常规 $s$ 波 BCS 图景中，常把一对电子写成：

$$
(\mathbf{k},\uparrow),\qquad(-\mathbf{k},\downarrow).
$$

即近似相反动量、相反自旋的配对。晶格声子介导的有效吸引可以使费米面附近的电子产生配对不稳定性。

但 Cooper pair **不是两个电子形成的局域小分子**。其空间尺度可以远大于晶格常数，大量 pair 高度重叠，形成集体的配对凝聚态。

因此“打碎一个 Cooper pair”更安全的理解是：

$$
\boxed{\text{从配对基态中制造两个准粒子激发}}
$$

而不是把它想象成机械地掰断一根两电子化学键。

> **常见误区：**“Cooper pair 的结合能就是 $2\Delta$。”  
> 对 KID 更稳妥的表述是：单个最低能准粒子激发至少需要 $\Delta$；制造两个最低能准粒子，因此 pair-breaking threshold 约为 $2\Delta$。

---

## 4.4 BCS 能隙 $\Delta$：把材料与探测频率连接起来

弱耦合 BCS 在零温给出：

$$
\boxed{\Delta_0\approx1.764k_BT_c.}
$$

当 $T\to T_c$：

$$
\Delta(T)\to0.
$$

工程画图常使用 BCS-like 插值：

$$
\Delta(T)\approx
\Delta_0\tanh\!\left[
1.74\sqrt{\frac{T_c}{T}-1}
\right].
$$

它是方便的插值，不是完整 gap equation 本身。

### pair-breaking threshold

要制造两个最低能准粒子：

$$
\boxed{h\nu_{\rm pb}\approx2\Delta.}
$$

低温弱耦合近似下：

$$
\boxed{
\nu_{\rm pb}(0)
\approx
73.5\ {\rm GHz/K}\times T_c.
}
$$

| 材料 | 代表性 $T_c$ (K) | $\Delta_0$ (meV) | $\nu_{\rm pb}$ (GHz) | 150 GHz 直接 pair break? |
|---|---:|---:|---:|---|
| Ti | 0.4 | 0.061 | 29 | 是 |
| Al | 1.2 | 0.182 | 88 | 是 |
| Nb | 9.2 | 1.40 | 676 | 否 |
| NbTiN | 14 | 2.13 | 1029 | 否 |

这些只是弱耦合公式和代表性 $T_c$ 的数量级估算。真实薄膜会受材料配比、膜厚、沉积工艺和强耦合修正影响。

### 映射到 150 GHz LEKID

若吸收膜近似为 Al，$T_c\sim1.2$ K：

$$
\nu_{\rm pb}\sim88\ {\rm GHz}.
$$

所以 150 GHz 高于阈值；而 1–5 GHz readout tone 远低于阈值。这正是“高频光改变器件、低频微波询问器件”的材料基础。

---

## 4.5 准粒子：不是普通电子，而是超导体系的激发

BCS quasiparticle 能量：

$$
\boxed{
E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2}
}
$$

所以：

$$
E_{\mathbf{k}}\ge\Delta.
$$

更严格地说，Bogoliubov quasiparticle 是电子与空穴自由度的量子叠加。KID 入门阶段暂时不需要推 Bogoliubov transformation，但要避免把 quasiparticle 简化成“从 Cooper pair 里掉出来的普通电子”。

理想 BCS $s$ 波超导体的归一化态密度：

$$
\frac{N_s(E)}{N_0}
=
\begin{cases}
0, & |E|<\Delta,\\
\dfrac{|E|}{\sqrt{E^2-\Delta^2}}, & |E|>\Delta.
\end{cases}
$$

能隙内部没有理想单粒子激发态，并在 $|E|=\Delta$ 附近出现 coherence peak。这也是后面 Mattis–Bardeen 积分为什么总围绕 $\Delta$ 附近状态展开的根源。

---

## 4.6 热准粒子：为什么降温如此有效？

准粒子热占据：

$$
f(E,T)=\frac{1}{e^{E/k_BT}+1}.
$$

当 $k_BT\ll\Delta$：

$$
\boxed{
n_{qp}^{\rm th}
\approx
2N_0\sqrt{2\pi k_BT\Delta}
e^{-\Delta/k_BT}
}
$$

其中 $N_0$ 是 normal-state Fermi level 处的 single-spin density of states（单自旋态密度）。

最重要的是指数项：

$$
\boxed{n_{qp}^{\rm th}\propto e^{-\Delta/k_BT}.}
$$

如果取 $\Delta\simeq\Delta_0=1.764k_BT_c$：

| $T/T_c$ | $n_{qp}^{\rm th}/(2N_0\Delta_0)$ |
|---:|---:|
| 0.10 | $1.3\times10^{-8}$ |
| 0.20 | $1.25\times10^{-4}$ |
| 0.30 | $2.9\times10^{-3}$ |
| 0.50 | $3.9\times10^{-2}$ |

因此讨论 KID 工作温度时，最好同时看：

$$
\boxed{T/T_c}
$$

而不只是“冰箱是多少 mK”。

### 为什么真实器件仍会有 excess quasiparticles？

理想热平衡公式只是 baseline。真实器件还可能受到：

- 外界毫米波、红外、黑体泄漏；
- 宇宙线、高能粒子或基底声子；
- readout power 引起的加热与非平衡分布；
- 材料缺陷、陷阱和复杂的声子动力学。

因此实际系统里 $T\to0$ 并不自动保证 $N_{qp}\to0$。

---

## 4.7 光子如何制造非平衡准粒子？

```mermaid
flowchart LR
    A["hν > 2Δ<br/>吸收光子"] --> B["高能准粒子<br/>初始激发"]
    B --> C["高能声子<br/>弛豫产生"]
    C --> D["近能隙准粒子池<br/>Nqp ↑"]
    D --> E["两个准粒子复合"]
    E --> F["≈2Δ 声子"]
    F --> G["逃逸到基底 / 降能"]
    F --> D
```

高能声子可能继续 pair break，因此一个高能光子不一定只对应两个最终准粒子。

常用 pair-breaking efficiency $\eta_{\rm pb}$ 概括吸收能量进入低能准粒子系统的比例：

$$
N_{qp}^{\rm excess}
\sim
\eta_{\rm pb}\frac{E_{\rm abs}}{\Delta}.
$$

连续光功率可用数量级关系：

$$
\boxed{
G_{\rm opt}
\sim
\eta_{\rm pb}\frac{P_{\rm abs}}{\Delta}.
}
$$

精确系数取决于非平衡能量级联、声子逃逸和材料。

---

## 4.8 recombination：为什么准粒子不会一直积累？

两个准粒子可以重新进入 Cooper-pair condensate，并释放约 $2\Delta$ 的声子能量。

最小教学模型：

$$
\boxed{
\frac{dN_{qp}}{dt}
=
G-\mathcal{R}N_{qp}^2.
}
$$

稳态：

$$
G=\mathcal{R}N_{qp,\rm ss}^2,
$$

因此：

$$
\boxed{
N_{qp,\rm ss}
=
\sqrt{\frac{G}{\mathcal{R}}}.
}
$$

真实超导薄膜通常需要 Rothwarf–Taylor 方程或 Kaplan 的电子–声子寿命理论；这里的 $G-\mathcal RN^2$ 只是为了理解“稳态”和“复合为何随 $N_{qp}$ 增快”。

---

## 4.9 准粒子寿命 $\tau_{qp}$：连接到探测器速度

稳态附近的小扰动常可写成：

$$
\boxed{
\delta N_{qp}(t)=
\delta N_{qp}(0)e^{-t/\tau_{qp}}.
}
$$

对简化模型线性化：

$$
\tau_{qp}\sim
\frac{1}{2\mathcal{R}N_{qp,\rm ss}}.
$$

如果只有一个主导一阶时间常数：

$$
f_{\rm 3dB}\sim\frac{1}{2\pi\tau_{qp}}.
$$

KID 还有谐振器 ring-down time：

$$
\boxed{
\tau_{\rm res}=
\frac{Q_r}{\pi f_0}.
}
$$

真实时域响应同时受到 $\tau_{qp}$ 和 $\tau_{\rm res}$ 约束。

**重要直觉：**较长的 $\tau_{qp}$ 往往意味着同样的持续光功率能积累更多准粒子，有利于 responsivity；但响应也更慢。

---

## 4.10 材料选择的核心轴

以后谈材料时，同时比较两个无量纲量：

$$
\boxed{\frac{T}{T_c}}
\qquad\text{和}\qquad
\boxed{\frac{h\nu}{2\Delta}}.
$$

- $T/T_c$ 控制 thermal quasiparticle baseline 的数量级；
- $h\nu/2\Delta$ 决定入射光是否满足直接 pair breaking 的能量条件。

因此：

- 降低 $T_c$：降低 pair-breaking threshold，并往往提高 kinetic-inductance sensitivity；
- 但同样 bath temperature 下 $T/T_c$ 会变大，热准粒子更难压低；
- 提高 $T_c$：热稳定和低损耗可能更好，但目标光可能根本达不到 $2\Delta$。

所以“$T_c$ 越低越好”或“越高越好”都不成立。

---

## 4.11 映射到当前 150 GHz 双偏振 LEKID

建议以后每次谈材料参数，都同时写：

$$
T_c,\quad
\Delta_0,\quad
\nu_{\rm pb}=\frac{2\Delta_0}{h},\quad
T/T_c.
$$

若使用 Al 类低能隙吸收膜：

- 150 GHz 通常高于 pair-breaking threshold；
- GHz readout tone 单个光子远低于 $2\Delta$，通常不会直接 pair break；
- 但过高 readout power 仍可能通过加热、非平衡分布、多光子过程或电流非线性改变准粒子系统。

如果只用 Nb/NbTiN 一类高 $T_c$ 材料作吸收体，150 GHz 可能低于直接 pair-breaking threshold。因此实际超导探测器中会出现“高能隙材料负责低损耗微波结构、低能隙材料负责吸收/准粒子产生”的混合材料思路。

---

## 4.12 七个常见误区

1. **Cooper pair 就是两个电子形成的小分子。**  
   不对。BCS pair 是高度重叠的集体量子配对结构。
2. **超导无电阻是因为电子不再散射。**  
   过度简化。关键是配对凝聚态与有能隙的激发谱。
3. **$\Delta$ 就是打碎一对电子所需的全部能量。**  
   单个最低能准粒子至少需要 $\Delta$，制造两个准粒子的门槛约为 $2\Delta$。
4. **只要 $h\nu>2\Delta$，吸收效率就一定高。**  
   错。阈值只说明能量允许 pair breaking；吸收仍取决于 sheet impedance、几何、偏振和 backshort。
5. **温度足够低，$N_{qp}$ 一定严格趋近零。**  
   真实器件可能被外界辐射、基底声子和读出功率维持在非平衡底噪。
6. **读出频率低于 $2\Delta/h$，所以 readout power 与超导状态无关。**  
   错。单个光子不能直接 pair break，不代表强微波场不会加热或引起非线性。
7. **$T_c$ 越低，KID 一定越灵敏。**  
   不成立。还要考虑工作温度、热准粒子、损耗、工艺、$\alpha$、噪声和光学匹配。

---

## 4.13 本章公式阶梯

$$
\boxed{\Delta_0\approx1.764k_BT_c}
$$

$$
\boxed{h\nu_{\rm pb}\approx2\Delta}
$$

$$
\boxed{E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2}}
$$

$$
\boxed{
n_{qp}^{\rm th}
\approx
2N_0\sqrt{2\pi k_BT\Delta}
e^{-\Delta/k_BT}
}
$$

$$
\boxed{
\frac{dN_{qp}}{dt}=G-\mathcal RN_{qp}^2
}
$$

$$
\boxed{
\delta N_{qp}(t)\propto e^{-t/\tau_{qp}}
}
$$

最终重新接回：

$$
\boxed{
N_{qp}
\rightarrow
\sigma_1,\sigma_2
\rightarrow
L_k,Q_i
\rightarrow
S_{21}
}
$$

下一版将正式打开中间这一步：Mattis–Bardeen 与 surface impedance。

---

## 4.14 90–120 分钟任务

1. 写函数用 $T_c$ 计算 $\Delta_0$ 和 $\nu_{\rm pb}$，代入 Ti、Al、Nb、NbTiN；
2. 画 $\Delta(T)/\Delta_0$ 对 $T/T_c$ 的 BCS-like 插值；
3. 画 $n_{qp}^{\rm th}/(2N_0\Delta_0)$ 对 $T/T_c$ 的半对数图；
4. 数值积分 $dN/dt=G-\mathcal RN^2$，从不同初值观察其收敛到同一 steady state；
5. 画 $\tau_{qp}=10\,\mu$s、$100\,\mu$s、$1$ ms 的恢复曲线；
6. 闭卷回答：为什么 KID 材料选择必须同时考虑 $T/T_c$ 与 $h\nu/2\Delta$？

---

## 4.15 闭卷理解检查

1. 普通金属和超导态在低能激发谱上最关键的区别是什么？
2. Cooper pair 为什么不能简单理解成两颗局域电子？
3. 为什么 pair-breaking threshold 约为 $2\Delta$？
4. 若 $T_c$ 增大一倍，$\Delta_0$ 和 $\nu_{\rm pb}$ 如何变化？
5. $n_{qp}^{\rm th}$ 为什么对温度极其敏感？
6. 为什么真实 KID 在极低温仍可能有 non-equilibrium quasiparticles？
7. generation 与 recombination 如何建立稳态？
8. $\tau_{qp}$ 为什么会进入 detector bandwidth？
9. 为什么 150 GHz 可以直接 pair break Al，却未必能直接 pair break NbTiN？
10. 为什么“读出光子低于 $2\Delta$”仍不代表 readout power 可以任意增加？

### 本章一句话

$$
\boxed{
T_c
\rightarrow
\Delta
\rightarrow
(N_{qp}^{\rm thermal}+N_{qp}^{\rm optical})
\rightarrow
\tau_{qp}
\rightarrow
\sigma_1,\sigma_2
\rightarrow
S_{21}
}
$$

