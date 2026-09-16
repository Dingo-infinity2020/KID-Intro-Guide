# 第二册章节契约（Chapter Contracts）

用途：控制每一章的边界。以后扩写时，先满足“必须回答的问题”和“出口”，再考虑增加细节。

## Chapter 0 — 一块 KID 芯片怎样出生

必须回答：

- GDS 为什么不等于最终器件？
- 一次 fabrication run 至少要留下哪些证据？
- witness sample、test coupon、process traveler 分别解决什么问题？

出口：读者能画出 `layout -> fabrication -> metrology -> cooldown -> feedback` 流程图，并建立 Batch ID。

## Chapter 1 — 洁净室、污染与工艺纪律

必须回答：

- particle、organic residue、metal cross-contamination、surface oxidation 有什么不同？
- 为什么 recipe 之外还需要 material policy、tool history 和 sample handling？
- 哪些问题必须服从本地 SOP，而不能靠网上抄参数？

出口：第一次进平台时知道应该记录什么、哪些事不能擅自做。

## Chapter 2 — 基底与表面

必须回答：

- substrate 怎样进入 GHz 与 mm-wave 两条电磁链？
- surface history 为什么可能影响损耗和 adhesion？
- 清洗步骤应怎样按“要去掉什么”来理解？

出口：能给 substrate/cleaning 写一张设计-工艺接口卡。

## Chapter 3 — 超导薄膜

必须回答：

- deposition 方法和最终 film properties 为什么不是同一件事？
- `t, Rsq, Tc, rho, roughness, stress, uniformity` 分别是什么意思？
- `Rsq/Tc/t` 怎样接回第一册的 `Lk_square`？
- 为什么 wafer map 对大阵列比单点数值更重要？

出口：能建立一个 film batch card，并知道哪些量必须由 witness sample 支撑。

## Chapter 4 — 光刻

必须回答：

- resist、exposure、develop 分别在改变什么？
- 什么是 CD、bias、process window？
- meander / IDC / coupler 哪些尺寸最值得测？
- 为什么设备最小分辨率不是 KID 设计规则？

出口：给一版 GDS 标出 fabrication-critical dimensions 和 inspection sites。

## Chapter 5 — Pattern transfer

必须回答：

- etch 与 lift-off 的核心区别是什么？
- over-etch、under-etch、undercut、fence、residue、sidewall 会怎样传播到器件？
- “图形看起来有了”为什么不等于工艺通过？

出口：能为一条具体 Al LEKID 工艺选择 pattern-transfer 路线，并列出 acceptance evidence。

## Chapter 6 — Dicing / Packaging / Wire bond

必须回答：

- 芯片离开 wafer 后还会引入哪些缺陷？
- package / bond / ground 怎样成为微波模型的一部分？
- 如何区分 chip fabrication 与 package parasitic？

出口：封装也有版本号、bond map 和照片证据。

## Chapter 7 — Metrology

必须回答：

- optical microscope、profilometer、4-probe、SEM、AFM、ellipsometry、stress、Tc 各关闭什么假设？
- 哪些测量适合主芯片，哪些应交给 witness sample？
- 如何做 wafer map？

出口：为一次 run 定义最小但足够的 metrology plan。

## Chapter 8 — Cryogenic feedback

必须回答：

- 第一次 cooldown 应先看什么，而不是急着做什么？
- `f0`, `Qi`, `Qc`, frequency scatter, collision, baseline 各能提示哪些方向？
- 为什么不能把一个症状机械对应到单一加工原因？

出口：得到一个 diagnosis tree，把异常分流到 design / material / fabrication / package / readout。

## Chapter 9 — Design for Fabrication

必须回答：

- nominal optimum 与 process window 有什么区别？
- fabrication scatter 怎样变成 array frequency collision 和 yield？
- test structures 怎样服务下一版设计？
- 哪些变量应该通过 Monte Carlo / tolerance budget 提前评估？

出口：下一版 GDS 不只是“电磁性能更好”，而是包含 process bias、tolerance、test coupon 和 acceptance gate。

## 全书最终验收问题

读者应能面对一批“频率整体偏低、Qi 分布变差、若干 resonance 消失”的芯片，不立刻猜一个原因，而是：

1. 先收集对应 Batch ID / GDS / deposition / lithography / etch / package 记录；
2. 对照 `t/Rsq/Tc/CD` 与 wafer map；
3. 看 resonance 的空间与频率分布；
4. 建立多个竞争假设；
5. 用下一项最有信息量的测量去排除假设；
6. 只在证据足够时改变下一批 process/design。

这就是第二册真正要教会的能力。
