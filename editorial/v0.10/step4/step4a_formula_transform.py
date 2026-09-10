from pathlib import Path
import shutil
import textwrap

ROOT = Path(__file__).resolve().parent
STEP3 = ROOT.parent / "step3"
TEX_PATH = ROOT / "KID入门讲义_v0.10_step4.tex"
MD_PATH = ROOT / "KID入门讲义_v0.10_step4.md"
NOTES_PATH = ROOT / "STEP4_NOTES.md"
AUDIT_PATH = ROOT / "STEP4_FORMULA_AUDIT.md"

# Start Step 4 from the frozen, zero-overfull Step 3 checkpoint.
if not TEX_PATH.exists():
    shutil.copy2(STEP3 / "KID入门讲义_v0.10_step3.tex", TEX_PATH)
if not MD_PATH.exists():
    shutil.copy2(STEP3 / "KID入门讲义_v0.10_step3.md", MD_PATH)

tex = TEX_PATH.read_text(encoding="utf-8")
md = MD_PATH.read_text(encoding="utf-8")

tex = tex.replace("KID入门讲义 v0.10 Step 3 Editorial Preview", "KID入门讲义 v0.10 Step 4 Formula Pedagogy Preview")
tex = tex.replace("KID 入门讲义 v0.10 Step 3 Editorial Preview", "KID 入门讲义 v0.10 Step 4 Formula Pedagogy Preview")
tex = tex.replace("Version 0.10 Step 3 Editorial Preview · 2026-09-10", "Version 0.10 Step 4 Formula Pedagogy Preview · 2026-09-10")
md = md.replace("# KID 入门讲义 v0.10 — Step 3 公开教材化审校预览", "# KID 入门讲义 v0.10 — Step 4 核心公式教学化预览")
md = md.replace("**版本：v0.10 Step 3 Editorial Preview · 2026-09-10**", "**版本：v0.10 Step 4 Formula Pedagogy Preview · 2026-09-10**")

# A deliberately simple four-layer explanation component.  Avoid tables here:
# beginner explanations should wrap naturally on narrow pages and mobile PDF views.
macro_marker = r"\newtcolorbox{formula}[1][]{colback=white,colframe=KidBlue!75,boxrule=0.9pt,arc=1mm,#1}"
macro_add = macro_marker + r'''
\newtcolorbox{formulaguidebox}{
  enhanced,breakable,
  colback=KidBlue!2,colframe=KidBlue!55,
  boxrule=0.65pt,arc=2mm,
  title=公式怎么读：不要只背等号,
  fonttitle=\bfseries,
  before skip=0.35em,after skip=0.8em
}
\newcommand{\formulaexplain}[4]{%
\begin{formulaguidebox}
\textbf{\color{KidBlue}数学上：}#1\par
\textbf{\color{KidTeal}物理上：}#2\par
\textbf{\color{KidGold!55!black}工程上：}#3\par
\textbf{\color{KidRed}适用条件：}#4
\end{formulaguidebox}%
}'''
if "\\newtcolorbox{formulaguidebox}" not in tex:
    if macro_marker not in tex:
        raise SystemExit("Formula macro insertion marker not found")
    tex = tex.replace(macro_marker, macro_add, 1)


def add_after(text: str, marker: str, addition: str, sentinel: str) -> str:
    if sentinel in text:
        return text
    if marker not in text:
        raise SystemExit("Missing formula marker: " + marker[:100])
    return text.replace(marker, marker + "\n" + addition, 1)


def md_guide(math_text: str, physics: str, engineering: str, conditions: str) -> str:
    return textwrap.dedent(f"""

> **公式怎么读：不要只背等号**  
> **数学上：** {math_text}  
> **物理上：** {physics}  
> **工程上：** {engineering}  
> **适用条件：** {conditions}
""").rstrip()

# ---------------------------------------------------------------------------
# 1) Photon energy E = h nu
# ---------------------------------------------------------------------------
marker = "\\[\nE_\\gamma=h\\nu.\n\\]"
addition = r'''\formulaexplain
{光子能量与频率成正比；频率增加一倍，单个光子的能量也增加一倍。}
{这里的 $\nu$ 是\textbf{被探测辐射的频率}，不是 GHz 谐振器的 $f_0$。更高频的单个光子携带更多可用于激发材料的能量。}
{把 $h\nu$ 与 $2\Delta$ 比较，可以快速判断“这个材料 + 这个观测频带”是否具备直接破对的能量条件。材料选择和光学频带因此不能彼此独立。}
{$E=h\nu$ 本身是普适的光子关系；但“有足够能量”不等于“能量一定被薄膜高效吸收”，更不等于吸收后全部能量都转化为可读出的准粒子。}'''
tex = add_after(tex, marker, addition, "光子能量与频率成正比；频率增加一倍")

md_marker = "$$\nE_\\gamma=h\\nu.\n$$"
md = add_after(md, md_marker, md_guide(
    "光子能量与频率成正比；频率增加一倍，单个光子的能量也增加一倍。",
    "这里的 $\\nu$ 是**被探测辐射的频率**，不是 GHz 谐振器的 $f_0$；更高频的单个光子携带更多可用于激发材料的能量。",
    "把 $h\\nu$ 与 $2\\Delta$ 比较，可以快速判断“材料 + 观测频带”是否具备直接破对的能量条件。",
    "$E=h\\nu$ 本身普适；但能量足够不代表薄膜一定高效吸收，也不代表吸收能量全部变成可读出的准粒子。",
), "光子能量与频率成正比；频率增加一倍")

# ---------------------------------------------------------------------------
# 2) Pair-breaking threshold h nu >= 2 Delta
# ---------------------------------------------------------------------------
marker = "\\[\n\\boxed{h\\nu\\ge 2\\Delta.}\n\\]"
addition = r'''\formulaexplain
{这是一个能量不等式：一个入射光子的能量 $h\nu$ 至少要达到 $2\Delta$。等号给出最基本的破对频率下限 $\nu_{\rm pb}=2\Delta/h$。}
{破坏一个 Cooper pair 后需要产生两个准粒子激发；每个最低激发能量至少约为 $\Delta$，所以最小总能量是 $2\Delta$，而不是 $\Delta$。}
{它是选择超导材料和 science band 的第一道快速门槛。例如降低 $T_c$ 通常会降低 $\Delta$，也随之降低可直接破对的频率阈值。}
{这是\textbf{必要的能量条件，不是高探测效率的充分条件}。实际吸收还取决于光学耦合、表面阻抗、偏振、几何以及 pair-breaking efficiency；用 $\Delta(0)\simeq1.764k_BT_c$ 时还隐含弱耦合 BCS 近似。}'''
tex = add_after(tex, marker, addition, "这是一个能量不等式：一个入射光子的能量")

md_marker = "$$\n\\boxed{h\\nu\\ge2\\Delta.}\n$$"
md = add_after(md, md_marker, md_guide(
    "这是能量不等式；等号给出最基本的破对频率下限 $\\nu_{\\rm pb}=2\\Delta/h$。",
    "破坏一个 Cooper pair 后需要产生两个准粒子激发，每个最低激发能量约为 $\\Delta$，所以门槛是 $2\\Delta$。",
    "这是选择超导材料和 science band 的第一道快速门槛；改变 $T_c$ 会改变 $\\Delta$ 和最低可直接破对频率。",
    "这是**必要条件，不是高效率的充分条件**。实际吸收还取决于耦合、表面阻抗、偏振、几何与 pair-breaking efficiency；$\\Delta(0)\\simeq1.764k_BT_c$ 还假设弱耦合 BCS。",
), "这是能量不等式；等号给出最基本的破对频率")

# Generalize one lingering case-study sentence found during formula review.
tex = tex.replace("你的目标频率约为 \\SI{150}{GHz}，明显高于这个阈值。", "工程案例的目标频率约为 \\SI{150}{GHz}，明显高于这个阈值。")

# ---------------------------------------------------------------------------
# 3) Kinetic-inductance fraction alpha
# ---------------------------------------------------------------------------
marker = "\\[\n\\boxed{\\alpha\\equiv\\frac{L_k}{L_g+L_k}.}\n\\]"
addition = r'''\formulaexplain
{$\alpha$ 是一个无量纲比例，范围通常在 0 到 1 之间；它衡量总电感 $L_g+L_k$ 中有多少来自动能电感。}
{$L_g$ 主要是几何磁场储能，$L_k$ 来自超导载流子的动能。只有后者会强烈跟随超导材料状态变化，所以 $\alpha$ 可以理解为“敏感电感占比”。}
{同样大小的 $\delta L_k/L_k$ 下，较大的 $\alpha$ 通常带来更明显的相对频移，因此它是连接材料设计与读出 responsivity 的关键参数。}
{$\alpha$ 大并不自动意味着探测器更好；提高 $L_k$ 可能同时改变 $Q_i$、非线性、临界电流、阻抗匹配与噪声。这里还默认总电感可以有意义地分成 $L_g+L_k$。}'''
tex = add_after(tex, marker, addition, "$\\alpha$ 是一个无量纲比例，范围通常在 0 到 1 之间")

md_marker = "$$\n\\boxed{\\alpha=\\frac{L_k}{L_g+L_k}.}\n$$"
md = add_after(md, md_marker, md_guide(
    "$\\alpha$ 是无量纲比例，通常位于 0–1，表示总电感里有多少来自 $L_k$。",
    "$L_g$ 主要对应几何磁场储能，$L_k$ 对应超导载流子动能；后者更直接跟随超导状态变化，所以 $\\alpha$ 可看成“敏感电感占比”。",
    "同样的 $\\delta L_k/L_k$ 下，较大 $\\alpha$ 通常产生更明显的相对频移，是材料设计连接到 responsivity 的关键参数。",
    "$\\alpha$ 不是越大越好；增大 $L_k$ 也会牵动 $Q_i$、非线性、临界电流、阻抗匹配和噪声。",
), "$\\alpha$ 是无量纲比例，通常位于 0–1")

# ---------------------------------------------------------------------------
# 4) Lumped LC resonance frequency
# ---------------------------------------------------------------------------
marker = "\\[\n\\boxed{f_0=\\frac{1}{2\\pi\\sqrt{LC}}.}\n\\]"
addition = r'''\formulaexplain
{$f_0$ 与 $L$、$C$ 的平方根成反比；因此小幅改变电感或电容，只会以约一半的相对比例改变谐振频率。}
{LC 谐振来自电场储能与电感储能之间周期性交换。电感或电容越大，一次能量交换越“慢”，谐振频率就越低。}
{在 LEKID 中，IDC 主要提供 $C$，meander 同时贡献 $L_g$ 与 $L_k$。所以 GHz resonance 位置不是单一几何尺寸决定的，而是电容、几何电感和材料动能电感共同决定。}
{这是集总或准集总谐振器的最低阶模型。器件尺寸接近导波波长、寄生耦合很强、驱动进入明显非线性，或需要精确电磁分布时，应转向更完整的分布参数/全波模型。}'''
tex = add_after(tex, marker, addition, "$f_0$ 与 $L$、$C$ 的平方根成反比")

md_marker = "$$\n\\boxed{f_0=\\frac1{2\\pi\\sqrt{LC}}.}\n$$"
md = add_after(md, md_marker, md_guide(
    "$f_0$ 与 $L,C$ 的平方根成反比，小幅改变其中一个量只以约一半的相对比例进入频移。",
    "LC 谐振是电场储能与电感储能周期性交换；$L$ 或 $C$ 越大，交换越慢，$f_0$ 越低。",
    "LEKID 中 IDC 主要提供 $C$，meander 同时贡献 $L_g$ 与 $L_k$；GHz resonance 是几何与材料共同决定的。",
    "这是集总/准集总最低阶模型；明显分布参数效应、寄生耦合或强非线性时需要更完整模型。",
), "$f_0$ 与 $L,C$ 的平方根成反比")

# ---------------------------------------------------------------------------
# 5) Small-signal frequency response
# ---------------------------------------------------------------------------
marker = """\\begin{formula}\n\\[\n\\boxed{\n\\frac{\\delta f_0}{f_0}\n=-\\frac{\\alpha}{2}\\frac{\\delta L_k}{L_k}.\n}\n\\]\n\\end{formula}"""
addition = r'''\formulaexplain
{这是对 $f_0\propto L^{-1/2}$ 的一阶微分结果，并用 $\alpha=L_k/L$ 把“总电感变化”改写成“动能电感自身的相对变化”。负号表示 $L_k$ 增大时 $f_0$ 降低。}
{光并不是直接把 GHz 频率“推低”；它先改变超导状态，再改变 $L_k$。谐振器只负责把这个很小的材料变化转成容易精密测量的频率变化。}
{这个式子直接告诉设计者两个增益旋钮：材料扰动能产生多大的 $\delta L_k/L_k$，以及器件有多大的 $\alpha$。它也是从材料模型走向频率 responsivity 的最短桥梁。}
{只适用于\textbf{小扰动一阶近似}，并假定这一小步中 $C$ 与 $L_g$ 基本不变、主要变化来自 $L_k$。强光载、强读出非线性、温度大幅变化或几何/介电常数同时变化时不能机械套用。}'''
tex = add_after(tex, marker, addition, "这是对 $f_0\\propto L^{-1/2}$ 的一阶微分结果")

md_marker = """$$\n\\boxed{\n\\frac{\\delta f_0}{f_0}\n=-\\frac{\\alpha}{2}\\frac{\\delta L_k}{L_k}.\n}\n$$"""
md = add_after(md, md_marker, md_guide(
    "这是 $f_0\\propto L^{-1/2}$ 的一阶微分，并用 $\\alpha=L_k/L$ 改写；负号表示 $L_k$ 增大时 $f_0$ 降低。",
    "光先改变超导状态和 $L_k$，谐振器再把微小材料变化转成易于精密测量的频率变化，并不是光直接把 GHz 频率‘推低’。",
    "它把 responsivity 拆成两个关键因素：材料能产生多大的 $\\delta L_k/L_k$，以及器件有多大的 $\\alpha$。",
    "只适用于**小扰动一阶近似**，并假设 $C$ 与 $L_g$ 基本不变、主要变化来自 $L_k$；强非线性或多参数同时漂移时不能机械套用。",
), "这是 $f_0\\propto L^{-1/2}$ 的一阶微分")

# ---------------------------------------------------------------------------
# 6) Kinetic-inductance strip formula
# ---------------------------------------------------------------------------
marker = """\\begin{formula}\n\\[\n\\boxed{\nL_k=\\frac{m^*l}{n_s(q^*)^2A}\n=\\frac{m^*l}{n_s(q^*)^2wt}\n}\n\\]\n\\end{formula}"""
addition = r'''\formulaexplain
{在这个均匀条带模型中，$L_k\propto l$，并与 $n_s$、$w$、$t$ 成反比；电荷以 $(q^*)^2$ 进入。}
{同样的总电流若被迫通过更少的超流载流子或更小的横截面，每个有效载流子需要更大的运动速度，因此储存更多集体动能；端口就看到更大的动能电感。}
{它提供非常有用的第一轮设计趋势：加长、变窄、变薄或降低有效 $n_s$ 都会提高 $L_k$。这能指导 meander 参数扫描，也解释为什么薄膜工艺偏差会推移 GHz resonance。}
{推导假设条带均匀、局域响应、忽略散射且电流密度近似均匀。真实薄膜还可能处于 dirty limit，弯角会有 current crowding，有限厚度与频率效应也会改变结果；精确设计应使用 $L_{k,\square}$、复电导/表面阻抗或全波模型。}'''
tex = add_after(tex, marker, addition, "在这个均匀条带模型中，$L_k\\propto l$")

md_marker = "$$\n\\boxed{L_k=\\frac{m^*l}{n_s(q^*)^2wt}}.\n$$"
md = add_after(md, md_marker, md_guide(
    "均匀条带模型中 $L_k\\propto l$，并与 $n_s,w,t$ 成反比，电荷以 $(q^*)^2$ 进入。",
    "同样电流通过更少载流子或更小横截面时，每个有效载流子需要更大速度，储存更多集体动能，因此端口看到更大的 $L_k$。",
    "加长、变窄、变薄或降低有效 $n_s$ 都会提高 $L_k$；这给 meander 参数扫描和工艺偏差分析提供第一轮趋势判断。",
    "假设均匀、局域、忽略散射且电流密度近似均匀；真实 dirty-limit 薄膜、弯角 current crowding、有限厚度/频率效应需要更完整模型。",
), "均匀条带模型中 $L_k\\propto l$")

# ---------------------------------------------------------------------------
# 7) Sheet kinetic inductance
# ---------------------------------------------------------------------------
marker = """\\begin{formula}\n\\[\n\\boxed{\nL_{k,\\Box}\\equiv\\mu_0\\frac{\\lambda_L^2}{t}\n}\n\\qquad (t\\ll\\lambda_L\\text{ 的简单 London 极限})\n\\]\n\\end{formula}"""
addition = r'''\formulaexplain
{$L_{k,\square}$ 把“材料 + 膜厚”的动能电感能力压缩成每一个几何方块的电感；总条带近似为 $L_k\approx L_{k,\square}(l/w)$。}
{对均匀薄膜而言，一个长宽相等的方块无论整体尺寸多大，$l/w=1$。因此“每方块”不是一块固定面积，而是一种特别适合二维薄膜版图的几何计数语言。}
{版图只需统计有效 squares，就能把 wafer 的材料参数快速映射到 meander 的 $L_k$，非常适合早期手算、参数化几何和加工后模型更新。}
{这里写出的 $\mu_0\lambda_L^2/t$ 是 $t\ll\lambda_L$ 的简单局域 London 极限。实际 KID 常需考虑 dirty limit、有限温度与有限频率；工程上更可靠的 $L_{k,\square}$ 往往来自 $R_{\square,n}$ + $T_c$ 估算或低温谐振测量反演。}'''
tex = add_after(tex, marker, addition, "$L_{k,\\square}$ 把“材料 + 膜厚”的动能电感能力")

md_marker = """$$\n\\boxed{L_{k,\\Box}\\equiv\\mu_0\\frac{\\lambda_L^2}{t}}\n\\qquad (t\\ll\\lambda_L\\text{ 的简单 London 极限})\n$$"""
md = add_after(md, md_marker, md_guide(
    "$L_{k,\\Box}$ 把“材料 + 膜厚”的动能电感能力压缩成每个几何方块的电感，总条带近似 $L_k\\approx L_{k,\\Box}(l/w)$。",
    "‘每方块’不是固定面积；长宽相等时 $l/w=1$，因此它是特别适合二维薄膜版图的几何计数语言。",
    "统计有效 squares 就能把 wafer 材料参数快速映射到 meander 的 $L_k$，适合手算、参数化版图和加工后模型更新。",
    "这里的 $\\mu_0\\lambda_L^2/t$ 是 $t\\ll\\lambda_L$ 的简单局域 London 极限；真实 KID 常需 dirty-limit、温度/频率修正，或从低温测量反演。",
), "$L_{k,\\Box}$ 把“材料 + 膜厚”的动能电感能力")

TEX_PATH.write_text(tex, encoding="utf-8")
MD_PATH.write_text(md, encoding="utf-8")

# Semantic gates.  Exactly seven formula guides are intentionally introduced in A.
if tex.count(r"\formulaexplain") != 8:  # 1 macro definition + 7 invocations
    raise SystemExit("Unexpected TeX formulaexplain count: " + str(tex.count(r"\formulaexplain")))
if md.count("**公式怎么读：不要只背等号**") != 7:
    raise SystemExit(f"Unexpected Markdown formula-guide count: {md.count('**公式怎么读：不要只背等号**')}")

core_equations = [
    r"E_\gamma=h\nu",
    r"h\nu\ge 2\Delta",
    r"\alpha\equiv\frac{L_k}{L_g+L_k}",
    r"f_0=\frac{1}{2\pi\sqrt{LC}}",
    r"-\frac{\alpha}{2}\frac{\delta L_k}{L_k}",
    r"L_k=\frac{m^*l}{n_s(q^*)^2A}",
    r"L_{k,\Box}\equiv\mu_0\frac{\lambda_L^2}{t}",
]
missing = [eq for eq in core_equations if eq not in tex]
if missing:
    raise SystemExit("Core equation unexpectedly missing: " + "; ".join(missing))

NOTES_PATH.write_text(textwrap.dedent(r"""
# v0.10 Step 4 — 核心公式教学化

## Step 4-A：第 2–3 章基础公式

本阶段不重推整本书，而是为真正承担“概念接口”的公式建立统一阅读模板：

1. **数学上**：公式的变量关系和符号结构是什么；
2. **物理上**：它背后的能量、载流子或谐振过程是什么；
3. **工程上**：设计、仿真、测量时拿它解决什么问题；
4. **适用条件**：近似在哪里成立，什么情况下不能机械套用。

Step 4-A 已覆盖 7 个基础公式/关系：$E=h\nu$、$h\nu\ge2\Delta$、$\alpha$、LC resonance、small-signal frequency shift、均匀条带 $L_k$、sheet kinetic inductance。

特别强调：公式解释层不替代原有推导，而是放在公式与后续工程叙述之间，帮助第一次接触 KID 的读者知道“为什么值得记、什么时候该怀疑”。

下一步 Step 4-B 继续覆盖超导热准粒子、复电导/表面阻抗、$Q_i/Q_c/Q_r$、notch $S_{21}$ 和 ring-down；Step 4-C 再处理 responsivity、NEP、photon/GR/TLS noise 与 optical coupling。
""").lstrip(), encoding="utf-8")

AUDIT_PATH.write_text(textwrap.dedent("""
# v0.10 Step 4-A — Formula pedagogy audit

- Four-layer formula explanation component: ADDED
- TeX formula-guide invocations: 7
- Markdown formula-guide blocks: 7
- Core equations preserved: PASS
- Chapters covered: 2–3
- Physics scope changed: NO (explanation layer only)
- One lingering private-case phrase `你的目标频率`: generalized

Compilation/layout status is filled by the Step 4-A workflow.
""").lstrip(), encoding="utf-8")

print("Step 4-A foundational formula pedagogy transform complete")
