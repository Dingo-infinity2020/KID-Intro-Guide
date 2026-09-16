# SECUF F1 微纳加工实验室与 KID 第二册的对应关系

> 目的：把目标学习平台的公开设备能力映射到第二册章节和实际学习问题。这里记录的是平台公开信息，不等于已确认可用于某一种 KID 工艺；具体材料兼容性、recipe、预约和培训要求必须向设备管理员确认。

资料入口：

- SECUF F1 微纳加工实验室：<https://secuf.iphy.ac.cn/system/tsp/micro-nano-fabrication-laboratory>
- SECUF 技术支撑平台：<https://secuf.iphy.ac.cn/system/tsp>
- SECUF 用户指南/开放申请信息：<https://secuf.iphy.ac.cn/>

公开页面显示，F1 微纳加工实验室包含百级和千级洁净区；百级黄光区主要覆盖曝光、显影和涂胶，千级区覆盖光刻、沉积、刻蚀、微纳结构表征和物性测试。平台公开列出 43 台套设备，包括 4 台曝光、9 台沉积、9 台刻蚀、10 台表征和 11 台辅助设备。

## 1. 光刻单元 → 第 4 章

公开设备包括：

- 高压电子束曝光机
- 电子束扫描/直写系统
- 激光直写系统
- 接触式光刻机

公开指标包括电子束曝光最小线宽 8 nm、紫外曝光最小线宽 0.5 μm、激光直写分辨率 600 nm。

### 对 KID 真正要问

1. 对我们计划的 Al LEKID，真正需要的是 EBL 还是 UV/激光直写已经足够？
2. meander linewidth、gap、IDC、coupler 的实际稳定 CD 是多少，而不是设备宣传的最小分辨率是多少？
3. 是否有长期 CD bias / dose calibration 数据？
4. 对整片阵列，uniformity、alignment、field/stitching（若使用 EBL）哪个更可能限制 yield？

第二册不把“8 nm”理解为 KID 必须追求的尺寸。对毫米波 LEKID，工艺窗口和可重复性通常比极限分辨率更重要。

## 2. 沉积单元 → 第 3 章

公开设备包括：

- PECVD
- 多腔室超高真空磁控溅射系统
- 多腔室超高真空电子束蒸发系统
- 热蒸发镀膜机
- ALD
- 离子束溅射沉积系统
- 富氧电子束沉积系统
- 离子溅射仪
- 晶圆光刻预处理系统

### 对 KID 真正要问

1. 哪些设备允许 Al，以及是否存在超导器件/低损耗器件的专用或低污染 chamber？
2. Al 的 base pressure、rate、thickness monitor、rotation 和 wafer-size uniformity 能否记录？
3. 是否可以配 witness sample，后续做 thickness / Rsq / Tc？
4. 设备历史材料是否可能带来交叉污染？
5. 对单层 Al LEKID，蒸发和溅射各自的实际工艺成熟度怎样？

这里是第二册最优先需要和管理员核实的一组问题。

## 3. 刻蚀单元 → 第 5 章

公开设备包括：

- FIB
- 反应离子束刻蚀
- ICP（2 台）
- RIE（2 台）
- Ar 离子束刻蚀
- 微波等离子体刻蚀
- 湿法刻蚀系统（2 台）

公开页面还给出硅材料刻蚀能力，但这些硅深刻蚀指标不应直接等同于 Al LEKID 的金属图形转移能力。

### 对 KID 真正要问

1. 若采用“整片 Al → 光刻 → 刻蚀”路线，平台推荐哪台设备和哪类工艺？
2. Al etch 对 Si substrate 的 selectivity 与 over-etch 风险如何？
3. 有无可用于估计 etch rate / CD loss / sidewall 的历史数据？
4. 若采用 lift-off 路线，哪一套沉积+resist profile 更成熟？
5. 如何检查 residue、fence、undercut、over-etch 进入器件的方式？

## 4. 表征单元 → 第 7 章

公开设备包括：

- AFM
- 台阶仪
- 金相显微镜
- 数字显微镜
- 体视显微镜
- 薄膜应力仪
- 激光共聚焦显微镜
- 椭偏仪
- 白光干涉仪

这些设备足以覆盖第二册很大一部分“进低温前的证据链”：膜厚/台阶、表面粗糙度、CD/大尺度缺陷、应力、三维形貌等。

### 尚需确认的缺口

公开 F1 页面没有把 four-probe、Tc measurement、SEM 明确列在 F1 表征单元中；SECUF 的样品预选和表征站公开列有 SEM 和超低温测量能力。因此后续调研要明确：

- Rsq 在哪个平台测？
- Tc 用哪套系统最方便？
- SEM 是 F1 内部可用、还是需要转 F2？
- witness sample 在不同站点之间如何流转？

## 5. 辅助单元 → 第 6 章

公开设备包括：

- 引线键合
- 激光划片机
- 砂轮切片机
- 快速退火炉
- 程控旋涂匀胶机
- 程控干胶仪
- 干燥样品柜
- 真空烘箱

这意味着从 resist coating 到 dicing / wirebond 的多个步骤在同一技术支撑平台内具备公开设备基础，但对 KID 来说仍需确认材料、die 尺寸、bond wire、sample holder 和 ground-bond 习惯。

## 6. 第一次现场学习的推荐路线

不要按“设备价格/先进程度”参观，而按一块单层 Al LEKID 的真实出生顺序：

1. substrate 与清洗/预处理；
2. Al deposition；
3. resist coat / bake；
4. lithography；
5. develop；
6. Al pattern transfer（etch 或 lift-off）；
7. strip / clean；
8. microscope + thickness/CD/metrology；
9. dicing；
10. package + wirebond；
11. Rsq / Tc / low-temperature S21 的后续接口。

每到一台设备，优先记录“输入是什么、输出是什么、有哪些不可逆风险、保存哪些日志、怎样做 witness sample”，而不是先抄 recipe 数值。

## 7. 当前判断

从公开设备类别看，SECUF F1 覆盖了 LEKID 原型加工所需要的大部分通用微纳环节；真正决定是否能顺利复制单层 Al LEKID 的，不是设备数量，而是 **Al 材料兼容性、已有成熟 recipe、低损耗器件污染控制、Rsq/Tc 表征接口，以及平台愿意开放到什么程度**。这五项应成为下一轮联系实验室时的核心问题。

资料核对日期：2026-09-16。
