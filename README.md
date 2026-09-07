# KID Intro Guide｜KID 入门讲义

一份面向 **Kinetic Inductance Detector（KID，动能电感探测器）/ LEKID** 初学者与器件设计者的中文开源讲义。

本项目不采用“先学完整套凝聚态物理，再开始做器件”的路线，而是从器件设计者真正需要理解的物理因果链出发：

**光场与吸收 → Cooper pair / 准粒子 → 动能电感与复电导 → GHz 谐振器 → S21 / I-Q 读出 → 噪声与 NEP → LEKID 电磁设计与实验。**

> 当前版本：**v0.5（2026-09-07）** · 57 页

## 最新版本

- [PDF 阅读版](docs/v0.5/KID入门讲义_v0.5.pdf)
- [LaTeX 权威排版源文件](docs/v0.5/KID入门讲义_v0.5.tex)
- [Markdown 内容源文件](docs/v0.5/KID入门讲义_v0.5.md)
- [v0.5 修改记录](docs/v0.5/CHANGELOG.md)

## 当前已经打通的主链

到 v0.5 为止，讲义已经从“一个光子”推进到可拟合的微波谐振器与 IQ 读出：

`光子 / 光功率 → Cooper pair breaking → Nqp → σ1, σ2 → Rs, Xs → Lk, Qi → f0, Qr, Qc → S21(f) → IQ circle → fixed-tone I/Q`

### v0.1

建立第一条完整因果链：

`入射光子 → pair breaking → Nqp ↑ → ns ↓ → Lk ↑ → f0 ↓ → S21 / I-Q 改变`

### v0.2

- 重做并统一流程图语义；
- 从 `m dv/dt = qE` 推导 kinetic inductance；
- 引入 London penetration depth、sheet kinetic inductance 与 `α`；
- 建立 `δf0/f0` 与 `δLk/Lk` 的关系。

### v0.3

- Cooper pair 与 BCS 能隙；
- pair-breaking threshold；
- thermal / non-equilibrium quasiparticles；
- generation-recombination；
- quasiparticle lifetime；
- `Tc` 与 150 GHz 材料选择的直接关系。

### v0.4

- `σ = σ1 - iσ2`；
- Mattis–Bardeen 的器件化理解；
- `σ → Zs = Rs + iXs`；
- 薄膜 `Z□ ≈ 1/(tσ)`；
- `Lk,□ ≈ 1/(ωtσ2)`；
- `δf0/f0 ≈ (α/2)δσ2/σ2`；
- `1/Qi,qp ≈ ασ1/σ2` 的直观薄膜近似；
- GHz readout 与 150 GHz optical absorber 的跨频段建模边界。

### v0.5

- `Qi/Qc/Qr` 与损耗/耦合率；
- linewidth 与 ring-down；
- ideal notch `S21` 与 IQ circle；
- fixed-tone readout；
- cable delay / complex gain / asymmetry / fitting；
- Python 数值示例。

## 总体学习路线

| 模块 | 核心主题 | 状态 |
|---|---|---|
| M1 | 从光子到 `S21` | 已完成 |
| M2 | 超导基础：Cooper pair、能隙、准粒子 | 已完成 |
| M3 | 动能电感与复电导 | 已完成至 MB / surface impedance |
| M4 | 微波谐振器与 I-Q 圆 | v0.5 |
| M5 | 光学响应与 responsivity | 后续 |
| M6 | 噪声与 NEP | 后续 |
| M7 | LEKID 电磁设计 | 后续 |
| M8 | 阵列与频分复用读出 | 后续 |
| M9 | Sonnet / CST / 实验闭环 | 后续 |
| M10 | 从学习走向可发表的研究问题 | 后续 |

## 仓库结构与版本规则

```text
KID-Intro-Guide/
├── README.md
├── LATEST_VERSION
├── LICENSE
├── CONTRIBUTING.md
├── ROADMAP.md
├── CHANGELOG.md
├── Makefile
├── .github/workflows/build-guide.yml
├── scripts/build_latest.sh
└── docs/
    ├── v0.1/
    ├── v0.2/
    ├── v0.3/
    ├── v0.4/
    └── v0.5/
        ├── KID入门讲义_v0.5.pdf
        ├── KID入门讲义_v0.5.tex
        ├── KID入门讲义_v0.5.md
        ├── README.md
        ├── CHANGELOG.md
        └── examples/
            ├── resonator_basics.py
            └── resonator_fit_demo.py
```

**发布规则：每个版本必须同时保留 PDF + LaTeX + Markdown；最新 PDF 必须作为普通 GitHub 仓库文件存在。**

## 本地编译

需要 XeLaTeX 与常见 TeX Live 宏包：

```bash
make pdf
```

或者：

```bash
bash ./scripts/build_latest.sh
```

脚本读取根目录 `LATEST_VERSION`，无需手工修改版本路径。

GitHub Actions 也使用同一版本指针，在 push / PR 时实际执行两次 XeLaTeX 编译并上传构建产物用于校验。

## 如何参与

欢迎提交公式或物理解释纠错、更好的示意图、KID / LEKID 教学案例、Python 数值练习、实验/仿真验证案例和文献补充。具体约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

代码、脚本与原创文本内容采用 [MIT License](LICENSE) 发布。外部论文、图像或资料的版权仍归原作者或原出版方所有。
