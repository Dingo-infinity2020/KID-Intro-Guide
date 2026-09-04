# CHANGELOG - v0.2

## 图示重做

- 重做 KID 总体路线图，移除原来的闭环式误导箭头。
- 重做“双频率协同工作”图：150 GHz 光学因果链与 GHz 读出信号流分成两条泳道。
- 重做 LEKID meander/IDC/feedline 图：结构组成和互易耦合不再用单向因果箭头表示。
- 重做全章因果链地图：感性支路与耗散支路明确分叉、再汇入谐振器响应。
- 新增统一箭头规范：实线=因果/信号流；虚线=参数影响；无箭头=结构/互易耦合。

## 新增理论内容

新增“动能电感”章节：

- 从 `m dv/dt = qE` 推导 `Lk`；
- 能量法交叉验证；
- 澄清 Cooper-pair density 与 superfluid electron density 的记号约定；
- 引入 London penetration depth；
- 引入 sheet kinetic inductance 与方块数；
- 给出薄膜近似及适用范围；
- 引入 kinetic inductance fraction `alpha` 与小信号频移；
- 映射到 150 GHz 双偏振 LEKID；
- 增加 PEC vs superconducting surface impedance 的 Sonnet/CST 建模提醒。

## 后续

v0.3 计划进入 Cooper pair、BCS 能隙、热准粒子与 `Nqp(T)`，再在 v0.4 进入复电导与 Mattis-Bardeen。
