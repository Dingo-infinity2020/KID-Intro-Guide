# KID Intro Guide｜KID 入门讲义

一份面向 **Kinetic Inductance Detector（KID，动能电感探测器）/ LEKID** 初学者与器件设计者的中文开源讲义。

本项目不采用“先学完整套凝聚态物理，再开始做器件”的路线，而是从器件设计者真正需要理解的物理因果链出发：

**光场与吸收 → Cooper pair / 准粒子 → 动能电感与复电导 → GHz 谐振器 → S21 / I-Q 读出 → 噪声与 NEP → LEKID 电磁设计与实验。**

> 当前版本：**v0.2（2026-09-04）**

## 最新版本

- [PDF 阅读版](docs/v0.2/KID入门讲义_v0.2.pdf)
- [LaTeX 权威排版源文件](docs/v0.2/KID入门讲义_v0.2.tex)
- [Markdown 内容源文件](docs/v0.2/KID入门讲义_v0.2.md)
- [v0.2 修改记录](docs/v0.2/CHANGELOG.md)

## 讲义定位

这份讲义希望最终回答的不只是“什么是 KID”，而是：

- 一个毫米/亚毫米波光子进入超导薄膜后，如何最终变成可测的 `S21` / I-Q 变化？
- kinetic inductance（动能电感）为什么存在，又为什么会随光学负载变化？
- `Qi`、`Qc`、`Qr`、复电导、Mattis–Bardeen、responsivity、NEP 分别位于哪一层物理链？
- LEKID 的 meander、IDC、backshort、偏振结构分别承担什么作用？
- Sonnet / CST 等电磁仿真到底验证了哪一层物理，又遗漏了什么？
- 如何把材料、器件、电磁、读出和实验重新闭合成一套可验证的研究流程？

## 总体学习路线

| 模块 | 核心主题 |
|---|---|
| M1 | 从光子到 `S21` |
| M2 | 超导基础：Cooper pair、能隙、准粒子 |
| M3 | 动能电感与复电导 |
| M4 | 微波谐振器与 I-Q 圆 |
| M5 | 光学响应与 responsivity |
| M6 | 噪声与 NEP |
| M7 | LEKID 电磁设计 |
| M8 | 阵列与频分复用读出 |
| M9 | Sonnet / CST / 实验闭环 |
| M10 | 从学习走向可发表的研究问题 |

详细路线会随着版本迭代逐步补齐。

## 当前版本内容

### v0.1

建立第一条完整因果链：

`入射光子 → pair breaking → Nqp ↑ → ns ↓ → Lk ↑ → f0 ↓ → S21 / I-Q 改变`

### v0.2

在 v0.1 基础上：

- 重做并统一全部流程图语义；
- 从 `m dv/dt = qE` 推导动能电感 `Lk`；
- 使用能量法进行交叉验证；
- 引入 London penetration depth；
- 引入薄膜 sheet kinetic inductance；
- 引入 kinetic inductance fraction `α`；
- 建立 `δf0/f0` 与 `δLk/Lk` 的小信号关系；
- 初步讨论 PEC 模型与真实超导薄膜建模的区别。

## 仓库结构

```text
KID-Intro-Guide/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── ROADMAP.md
├── CHANGELOG.md
├── Makefile
├── .gitignore
├── docs/
│   ├── v0.1/
│   │   ├── KID入门讲义_v0.1.pdf
│   │   ├── KID入门讲义_v0.1.tex
│   │   └── KID入门讲义_v0.1.md
│   └── v0.2/
│       ├── KID入门讲义_v0.2.pdf
│       ├── KID入门讲义_v0.2.tex
│       ├── KID入门讲义_v0.2.md
│       └── CHANGELOG.md
└── scripts/
    └── build_latest.sh
```

## 本地编译

需要 XeLaTeX 与常见 TeX Live 宏包。

```bash
make pdf
```

或者：

```bash
./scripts/build_latest.sh
```

当前脚本默认编译 v0.2，两次运行 XeLaTeX 以刷新目录和交叉引用。

## 如何参与

欢迎提交：

- 公式或物理解释纠错；
- 更好的示意图和流程图；
- KID / LEKID 教学案例；
- Python 数值练习；
- 实验与仿真验证案例；
- 文献推荐与引用补充。

具体约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 版本原则

本项目优先保证：

1. **物理因果关系正确**；
2. **图示不误导**；
3. **中文表达尽量清晰，专业英文首次出现时给出中文解释**；
4. **公式不仅给结论，还说明它在器件中的意义**；
5. **逐步连接到真实 LEKID 设计、仿真和实验。**

## License

代码、脚本与原创文本内容采用 [MIT License](LICENSE) 发布。引用外部论文、图像或资料时，其版权仍归原作者或原出版方所有；后续版本会逐步完善正式参考文献与引用说明。
