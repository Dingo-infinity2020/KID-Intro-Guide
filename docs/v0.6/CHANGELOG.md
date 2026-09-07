# v0.6 Changelog — 2026-09-07

## 新增
- 新增第 7 章“光学响应、噪声与 NEP”。
- 从 absorbed optical power 与 pair-breaking efficiency 推到 quasiparticle generation rate。
- 建立线性工作点附近 `dNqp/dPabs ≈ eta_pb tau_qp / Delta`。
- 定义 frequency、dissipation 与 complex I/Q responsivity。
- 引入 quasiparticle lifetime 与 resonator ring-down 的级联动态响应。
- 区分 PSD、ASD，并严格定义 input-referred NEP。
- 引入 photon shot / bunching noise、generation-recombination noise、TLS noise 与 amplifier/readout noise。
- 给出 150 GHz、Al、1 pW absorbed loading 的数量级例子。
- 新增 `examples/optical_responsivity_demo.py` 与 `examples/noise_budget_demo.py`。

## 视觉与维护
- 完整渲染检查新增章节及流程图，箭头语义延续 v0.2+ 规则。
- 每个正式版本继续同时保存 PDF + LaTeX + Markdown + README + CHANGELOG + 配套代码。
- 最新 PDF 必须作为普通 Git 文件存在于 `docs/v0.6/`。

## 说明
- GR noise 中的 factor-of-two 依赖 one-sided/two-sided PSD 和 quasiparticle generation convention；正文显式提醒比较文献时先统一约定。
