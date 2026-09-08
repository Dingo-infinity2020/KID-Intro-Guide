# v0.8 Changelog

发布日期：2026-09-08

## Added

- 新增“从光子到 IQ：KID 理论闭环复习与手写笔记册”。
- 新增一页式完整因果链：`hν -> pair breaking -> Nqp -> σ1/σ2 -> Lk/Qi -> f0 -> S21 -> IQ -> responsivity/noise -> NEP`。
- 新增 9 张核心复习笔记卡：pair breaking、kinetic inductance、complex conductivity、Q、IQ circle、fixed-tone readout、frequency/dissipation response、responsivity/NEP、LEKID 双频电磁身份。
- 新增“公式三问”和 5 组公式阶梯。
- 新增 15 道闭卷概念题。
- 新增一个 150 GHz、Tc=1.2 K、f0=2.5 GHz 的 Al LEKID 综合闭环题。
- 新增独立的“参考答案与详细解析”章节，答案按推导步骤、物理解释、工程意义和常见误区展开。
- 新增 `capstone_chain_demo.py` 与 `iq_circle_workbook.py` 两个复习用 Python 示例。

## Changed

- 讲义版本更新为 v0.8。
- 后续路线调整：v0.9 进入理论—Sonnet—CST—加工—低温 S21—光学标定验证矩阵；v1.0+ 再进入阵列与实时读出。

## Validation

- XeLaTeX 连续编译两次通过。
- 最终 PDF：106 页。
- 新增章节已渲染检查，修正了公式阶梯中一处越界排版。
- `capstone_chain_demo.py` 和 `iq_circle_workbook.py` 已实际运行验证。
