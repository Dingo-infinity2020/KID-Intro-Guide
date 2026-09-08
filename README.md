# KID Intro Guide｜KID 入门讲义

一份面向 **Kinetic Inductance Detector（KID，动能电感探测器）/ LEKID** 初学者与器件设计者的中文开源讲义。

本项目不采用“先学完整套凝聚态物理，再开始做器件”的路线，而是从器件设计者真正需要理解的物理因果链出发：

**光场与吸收 → Cooper pair / 准粒子 → 动能电感与复电导 → GHz 谐振器 → S21 / I-Q 读出 → 光学响应 → 噪声与 NEP → LEKID 电磁设计 → 仿真/实验闭环。**

> 当前版本：**v0.7（2026-09-07）** · 81 页

## 最新版本

- [PDF 阅读版](docs/v0.7/KID入门讲义_v0.7.pdf)
- [LaTeX 权威排版源文件](docs/v0.7/KID入门讲义_v0.7.tex)
- [Markdown 内容源文件](docs/v0.7/KID入门讲义_v0.7.md)
- [v0.7 修改记录](docs/v0.7/CHANGELOG.md)
- [v0.7 Python 示例](docs/v0.7/examples/)

## 当前已经打通的主链

到 v0.7 为止，讲义已经从“一个光子”推进到真实 LEKID 几何的双频电磁设计：

`P_abs → Γ_qp → Nqp → σ1,σ2 → Rs,Xs → Lk,Qi → f0,Qr,Qc → S21(f) → IQ → responsivity → PSD/ASD → NEP`

并进一步把同一几何拆成两条工程链：

`150 GHz: waveguide / polarization / Z_eff / backshort → absorption`

`GHz: meander Lg+Lk / IDC C / coupler Cc → f0, Qi, Qc, S21`

### v0.1
建立第一条完整因果链：`入射光子 → pair breaking → Nqp ↑ → ns ↓ → Lk ↑ → f0 ↓ → S21 / I-Q 改变`。

### v0.2
动能电感推导、London penetration depth、sheet kinetic inductance、`α` 与频移。

### v0.3
Cooper pair、BCS 能隙、热/非平衡准粒子、generation-recombination、quasiparticle lifetime。

### v0.4
复电导 `σ1/σ2`、Mattis–Bardeen、surface impedance、`Lk`、`Qi` 与 GHz/150 GHz 材料模型边界。

### v0.5
`Qi/Qc/Qr`、linewidth、ring-down、ideal notch、IQ circle、fixed-tone readout 与 complex `S21` fitting。

### v0.6
absorbed power、responsivity、detector dynamics、PSD/ASD、input-referred NEP、photon/GR/TLS/amplifier noise。

### v0.7
- meander 作为 150 GHz absorber + GHz kinetic inductor；
- fill factor / effective sheet impedance / active volume 权衡；
- quarter-wave backshort 的 transmission-line 物理；
- 圆波导 TE11/TM01/TE21 cutoff 与 TE11 偏振简并；
- co-pol / cross-pol、hairpin end-turn、双偏振对称性；
- IDC/TLS、coupling capacitor 与 `Qc`；
- optical cross-pol 与 microwave resonator crosstalk 的区分；
- Sonnet vs CST/HFSS 分工、full-wave mode power closure；
- D=1.6 mm、149–151 GHz 的直接数值示例；
- waveguide / backshort 两个新的 Python 教学脚本。

## 总体学习路线

| 模块 | 核心主题 | 状态 |
|---|---|---|
| M1 | 从光子到 `S21` | 已完成 |
| M2 | 超导基础：Cooper pair、能隙、准粒子 | 已完成 |
| M3 | 动能电感与复电导 | 已完成 |
| M4 | 微波谐振器与 I-Q 圆 | 已完成 |
| M5 | 光学响应与 responsivity | 已完成基础模型 |
| M6 | 噪声与 NEP | 已完成基础 noise budget |
| M7 | LEKID 电磁设计 | **v0.7 已完成** |
| M8 | 当前 150 GHz 项目验证矩阵 | 下一阶段 v0.8 |
| M9 | 阵列/FDM 与实时读出 | 后续 |
| M10 | 从学习走向可发表研究问题 | 后续 |

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
    ├── ...
    ├── v0.6/
    └── v0.7/
        ├── KID入门讲义_v0.7.pdf
        ├── KID入门讲义_v0.7.tex
        ├── KID入门讲义_v0.7.md
        ├── README.md
        ├── CHANGELOG.md
        └── examples/
            ├── README.md
            ├── resonator_basics.py
            ├── resonator_fit_demo.py
            ├── optical_responsivity_demo.py
            ├── noise_budget_demo.py
            ├── waveguide_modes_demo.py
            └── backshort_toy_model.py
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

脚本读取根目录 `LATEST_VERSION`。GitHub Actions 使用同一版本指针，在 push / PR 时执行两次 XeLaTeX 编译并上传构建产物作为独立校验。

## 如何参与

欢迎提交公式/物理解释纠错、示意图、KID/LEKID 教学案例、Python 数值练习、实验/仿真验证案例和文献补充。具体约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

代码、脚本与原创文本内容采用 [MIT License](LICENSE) 发布。外部论文、图像或资料的版权仍归原作者或原出版方所有。
