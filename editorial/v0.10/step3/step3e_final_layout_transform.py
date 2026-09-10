from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
TEX_PATH = ROOT / "KID入门讲义_v0.10_step3.tex"
NOTES_PATH = ROOT / "STEP3_NOTES.md"
tex = TEX_PATH.read_text(encoding="utf-8")

# 1) Chapter-1 overview diagram: a small residual overfull remained after the
# major cleanup.  Tighten only the top row; keep labels/content unchanged.
old = r"""\begin{tikzpicture}[node distance=9mm and 6mm]
\node[flowbox,fill=KidGold!20,minimum width=31mm] (opt) {光场与吸收\\$P_{\rm abs},\nu$};
\node[flowbox,right=of opt,minimum width=36mm] (mat) {超导态与材料响应\\$\Delta,N_{\qp},\sigma_1,\sigma_2,L_k$};
\node[flowbox,right=of mat,minimum width=31mm] (res) {GHz 谐振器\\$f_0,Q_i,Q_c$};
\node[flowbox,right=of res,minimum width=34mm] (read) {读出与灵敏度\\$S_{21},I/Q,$ NEP};"""
new = r"""\begin{tikzpicture}[node distance=9mm and 4mm]
\node[flowbox,fill=KidGold!20,minimum width=28mm] (opt) {光场与吸收\\$P_{\rm abs},\nu$};
\node[flowbox,right=of opt,minimum width=32mm] (mat) {超导态与材料响应\\$\Delta,N_{\qp},\sigma_1,\sigma_2,L_k$};
\node[flowbox,right=of mat,minimum width=28mm] (res) {GHz 谐振器\\$f_0,Q_i,Q_c$};
\node[flowbox,right=of res,minimum width=30mm] (read) {读出与灵敏度\\$S_{21},I/Q,$ NEP};"""
if old not in tex:
    raise SystemExit("Chapter-1 overview flow marker not found")
tex = tex.replace(old, new, 1)

# 2) Let TeX break the short slash-separated solver vocabulary naturally.
tex = tex.replace("Solver & mesh/modes/ports &", "Solver & mesh / modes / ports &", 1)

# 3) The remaining reference overflows are caused by DOI strings.  Put the DOI
# on a separate line and use \url so legal breakpoints are available.
tex = tex.replace(
    r"\textit{Journal of Applied Physics}, 111, 054510 (2012), doi:10.1063/1.3692073.",
    r"\textit{Journal of Applied Physics}, 111, 054510 (2012).\\ DOI: \url{https://doi.org/10.1063/1.3692073}.",
    1,
)
tex = tex.replace(
    r"\textit{Review of Scientific Instruments}, 86, 024706 (2015), doi:10.1063/1.4907935.",
    r"\textit{Review of Scientific Instruments}, 86, 024706 (2015).\\ DOI: \url{https://doi.org/10.1063/1.4907935}.",
    1,
)

TEX_PATH.write_text(tex, encoding="utf-8")

notes = NOTES_PATH.read_text(encoding="utf-8")
if "## Step 3-E 补充" not in notes:
    notes += textwrap.dedent(r"""

## Step 3-E 补充：零 overfull 收尾

Step 3-D 已将严重版式问题全部压到 8 pt 以下。本小步继续清理剩余 4 个轻微 overfull：

- 收紧第 1 章总览流程图的顶层节点宽度与间距；
- 将 `mesh/modes/ports` 改为可自然断行的 `mesh / modes / ports`；
- 将 Khalil (2012) 与 Probst (2015) 的 DOI 单独换行，并使用 `\\url{}` 提供合法断点。

Step 3-E 的验收门槛提升为：第二遍 XeLaTeX 日志中 `Overfull \\hbox` 数量必须为 0。
""")
    NOTES_PATH.write_text(notes, encoding="utf-8")

print("Step 3-E final layout transform complete")
