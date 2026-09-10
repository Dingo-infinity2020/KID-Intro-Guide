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
