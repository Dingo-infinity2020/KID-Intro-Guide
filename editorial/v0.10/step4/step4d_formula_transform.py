from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
TEX_PATH = ROOT / 'KID入门讲义_v0.10_step4.tex'
MD_PATH = ROOT / 'KID入门讲义_v0.10_step4.md'
NOTES_PATH = ROOT / 'STEP4_NOTES.md'
tex = TEX_PATH.read_text(encoding='utf-8')
md = MD_PATH.read_text(encoding='utf-8')


def guide_tex(a,b,c,d):
    return '\\formulaexplain\n{' + a + '}\n{' + b + '}\n{' + c + '}\n{' + d + '}'


def guide_md(a,b,c,d):
    return textwrap.dedent(f'''\
> **公式怎么读：不要只背等号**  
> **数学上：** {a}  
> **物理上：** {b}  
> **工程上：** {c}  
> **适用条件：** {d}
''').rstrip()


def norm(s):
    return s.replace('\\\\','\\').replace('\\n','\n')


def add_tex(text, scope, anchor, block, key):
    sent = f'% STEP4D:{key}'
    if sent in text: return text
    scope, anchor = norm(scope), norm(anchor)
    p = text.find(scope)
    if p < 0: raise SystemExit('Missing TeX scope: ' + scope)
    a = text.find(anchor, p)
    if a < 0: raise SystemExit('Missing TeX anchor: ' + anchor)
    e = text.find('\\]', a)
    if e < 0: raise SystemExit('Missing TeX display end: ' + key)
    e += 2
    return text[:e] + '\n' + sent + '\n' + block + text[e:]


def add_md(text, scope, anchor, block, key):
    sent = f'<!-- STEP4D:{key} -->'
    if sent in text: return text
    scope, anchor = norm(scope), norm(anchor)
    p = text.find(scope)
    if p < 0: raise SystemExit('Missing MD scope: ' + scope)
    a = text.find(anchor, p)
    if a < 0: raise SystemExit('Missing MD anchor: ' + anchor)
    e = text.find('$$', a)
    if e < 0: raise SystemExit('Missing MD display end: ' + key)
    e += 2
    return text[:e] + '\n\n' + sent + '\n' + block + text[e:]

CH8T = 'LEKID 电磁设计：把 absorber、resonator、polarization 与 backshort 放进同一个模型'
CH8M = '# 第 8 章：LEKID 电磁设计'

items = [
('fill-factor', r'R_{\\rm eff}\\sim \\frac{R_{\\square}}{F}',
 '在这个极粗略均匀化模型里，金属占空比 $F$ 越小，有效电阻尺度约按 $1/F$ 增大。',
 '电流只能在部分面积的金属条中流动；从更大的光学单元平均来看，稀疏化会抬高沿条带方向看到的有效阻抗。',
 '它提供线宽/线距对 optical impedance 的第一轮趋势判断，可用来缩小 full-wave 参数扫描范围。',
 '只是一维条栅、特定偏振下的均匀化直觉。真实 meander 有各向异性、几何电抗、边缘电流、基底与波导模，不能用它替代 full-wave。'),
('absorber-volume', r'V\\approx lwt',
 '简单条带的 active volume 是长度、宽度和膜厚的乘积。',
 '同样吸收能量分布到更大的超导体积中，会降低平均 quasiparticle density，但几何改变也会同时改变电流路径和电磁阻抗。',
 '这个式子提醒设计者：增加 volume 不是独立旋钮，$l,w,t$ 分别会牵动 GHz 电感、sheet impedance、临界电流、cross-pol 和工艺容差。',
 '仅适用于把有效 absorber 当作均匀条带体积计数；真正参与响应的 active volume 还可能受电流分布、扩散、材料非均匀和 proximity effect 影响。'),
('backshort-match', r'\\boxed{Z_s\\approx Z_0',
 '在 toy model 的 quarter-wave 条件下，若 absorber 的等效 sheet impedance 匹配前侧波阻抗，反射系数趋近零，而 backshort 又封住透射通道，因此吸收可趋近 1。',
 '高吸收的核心不是“多反射一次”，而是让前表面看到的复阻抗与入射模匹配，使反射路径发生正确的幅相抵消。',
 '它给出 backshort + absorber 联合设计的第一性目标：同时调 sheet impedance 与电长度，而不是只追求某一个几何尺寸。',
 '这是平面、单模、理想背短路的简化阻抗匹配图景。真实 horn/waveguide、vacuum gap、各向异性 meander、多模和损耗会移动最佳条件。'),
('quarter-wave', r'd_{\\lambda/4}=\\frac{\\lambda_0}{4n}=\\frac{c}{4n\\nu}',
 '介质中的四分之一波长厚度随频率和折射率均成反比。',
 '短路面经过约四分之一导波波长的传播后，在 absorber 所在平面被阻抗变换成近似开路，从而改变干涉边界条件。',
 '它是确定 backshort/substrate thickness 参数扫描中心的快速手算式；随后应围绕该值做 broadband full-wave sweep。',
 '使用的是均匀介质中的简单相位速度 $c/n$。实际 guided wavelength 受结构色散、角度、waveguide aperture、gap 与多模传播影响，所以 $\\lambda/4$ 不是最终尺寸。'),
('waveguide-cutoff', r'f_c=\\frac{x\\,c}{2\\pi a}=\\frac{x\\,c}{\\pi D}',
 '圆波导各 TE/TM 模的截止频率由相应 Bessel 根 $x$ 和直径 $D$ 决定，并与 $1/D$ 成正比。',
 '横向场必须在圆形边界中“塞得下”相应本征分布；频率低于 cutoff 时纵向传播常数变成倏逝，高于 cutoff 才能携带远距离功率。',
 '在设置 CST/HFSS waveguide port 和做 power closure 前，先用该式列出所有传播模，能避免漏算 TM01 等功率通道。',
 '理想均匀圆波导公式。真实 corrugation、介质加载、渐变 horn、有限长度和不规则截面会改变模态与截止条件，应以实际 eigenmode/port 求解确认。'),
('polarization-selectivity', r'\\eta_{p,X}=\\frac{A_{XX}-A_{XY}}{A_{XX}+A_{XY}}',
 '这个归一化差值在 co-pol 远大于 cross-pol 时趋近 1，两者相等时为 0。',
 '它比较同一目标偏振通道对期望偏振与正交泄漏的相对偏好，而不是只看绝对吸收有多高。',
 '可作为双偏振参数扫描的辅助目标，与 co-pol efficiency、bandshape mismatch 和 angle dependence 一起看。',
 '偏振指标在文献中定义并不统一；使用前必须声明 $A_{ij}$ 下标、归一化和入射基底。它也不能替代完整 Mueller/Jones 描述。'),
('coupling-q-scaling', r'Q_c\\propto\\frac{C}{\\omega_0 Z_0 C_c^2}',
 '弱电容耦合的简化尺度关系显示 $Q_c$ 对 coupling capacitance 近似按 $1/C_c^2$ 变化。',
 '耦合电容稍微增大，就能显著提高谐振器与 feedline 的能量交换率，因此外部 $Q$ 会快速下降。',
 '它解释 coupler finger/gap 为什么需要细致扫参，也能帮助把目标 $Q_c$ 反推到版图灵敏度和加工容差。',
 '这里只给 scaling，不是任意拓扑的精确闭式公式。寄生电容、feedline geometry、分布参数效应和强耦合时必须用 EM 仿真或更完整等效电路。'),
('power-closure', r'1=P_{\\rm refl}+P_{\\rm trans}+P_{\\rm abs}+P_{\\rm other}',
 '归一化输入功率必须被反射、透射、材料吸收和其他明确通道完整分账。',
 '这是 Poynting 能量守恒在数值模型里的审计形式；任何“消失的功率”要么进入了未统计通道，要么说明端口/材料/网格/求解设置有问题。',
 '它应作为所有 full-wave optical 结果的 numerical gate：先证明功率闭合，再比较 B0/B1、偏振或几何优劣。',
 '必须统计所有传播端口模、材料耗散、辐射边界等真实通道，并统一 S 参数的功率归一化。倏逝模本身不携带远场净功率但会影响局部场。'),
('band-weighted-absorption', r'\\bar A=\\frac{\\int W(\\nu)A(\\nu)d\\nu}{\\int W(\\nu)d\\nu}',
 '这是用权重函数 $W(\\nu)$ 对频率相关吸收做归一化加权平均。',
 '真实仪器接收的是一整个 band，不是中心频率上的一个点；不同频率对最终科学信号的贡献还会被 bandpass、源谱和光学链重新加权。',
 '它把“单点 99.9%”升级成真正可比较的 broadband figure of merit，并可进一步加入 cross-pol、angle 和双偏振 mismatch penalty。',
 '必须说明 $W(\\nu)$ 代表什么：平坦权重、仪器 bandpass、源谱还是系统 throughput。不同权重下的 $\\bar A$ 不能不加说明直接比较。'),
]

for key,anchor,a,b,c,d in items:
    tex = add_tex(tex, CH8T, anchor, guide_tex(a,b,c,d), key)

md_anchors = {
'fill-factor': r'R_{\\rm eff}\\sim\\frac{R_\\square}{F}',
'absorber-volume': r'V\\approx lwt',
'backshort-match': r'Z_s\\approx Z_0',
'quarter-wave': r'd_{\\lambda/4}=\\frac{\\lambda_0}{4n}=\\frac{c}{4n\\nu}',
'waveguide-cutoff': r'f_c=\\frac{x c}{\\pi D}',
'polarization-selectivity': r'\\eta_{p,X}=\\frac{A_{XX}-A_{XY}}{A_{XX}+A_{XY}}',
'coupling-q-scaling': r'Q_c\\propto\\frac{C}{\\omega_0 Z_0 C_c^2}',
'power-closure': r'1=P_{\\rm refl}+P_{\\rm trans}+P_{\\rm abs}+P_{\\rm other}',
'band-weighted-absorption': r'\\bar A=\\frac{\\int W(\\nu)A(\\nu)d\\nu}{\\int W(\\nu)d\\nu}',
}
lookup = {x[0]:x[2:] for x in items}
for key,anchor in md_anchors.items():
    a,b,c,d = lookup[key]
    md = add_md(md, CH8M, anchor, guide_md(a,b,c,d), key)

# Remove one lingering private-project heading in Markdown while preserving the case study.
md = md.replace('## 8.17 映射到当前 150 GHz 双偏振项目', '## 8.17 工程案例：150 GHz 双偏振 LEKID 的五层验证')

TEX_PATH.write_text(tex, encoding='utf-8')
MD_PATH.write_text(md, encoding='utf-8')
if tex.count('% STEP4D:') != 9 or md.count('<!-- STEP4D:') != 9:
    raise SystemExit(f'Step4D marker mismatch tex={tex.count("% STEP4D:")} md={md.count("<!-- STEP4D:")}')

AUDIT = ROOT / 'STEP4D_FORMULA_AUDIT.md'
AUDIT.write_text(textwrap.dedent('''\
# v0.10 Step 4-D — LEKID electromagnetic formula pedagogy audit

- New four-layer formula explanations: **9**
- Chapter covered: **8**
- Earlier reader-facing Step 4 guides retained: **34**
- Reader-facing formula guides after this pass: **43**
- Core equations replaced: **NO**
- Scope: optical/microwave co-design, impedance matching, waveguide modes, polarization, coupling and numerical validation.

## Relations covered

1. fill-factor effective-resistance intuition;
2. absorber active volume;
3. backshort impedance matching condition;
4. quarter-wave thickness estimate;
5. circular-waveguide cutoff;
6. polarization selectivity;
7. coupling-$Q$ scaling;
8. full-wave power closure;
9. band-weighted absorption.

Compilation/layout status is filled by CI.
'''), encoding='utf-8')

notes = NOTES_PATH.read_text(encoding='utf-8')
if '## Step 4-D' not in notes:
    notes += textwrap.dedent('''

## Step 4-D — LEKID electromagnetic co-design

第 8 章新增 9 组公式四层解释，将 fill factor、absorber volume、backshort matching、quarter-wave、waveguide cutoff、polarization selectivity、coupling Q、power closure 与 band-weighted absorption 从“会写公式”提升到“知道为什么、怎么用、哪里会失效”。同时把 Markdown 中残留的私人项目标题改成公开教材的工程案例标题。
''')
    NOTES_PATH.write_text(notes, encoding='utf-8')
print('Step 4-D transform complete')
