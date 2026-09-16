# 第二册首批参考资料种子

这不是最终 bibliography，而是 v0.1 阶段先固定几条高价值证据链，避免正文从“常识印象”开始长歪。

## 1. 与当前 150 GHz Al LEKID 路线最直接相关

### McCarrick et al., 2014 — Horn-coupled, commercially-fabricated aluminum LEKIDs

- Review of Scientific Instruments 85, 123117 (2014)
- DOI: <https://doi.org/10.1063/1.4903855>
- arXiv: <https://arxiv.org/abs/1407.7749>

为什么重要：薄 Al film + silicon wafer + standard photolithography，且目标就是 150 GHz horn-coupled LEKID。第二册用它作为“单层 Al LEKID 工艺最小闭环”的代表案例，而不是把它当成唯一 recipe。

### McCarrick et al., 2017/2018 — Design and performance of dual-polarization LEKIDs

- arXiv: <https://arxiv.org/abs/1710.02239>

为什么重要：与我们第一册中 150 GHz 双偏振 LEKID 工程案例直接衔接；适合把 fabrication、module assembly、readout 和 polarization performance 串起来。

## 2. 加工不均匀如何变成 frequency scatter / collision

### Shu et al., 2021 — Understanding and minimizing resonance frequency deviations on a 4-in. kilo-pixel KID array

- CaltechAUTHORS: <https://authors.library.caltech.edu/records/ewdqy-w8655>
- arXiv: <https://arxiv.org/abs/2105.14046>

为什么重要：直接把 measured resonator dimensions、film thickness 与 resonance frequency deviations 对上，并讨论 fabrication imperfection → collision → yield。这篇应成为第 9 章 DfM 的核心文献之一。

### McKenney et al., 2019 — Tile-and-trim micro-resonator array fabrication optimized for high multiplexing factors

- NIST: <https://www.nist.gov/publications/tile-and-trim-micro-resonator-array-fabrication-optimized-high-multiplexing-factors>
- DOI: <https://doi.org/10.1063/1.5037301>

为什么重要：展示 wafer-scale material variation 如何变成 frequency spacing deviation，并把 fabrication statistics 与 multiplexing yield 连起来。

## 3. 刻蚀本身也可能制造 frequency non-uniformity

### Improvement of Design and Fabrication for Equally Spaced Resonant Frequencies in Niobium LEKIDs, 2019

- J-STAGE: <https://www.jstage.jst.go.jp/article/jcsj/54/1/54_33/_article/-char/en>

为什么重要：文中把 resonance spacing non-uniformity 与 silicon surface over-etch depth 联系起来，并用 etch-stop 思路改进。它很适合作为第 5 章的案例：不要把“金属已经刻干净”当作图形转移结束。

## 4. 单层 LEKID 工艺为什么适合入门

### Roesch et al., 2012 — Development of Lumped Element Kinetic Inductance Detectors for NIKA

- arXiv: <https://arxiv.org/abs/1212.4585>

为什么重要：文章明确讨论单金属层 silicon-substrate LEKID 的相对简洁加工，并把 feedline coupling、pixel geometry、frequency spacing 与实际阵列测试联系起来。适合第 0 章解释为什么第二册先以 single-layer Al LEKID 为主线。

## 5. 平台一手资料

### SECUF F1 微纳加工实验室

- <https://secuf.iphy.ac.cn/system/tsp/micro-nano-fabrication-laboratory>

为什么重要：决定我们真正可能接触到的曝光、沉积、刻蚀、表征、dicing 和 wire-bond 能力。公开设备清单只能定义“可能性”，真正 recipe / material policy / SOP 仍需现场确认。

## 下一轮文献缺口

v0.2 前还需要系统补齐：

- Al thin-film `Rsq / Tc / thickness / Lk_square` 的实验关联；
- substrate surface preparation 与 microwave loss；
- lithography / resist residue / descum / etch damage 与 superconducting resonator `Qi`；
- packaging / wirebond / slotline / cavity modes；
- KID fabrication traveler、test coupon、wafer map 的工程案例；
- 适合第一次 Al LEKID run 的 room-temperature metrology 与 acceptance gate。

注意：第二册不会从论文中直接复制工艺参数作为本地 recipe；任何可执行工艺条件最终必须由目标加工平台 SOP 和管理员确认。
