from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
TEX_PATH = ROOT / "KID入门讲义_v0.10_step3.tex"
MD_PATH = ROOT / "KID入门讲义_v0.10_step3.md"
NOTES_PATH = ROOT / "STEP3_NOTES.md"
AUDIT_PATH = ROOT / "STEP3_AUDIT.md"

tex = TEX_PATH.read_text(encoding="utf-8")
md = MD_PATH.read_text(encoding="utf-8")


def insert_before_once(text: str, marker: str, addition: str, sentinel: str) -> str:
    if sentinel in text:
        return text
    if marker not in text:
        raise SystemExit(f"Missing insertion marker: {marker[:100]}")
    return text.replace(marker, addition + "\n\n" + marker, 1)

# Clean two small development-history artifacts discovered while checking the
# actual Markdown structure for this pass.
md = md.replace(
    "# Part II：超导材料与微波谐振器\n\n# Part II：超导材料与微波谐振器",
    "# Part II：超导材料与微波谐振器",
)
md = md.replace("这一版故意还没有完整推导：", "本章暂时不展开：")
md = md.replace(
    "下一版将正式打开中间这一步：Mattis–Bardeen 与 surface impedance。",
    "下一章将正式打开中间这一步：Mattis–Bardeen 与 surface impedance。",
)
tex = tex.replace("这一版故意还没有完整推导：", "本章暂时不展开：")
tex = tex.replace(
    "下一版将正式打开中间这一步：Mattis--Bardeen 与 surface impedance。",
    "下一章将正式打开中间这一步：Mattis--Bardeen 与 surface impedance。",
)

# ---------------------------------------------------------------------------
# Chapter 2: tell a true beginner what kind of reading task this chapter is.
# It is intentionally a causal map, not the place to master all later theory.
# ---------------------------------------------------------------------------
ch2_tex = textwrap.dedent(r"""
\begin{tcolorbox}[colback=KidGold!10,colframe=KidGold!75!black,boxrule=0.7pt,arc=2mm,title=第一次读这一章：先看地图，不要试图当场学完所有理论,fonttitle=\bfseries]
这一章会提前出现 $\Delta$、$N_{\rm qp}$、$L_k$、$Q_i$ 和 $S_{21}$。它们中的大多数都会在后面各用一整章重新解释。\textbf{第一次阅读时，先把这些符号当作路标，而不是考试内容。}

只要求先跟住四件事：\textbf{光把能量送进薄膜；材料状态改变；谐振器状态改变；微波读出把变化显示出来。} 如果某一步暂时只能接受“后面会解释”，完全正常。本章的任务是先知道整台机器怎样连起来，后文再逐个打开黑箱。
\end{tcolorbox}
""").strip()
tex = insert_before_once(
    tex,
    r"\section{先看全局：KID 是一台“两种频率协同工作”的机器}",
    ch2_tex,
    "第一次读这一章：先看地图，不要试图当场学完所有理论",
)

ch2_md = textwrap.dedent(r"""
> **第一次读这一章：先看地图，不要试图当场学完所有理论。** 这一章会提前出现 $\Delta$、$N_{\rm qp}$、$L_k$、$Q_i$ 和 $S_{21}$，它们中的大多数都会在后面各用一整章重新解释。第一次阅读时，先把这些符号当作路标，而不是考试内容。只要先跟住“光把能量送进薄膜 → 材料状态改变 → 谐振器状态改变 → 微波读出显示变化”这四步即可；某一步暂时只能接受“后面会解释”完全正常。
""").strip()
md = insert_before_once(
    md,
    "## 1. KID 是一台“两种频率协同工作”的机器",
    ch2_md,
    "第一次读这一章：先看地图",
)

# ---------------------------------------------------------------------------
# Chapter 3: bridge circuit-level V/I/L language to material-level E/J/n_s/v.
# ---------------------------------------------------------------------------
ch3_tex = textwrap.dedent(r"""
\begin{tcolorbox}[colback=KidBlue!4,colframe=KidBlue!60,boxrule=0.7pt,arc=2mm,title=先认清两套语言：这一章为什么突然出现 $E$、$J$、$n_s$ 和 $v$？,fonttitle=\bfseries]
前面一直在用\textbf{电路语言}：电压 $V$、电流 $I$、电感 $L$。这一章要回答“$L_k$ 从材料内部哪里来”，所以必须短暂切换到\textbf{材料语言}：电场 $E$、电流密度 $J$、有效超导载流子密度 $n_s$ 和平均速度 $v$。

两套语言并不矛盾。对一段近似均匀的条带，最重要的转换只有
\[
\boxed{V=El,\qquad I=JA.}
\]
其中 $l$ 是条带长度，$A=wt$ 是横截面积，而 $J$ 可以先直观理解成“\textbf{每单位横截面积流过多少电流}”。接下来的推导只是把微观的“载流子需要被加速”翻译成端口看到的 $V=L_k\,dI/dt$。

此处也\textbf{不要求已经理解 Cooper pair 的完整量子理论}。$m^*$、$q^*$、$n_s$ 先作为有效参数使用；第 4 章会再解释超导状态和准粒子到底是什么。
\end{tcolorbox}
""").strip()
tex = insert_before_once(
    tex,
    r"\section{先把“电感”拆成两种储能机制}",
    ch3_tex,
    "先认清两套语言：这一章为什么突然出现",
)

ch3_md = textwrap.dedent(r"""
> **先认清两套语言。** 前面一直在用电路语言：电压 $V$、电流 $I$、电感 $L$。这一章为了回答“$L_k$ 从材料内部哪里来”，会短暂切换到材料语言：电场 $E$、电流密度 $J$、有效超导载流子密度 $n_s$ 和平均速度 $v$。对均匀条带，两套语言最重要的转换只有 $V=El$ 和 $I=JA$；$J$ 可以先理解为“每单位横截面积流过多少电流”。此处不要求已经掌握 Cooper pair 的完整量子理论，$m^*$、$q^*$、$n_s$ 先作为有效参数使用，第 4 章再打开这个黑箱。
""").strip()
md = insert_before_once(
    md,
    "## 3.1 电感并不只有一种储能机制",
    ch3_md,
    "先认清两套语言",
)

# ---------------------------------------------------------------------------
# Chapter 4: prevent three classic conceptual misreadings before BCS notation.
# ---------------------------------------------------------------------------
ch4_tex = textwrap.dedent(r"""
\begin{tcolorbox}[colback=KidTeal!5,colframe=KidTeal!70!black,boxrule=0.7pt,arc=2mm,title=在看能带图之前，先把三个词翻成普通话,fonttitle=\bfseries]
\begin{itemize}
  \item \textbf{$E_F$（Fermi energy，费米能）：}这里主要把它当作描述“哪些电子态最容易参与低能变化”的参考能量。图上画一条 $E_F$，不表示材料内部真的有一堵能量墙。
  \item \textbf{$\Delta$（energy gap，能隙）：}它是\textbf{激发能量上的门槛}，不是材料内部裂开了一条空间缝隙。对最低能的单个 BCS 准粒子，其激发能量至少为 $\Delta$。
  \item \textbf{quasiparticle（准粒子）：}它是描述超导体系激发的一种有效语言，不应简单等同为“一颗恢复正常的普通电子”。KID 之所以关心它，是因为准粒子人口变化会改变薄膜的微波电磁响应。
\end{itemize}
先抓住这三句话，再看 $E=\sqrt{\xi^2+\Delta^2}$，公式就不再只是突然出现的一串符号。
\end{tcolorbox}
""").strip()
tex = insert_before_once(
    tex,
    r"\section{正常金属与超导态：区别不只是“电阻变成零”}",
    ch4_tex,
    "在看能带图之前，先把三个词翻成普通话",
)

ch4_md = textwrap.dedent(r"""
> **在看能带图之前，先把三个词翻成普通话。** $E_F$（Fermi energy，费米能）在这里主要作为描述低能电子态的参考能量，不是材料内部的一堵墙；$\Delta$（energy gap，能隙）是**激发能量上的门槛**，不是空间里的缝；quasiparticle（准粒子）是描述超导体系激发的有效语言，不能简单等同为“一颗恢复正常的普通电子”。先抓住这三点，再看 $E=\sqrt{\xi^2+\Delta^2}$。
""").strip()
md = insert_before_once(
    md,
    "## 4.2 正常金属与超导态：区别不只是“电阻变成零”",
    ch4_md,
    "在看能带图之前，先把三个词翻成普通话",
)

# ---------------------------------------------------------------------------
# Chapter 5: two-pass reading strategy plus resistor/inductor phase analogy.
# ---------------------------------------------------------------------------
ch5_tex = textwrap.dedent(r"""
\begin{tcolorbox}[colback=KidGold!9,colframe=KidGold!75!black,boxrule=0.7pt,arc=2mm,title=这一章建议读两遍：第一遍只抓住 $\sigma_1$ 和 $\sigma_2$,fonttitle=\bfseries]
Mattis--Bardeen 往往是 KID 初学者第一次明显“掉队”的地方，因为它把超导微观理论、复数交流响应和器件参数同时放在了一页上。\textbf{第一遍不需要会算 MB 积分。}

第一遍只建立下面的翻译关系：
\[
\boxed{
\sigma_1\;\longleftrightarrow\;\text{耗散更像电阻支路},
\qquad
\sigma_2\;\longleftrightarrow\;\text{储能更像感性支路}
}
\]
这里的“像”是帮助理解交流相位关系，并不是说超导薄膜真的由一个独立电阻和一个独立电感拼起来。理解 $\sigma_1$ 会进入损耗、$\sigma_2$ 会进入动能电感，就已经完成第一遍。

第二遍再回来追问：给定 $T$、$\omega$、$\Delta$ 和准粒子分布，Mattis--Bardeen 怎样定量给出 $\sigma_1$、$\sigma_2$，以及怎样进一步得到 $Z_s$、$Q_i$ 和 $f_0$。这样读，比第一次就死磕积分更稳。
\end{tcolorbox}
""").strip()
tex = insert_before_once(
    tex,
    r"\section{为什么需要“复电导”这层语言？}",
    ch5_tex,
    "这一章建议读两遍：第一遍只抓住",
)

ch5_md = textwrap.dedent(r"""
> **这一章建议读两遍。** Mattis–Bardeen 往往是 KID 初学者第一次明显“掉队”的地方。第一遍不需要会算 MB 积分，只要先建立 $\sigma_1\leftrightarrow$ 耗散（直觉上更像电阻支路）、$\sigma_2\leftrightarrow$ 储能/感性响应这组翻译，知道前者会进入损耗、后者会进入动能电感即可。第二遍再追问给定 $T$、$\omega$、$\Delta$ 和准粒子分布后，MB 怎样定量给出 $\sigma_1,\sigma_2$，再走到 $Z_s,Q_i,f_0$。这里的“像电阻/像电感”只是相位与能量交换的直觉，不表示薄膜真的由两个独立元件拼成。
""").strip()
md = insert_before_once(
    md,
    "## 1. 为什么需要复电导？",
    ch5_md,
    "这一章建议读两遍",
)

TEX_PATH.write_text(tex, encoding="utf-8")
MD_PATH.write_text(md, encoding="utf-8")

# Hard semantic gates: each bridge must exist exactly once in each reader-facing source.
checks = [
    "第一次读这一章：先看地图，不要试图当场学完所有理论",
    "先认清两套语言：这一章为什么突然出现",
    "在看能带图之前，先把三个词翻成普通话",
    "这一章建议读两遍：第一遍只抓住",
]
for phrase in checks:
    if tex.count(phrase) != 1:
        raise SystemExit(f"TeX bridge count failed for: {phrase}")

md_checks = [
    "第一次读这一章：先看地图",
    "先认清两套语言",
    "在看能带图之前，先把三个词翻成普通话",
    "这一章建议读两遍",
]
for phrase in md_checks:
    if md.count(phrase) != 1:
        raise SystemExit(f"Markdown bridge count failed for: {phrase}")

if md.count("# Part II：超导材料与微波谐振器") != 1:
    raise SystemExit("Duplicate Part II heading remains in Markdown")

notes = NOTES_PATH.read_text(encoding="utf-8")
if "## Step 3-C 补充" not in notes:
    notes += textwrap.dedent(r"""

## Step 3-C 补充：知识跳跃桥接

本小步不增加新的理论主线，而是针对完全新手最容易中断连续阅读的四个位置补桥：

- 第 2 章明确“先看因果地图、允许黑箱暂存”，避免读者把首次出现的所有符号都当成必须当场掌握；
- 第 3 章先解释电路语言 $(V,I,L)$ 与材料语言 $(E,J,n_s,v)$ 的关系，再进入动能电感推导；
- 第 4 章在能带/BCS 公式前先澄清 $E_F$、$\Delta$、quasiparticle 三个概念的直觉含义；
- 第 5 章采用“两遍阅读法”：第一遍只建立 $\sigma_1$=耗散、$\sigma_2$=感性响应的桥，第二遍再进入 Mattis--Bardeen 的定量层；
- 同时修复 Markdown 中重复的 Part II 标题，并清除“这一版/下一版”两处开发历史式措辞。

这些改动遵循“少改物理、多改解释”，不改变原有核心公式、公式约定或章节编号。
""")
    NOTES_PATH.write_text(notes, encoding="utf-8")

existing_audit = AUDIT_PATH.read_text(encoding="utf-8")
if "Step 3-C knowledge-jump gate" not in existing_audit:
    existing_audit += textwrap.dedent("""

## Step 3-C knowledge-jump gate

- Chapter 2 map-first bridge: PASS
- Chapter 3 circuit/material language bridge: PASS
- Chapter 4 EF/gap/quasiparticle bridge: PASS
- Chapter 5 two-pass MB reading bridge: PASS
- Duplicate Markdown Part II heading: REMOVED
- Development-history wording (`这一版` / `下一版` at the audited locations): CLEANED

No core physics equations were replaced by this transform; additions are explanatory bridge boxes only.
""")
    AUDIT_PATH.write_text(existing_audit, encoding="utf-8")

print("Step 3-C beginner bridge transform complete")
