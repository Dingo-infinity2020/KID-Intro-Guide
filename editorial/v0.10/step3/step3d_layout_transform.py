from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
TEX_PATH = ROOT / "KID入门讲义_v0.10_step3.tex"
MD_PATH = ROOT / "KID入门讲义_v0.10_step3.md"
NOTES_PATH = ROOT / "STEP3_NOTES.md"
AUDIT_PATH = ROOT / "STEP3_AUDIT.md"

tex = TEX_PATH.read_text(encoding="utf-8")
md = MD_PATH.read_text(encoding="utf-8")

# ---------------------------------------------------------------------------
# 1) Tables: a full-width tabularx started as an ordinary paragraph receives
# paragraph indentation, producing an ~20 pt overfull box.  Make full-width
# tables explicitly unindented.  This is safe and also prevents the same bug
# from reappearing in later sections.
# ---------------------------------------------------------------------------
tex = tex.replace("\n\\begin{tabularx}{\\textwidth}", "\n\\noindent\\begin{tabularx}{\\textwidth}")

# ---------------------------------------------------------------------------
# 2) PDF bookmarks: keep mathematics in the printed heading, but provide clean
# text-only optional titles to hyperref/TOC so PDF outline strings are valid.
# ---------------------------------------------------------------------------
chapter_replacements = {
    r"\chapter{从一个光子到 $S_{21}$：KID 的第一性物理图景}":
        r"\chapter[从一个光子到 S21：KID 的第一性物理图景]{从一个光子到 $S_{21}$：KID 的第一性物理图景}",
    r"\chapter{复电导与 Mattis--Bardeen：把准粒子真正连接到 $L_k$ 与 $Q_i$}":
        r"\chapter[复电导与 Mattis--Bardeen：把准粒子连接到 Lk 与 Qi]{复电导与 Mattis--Bardeen：把准粒子真正连接到 $L_k$ 与 $Q_i$}",
    r"\chapter{微波谐振器与 IQ 读出：从 $Q$ 到可拟合的 $S_{21}$}":
        r"\chapter[微波谐振器与 IQ 读出：从 Q 到可拟合的 S21]{微波谐振器与 IQ 读出：从 $Q$ 到可拟合的 $S_{21}$}",
}
for old, new in chapter_replacements.items():
    tex = tex.replace(old, new)

# ---------------------------------------------------------------------------
# 3) Five-stage material-response flow: compact widths/gaps while retaining the
# same causal content.
# ---------------------------------------------------------------------------
old = r"""\begin{center}
\begin{tikzpicture}[node distance=8mm and 5mm]
\node[flowbox,fill=KidGold!18,minimum width=28mm] (n) {$N_{\qp}\uparrow$};
\node[flowbox,right=of n,minimum width=29mm] (sig) {$\sigma_1\uparrow$\\$\sigma_2\downarrow$};
\node[flowbox,right=of sig,minimum width=30mm] (z) {$R_s\uparrow$\\$X_s\uparrow$};
\node[flowbox,right=of z,minimum width=31mm] (res) {$Q_i\downarrow$\\$f_0\downarrow$};
\node[flowbox,right=of res,minimum width=29mm] (s) {$S_{21}$\\幅度/相位改变};
\draw[flowarrow] (n.east)--(sig.west);
\draw[flowarrow] (sig.east)--(z.west);
\draw[flowarrow] (z.east)--(res.west);
\draw[flowarrow] (res.east)--(s.west);
\end{tikzpicture}
\end{center}"""
new = r"""\begin{center}
\begin{tikzpicture}[node distance=8mm and 3.8mm]
\node[flowbox,fill=KidGold!18,minimum width=24mm] (n) {$N_{\qp}\uparrow$};
\node[flowbox,right=of n,minimum width=25mm] (sig) {$\sigma_1\uparrow$\\$\sigma_2\downarrow$};
\node[flowbox,right=of sig,minimum width=25mm] (z) {$R_s\uparrow$\\$X_s\uparrow$};
\node[flowbox,right=of z,minimum width=26mm] (res) {$Q_i\downarrow$\\$f_0\downarrow$};
\node[flowbox,right=of res,minimum width=25mm] (s) {$S_{21}$\\幅度/相位改变};
\draw[flowarrow] (n.east)--(sig.west);
\draw[flowarrow] (sig.east)--(z.west);
\draw[flowarrow] (z.east)--(res.west);
\draw[flowarrow] (res.east)--(s.west);
\end{tikzpicture}
\end{center}"""
if old not in tex:
    raise SystemExit("Material-response flow block not found")
tex = tex.replace(old, new, 1)

# ---------------------------------------------------------------------------
# 4) GHz-vs-optical frequency sketch: shorten horizontal scale so right-hand
# axis label and annotation remain inside the text block.
# ---------------------------------------------------------------------------
if r"\begin{tikzpicture}[x=0.085cm,y=1cm]" not in tex:
    raise SystemExit("Frequency-sketch scale marker not found")
tex = tex.replace(r"\begin{tikzpicture}[x=0.085cm,y=1cm]", r"\begin{tikzpicture}[x=0.072cm,y=1cm]", 1)

# ---------------------------------------------------------------------------
# 5) Resonance-fitting workflow: long English labels were forcing node width.
# Introduce sensible manual line breaks and slightly tighter gaps.
# ---------------------------------------------------------------------------
old = r"""\begin{tikzpicture}[node distance=7mm and 5mm]
\node[flowbox,fill=KidGray,minimum width=25mm] (raw) {raw complex\\$S_{21}(f)$};
\node[flowbox,right=of raw,minimum width=27mm] (delay) {估计/去除\\cable delay};
\node[flowbox,right=of delay,minimum width=28mm] (base) {complex gain\\baseline normalization};
\node[flowbox,right=of base,minimum width=27mm] (circle) {circle / line-shape\\fit};
\node[flowbox,right=of circle,minimum width=28mm] (par) {$f_0,Q_r,Q_c,Q_i$\\+ uncertainty};"""
new = r"""\begin{tikzpicture}[node distance=7mm and 3.8mm]
\node[flowbox,fill=KidGray,minimum width=24mm] (raw) {raw complex\\$S_{21}(f)$};
\node[flowbox,right=of raw,minimum width=24mm] (delay) {估计/去除\\cable delay};
\node[flowbox,right=of delay,minimum width=25mm] (base) {complex gain\\baseline\\normalization};
\node[flowbox,right=of base,minimum width=24mm] (circle) {circle /\\line-shape fit};
\node[flowbox,right=of circle,minimum width=25mm] (par) {$f_0,Q_r,Q_c,Q_i$\\+ uncertainty};"""
if old not in tex:
    raise SystemExit("Resonance-fitting flow block not found")
tex = tex.replace(old, new, 1)

# ---------------------------------------------------------------------------
# 6) Optical-response/noise flow: the original five boxes plus 7 mm gaps were
# wider than the printable area.  Compact only geometry, not content.
# ---------------------------------------------------------------------------
old = r"""\begin{tikzpicture}[node distance=9mm and 7mm]
\node[flowbox,fill=KidGold!22,minimum width=27mm] (p) {$P_{\rm abs}$\\吸收光功率};
\node[flowbox,right=of p,minimum width=29mm] (g) {$\Gamma_{\rm qp}$\\准粒子产生率};
\node[flowbox,right=of g,minimum width=27mm] (n) {$N_{\rm qp}$\\稳态与涨落};
\node[flowbox,right=of n,minimum width=31mm] (r) {$f_0,Q_i$\\谐振器响应};
\node[flowbox,right=of r,minimum width=28mm] (iq) {$I,Q$\\数字读出};"""
new = r"""\begin{tikzpicture}[node distance=9mm and 4mm]
\node[flowbox,fill=KidGold!22,minimum width=23mm] (p) {$P_{\rm abs}$\\吸收光功率};
\node[flowbox,right=of p,minimum width=24mm] (g) {$\Gamma_{\rm qp}$\\准粒子产生率};
\node[flowbox,right=of g,minimum width=23mm] (n) {$N_{\rm qp}$\\稳态与涨落};
\node[flowbox,right=of n,minimum width=25mm] (r) {$f_0,Q_i$\\谐振器响应};
\node[flowbox,right=of r,minimum width=23mm] (iq) {$I,Q$\\数字读出};"""
if old not in tex:
    raise SystemExit("Optical-response flow block not found")
tex = tex.replace(old, new, 1)

# ---------------------------------------------------------------------------
# 7) Chapter 11 evidence chain: split one overlong boxed math line into two
# aligned lines.  This removes the ~99 pt overflow without shrinking the font.
# ---------------------------------------------------------------------------
old = r"""\[
\boxed{
\text{设计参数}
\rightarrow
\text{GHz 电磁}
\rightarrow
\text{150 GHz 光学电磁}
\rightarrow
\text{数值收敛}
\rightarrow
\text{加工}
\rightarrow
\text{低温 }S_{21}
\rightarrow
\text{光学/偏振标定}
\rightarrow
\text{端到端结论}
}
\]"""
new = r"""\[
\boxed{
\begin{aligned}
\text{设计参数}
&\rightarrow \text{GHz 电磁}
\rightarrow \text{150 GHz 光学电磁}
\rightarrow \text{数值收敛}\\
&\rightarrow \text{加工}
\rightarrow \text{低温 }S_{21}
\rightarrow \text{光学/偏振标定}
\rightarrow \text{端到端结论}
\end{aligned}
}
\]"""
if old not in tex:
    raise SystemExit("Chapter 11 evidence chain not found")
tex = tex.replace(old, new, 1)

# Reader-facing wording found while reviewing the affected pages.
tex = tex.replace("前五个版本主要解决了“材料变化怎样变成 GHz 复数 $S_{21}$”。", "前面的章节主要解决了“材料变化怎样变成 GHz 复数 $S_{21}$”。")
md = md.replace("前五个版本主要解决了“材料变化怎样变成 GHz 复数 $S_{21}$”。", "前面的章节主要解决了“材料变化怎样变成 GHz 复数 $S_{21}$”。")
tex = tex.replace("阅读 Day 2003 的摘要/图 1", "阅读 Day et al. (2003) 的摘要与图 1")
md = md.replace("阅读 Day 2003 的摘要/图 1", "阅读 Day et al. (2003) 的摘要与图 1")

TEX_PATH.write_text(tex, encoding="utf-8")
MD_PATH.write_text(md, encoding="utf-8")

# Static gates before expensive XeLaTeX run.
if "x=0.085cm" in tex:
    raise SystemExit("Old oversized frequency sketch remains")
if "前五个版本主要解决了" in tex or "前五个版本主要解决了" in md:
    raise SystemExit("Development-history wording remains")
if tex.count(r"\noindent\begin{tabularx}{\textwidth}") < 2:
    raise SystemExit("Expected full-width table indentation fixes not found")
for bookmark in (
    "从一个光子到 S21：KID 的第一性物理图景",
    "复电导与 Mattis--Bardeen：把准粒子连接到 Lk 与 Qi",
    "微波谐振器与 IQ 读出：从 Q 到可拟合的 S21",
):
    if bookmark not in tex:
        raise SystemExit("Missing clean PDF bookmark title: " + bookmark)

notes = NOTES_PATH.read_text(encoding="utf-8")
if "## Step 3-D 补充" not in notes:
    notes += textwrap.dedent(r"""

## Step 3-D 补充：版式与 PDF outline 清障

根据 Step 3-C 两遍 XeLaTeX 日志，本轮优先处理明确可定位的横向溢出，而不是凭肉眼猜排版：

- 全宽 `tabularx` 显式取消段首缩进，修复约 20–22 pt 的整表右移；
- 压缩材料响应、resonance fitting、光学响应三张横向流程图的节点间距与最小宽度；
- 将 GHz/150 GHz 频率示意图横向比例从 0.085 cm/GHz 收紧为 0.072 cm/GHz；
- 将第 11 章单行验证证据链拆为两行 aligned box，针对日志中约 99 pt 的严重 overfull；
- 为 3 个含数学符号的章标题增加纯文本 PDF/TOC 标题，消除 hyperref 对 math token 的 outline 警告；
- 顺手清理“前五个版本”和“Day 2003”两处公开教材不够自然的措辞。

验收方式：Step 3-D workflow 在第二遍 XeLaTeX 后自动解析 log；任何超过 8 pt 的 `Overfull \\hbox` 都视为失败并阻止 checkpoint 提交。
""")
    NOTES_PATH.write_text(notes, encoding="utf-8")

print("Step 3-D layout transform complete")
