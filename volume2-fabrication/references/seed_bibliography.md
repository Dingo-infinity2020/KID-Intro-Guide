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

## 6. Substrate / interface / TLS loss

### McRae et al., 2020 — Materials loss measurements using superconducting microwave resonators

- NIST: <https://www.nist.gov/publications/materials-loss-measurements-using-superconducting-microwave-resonators>
- Review of Scientific Instruments 91, 091101 (2020)

为什么重要：建立 participation ratio、TLS、quasiparticle、vortex 等损耗机制的统一实验语言。第二册第 2、7、8 章可以用它避免把低 `Qi` 简化成某一个工艺步骤。

### Bruno et al., 2015 — Reducing intrinsic loss in superconducting resonators by surface treatment and deep etching of silicon substrates

- arXiv: <https://arxiv.org/abs/1502.04082>

为什么重要：直接展示 substrate surface treatment 与改变高场界面 participation 可以改善 resonator loss，是“基底表面不是机械背景”的强证据。

### Earnest et al., 2018 — Substrate surface engineering for high-quality silicon/aluminum superconducting resonators

- arXiv: <https://arxiv.org/abs/1807.08072>

为什么重要：Al-on-Si 体系中对不同 substrate preparation 做对照，并结合截面表征与低温 `Qi`。很适合作为第 2 章 controlled split 的例子。

## 7. Lithography / linewidth 与 resonance frequency

### Li et al., 2022 — Strategies for reducing frequency scatter in large arrays of superconducting resonators

- arXiv: <https://arxiv.org/abs/2203.17244>

为什么重要：用专门设计的 linewidth sweep 证明 inductor linewidth fluctuation 可以系统性地移动 resonance frequency。第 4 章据此把 CD metrology 与 frequency collision 直接连起来。

### Liu et al., 2017 — Superconducting micro-resonator arrays with ideal frequency spacing and extremely low frequency collision rate

- arXiv: <https://arxiv.org/abs/1711.07914>

为什么重要：展示通过 lithographic trimming 修正实际 resonance frequencies、改善 collision-limited yield。可用于第 4、9 章说明“测量 → 版图反馈”是真实可行的工程路线。

## 8. Etch edge / residue 与 microwave loss

### High-Q trenched aluminum coplanar resonators with an ultrasonic edge microcutting for superconducting quantum devices, 2023

- Scientific Reports: <https://www.nature.com/articles/s41598-023-42332-6>

为什么重要：比较不同 substrate / metal etch 条件下的 resonator `Qi`，并讨论受损边缘、聚合物残留和高场界面。它不直接等价于 LEKID 工艺，但很适合提醒第 5 章：etch 的评价指标不能只有“刻通了”。

## 当前文献缺口

v0.2 前继续补齐：

- Al thin-film `Rsq / Tc / thickness / Lk_square` 的更多定量实验关联；
- packaging / wirebond / slotline / cavity modes；
- KID fabrication traveler、test coupon、wafer map 的公开工程案例；
- 适合第一次 Al LEKID run 的 room-temperature metrology 与 acceptance gate；
- dicing / backside / package 对毫米波 optical stack 与微波寄生模式的影响；
- 从 `f0, Qi, Qc` 空间分布做 fabrication root-cause analysis 的实例。

注意：第二册不会从论文中直接复制工艺参数作为本地 recipe；任何可执行工艺条件最终必须由目标加工平台 SOP 和管理员确认。
