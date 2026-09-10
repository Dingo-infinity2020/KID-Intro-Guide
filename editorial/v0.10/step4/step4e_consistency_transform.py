from pathlib import Path
import re
import textwrap

ROOT = Path(__file__).resolve().parent
TEX = ROOT / 'KID入门讲义_v0.10_step4.tex'
MD = ROOT / 'KID入门讲义_v0.10_step4.md'
NOTES = ROOT / 'STEP4_NOTES.md'
tex = TEX.read_text(encoding='utf-8')
md = MD.read_text(encoding='utf-8')

# ------------------------------------------------------------------
# 1. Public-textbook wording: keep the real 150 GHz design as a case
#    study, but stop assuming the reader owns the project.
# ------------------------------------------------------------------
tex_repl = {
    r'\section{映射到当前 \SI{150}{GHz} 双偏振 LEKID}': r'\section{工程案例：\SI{150}{GHz} 双偏振 LEKID 的材料判据}',
    r'对当前 \SI{150}{GHz} LEKID，建议以后每次谈材料或仿真参数，都同时写出四个量：': r'对于这一 \SI{150}{GHz} 工程案例，建议每次谈材料或仿真参数时都同时写出四个量：',
    '当前器件的系统边界：不要把所有东西塞进一个模型': '工程案例的系统边界：不要把所有东西塞进一个模型',
    '当前像素同时存在两个相差约两个数量级的频率域': '该工程案例的像素同时存在两个相差约两个数量级的频率域',
    '对当前双偏振 LEKID，一个很有用的项目原则是': '对双偏振 LEKID 工程案例，一个很有用的建模原则是',
    '当前圆波导名义直径': '圆波导名义直径',
    '当前 149--151 GHz 属于窄带验证窗口': '例如 149--151 GHz 可作为窄带验证窗口',
    '当前双偏振单层结构至少要检查': '本工程案例的双偏振单层结构至少要检查',
    r'当前 $D=\SI{1.6}{mm}$ 圆波导在 150 GHz 附近': r'以 $D=\SI{1.6}{mm}$ 圆波导、150 GHz 附近为例',
    'title=当前窄带验证的 modal accounting': 'title=工程案例窄带验证的 modal accounting',
    '当前研究问题的价值不在': '该工程问题的价值不在',
    '在当前模型下有趋势': '在给定模型下有趋势',
}
for old,new in tex_repl.items():
    tex = tex.replace(old,new)

md_repl = {
    '## 4.11 映射到当前 150 GHz 双偏振 LEKID': '## 4.11 工程案例：150 GHz 双偏振 LEKID 的材料判据',
    '## 7. 映射到当前 LEKID': '## 7. 工程案例：从 GHz resonance 回到可解释的器件参数',
    '## 8.17 映射到当前 150 GHz 双偏振项目': '## 8.17 工程案例：150 GHz 双偏振 LEKID 的五层验证',
    '当前器件的系统边界：不要把所有东西塞进一个模型': '工程案例的系统边界：不要把所有东西塞进一个模型',
    '当前像素同时存在两个相差约两个数量级的频率域': '该工程案例的像素同时存在两个相差约两个数量级的频率域',
    '对当前双偏振 LEKID，一个很有用的项目原则是': '对双偏振 LEKID 工程案例，一个很有用的建模原则是',
    '当前圆波导名义直径': '圆波导名义直径',
    '当前 149–151 GHz 属于窄带验证窗口': '例如 149–151 GHz 可作为窄带验证窗口',
    '当前 149--151 GHz 属于窄带验证窗口': '例如 149--151 GHz 可作为窄带验证窗口',
    '当前双偏振单层结构至少要检查': '本工程案例的双偏振单层结构至少要检查',
    '当前 $D=1.6$ mm 圆波导': '以 $D=1.6$ mm 圆波导为例',
    '当前 $D=1.6\,\mathrm{mm}$ 圆波导': '以 $D=1.6\,\mathrm{mm}$ 圆波导为例',
    '当前研究问题的价值不在': '该工程问题的价值不在',
    '在当前模型下有趋势': '在给定模型下有趋势',
}
for old,new in md_repl.items():
    md = md.replace(old,new)

# ------------------------------------------------------------------
# 2. Complex-number notation: material-response equations use i;
#    RF S21 equations may retain the conventional engineering j.
# ------------------------------------------------------------------
tex = tex.replace(r'\sigma=\sigma_1-j\sigma_2', r'\sigma=\sigma_1-i\sigma_2')
md = md.replace(r'\sigma=\sigma_1-j\sigma_2', r'\sigma=\sigma_1-i\sigma_2')
tex = tex.replace(r'$Z_s=R_s+jX_s$ & 表面阻抗', r'$Z_s=R_s+iX_s$ & 表面阻抗')
md = md.replace('| $Z_s$ | 表面阻抗 |', '| $Z_s$ | 表面阻抗 |')

# ------------------------------------------------------------------
# 3. Expand the front-matter symbol table: number vs density,
#    optical bandwidth, and the three powers that beginners mix up.
# ------------------------------------------------------------------
tex_needle = r'$N_{\rm qp}$ & 准粒子数 & 吸收功率增加后通常会上升，是“光”到“材料状态”之间的关键中间量。 \\'
tex_extra = tex_needle + '\n' + r'$n_{\rm qp}$ & 准粒子数密度 & 单位体积内的准粒子数；若体积为 $V$ 且分布近似均匀，则 $N_{\rm qp}\approx n_{\rm qp}V$。 \\'
if '$n_{\\rm qp}$ & 准粒子数密度' not in tex:
    if tex_needle not in tex: raise SystemExit('Missing TeX Nqp glossary row')
    tex = tex.replace(tex_needle, tex_extra, 1)

tex_needle2 = r'$P_{\rm abs}$ & 吸收光功率 & 真正进入 absorber 并转化为探测器激发的功率。 \\'
tex_extra2 = '\n'.join([
    r'$P_{\rm inc}$ & 入射光功率 & 到达器件/定义参考面的光功率；通常有 $P_{\rm abs}\le P_{\rm inc}$。 \\',
    tex_needle2,
    r'$P_{\rm read}$ & 微波读出功率 & GHz probe tone 的功率；与被探测的毫米波/亚毫米波光功率不是同一个量。 \\',
    r'$\Delta\nu$ & 光学等效带宽 & 频带宽度；这里的 $\Delta\nu$ 与超导能隙 $\Delta$ 完全不是同一个物理量。 \\',
])
if '$P_{\\rm inc}$ & 入射光功率' not in tex:
    if tex_needle2 not in tex: raise SystemExit('Missing TeX Pabs glossary row')
    tex = tex.replace(tex_needle2, tex_extra2, 1)

md_needle = '| $N_{\\rm qp}$ | 准粒子数 | 光到材料状态之间的关键中间量 |'
md_extra = md_needle + '\n| $n_{\\rm qp}$ | 准粒子数密度 | 单位体积内的准粒子数；均匀时 $N_{\\rm qp}\\approx n_{\\rm qp}V$ |'
if '| $n_{\\rm qp}$ | 准粒子数密度 |' not in md:
    if md_needle not in md: raise SystemExit('Missing MD Nqp glossary row')
    md = md.replace(md_needle, md_extra, 1)

md_needle2 = '| $P_{\\rm abs}$ | 吸收光功率 | 真正进入 absorber 的功率 |'
md_extra2 = '\n'.join([
    '| $P_{\\rm inc}$ | 入射光功率 | 到达器件/参考面的光功率；通常 $P_{\\rm abs}\\le P_{\\rm inc}$ |',
    md_needle2,
    '| $P_{\\rm read}$ | 微波读出功率 | GHz probe tone 功率，与被探测光功率不同 |',
    '| $\\Delta\\nu$ | 光学等效带宽 | 频带宽度，与超导能隙 $\\Delta$ 不同 |',
])
if '| $P_{\\rm inc}$ | 入射光功率 |' not in md:
    if md_needle2 not in md: raise SystemExit('Missing MD Pabs glossary row')
    md = md.replace(md_needle2, md_extra2, 1)

# ------------------------------------------------------------------
# 4. Add a concise notation/convention box after the existing frequency
#    checkpoint. It is intentionally beginner-facing rather than formal.
# ------------------------------------------------------------------
tex_marker = r'''\begin{checkpointbox}
三个特别值得从一开始就区分的量：\textbf{$\nu$ 是被探测光的频率，$f_0$ 是 GHz 谐振器的谐振频率，$f$ 在噪声谱章节里还会表示 Fourier frequency。} 它们都叫“频率”，但在物理链条中的职责完全不同。
\end{checkpointbox}'''
tex_box = textwrap.dedent(r'''
\begin{tcolorbox}[colback=white,colframe=KidBlue!55,arc=2mm,title=全书统一约定：五组最容易混淆的符号,fonttitle=\bfseries]
\begin{enumerate}
  \item \textbf{$N_{\rm qp}$ 与 $n_{\rm qp}$：}前者是准粒子总数，后者是准粒子数密度；只有在给定有效体积后才能互相换算。
  \item \textbf{$\Delta$ 与 $\Delta\nu$：}$\Delta$ 是超导能隙，$\Delta\nu$ 是光学频带宽度；看起来相似，量纲完全不同。
  \item \textbf{$P_{\rm inc}$、$P_{\rm abs}$ 与 $P_{\rm read}$：}分别表示入射光功率、真正被 absorber 吸收的光功率和 GHz 微波读出功率。响应度/NEP 的分母必须写清到底指哪一种功率。
  \item \textbf{$i$ 与 $j$：}二者都表示虚数单位，$i^2=j^2=-1$。本书在材料复电导/表面阻抗中优先用 $i$，在 RF 的 $S_{21}$、IQ 和电路公式中常保留工程习惯 $j$。
  \item \textbf{PSD 与 ASD：}ASD 是 PSD 的平方根。涉及绝对噪声系数或与文献比较时，还必须声明采用 one-sided 还是 two-sided PSD；这类约定常带来因子 2。
\end{enumerate}
\end{tcolorbox}
''').strip()
if '全书统一约定：五组最容易混淆的符号' not in tex:
    if tex_marker not in tex: raise SystemExit('Missing TeX convention insertion point')
    tex = tex.replace(tex_marker, tex_marker + '\n\n' + tex_box, 1)

md_marker = '**特别提醒：** $\\nu$ 常表示被探测光频率，$f_0$ 表示 GHz 谐振频率，而噪声谱里的 $f$ 常表示 Fourier frequency。三者都叫“频率”，但职责不同。'
md_box = textwrap.dedent(r'''

> **全书统一约定：五组最容易混淆的符号。**  
> 1. $N_{\rm qp}$ 是准粒子**总数**，$n_{\rm qp}$ 是准粒子**数密度**；给定有效体积后才能互换。  
> 2. $\Delta$ 是超导能隙，$\Delta\nu$ 是光学频带宽度，量纲不同。  
> 3. $P_{\rm inc}$、$P_{\rm abs}$、$P_{\rm read}$ 分别是入射光功率、吸收光功率和 GHz 读出功率；写 responsivity/NEP 时必须声明输入功率定义。  
> 4. $i$ 与 $j$ 都是虚数单位。本书在材料复电导/表面阻抗中优先用 $i$，在 RF 的 $S_{21}$/IQ 公式中保留常见的 $j$。  
> 5. ASD 是 PSD 的平方根；比较绝对噪声系数时还要声明 one-sided / two-sided PSD 约定，否则很容易出现因子 2。
''').rstrip()
if '全书统一约定：五组最容易混淆的符号' not in md:
    if md_marker not in md: raise SystemExit('Missing MD convention insertion point')
    md = md.replace(md_marker, md_marker + md_box, 1)

TEX.write_text(tex, encoding='utf-8')
MD.write_text(md, encoding='utf-8')

# ------------------------------------------------------------------
# Static editorial gates.
# ------------------------------------------------------------------
# Historical development labels should not appear outside current-version metadata.
for label,text in [('TeX',tex),('Markdown',md)]:
    for ln,line in enumerate(text.splitlines(),1):
        if re.search(r'v0\.(?!10\b)[0-9]+', line):
            raise SystemExit(f'{label} historical release label at L{ln}: {line[:150]}')

private_markers = ['映射到当前', '当前器件的系统边界', '对当前双偏振 LEKID', '你的项目', '你当前的 LEKID']
for marker in private_markers:
    if marker in tex or marker in md:
        raise SystemExit('Private-project marker remains: ' + marker)

if r'\sigma=\sigma_1-j\sigma_2' in tex or r'\sigma=\sigma_1-j\sigma_2' in md:
    raise SystemExit('Conductivity review still uses j after notation unification')

for required in ['准粒子数密度', '全书统一约定：五组最容易混淆的符号', 'one-sided', 'P_{\\rm read}']:
    if required not in tex or required not in md:
        raise SystemExit('Missing required convention content: ' + required)

# Step 4 should now retain all 43 reader-facing guides from A-D.
formula_invocations = tex.count('\\formulaexplain') - 1  # subtract macro definition
if formula_invocations != 43:
    raise SystemExit(f'Expected 43 reader-facing formula guides, got {formula_invocations}')

AUDIT = ROOT / 'STEP4E_CONSISTENCY_AUDIT.md'
AUDIT.write_text(textwrap.dedent(f'''\
# v0.10 Step 4-E — Notation and public-textbook consistency audit

- Reader-facing formula guides retained: **{formula_invocations}**
- Historical v0.1–v0.9 development labels in body: **0**
- Known private-project markers: **0**
- Conductivity convention in review sections: **$\\sigma=\\sigma_1-i\\sigma_2$**
- RF $S_{{21}}$ formulas may retain engineering $j$: **intentional**
- $N_{{qp}}$ (total) vs $n_{{qp}}$ (density): **defined explicitly**
- $\\Delta$ (gap) vs $\\Delta\\nu$ (bandwidth): **defined explicitly**
- $P_{{inc}}$ vs $P_{{abs}}$ vs $P_{{read}}$: **defined explicitly**
- PSD/ASD and one-sided/two-sided convention warning: **added**

Compilation, cross-reference and example-script gates are filled by CI.
'''), encoding='utf-8')

notes = NOTES.read_text(encoding='utf-8')
if '## Step 4-E' not in notes:
    notes += textwrap.dedent('''

## Step 4-E — notation / public-textbook consistency

- 清理剩余“当前项目/当前器件”式私人语境，把 150 GHz 双偏振 LEKID 固定为公开教材中的工程案例；
- 统一材料复电导使用 $i$，同时说明 RF/$S_{21}$ 公式保留工程习惯 $j$，二者均为虚数单位；
- 明确 $N_{qp}$（总数）与 $n_{qp}$（数密度）、$Delta$（能隙）与 $Delta nu$（光学带宽）；
- 明确 incident / absorbed / readout 三种功率定义；
- 在 PSD/ASD 处加入 one-sided / two-sided convention 警告。
''')
    NOTES.write_text(notes, encoding='utf-8')

print('Step 4-E consistency transform complete')
