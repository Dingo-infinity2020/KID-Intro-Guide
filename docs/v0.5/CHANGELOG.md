# v0.5 Changelog — 2026-09-07

## 新增

- 新增“微波谐振器与 IQ 读出”完整章节。
- 从 `Q = ω0 U / Ploss` 推导 `Qi/Qc/Qr` 及 `1/Qr = 1/Qi + 1/Qc`。
- 建立 `Δf = f0/Qr` 与 time-domain ring-down 的统一图景。
- 区分 energy lifetime `τE = Qr/ω0` 与 amplitude lifetime `τA = 2Qr/ω0`。
- 推导 ideal hanger/notch resonator 的复数 `S21`。
- 解析推导 IQ circle 的圆心、半径与 resonance point。
- 引入 fixed-tone readout 的小信号线性化，以及 frequency / dissipation response 的几何直觉。
- 引入 cable delay、complex gain、effective asymmetry 和真实 VNA fitting 流程。
- 新增 `examples/resonator_basics.py`。
- 新增 `examples/resonator_fit_demo.py`。

## 维护

- 每个正式版本目录同时保存 PDF、LaTeX、Markdown、README、CHANGELOG 和配套代码。
- 最新 PDF 必须作为 `docs/v0.5/` 中的普通 Git 文件长期保存，不只作为 Actions artifact。
- v0.5 在 GitHub 的独立 TeX Live 环境中执行两次 XeLaTeX 编译，并校验为 57 页。

## 参考资料新增

- M. S. Khalil et al., “An analysis method for asymmetric resonator transmission applied to superconducting devices,” *Journal of Applied Physics* 111, 054510 (2012), DOI 10.1063/1.3692073。
- S. Probst et al., “Efficient and robust analysis of complex scattering data under noise in microwave resonators,” *Review of Scientific Instruments* 86, 024706 (2015), DOI 10.1063/1.4907935。
