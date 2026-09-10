# v0.10 Step 3-A — 公开教材化语言审校

本阶段建立在已冻结的 Step 2 架构 checkpoint 上，只处理读者可见语言与稳定引用，不改变核心物理、公式和章节主结构。

## 本轮完成

- 将“你的 150 GHz LEKID”“你现在的 Sonnet/CST”“你当前几何”等项目私人化表述改为公开教材/工程案例语气；
- 清除正文标题与叙述中的 v0.5/v0.6/v0.7/v0.8/v0.9 开发历史泄漏；
- 将配套 Python 指针统一到稳定的 `examples/` 路径，并在仓库根目录建立六个 canonical 示例；
- 将 150 GHz 双偏振 LEKID 保留为真实的进阶工程案例，但不再默认读者就是该项目的研究者；
- 保留教学性的第二人称（例如“你应该能回答”），避免把教材改成僵硬的论文口吻。

## 明确未处理

Step 3-B 将继续做：术语首次出现时的中英正式定义、缩写表、常用符号表，以及最影响陌生初学者连续阅读的知识跳跃。

后续 Step 4 再统一核心公式的“数学—物理—工程—适用条件”解释层；Step 5 做全书版式、宽表、代码块、参考文献、尾页与 PDF metadata 收尾。


## Step 3-B 补充

- 根据 Step 3-A 自动审计逐项清除了剩余私人项目口吻和历史版本标签；
- 新增“符号、缩写与术语速查”前置章节，覆盖 KID/LEKID/VNA/ADC/DDC/FDM/NEP/PSD/ASD/TLS 与核心符号；
- 明确 $\nu$（信号光频率）、$f_0$（GHz 谐振频率）和 noise PSD 中 Fourier frequency 的区别；
- 统一说明 quasiparticle、pair breaking、meander、notch、probe tone、responsivity、co/cross-pol、backshort 的中文口径；
- reader-facing 正文中 v0.1–v0.9 历史版本标签已作为硬门禁清零。

Step 3 下一小步转为“知识跳跃审校”：优先检查第 2–5 章是否对完全没有超导背景的读者过快，并补桥接段，而不是继续机械替换措辞。


## Step 3-C 补充：知识跳跃桥接

本小步不增加新的理论主线，而是针对完全新手最容易中断连续阅读的四个位置补桥：

- 第 2 章明确“先看因果地图、允许黑箱暂存”，避免读者把首次出现的所有符号都当成必须当场掌握；
- 第 3 章先解释电路语言 $(V,I,L)$ 与材料语言 $(E,J,n_s,v)$ 的关系，再进入动能电感推导；
- 第 4 章在能带/BCS 公式前先澄清 $E_F$、$\Delta$、quasiparticle 三个概念的直觉含义；
- 第 5 章采用“两遍阅读法”：第一遍只建立 $\sigma_1$=耗散、$\sigma_2$=感性响应的桥，第二遍再进入 Mattis--Bardeen 的定量层；
- 同时修复 Markdown 中重复的 Part II 标题，并清除“这一版/下一版”两处开发历史式措辞。

这些改动遵循“少改物理、多改解释”，不改变原有核心公式、公式约定或章节编号。


## Step 3-D 补充：版式与 PDF outline 清障

根据 Step 3-C 两遍 XeLaTeX 日志，本轮优先处理明确可定位的横向溢出，而不是凭肉眼猜排版：

- 全宽 `tabularx` 显式取消段首缩进，修复约 20–22 pt 的整表右移；
- 压缩材料响应、resonance fitting、光学响应三张横向流程图的节点间距与最小宽度；
- 将 GHz/150 GHz 频率示意图横向比例从 0.085 cm/GHz 收紧为 0.072 cm/GHz；
- 将第 11 章单行验证证据链拆为两行 aligned box，针对日志中约 99 pt 的严重 overfull；
- 为 3 个含数学符号的章标题增加纯文本 PDF/TOC 标题，消除 hyperref 对 math token 的 outline 警告；
- 顺手清理“前五个版本”和“Day 2003”两处公开教材不够自然的措辞。

验收方式：Step 3-D workflow 在第二遍 XeLaTeX 后自动解析 log；任何超过 8 pt 的 `Overfull \\hbox` 都视为失败并阻止 checkpoint 提交。
