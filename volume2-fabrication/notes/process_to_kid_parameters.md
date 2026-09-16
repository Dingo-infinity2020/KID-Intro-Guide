# 工艺—KID 参数对应表（v0.1）

这张表是第二册的核心索引。后续每章正文都应回填这里，而不是各讲各的。

| 工艺/过程变量 | 首先改变什么 | 可能传播到 KID 的量 | 优先表征/证据 | 备注 |
|---|---|---|---|---|
| substrate 材料/厚度 | 介电边界、机械厚度 | `C, f0, optical boundary` | wafer spec、厚度、材料批次 | 需要与 EM 模型一致 |
| 表面清洗/暴露历史 | 界面、残留、氧化状态 | `Qi, TLS-like loss, adhesion` | traveler、表面检查、对照片 | 不应把低 Qi 自动归因于此 |
| 超导膜厚 `t` | sheet geometry | `Rsq, Lk_square, f0` | profilometer/ellipsometry、map | 与电阻率共同决定 Rsq |
| 薄膜电阻率/方阻 | normal-state transport | `Lk` 先验、频率散布 | four-probe / witness sample | 应和 Tc 一起看 |
| `Tc` | gap / superconducting state | `Lk`, responsivity 模型输入 | Tc test | 材料批次关键指标 |
| 膜厚/材料均匀性 | wafer-scale material gradient | `f0` spatial scatter、collision | thickness/Rsq wafer map | 阵列尤其关键 |
| lithography linewidth bias | 实际 `w` | `Lg, Lk, current density` | CD measurement / SEM | meander 敏感 |
| lithography gap bias | 实际 gap | `C, Cc`, optical fill | CD measurement | IDC/coupler 敏感 |
| over/under etch | CD、sidewall、残留 | `f0, Qi`, shorts/opens | microscope/SEM/profile | 需要区分系统偏差与随机缺陷 |
| lift-off residue/fence | 边缘与局部残留 | `Qi`, shorts, local current | microscope/SEM | 与 resist profile 相关 |
| dicing/handling | edge damage、particles、stress | yield、局部缺陷 | optical inspection | 加工末端仍可引入问题 |
| package geometry | EM cavity / parasitics | baseline、spurious mode、coupling | package drawing + EM check | 不属于“芯片工艺”但会混淆诊断 |
| wirebond/ground | return path / parasitic L | feedline response、slotline-like issues | bond map、照片 | 必须版本化记录 |

## 使用方法

遇到异常时从“可观测量”反向查，而不是从最熟悉的工艺步骤开始猜。例如 `f0` 整片偏移，应同时检查材料（`Rsq/t/Tc`）、几何（CD bias）和电磁边界，而不是只调整版图。
