# v0.10 Step 3-A — Editorial residual audit

自动扫描 reader-facing Step 3 源码中仍可能带有版本历史或项目私人化语气的文本。此文件用于下一轮人工审校，不代表所有命中都必须删除。

## LaTeX

- L27: `\hypersetup{colorlinks=true,linkcolor=KidBlue,urlcolor=KidBlue,citecolor=KidTeal,pdftitle={KID入门讲义 v0.10 Step 3 Editorial Preview},pdfauthor={KID Intro Guide project}}`
- L36: `\fancyhead[L]{KID 入门讲义 v0.10 Step 3 Editorial Preview}`
- L92: `% --- Flow-chart conventions (v0.2+, retained in v0.3) ---`
- L746: `对你的双偏振直接吸收 LEKID，今后每次看一个几何结构都可以问两个问题：\\`
- L1150: `对你当前的 \SI{150}{GHz} 双偏振直接吸收 LEKID，meander 的线宽、总路径长度和膜厚至少同时参与四件事：`
- L2436: `v0.4 已经把材料链条推进到`
- L2505: `例如采用一个与你当前读出频段接近的示例：`
- L2862: `  \item 对你当前 Sonnet 结果，哪些 $Q$ 可以直接从 $S_{21}$ 得到，哪些解释依赖真实超导材料模型？`
- L3526: `你现在采用 hairpin / half-hairpin + wiggle 的思路，本质上就是在同时优化四件事：\textbf{active volume、毫米波有效阻抗、GHz 电感、偏振纯度}。所以以后不要把“wiggle 长度”只当成机械几何参数；它应该进入 optical + microwave 两套 sweep。`
- L3640: `这正好解释你当前 CST 验证中为什么反射/散射能量闭合不能只看 TE$_{11}$ 的两个偏振分量：在 \SI{150}{GHz}、$D=\SI{1.6}{mm}$ 的圆波导里，TM$_{01}$ 已经是传播通道。若忽略它，$|S|^2$ 能量闭合可能看起来“凭空丢失”。`
- L3951: `这一章\textbf{不再引入新的核心理论}。目标是把前面 v0.1--v0.7 中已经出现的概念重新压缩、重排，并训练你在不翻书的情况下完成三件事：`
- L5154: `\section{v0.8 最终闭卷清单}`
- L5156: `如果下面 12 项中有 10 项以上能够不翻书讲清楚，可以认为 v0.1--v0.7 的理论主链已经基本串起来：`
- L5535: `v0.9 不要求你一开始就拥有完美材料参数，而要求把材料不确定度\textbf{显式化}。例如对 $L_{k,\square}$、film thickness、$R_\square$ 做上下界 sweep，回答：`
- L5636: `下面是 v0.9 最核心的表。以后每做完一个结果，都应能落到其中一行。`
- L5742: `\section{v0.9 项目执行顺序：不要并行做所有事情}`
- L5832: `\section{v0.9 最终总图：把所有东西压回一条科研证据链}`
- L5861: `v0.9 的目标不是让你“多会几个软件”，而是形成一种以后做任何 KID 都能复用的习惯：\textbf{先写 claim，再定义 observable；先过数值 gate，再比较设计；先做 uncertainty，再谈 improvement；最后让实验结果反过来更新模型。}`

## Markdown

- L1: `# KID 入门讲义 v0.10 — Step 3 公开教材化审校预览`
- L4: `**版本：v0.10 Step 3 Editorial Preview · 2026-09-10**`
- L859: `## 3.9 映射到你的 150 GHz 双偏振 LEKID`
- L1730: `本章把 v0.4 的材料响应真正接到读出：理解 $Q_i,Q_c,Q_r$、linewidth、ring-down、ideal notch、IQ circle、fixed-tone readout 与真实 resonance fitting。`
- L1877: `- `examples/v0.6/resonator_basics.py`：理想 notch、IQ circle、频移和 fixed-tone IQ 响应；`
- L1878: `- `examples/v0.6/resonator_fit_demo.py`：加入 complex gain、cable delay、asymmetry 和噪声，拟合回 resonance 参数。`
- L1898: `本章对应 LaTeX/PDF v0.6 的完整第 7 章。核心链条：`
- L2248: `5. **Detector layer**：把 $P_{\rm abs}$ 接入 v0.6 responsivity / NEP。`
- L2252: `## 8.18 v0.7 Python 示例`
- L2261: `- v0.8：把 v0.1–v0.7 理论逐项映射到当前双偏振 150 GHz LEKID，形成 Sonnet/CST/实验验证矩阵；`
- L2262: `- v0.9+：阵列 FDM、resonance collision、readout budget、RFSoC/FPGA/GPU 实时读出与 instrument closure。`
- L2273: `> **本章目标**：不再引入新的核心理论，而是把 v0.1–v0.7 压缩成一套可以手写、闭卷复述、自己推导的知识闭环。建议第一次阅读时遮住第 10 章答案，真的拿一张纸完成空格、推导和综合题。`
- L3500: `v0.9 的核心习惯：**先写 claim，再定义 observable；先过 numerical gate，再比较设计；先量 uncertainty，再谈 improvement；最后让实验反过来更新模型。**`
- L3502: `- v0.9：把 v0.1–v0.8 理论逐项映射到当前双偏振 150 GHz LEKID，形成 Sonnet/CST/加工/低温 S21/光学标定验证矩阵；`
- L3507: `- v0.6：$Q_i/Q_c/Q_r$、notch resonator、IQ circle、固定 tone 读出与实际 fitting`
- L3508: `- v0.6：optical responsivity、NEP 与 photon / GR / TLS / amplifier noise`
- L3509: `- v0.7：LEKID absorber / IDC / coupling / polarization / backshort 电磁设计`
- L3510: `- v0.8：映射到当前双偏振 150 GHz LEKID 项目与 Sonnet/CST 验证矩阵，并加入 Python 数值练习`
