\chapter{超导基础最小知识集：Cooper pair、能隙与准粒子}

\begin{goalbox}
这一章不试图把 BCS 理论从头推完。目标是建立一套足够支撑 KID 设计的“最小超导语言”。学完后，你应该能回答：
\begin{enumerate}
  \item 普通金属与超导态在“可激发的低能状态”上有什么本质区别？
  \item Cooper pair 为什么不能简单理解成两个紧紧抱在一起的电子？
  \item 能隙 $\Delta$、临界温度 $T_c$ 与 pair-breaking 阈值之间是什么关系？
  \item 什么是 quasiparticle（准粒子），为什么 KID 真正关心的是 $N_{\qp}$？
  \item 为什么热准粒子在低温下呈指数压低，而真实器件仍可能存在 excess quasiparticles？
  \item pair breaking、recombination（复合）与 quasiparticle lifetime（准粒子寿命）如何决定 KID 的响应速度与灵敏度？
\end{enumerate}
\end{goalbox}

\section{为什么现在才补“超导基础”？}
前两章我们已经知道：
\[
P_{\rm abs}\rightarrow N_{\qp}\rightarrow L_k,Q_i\rightarrow f_0,S_{21}.
\]
第 3 章又从载流子惯性推出了 $L_k$。但这里一直有一个“黑箱”：
\[
\boxed{\text{光子为什么会让 }N_{\qp}\text{ 增加？}\qquad
N_{\qp}\text{ 到底是什么？}}
\]

本章就是打开这个黑箱。对 KID 设计者来说，最重要的不是会写完整 BCS gap equation，而是建立下面这条微观链：
\[
\boxed{
T_c\rightarrow\Delta(T)
\rightarrow
\text{准粒子可激发能量}
\rightarrow
N_{\qp}(T,P_{\rm abs})
\rightarrow
\tau_{\qp}
\rightarrow
L_k,Q_i,S_{21}
}
\]

\begin{intuitionbox}
把超导体想成一个“低能激发被能隙挡住的电子系统”。KID 的工作，本质上是用毫米波/亚毫米波给这个系统制造少量准粒子，再用 GHz 谐振器非常灵敏地读出这些准粒子改变了多少复电导。
\end{intuitionbox}

\section{正常金属与超导态：区别不只是“电阻变成零”}

\subsection{正常金属：费米面附近有大量低能激发}
在金属中，电子填充到 Fermi energy（费米能）$E_F$ 附近。只要提供很小的能量，就可以在 $E_F$ 附近制造电子--空穴激发。对交流电流来说，电子还会不断受到晶格、杂质和缺陷散射，因此产生耗散。

这时可以用一句非常粗略但有用的话概括：
\[
\boxed{\text{正常金属在 }E_F\text{ 附近“很容易被激发”。}}
\]

\subsection{超导态：形成具有共同相位的配对基态}
对于常规超导体，温度降到 $T_c$ 以下后，费米面附近的一部分电子通过有效吸引相互作用形成 Cooper pairs，并进入一个具有宏观相干相位的配对基态。

这里有两个需要立即纠正的直觉：
\begin{itemize}
  \item 超导不是因为“电子突然不与任何东西碰撞”；
  \item Cooper pair 也不是两个电子变成了一颗局域的小分子。
\end{itemize}

真正关键的是：\textbf{体系的低能激发谱发生了重构，并出现能隙 $\Delta$。}

\begin{center}
\begin{tikzpicture}[x=1.05cm,y=0.78cm]
  \draw[->,draw=KidDark!75] (-4.4,0)--(4.7,0) node[right,font=\small] {$\xi=\varepsilon-E_F$};
  \draw[->,draw=KidDark!75] (0,-0.2)--(0,3.4) node[above,font=\small] {准粒子激发能量 $E$};

  \draw[dashed,draw=KidDark!45,line width=0.8pt] (-3.6,3.0)--(0,0)--(3.6,3.0);
  \node[font=\scriptsize,anchor=west,text=KidDark!65] at (2.05,2.75) {正常态：$E=|\xi|$};

  \draw[draw=KidBlue,line width=1.35pt,domain=-3.5:3.5,samples=100,smooth,variable=\x]
    plot ({\x},{sqrt(\x*\x+0.75*0.75)});
  \node[font=\scriptsize,text=KidBlue,anchor=west] at (2.0,2.05) {超导态：$E=\sqrt{\xi^2+\Delta^2}$};

  \draw[KidRed,-{Stealth[length=2mm]},line width=1pt] (-0.55,0.04)--(-0.55,0.72);
  \draw[KidRed,dashed,line width=0.7pt] (-0.55,0.75)--(0,0.75);
  \node[font=\scriptsize,text=KidRed,anchor=east] at (-0.67,0.39) {$\Delta$};
  \fill[KidBlue] (0,0.75) circle (1.3pt);
  \node[font=\scriptsize,text=KidDark!70] at (0,-0.42) {$E_F$};
\end{tikzpicture}
\end{center}

上图只想表达一件事：当 $\xi=0$，正常态可以有趋近于零的激发能量；而超导态的准粒子最小激发能量是 $\Delta$。

\section{Cooper pair：KID 需要掌握到什么程度？}

\subsection{一对典型的量子数}
在最简单的常规 $s$ 波 BCS 图景中，常把一对电子写成：
\[
(\mathbf{k},\uparrow),\qquad(-\mathbf{k},\downarrow).
\]
也就是近似相反动量、相反自旋的配对。晶格振动（phonon，声子）介导的有效吸引可以战胜一部分库仑排斥，使费米面附近的电子产生配对不稳定性。

\subsection{它不是“两颗电子抱成一个小球”}
Cooper pair 的空间尺度可以远大于晶格常数，许多 pair 彼此高度重叠。真正形成超导的是一个集体的配对凝聚态，而不是大量彼此独立的小分子。

因此我们以后写“打碎一个 Cooper pair”时，应该把它理解成：
\[
\boxed{\text{从配对基态中制造两个准粒子激发}}
\]
而不是机械地想象“把一根两电子化学键掰断”。

\begin{mistakebox}
“Cooper pair 的结合能就是 $2\Delta$”是容易误导的说法。对 KID 而言，最安全的表述是：\textbf{制造两个最低能准粒子激发至少需要约 $2\Delta$ 的能量}。$\Delta$ 是单个准粒子激发谱的能隙参数。
\end{mistakebox}

\section{BCS 能隙 $\Delta$：把材料与探测频率连接起来}

\subsection{零温弱耦合关系}
对于常规弱耦合 BCS 超导体，
\[
\boxed{\Delta_0\equiv\Delta(T=0)\approx1.764\,k_B T_c.}
\]

这条关系对 KID 特别重要，因为它把一个容易测量的材料参数 $T_c$ 直接变成能量尺度。

当 $T\rightarrow T_c$ 时，
\[
\Delta(T)\rightarrow0.
\]
工程计算中常用下面的近似插值来画趋势：
\[
\Delta(T)\approx
\Delta_0\tanh\!\left[
1.74\sqrt{\frac{T_c}{T}-1}
\right],\qquad 0<T<T_c.
\]
它是方便的 BCS-like 插值，不应被当成完整 gap equation 本身。

\subsection{pair-breaking 阈值}
要制造两个最低能准粒子，最基本阈值是：
\[
\boxed{h\nu_{\rm pb}\approx2\Delta.}
\]
在低温、弱耦合近似下：
\[
\boxed{
\nu_{\rm pb}(0)
\approx
\frac{2\Delta_0}{h}
\approx
73.5\ \mathrm{GHz/K}\times T_c.
}
\]

于是 KID 的材料选择第一次和观测频率直接相遇。

\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lcccc}
\toprule
材料 & 代表性 $T_c$ (K) & $\Delta_0$ (meV) & $\nu_{\rm pb}$ (GHz) & \SI{150}{GHz} 直接 pair break?\\
\midrule
Ti & 0.4 & 0.061 & 29 & 是 \\
Al & 1.2 & 0.182 & 88 & 是 \\
Nb & 9.2 & 1.40 & 676 & 否 \\
NbTiN & 14 & 2.13 & 1029 & 否 \\
\bottomrule
\end{tabular}
\end{center}

\noindent
上表只使用弱耦合公式与代表性 $T_c$ 做数量级估算。\textbf{真实薄膜的 $T_c$、能隙和强耦合修正会随材料配比、膜厚与沉积工艺改变。}

\begin{projectbox}
若吸收材料近似为 Al，$T_c\sim\SI{1.2}{K}$ 时 $\nu_{\rm pb}\sim\SI{88}{GHz}$，因此 \SI{150}{GHz} 光子高于 pair-breaking 阈值；而 1--5 GHz 读出微波远低于该阈值。这个频率层级正是 KID “高频光负责改变器件、低频微波负责询问器件”的材料基础。
\end{projectbox}

\section{准粒子：不是普通电子，而是超导体系的激发}

\subsection{最小能量}
BCS 准粒子能量写成：
\[
\boxed{
E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2},
\qquad
\xi_{\mathbf{k}}=\varepsilon_{\mathbf{k}}-E_F.
}
\]
因此：
\[
E_{\mathbf{k}}\ge\Delta.
\]

更严格地说，Bogoliubov quasiparticle 是电子与空穴自由度的量子叠加。KID 初学阶段暂时不需要推 Bogoliubov transformation，但要避免把 quasiparticle 简化成“一个从 Cooper pair 里掉出来的普通电子”。

\subsection{超导态密度状态}
理想 BCS $s$ 波超导体的归一化态密度可写成：
\[
\frac{N_s(E)}{N_0}
=
\begin{cases}
0, & |E|<\Delta,\\[0.4em]
\dfrac{|E|}{\sqrt{E^2-\Delta^2}}, & |E|>\Delta.
\end{cases}
\]

因此能隙内部没有理想单粒子激发态，并在 $|E|=\Delta$ 附近出现 coherence peak（相干峰）。这也是后面 Mattis--Bardeen 积分为什么总围着 $\Delta$ 附近的状态打转的根源。

\section{热准粒子：为什么降温如此有效？}

\subsection{Fermi--Dirac 占据}
准粒子的热占据服从：
\[
f(E,T)=\frac{1}{\exp(E/k_BT)+1}.
\]

当 $k_BT\ll\Delta$，热激发必须跨过能隙，因此平衡热准粒子密度近似为：
\[
\boxed{
n_{\qp}^{\rm th}(T)
\approx
2N_0\sqrt{2\pi k_BT\Delta}
\exp\!\left(-\frac{\Delta}{k_BT}\right)
}
\]
其中 $N_0$ 是 normal-state Fermi level 处的 single-spin density of states（单自旋态密度）。

这个公式最重要的不是前面的平方根，而是：
\[
\boxed{n_{\qp}^{\rm th}\propto e^{-\Delta/k_BT}.}
\]

\subsection{把指数压低看成数量级}
令 $\Delta\approx\Delta_0=1.764k_BT_c$，则：
\[
\frac{n_{\qp}^{\rm th}}{2N_0\Delta_0}
\approx
\sqrt{\frac{2\pi(T/T_c)}{1.764}}
\exp\!\left(-\frac{1.764}{T/T_c}\right).
\]

\begin{center}
\begin{tabular}{ccc}
\toprule
$T/T_c$ & $n_{\qp}^{\rm th}/(2N_0\Delta_0)$ & 直觉 \\
\midrule
0.10 & $1.3\times10^{-8}$ & 极强指数压低 \\
0.20 & $1.25\times10^{-4}$ & 已高出约 $10^4$ 倍 \\
0.30 & $2.9\times10^{-3}$ & 热准粒子开始更难忽略 \\
0.50 & $3.9\times10^{-2}$ & 已远离“深低温”极限 \\
\bottomrule
\end{tabular}
\end{center}

\begin{intuitionbox}
对 KID 而言，“低温”最好不要只写成多少 mK，而要同时问 \textbf{$T/T_c$ 是多少}。同样 \SI{100}{mK}，对 $T_c=\SI{1.2}{K}$ 的 Al 和 $T_c=\SI{0.4}{K}$ 的 Ti 意义完全不同。
\end{intuitionbox}

\subsection{真实器件为什么常常比这个公式“脏”？}
理想热平衡公式给的是 baseline（基线），但真实 KID 在很低温时常出现 excess quasiparticles（额外准粒子），来源可能包括：
\begin{itemize}
  \item 外界毫米波、红外或黑体泄漏；
  \item 宇宙线、高能粒子或基底声子；
  \item 读出功率引起的加热与非平衡分布；
  \item 材料缺陷、陷阱和复杂的声子动力学。
\end{itemize}

因此：
\[
T\rightarrow0
\]
并不自动保证
\[
N_{\qp}\rightarrow0
\]
在真实系统里严格成立。实验上看到低温频移或损耗“饱和”，不能简单归因于 BCS 热准粒子。

\section{光子如何制造非平衡准粒子：从 pair breaking 到能量级联}

吸收一个满足 $h\nu>2\Delta$ 的光子后，最初产生的激发通常高于能隙边缘，随后通过 electron--phonon interaction（电子--声子相互作用）向低能弛豫。产生的高能声子又可能继续打断其他 pair。

\begin{center}
\begin{tikzpicture}[node distance=10mm and 10mm]
  \node[flowbox,fill=KidGold!22,minimum width=25mm] (ph) {$h\nu>2\Delta$\\吸收光子};
  \node[flowbox,right=of ph,minimum width=29mm] (hq) {高能准粒子\\初始激发};
  \node[flowbox,right=of hq,minimum width=27mm] (phon) {高能声子\\弛豫产生};
  \node[flowbox,right=of phon,minimum width=31mm] (pool) {近能隙准粒子池\\$N_{\qp}\uparrow$};
  \draw[flowarrow] (ph.east)--(hq.west);
  \draw[flowarrow] (hq.east)--(phon.west);
  \draw[flowarrow] (phon.east)--(pool.west);

  \node[flowbox,below=13mm of pool,minimum width=29mm] (rec) {两个准粒子复合\\形成 Cooper pair};
  \node[flowbox,left=of rec,minimum width=29mm] (p2) {$\sim2\Delta$ 声子};
  \node[flowbox,left=of p2,minimum width=28mm,fill=KidGray] (esc) {逃逸到基底\\或降能};
  \draw[flowarrow] (pool.south)--(rec.north);
  \draw[flowarrow] (rec.west)--(p2.east);
  \draw[flowarrow] (p2.west)--(esc.east);
  \draw[flowarrow] (p2.north east) to[out=65,in=215]
    node[pos=0.52,right,font=\scriptsize]{再次 pair break} (pool.south west);
\end{tikzpicture}
\end{center}

这说明一个高能光子并不一定只对应“两个准粒子”。常用一个 pair-breaking efficiency $\eta_{\rm pb}$ 把吸收能量中最终进入低能准粒子系统的比例概括进去：
\[
N_{\qp}^{\rm excess}
\sim
\eta_{\rm pb}\frac{E_{\rm abs}}{\Delta}.
\]

对连续吸收功率，也常用能量守恒的数量级形式：
\[
\boxed{
G_{\rm opt}
\sim
\eta_{\rm pb}\frac{P_{\rm abs}}{\Delta}
}
\]
其中 $G_{\rm opt}$ 是准粒子 generation rate（产生率）。精确系数与非平衡能量级联、声子逃逸和材料有关。

\section{recombination：为什么准粒子不会一直积累？}

两个准粒子可以重新进入 Cooper-pair condensate，并释放约 $2\Delta$ 的声子能量。于是 KID 中持续存在：
\[
\boxed{\text{generation}\quad\leftrightarrow\quad\text{recombination}}
\]

一个用于建立直觉的最小 rate equation（速率方程）是：
\[
\boxed{
\frac{dN_{\qp}}{dt}
=
G-\mathcal{R}N_{\qp}^2.
}
\]
这里把几何体积等因素都吸收到有效复合系数 $\mathcal{R}$ 里，因此它只是教学用简化模型。

稳态满足：
\[
G=\mathcal{R}N_{\qp,\rm ss}^2,
\]
因此：
\[
\boxed{
N_{\qp,\rm ss}
=
\sqrt{\frac{G}{\mathcal{R}}}.
}
\]

这已经给出一个非常重要的非线性直觉：
\[
G\uparrow
\Rightarrow
N_{\qp}\uparrow
\Rightarrow
\text{recombination rate}\propto N_{\qp}^2\uparrow.
\]
所以准粒子不会无限累积。

\begin{mistakebox}
真实超导薄膜中的 quasiparticle--phonon 动力学通常需要 Rothwarf--Taylor 方程或 Kaplan 等人的电子--声子寿命理论。上面的 $G-\mathcal{R}N^2$ 是为了看懂“为什么存在稳态”和“为什么复合随 $N_{\qp}$ 增快”，不是完整材料模型。
\end{mistakebox}

\section{准粒子寿命 $\tau_{\qp}$：把微观物理连接到探测器速度}

如果在稳态附近突然增加少量准粒子，常可用单指数近似描述其恢复：
\[
\boxed{
\delta N_{\qp}(t)
=
\delta N_{\qp}(0)e^{-t/\tau_{\qp}}.
}
\]

对前面的简化模型线性化：
\[
\frac{d\,\delta N_{\qp}}{dt}
\approx
-2\mathcal{R}N_{\qp,\rm ss}\,\delta N_{\qp},
\]
所以：
\[
\tau_{\qp}
\sim
\frac{1}{2\mathcal{R}N_{\qp,\rm ss}}.
\]

它告诉我们：
\begin{itemize}
  \item 准粒子越少，复合事件越难相遇，寿命可能更长；
  \item 光学负载升高后 $N_{\qp}$ 增大，实际有效寿命常会缩短；
  \item 声子若被薄膜/基底结构反复吸收，phonon trapping 会改变观测到的有效寿命。
\end{itemize}

如果系统只有一个主导一阶时间常数，则：
\[
f_{\rm 3dB}\sim\frac{1}{2\pi\tau_{\qp}}.
\]

但 KID 还有谐振器自己的 ring-down time（衰减时间）：
\[
\boxed{
\tau_{\rm res}
=
\frac{Q_r}{\pi f_0}.
}
\]
真实时域响应通常同时受到 $\tau_{\qp}$ 与 $\tau_{\rm res}$ 约束，较慢的一环往往更容易成为带宽瓶颈。

\begin{intuitionbox}
较长的 $\tau_{\qp}$ 往往意味着同样的持续光功率可以在器件中“积累”更多准粒子，从而有利于 responsivity；但它也让响应变慢。KID 的灵敏度与时间响应并不是两个完全独立的设计指标。
\end{intuitionbox}

\section{材料选择的一条核心轴：同时比较 $T/T_c$ 与 $h\nu/2\Delta$}

现在可以把材料选择压缩成两个无量纲问题：
\[
\boxed{
\frac{T}{T_c}\quad\text{有多小？}
}
\qquad
\boxed{
\frac{h\nu}{2\Delta}\quad\text{是否大于 1？}
}
\]

前者控制 thermal quasiparticle baseline 的数量级；后者决定入射光是否具备直接 pair breaking 的能量条件。

这会产生一个很真实的工程 trade-off：
\begin{itemize}
  \item 降低 $T_c$：降低 pair-breaking threshold，并往往提高 kinetic inductance sensitivity；
  \item 但在同样 bath temperature 下，$T/T_c$ 变大，热准粒子更难压低；
  \item 提高 $T_c$：有利于低损耗和热稳定，但可能让目标光子根本达不到 $2\Delta$。
\end{itemize}

因此“$T_c$ 越低越好”或“$T_c$ 越高越好”都不是普遍结论。

\section{映射到当前 \SI{150}{GHz} 双偏振 LEKID}

\begin{projectbox}
对当前 \SI{150}{GHz} LEKID，建议以后每次谈材料或仿真参数，都同时写出四个量：
\[
T_c,\qquad
\Delta_0,\qquad
\nu_{\rm pb}=\frac{2\Delta_0}{h},\qquad
T/T_c.
\]
这样可以在设计表格里一眼判断“目标光是否能 pair break”和“工作温度是否足够深低温”。

若使用 Al 类低能隙吸收膜：
\begin{itemize}
  \item \SI{150}{GHz} 通常高于 pair-breaking threshold；
  \item GHz readout tone 单个光子远低于 $2\Delta$，通常不会直接 pair break；
  \item 但过高 readout power 仍可能通过加热、非平衡分布、多光子过程或电流非线性改变准粒子系统，所以“低于 $2\Delta$”不等于“读出功率可以无限加大”。
\end{itemize}

若只使用 Nb/NbTiN 这类高 $T_c$ 材料作为吸收体，\SI{150}{GHz} 可能低于直接 pair-breaking threshold。工程上因此常见“高能隙材料负责低损耗微波结构、低能隙材料负责吸收/准粒子产生”的混合材料思路。
\end{projectbox}

\section{七个常见误区}

\begin{mistakebox}
\begin{enumerate}
  \item \textbf{“Cooper pair 就是两个电子形成的小分子。”}\\
  不对。BCS pair 是高度重叠的集体量子配对结构。
  \item \textbf{“超导无电阻是因为电子不再散射。”}\\
  过度简化。关键是配对凝聚态与有能隙的激发谱。
  \item \textbf{“$\Delta$ 就是打碎一对电子所需的全部能量。”}\\
  对 KID 最安全的说法是：单个最低能准粒子至少需要 $\Delta$，制造两个准粒子的 pair-breaking threshold 约为 $2\Delta$。
  \item \textbf{“只要 $h\nu>2\Delta$，吸收效率就一定很高。”}\\
  错。阈值只说明能量上允许 pair breaking；光学吸收还取决于 sheet impedance、几何、偏振、backshort 等。
  \item \textbf{“温度足够低后，$N_{\qp}$ 一定严格趋近零。”}\\
  理想热平衡模型如此，但真实器件可能被外界辐射、基底声子和读出功率维持在非平衡准粒子底噪上。
  \item \textbf{“读出频率低于 $2\Delta/h$，所以 readout power 与超导状态完全无关。”}\\
  错。单个读出光子不能直接 pair break，不代表强微波场不会产生加热和非线性。
  \item \textbf{“$T_c$ 越低，KID 一定越灵敏。”}\\
  不成立。还要同时考虑工作温度、热准粒子、薄膜损耗、可加工性、$\alpha$、噪声和光学匹配。
\end{enumerate}
\end{mistakebox}

\section{本章公式阶梯}

第一层，只记能隙：
\[
\boxed{\Delta_0\approx1.764k_BT_c}
\]

第二层，把能隙变成探测频率门槛：
\[
\boxed{h\nu_{\rm pb}\approx2\Delta}
\]

第三层，认识准粒子的激发谱：
\[
\boxed{E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2}}
\]

第四层，看懂为什么冷却能压低 dark quasiparticles：
\[
\boxed{
n_{\qp}^{\rm th}
\approx
2N_0\sqrt{2\pi k_BT\Delta}
e^{-\Delta/k_BT}
}
\]

第五层，把光学负载写成 generation--recombination：
\[
\boxed{
\frac{dN_{\qp}}{dt}
=
G-\mathcal{R}N_{\qp}^2
}
\]

第六层，把准粒子动力学连接到响应速度：
\[
\boxed{
\delta N_{\qp}(t)\propto e^{-t/\tau_{\qp}}
}
\]

最后重新接回 KID：
\[
\boxed{
N_{\qp}
\rightarrow
\sigma_1,\sigma_2
\rightarrow
L_k,Q_i
\rightarrow
S_{21}
}
\]
下一版将正式打开中间这一步：Mattis--Bardeen 与 surface impedance。

\section{建议用 90--120 分钟完成的代码与手算任务}

\begin{enumerate}
  \item 写一个函数，用 $T_c$ 计算 $\Delta_0$ 与 $\nu_{\rm pb}$，分别代入 Ti、Al、Nb、NbTiN 的代表性 $T_c$；
  \item 画出
  \[
  \Delta(T)/\Delta_0
  \]
  对 $T/T_c$ 的 BCS-like 插值曲线；
  \item 用低温近似画
  \[
  n_{\qp}^{\rm th}/(2N_0\Delta_0)
  \]
  对 $T/T_c$ 的半对数图，观察从 $0.1T_c$ 到 $0.3T_c$ 跨过了多少数量级；
  \item 数值积分
  \[
  \frac{dN}{dt}=G-\mathcal{R}N^2
  \]
  ，从不同初值观察它如何回到同一个 steady state；
  \item 对 $\delta N(t)=\delta N_0e^{-t/\tau_{\qp}}$，分别画 $\tau_{\qp}=10\,\mu{\rm s}$、$100\,\mu{\rm s}$、$1\,{\rm ms}$ 的恢复曲线；
  \item 最后闭卷回答：\textbf{为什么 KID 的材料选择必须同时考虑 $T/T_c$ 与 $h\nu/2\Delta$？}
\end{enumerate}

\section{闭卷理解检查}

\begin{checkpointbox}
\begin{enumerate}
  \item 普通金属和超导态在低能激发谱上最关键的区别是什么？
  \item Cooper pair 为什么不能简单理解成两颗局域电子？
  \item 为什么 pair-breaking threshold 是约 $2\Delta$ 而不是 $\Delta$？
  \item 若 $T_c$ 增大一倍，弱耦合近似下 $\Delta_0$ 与 $\nu_{\rm pb}$ 如何变化？
  \item $n_{\qp}^{\rm th}$ 为什么对温度极其敏感？
  \item 为什么真实 KID 在极低温下仍可能存在 non-equilibrium quasiparticles？
  \item generation 与 recombination 如何建立稳态？
  \item $\tau_{\qp}$ 为什么会进入 detector bandwidth？
  \item 为什么 \SI{150}{GHz} 可以直接 pair break Al，却未必能直接 pair break NbTiN？
  \item 为什么“读出光子低于 $2\Delta$”仍不代表 readout power 可以任意增加？
\end{enumerate}
\end{checkpointbox}

\begin{formula}[title=\bfseries 本章的一句话]
\centering
\[
\boxed{
T_c
\rightarrow
\Delta
\rightarrow
\left(
N_{\qp}^{\rm thermal}
+
N_{\qp}^{\rm optical}
\right)
\rightarrow
\tau_{\qp}
\rightarrow
\sigma_1,\sigma_2
\rightarrow
S_{21}
}
\]
\end{formula}
