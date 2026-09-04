from pathlib import Path

root = Path(__file__).resolve().parents[1]
v02 = root / 'docs' / 'v0.2'
v03 = root / 'docs' / 'v0.3'

# ---------- LaTeX ----------
tex = (v02 / 'KID入门讲义_v0.2.tex').read_text(encoding='utf-8')
tex = tex.replace('pdftitle={KID入门讲义 v0.2}', 'pdftitle={KID入门讲义 v0.3}')
tex = tex.replace('\\fancyhead[L]{KID 入门讲义 v0.2}', '\\fancyhead[L]{KID 入门讲义 v0.3}')
tex = tex.replace('Version 0.2 · 2026-09-04', 'Version 0.3 · 2026-09-04')
old_intro = r'''当前版本 v0.2 在 v0.1 的基础上重点完成三件事：
\begin{itemize}
  \item 给出整个 KID 入门学习路线；
  \item 完整建立“从光子到 $\Stwentyone$”的基础物理图景，并重绘全部流程图；
  \item 新增“动能电感”专题章，从载流子惯性推到薄膜 sheet kinetic inductance 与 $\alpha$。
\end{itemize}
后续版本会逐章增加推导、数值练习、Python notebook、Sonnet/全波仿真任务以及与你的双偏振 LEKID 项目的对应分析。'''
new_intro = r'''当前版本 v0.3 在 v0.2 的基础上继续推进四件事：
\begin{itemize}
  \item 保留整个 KID 入门学习路线与“从光子到 $\Stwentyone$”的基础物理图景；
  \item 保留第 3 章动能电感推导，并继续把宏观电路量连接到微观超导状态；
  \item 新增“超导基础最小知识集”：Cooper pair、BCS 能隙、准粒子与热激发；
  \item 新增 generation--recombination、quasiparticle lifetime，以及材料 $T_c$ 与 \SI{150}{GHz} pair-breaking threshold 的直接设计联系。
\end{itemize}
后续版本会继续进入复电导、Mattis--Bardeen、谐振器拟合、NEP、噪声与 LEKID 电磁设计。'''
if old_intro not in tex:
    raise RuntimeError('LaTeX intro block not found')
tex = tex.replace(old_intro, new_intro)
chapter_tex = (v03 / '_chapter4.tex.inc').read_text(encoding='utf-8').rstrip() + '\n\n'
marker = '\\chapter*{后续版本计划}'
if marker not in tex:
    raise RuntimeError('LaTeX plan marker not found')
tex = tex.replace(marker, chapter_tex + marker, 1)
tex = tex.replace('  \\item v0.3：Cooper pair、BCS 能隙、热准粒子与 $N_{qp}(T)$；\n', '')
tex = tex.replace('  \\item v0.6：optical responsivity、quasiparticle lifetime、NEP 与噪声；',
                  '  \\item v0.6：optical responsivity、NEP 与 photon / GR / TLS / amplifier noise；')
old_refs = r'''\begin{enumerate}
  \item P. K. Day et al., ``A broadband superconducting detector suitable for use in large arrays,'' \textit{Nature}, 425, 817--821 (2003).
  \item S. Doyle, \textit{Lumped Element Kinetic Inductance Detectors}, PhD thesis, Cardiff University (2008).
  \item J. Zmuidzinas, ``Superconducting Microresonators: Physics and Applications,'' \textit{Annual Review of Condensed Matter Physics}, 3, 169--214 (2012).
  \item J. Gao, \textit{The Physics of Superconducting Microwave Resonators}, PhD thesis, California Institute of Technology (2008).
\end{enumerate}'''
new_refs = r'''\begin{enumerate}
  \item P. K. Day et al., ``A broadband superconducting detector suitable for use in large arrays,'' \textit{Nature}, 425, 817--821 (2003).
  \item S. Doyle, \textit{Lumped Element Kinetic Inductance Detectors}, PhD thesis, Cardiff University (2008).
  \item J. Zmuidzinas, ``Superconducting Microresonators: Physics and Applications,'' \textit{Annual Review of Condensed Matter Physics}, 3, 169--214 (2012).
  \item J. Gao, \textit{The Physics of Superconducting Microwave Resonators}, PhD thesis, California Institute of Technology (2008).
  \item M. Tinkham, \textit{Introduction to Superconductivity}, 2nd ed., Dover Publications (2004 reprint).
  \item S. B. Kaplan et al., ``Quasiparticle and phonon lifetimes in superconductors,'' \textit{Physical Review B}, 14, 4854--4873 (1976).
  \item A. Rothwarf and B. N. Taylor, ``Measurement of Recombination Lifetimes in Superconductors,'' \textit{Physical Review Letters}, 19, 27--30 (1967).
  \item P. J. de Visser et al., ``Number Fluctuations of Sparse Quasiparticles in a Superconductor,'' \textit{Physical Review Letters}, 106, 167004 (2011/2012 literature context).
\end{enumerate}'''
if old_refs not in tex:
    raise RuntimeError('LaTeX reference block not found')
tex = tex.replace(old_refs, new_refs)
(v03 / 'KID入门讲义_v0.3.tex').write_text(tex, encoding='utf-8')

# ---------- Markdown ----------
md = (v02 / 'KID入门讲义_v0.2.md').read_text(encoding='utf-8')
md = md.replace('# KID 入门讲义 v0.2', '# KID 入门讲义 v0.3', 1)
md = md.replace('**版本：v0.2 · 2026-09-04**', '**版本：v0.3 · 2026-09-04**', 1)
old_md_intro = '''当前 v0.2 在 v0.1 的基础上重点完成：
- 保留完整的 KID 入门学习路线；
- 重绘“从光子到 $S_{21}$”章节中的流程图，并统一箭头语义；
- 新增“动能电感”专题章：从载流子惯性推到薄膜 sheet kinetic inductance 与 $\\alpha$。'''
new_md_intro = '''当前 v0.3 在 v0.2 的基础上继续完成：
- 保留完整的 KID 入门学习路线与统一图示规范；
- 保留“从光子到 $S_{21}$”和“动能电感”两章；
- 新增“超导基础最小知识集”：Cooper pair、BCS 能隙、准粒子与热激发；
- 新增 generation–recombination、quasiparticle lifetime，以及材料 $T_c$ 与 150 GHz pair-breaking threshold 的直接设计联系。'''
if old_md_intro not in md:
    raise RuntimeError('Markdown intro block not found')
md = md.replace(old_md_intro, new_md_intro)
md = md.replace('### v0.2 的图示约定', '### v0.3 延续的图示约定', 1)
chapter_md = (v03 / '_chapter4.md.inc').read_text(encoding='utf-8').rstrip() + '\n\n'
md_marker = '# 后续版本计划'
if md_marker not in md:
    raise RuntimeError('Markdown plan marker not found')
md = md.replace(md_marker, chapter_md + md_marker, 1)
md = md.replace('- v0.3：Cooper pair、BCS 能隙、热准粒子与 $N_{qp}(T)$\n', '')
md = md.replace('- v0.6：responsivity、quasiparticle lifetime、NEP 与噪声',
                '- v0.6：optical responsivity、NEP 与 photon / GR / TLS / amplifier noise')
md = md.replace('4. J. Gao, *The Physics of Superconducting Microwave Resonators*, PhD thesis, California Institute of Technology (2008).',
'''4. J. Gao, *The Physics of Superconducting Microwave Resonators*, PhD thesis, California Institute of Technology (2008).
5. M. Tinkham, *Introduction to Superconductivity*, 2nd ed., Dover Publications.
6. S. B. Kaplan et al., “Quasiparticle and phonon lifetimes in superconductors,” *Physical Review B*, 14, 4854–4873 (1976).
7. A. Rothwarf and B. N. Taylor, “Measurement of Recombination Lifetimes in Superconductors,” *Physical Review Letters*, 19, 27–30 (1967).
8. P. J. de Visser et al., generation–recombination / sparse quasiparticle fluctuation studies in superconducting resonators.''')
(v03 / 'KID入门讲义_v0.3.md').write_text(md, encoding='utf-8')

print('Generated v0.3 LaTeX and Markdown sources')
