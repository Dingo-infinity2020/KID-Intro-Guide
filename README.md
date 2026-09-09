# KID Intro Guide｜KID 入门讲义

一份面向 **Kinetic Inductance Detector（KID，动能电感探测器）/ LEKID** 初学者与器件设计者的中文开源讲义。

本项目不采用“先学完整套凝聚态物理，再开始做器件”的路线，而是从器件设计者真正需要理解的物理因果链出发：

**光场与吸收 → Cooper pair / 准粒子 → 动能电感与复电导 → GHz 谐振器 → S21 / I-Q 读出 → 光学响应 → 噪声与 NEP → LEKID 电磁设计 → 理论闭环复习 → 仿真/实验闭环。**

> 当前版本：**v0.9（2026-09-08）** · 121 页

## 最新版本

- [PDF 阅读版](docs/v0.9/KID入门讲义_v0.9.pdf)
- [LaTeX 权威排版源文件](docs/v0.9/KID入门讲义_v0.9.tex)
- [Markdown 内容源文件](docs/v0.9/KID入门讲义_v0.9.md)
- [v0.9 修改记录](docs/v0.9/CHANGELOG.md)
- [v0.9 Python 示例](docs/v0.9/examples/)
- [v0.9 项目验证模板](docs/v0.9/templates/)

## 当前已经打通的主链

`hν → pair breaking → Nqp → σ1,σ2 → Rs,Xs → Lk,Qi → f0,Qr,Qc → S21(f) → IQ → responsivity → PSD/ASD → NEP`

并进一步把同一几何拆成两条工程链：

`150 GHz: waveguide / polarization / Z_eff / backshort → absorption`

`GHz: meander Lg+Lk / IDC C / coupler Cc → f0, Qi, Qc, S21`

### v0.1–v0.8
依次建立光子到 S21、动能电感、超导基础、Mattis–Bardeen、微波谐振器/IQ、responsivity/NEP、LEKID 电磁设计，以及完整理论复习与手写训练。

### v0.9
- 将当前 150 GHz 双偏振 LEKID 拆成 geometry / GHz / optical / numerical / fabrication / cryogenic / calibration 多层 gate；
- 建立 `Claim–Observable–Method–Acceptance–Evidence` traceability；
- 增加 B0/B1 FOM、modal closure、convergence、material/tolerance、run manifest 与 evidence level；
- 增加 fabrication checklist、validation matrix 和三个项目验证 Python 示例。

## 总体学习路线

| 模块 | 核心主题 | 状态 |
|---|---|---|
| M1 | 从光子到 `S21` | 已完成 |
| M2 | 超导基础：Cooper pair、能隙、准粒子 | 已完成 |
| M3 | 动能电感与复电导 | 已完成 |
| M4 | 微波谐振器与 I-Q 圆 | 已完成 |
| M5 | 光学响应与 responsivity | 已完成基础模型 |
| M6 | 噪声与 NEP | 已完成基础 noise budget |
| M7 | LEKID 电磁设计 | 已完成 |
| M8 | 理论闭环复习、手写训练与自测 | v0.8 已完成 |
| M9 | 当前 150 GHz 项目验证矩阵 | **v0.9 已完成** |
| M10 | 阵列/FDM、实时读出与研究闭环 | 下一阶段 v1.0 |

## 仓库结构与版本规则

每个发布版本保留 PDF + LaTeX + Markdown；最新版 PDF 必须作为普通 GitHub 仓库文件存在。`LATEST_VERSION` 是唯一最新版指针，永久 GitHub Actions 使用同一指针独立重编译。

## 本地编译

```bash
make pdf
# 或
bash ./scripts/build_latest.sh
```

## License

代码、脚本与原创文本内容采用 [MIT License](LICENSE) 发布。外部论文、图像或资料版权归原作者/出版方所有。
