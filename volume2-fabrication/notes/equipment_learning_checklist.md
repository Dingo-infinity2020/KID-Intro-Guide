# 微纳加工设备学习清单

目的不是提前背设备按钮，而是第一次培训时知道应该问什么、记录什么。实际操作以平台 SOP 和培训为准。

## 通用问题（所有设备都问）

- 设备允许哪些材料？有哪些交叉污染禁忌？
- sample / wafer 尺寸、厚度和夹持限制是什么？
- recipe 是固定模板还是允许用户改参数？谁有权限改？
- 哪些参数是设定值，哪些有实际 readback/log？
- 设备最近一次 calibration / maintenance 在哪里查？
- 一次 run 应保存哪些日志、截图、文件名？
- 什么异常必须立即停止并联系管理员？
- 有无 witness sample / dummy wafer 的常规做法？

## 1. 清洗与湿法台

关注：材料兼容性、容器/镊子分区、DI water、干燥方式、从清洗到下一步的允许时间窗口、废液分类与 PPE。

对 KID 的问题：这一步主要是在去颗粒、有机物、氧化物还是别的污染？会不会改变下一步超导膜的界面？

## 2. 薄膜沉积（蒸发 / sputter 等）

关注：base pressure、材料源/靶材、deposition rate、厚度监控方式、substrate rotation/heating、uniformity、sample position、历史材料、chamber conditioning。

对 KID 的问题：如何把 run log 与 `t, Rsq, Tc, stress, roughness` 对起来？平台是否支持 wafer map 或见证片？

## 3. Spin coater / hotplate

关注：允许的 resist、黏度、目标厚度范围、edge bead、烘烤温度校准、sample size 对旋涂均匀性的影响。

对 KID 的问题：resist thickness/profile 是否足以支持后续曝光、刻蚀或 lift-off？

## 4. Mask aligner / stepper / EBL

关注：分辨率、alignment、dose/exposure calibration、focus/contact mode、field stitching（如适用）、CD bias、可接受的 mask/GDS 格式。

对 KID 的问题：meander / IDC / coupler 哪些是 critical dimensions？平台历史上实际能稳定做到什么，而不是标称极限是什么？

## 5. Developer / post-exposure process

关注：显影终点、温度/时间控制、agitation 规则、rinse/dry、残胶检查方法。

对 KID 的问题：怎样验证 opening 真正打开？是否有稳定的 linewidth/gap bias 数据？

## 6. Dry etch / RIE / ICP

关注：允许材料、gas/reaction family、selectivity、endpoint、etch rate calibration、sidewall、overetch、chamber history、sample cooling。

对 KID 的问题：超导膜的实际 etch depth、CD loss、残留和 substrate damage 如何表征？

## 7. Wet etch（如使用）

关注：材料选择性、isotropy、温度与 bath 状态、undercut、废液规则。

对 KID 的问题：undercut/edge profile 会不会改变窄线和 gap？

## 8. Profilometer / ellipsometer / thickness monitor

关注：测量范围、step sample 准备、stylus force（如适用）、模型依赖（ellipsometry）、重复性与系统误差。

对 KID 的问题：怎样做 wafer-scale thickness map，而不是只测一个点？

## 9. Four-probe / transport / Tc measurement

关注：contact geometry、current range、temperature calibration、sample requirement、map capability。

对 KID 的问题：怎样形成 `Rsq + Tc + thickness` 的材料 batch card？

## 10. Optical microscope / SEM / AFM

关注：分辨率、charging/coating 要求、样品是否会被污染或损伤、CD measurement calibration。

对 KID 的问题：哪些位置预先定义为 inspection sites？避免只挑“最好看的地方”拍照。

## 11. Dicing / packaging / wire bonder

关注：保护膜、blade、chipping、cleaning、die attach、bond wire/material、bond pull test（如适用）、ground bond 规则。

对 KID 的问题：封装版本、bond map 和芯片方向如何进入 run manifest？
