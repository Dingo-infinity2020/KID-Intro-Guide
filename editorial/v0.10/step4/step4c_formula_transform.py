from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
TEX_PATH = ROOT / 'KID入门讲义_v0.10_step4.tex'
MD_PATH = ROOT / 'KID入门讲义_v0.10_step4.md'
NOTES_PATH = ROOT / 'STEP4_NOTES.md'

tex = TEX_PATH.read_text(encoding='utf-8')
md = MD_PATH.read_text(encoding='utf-8')


def tex_guide(math, physics, engineering, validity):
    return '\\formulaexplain\n{' + math + '}\n{' + physics + '}\n{' + engineering + '}\n{' + validity + '}'


def md_guide(math, physics, engineering, validity):
    return textwrap.dedent(f'''\
> **公式怎么读：不要只背等号**  
> **数学上：** {math}  
> **物理上：** {physics}  
> **工程上：** {engineering}  
> **适用条件：** {validity}
''').rstrip()


def insert_after_tex_display(text, scope, anchor, addition, marker):
    sentinel = f'% STEP4C:{marker}'
    if sentinel in text:
        return text
    s = text.find(scope)
    if s < 0:
        raise SystemExit(f'Missing TeX scope: {scope}')
    a = text.find(anchor, s)
    if a < 0:
        raise SystemExit(f'Missing TeX anchor after {scope}: {anchor}')
    end = text.find('\\]', a)
    if end < 0:
        raise SystemExit(f'Missing TeX display end after {anchor}')
    end += 2
    return text[:end] + '\n' + sentinel + '\n' + addition + text[end:]


def insert_after_md_display(text, scope, anchor, addition, marker):
    sentinel = f'<!-- STEP4C:{marker} -->'
    if sentinel in text:
        return text
    s = text.find(scope)
    if s < 0:
        raise SystemExit(f'Missing Markdown scope: {scope}')
    a = text.find(anchor, s)
    if a < 0:
        raise SystemExit(f'Missing Markdown anchor after {scope}: {anchor}')
    end = text.find('$$', a)
    if end < 0:
        raise SystemExit(f'Missing Markdown display end after {anchor}')
    end += 2
    return text[:end] + '\n\n' + sentinel + '\n' + addition + text[end:]

# ------------------------------ Chapter 6 ------------------------------
CH6T = r'\\chapter[微波谐振器与 IQ 读出'
CH6M = '# 第 6 章：微波谐振器与 IQ 读出'

items = [
('q-definition', r'Q=\\omega_0\\frac{U}{P_{\\rm loss}}',
 '品质因数是“每个弧度储存的能量 / 损失的能量”的无量纲比值；$Q$ 越大，同样储能下单位时间损失越小。',
 '谐振器并不是凭空把信号放大，而是让能量在结构里反复交换许多周期；损失越慢，频率选择性越尖锐。',
 '它是理解 $Q_i,Q_c,Q_r$ 的共同起点，也能把材料损耗、耦合和最终 linewidth 放进同一套能量语言。',
 '默认线性、稳定的谐振模式，并用周期平均储能与损耗定义。强非线性、模式混合或随时间快速变化时，一个单一 $Q$ 可能不足以描述系统。'),
('loaded-q', r'\\frac{1}{Q_r}=\\frac{1}{Q_i}+\\frac{1}{Q_c}',
 '独立能量衰减通道的“损耗率”相加，因此是 $1/Q$ 相加，而不是 $Q$ 本身相加。',
 '$Q_i$ 像器件内部的漏水口，$Q_c$ 像与 feedline 相连的可控出口；两个出口同时存在时，总排空速度是两者之和。',
 '从实测 $Q_r$ 判断器件时必须同时分解 $Q_i$ 与 $Q_c$；否则 notch 变宽究竟来自材料变差还是耦合变强无法区分。',
 '假设两个通道可近似独立并由同一个单模谐振器描述。复杂非对称耦合、多端口、辐射模或模式杂化时需要更完整的耦合模模型。'),
('linewidth', r'\\Delta f_{\\rm FWHM}\\approx\\frac{f_0}{Q_r}',
 '谐振器的半功率带宽约等于中心频率除以 loaded $Q$；因此 $Q_r=f_0/\\Delta f$。',
 '能量保存得越久，系统对“驱动频率是否刚好匹配”越挑剔，所以频域 resonance 越窄。',
 '它把拟合得到的 $Q_r$ 立刻转换成 tone spacing、扫频步长和允许频移的工程尺度。',
 '适用于孤立、近似 Lorentzian、弱非线性的单模 resonance。强功率导致 bifurcation、邻近 resonance 重叠或非 Lorentzian 线形时不能机械使用。'),
('ringdown-factor2', r'\\tau_A=\\frac{2Q_r}{\\omega_0}',
 '能量时间常数 $\\tau_E=Q_r/\\omega_0$，振幅时间常数 $\\tau_A=2Q_r/\\omega_0$；二者相差 2，因为能量正比于振幅平方。',
 '若场振幅衰减为 $e^{-t/\\tau_A}$，能量就按 $e^{-2t/\\tau_A}$ 衰减，所以能量更快下降。',
 '阅读论文或设定 detector bandwidth 时必须先确认作者所谓 resonator lifetime 指能量还是振幅；差一个 2 足以造成带宽估计错误。',
 '这里使用单指数 ring-down 的线性单模模型。读出链滤波、多模 beating 或非线性恢复过程会引入额外时间尺度。'),
('ideal-s21', r'S_{21}(f)\n=1-',
 '最小 hanger 模型把一个直通背景“1”和一个经谐振器再耦回 feedline 的复振幅相减；分母中的 detuning 决定离 resonance 多远。',
 'notch 来自两条相干路径的干涉，不等于“谐振器把所有功率吸收掉”；内部损耗与外部耦合共同决定凹口深度和宽度。',
 '这是理解 notch、IQ circle、$Q$ 拟合和 fixed-tone 工作点的母公式，也是合成 VNA 数据的第一层模型。',
 '假设已做背景归一化、没有 cable delay、耦合可视为实数且系统线性。真实数据通常还需要 complex gain、delay 与 asymmetry 参数。'),
('iq-circle', r'\\left(\\operatorname{Re}S_{21}-\\left(1-\\frac d2\\right)\\right)^2',
 '消去 detuning 参数 $y$ 后，理想复数 $S_{21}$ 满足标准圆方程，圆心为 $(1-d/2,0)$、半径为 $d/2$。',
 '扫频改变的是同一个谐振响应的相位与幅度组合，所以复平面轨迹不是任意曲线，而被一维 detuning 参数限制在圆上。',
 'circle fit 利用了这个几何约束，因此通常比只拟合 $|S_{21}|$ 更充分地使用信息，也更容易识别 delay/baseline 问题。',
 '严格圆形依赖理想单 pole、线性和正确背景处理。阻抗失配、频率依赖 gain、邻近模与非线性会使圆被旋转、偏置或变形。'),
('fixed-tone-linearization', r'\\delta S_{21}\n\\approx',
 '在固定工作点对 $S_{21}(f_0,Q_i^{-1})$ 做一阶 Taylor 展开，把小的频移和损耗变化线性映射到复数 IQ 位移。',
 'probe tone 本身不需要跟着信号扫频；器件 resonance 移动时，相当于固定探针在局部响应曲面上看到位置发生变化。',
 '这是把 detector physics 接到实时 DDC 输出 $I(t),Q(t)$ 的核心公式，也说明为什么需要选合适的 tone 位置与局部基底。',
 '只在小信号、工作点附近线性有效。大光学负载导致 resonance 漂出线性区、$Q_i$ 大幅变化或读出进入 bifurcation 时要重新扫频/跟踪或用非线性模型。'),
('measured-s21', r'S_{21}^{\\rm meas}(f)\n=',
 '实测模型在理想 notch 外乘上复增益 $G(f)$ 和 electrical-delay 相位，并用 $\\phi$ 描述有效非对称耦合。',
 'VNA 看到的是“器件 + 线缆 + 放大器 + 阻抗失配”的总复传输；这些读出链效应会旋转、缩放甚至扭曲原本的谐振圆。',
 '拟合时把器件参数与 readout-chain nuisance parameters 分开，才能避免把 cable delay 或 baseline 错认成 $Q_i$、$Q_c$ 或真实光学响应。',
 '不同文献对 complex $Q_c$、$\\phi$ 和背景多项式的参数化不完全相同；复现结果时必须使用同一模型约定，并检查残差与窗口稳定性。'),
]
for key, anchor, ma, ph, en, va in items:
    tex = insert_after_tex_display(tex, CH6T, anchor, tex_guide(ma,ph,en,va), key)

md_items = [
('q-definition', r'Q=\\omega_0\\frac{U}{P_{\\rm loss}}'),
('loaded-q', r'\\boxed{\\frac1{Q_r}=\\frac1{Q_i}+\\frac1{Q_c}}'),
('linewidth', r'\\boxed{\\Delta f_{\\rm FWHM}\\approx\\frac{f_0}{Q_r}}'),
('ringdown-factor2', r'\\boxed{\\tau_A=\\frac{2Q_r}{\\omega_0}'),
('ideal-s21', r'S_{21}(f)=1-\\frac{Q_r/Q_c}'),
('iq-circle', r'\\left(\\operatorname{Re}S_{21}-1+\\frac d2\\right)^2'),
('fixed-tone-linearization', r'\\delta S_{21}\\approx'),
('measured-s21', r'S_{21}^{\\rm meas}(f)=G(f)e^{-j2\\pi f\\tau}'),
]
lookup = {x[0]: x[2:] for x in items}
for key, anchor in md_items:
    ma,ph,en,va = lookup[key]
    md = insert_after_md_display(md, CH6M, anchor, md_guide(ma,ph,en,va), key)

# ------------------------------ Chapter 7 ------------------------------
CH7T = r'\\chapter{光学响应、噪声与 NEP'
CH7M = '# 第 7 章：光学响应、噪声与 NEP'
items7 = [
('qp-generation', r'\\Gamma_{\\rm qp}\\simeq \\frac{\\eta_{\\rm pb}P_{\\rm abs}}{\\Delta}',
 '吸收功率除以单个准粒子的特征能量 $\\Delta$ 给出每秒可产生的激发数量级，再乘 $\\eta_{\\rm pb}$ 表示能量级联的有效效率。',
 '连续光功率不断向准粒子系统注入能量；高能光子先破对，再通过声子级联形成更多接近能隙边缘的激发。',
 '它是从 full-wave 得到的 $P_{\\rm abs}$ 接到 detector dynamics 的第一座桥，可用于响应度与噪声预算。',
 '这是能量守恒的有效工程近似，$\\eta_{\\rm pb}$ 依赖材料、频率、声子逃逸与非平衡动力学；不能理解成每个光子固定产生某个整数准粒子。'),
('qp-responsivity', r'\\frac{\\partial N_{\\rm qp}}{\\partial P_{\\rm abs}}',
 '在线性稳态模型里，准粒子数对吸收功率的斜率为 $\\eta_{\\rm pb}\\tau_{\\rm qp}/\\Delta$。',
 '产生得越快或活得越久，稳态池子里积累的准粒子就越多；因此 lifetime 同时是“积分时间”和物理增益。',
 '这个斜率把材料动力学压缩成一个可直接与光功率标定连接的参数，是计算 frequency/dissipation responsivity 的公共因子。',
 '假设小扰动、单一有效 lifetime 且 $\\tau_{\\rm qp}$ 在工作点附近近似常数。强负载下 recombination 往往使 lifetime 随 $N_{\\rm qp}$ 改变。'),
('frequency-responsivity', r'\\mathcal R_x\n\\equiv',
 '链式法则把“每个准粒子造成多少 fractional frequency shift”和“每瓦吸收功率产生多少准粒子”相乘。',
 '响应度不是新的独立物理机制，而是把材料敏感度与准粒子 population gain 串联后的系统斜率。',
 '有了 $\\mathcal R_x$ 才能把测得的 frequency-noise ASD 折回 input-referred NEP，也能比较不同体积、材料和 lifetime 的器件。',
 '只针对给定 bias/temperature/loading 工作点附近的小信号导数。响应明显非线性时应使用局部标定曲线或完整 $x(P)$ 模型。'),
('detector-transfer', r'H_{\\rm det}(f)\n\\simeq',
 '最小动态模型把准粒子的一阶低通和谐振器振幅 ring-down 的一阶低通相乘。',
 '信号必须先改变准粒子 population，再通过有限响应速度的谐振器被读出；两道“惯性”中更慢的一个通常主导带宽。',
 '它帮助决定采样率、调制频率、脉冲恢复时间，并判断优化 $Q_r$ 或 $\\tau_{\\rm qp}$ 哪一个更有意义。',
 '假设两个过程近似线性、可串联且分别由单一时间常数描述。真实器件可能还有 thermal、phonon、electronics/filter 等额外 poles。'),
('nep-definition', r'\\mathrm{NEP}(f)\n=',
 'NEP 等于输出 observable 的噪声 ASD 除以该 observable 对输入功率的响应度，量纲因此是 $\\mathrm{W}/\\sqrt{Hz}$。',
 '它问的是：需要多大的等效输入功率涨落，才能在输出端产生与现有噪声一样大的变化。',
 'NEP 把不同读出坐标、不同 gain 的探测器投影回统一的输入功率尺度，因此可以公平比较灵敏度和建立系统 noise budget。',
 '噪声与响应度必须使用同一个 observable、同一个 Fourier-frequency convention 和同一个输入功率定义（absorbed/incident 必须说明）。'),
('photon-nep', r'\\mathrm{NEP}_{\\rm ph}^2\n\\simeq',
 '单模近似中 photon-noise 方差由与 $P$ 成正比的 shot term 和与 $P^2/\\Delta\\nu$ 成正比的 bunching/wave term 相加。',
 '光子到达本身是随机过程；热场还具有 Bose bunching，因此即使探测器完全无噪声，输入光也存在不可消除的统计涨落。',
 '它给出“photon-noise limited”必须面对的输入端基准，可与 detector/readout NEP 平方相加做预算。',
 '该形式对应简化单模、给定等效带宽的情形；多模、多偏振、非平坦 bandpass 或非热辐射源应对频率、模式和 occupation number 积分。'),
('gr-nep', r'\\mathrm{NEP}_{\\rm GR}\n\\simeq',
 'GR NEP 把随机准粒子数涨落折回输入功率，尺度随 $\\Delta/\\eta_{\\rm pb}$ 增大，并随 $\\sqrt{N_{\\rm qp}/\\tau_{\\rm qp}}$ 增大。',
 'generation 和 recombination 都是离散随机事件；即使平均准粒子数稳定，瞬时 population 仍会围绕平均值涨落。',
 '可用于判断器件是受光子统计、准粒子统计还是读出链限制，也能检查改变 lifetime 后“响应变大”和“GR noise 改变”之间的联动。',
 'one-sided/two-sided PSD、事件定义和 spin convention 会造成常见 factor-of-two 差异；与文献比较必须先对齐定义。'),
]
for key, anchor, ma,ph,en,va in items7:
    tex = insert_after_tex_display(tex, CH7T, anchor, tex_guide(ma,ph,en,va), key)

md7anchors = [
('qp-generation', r'\\Gamma_{\\rm qp}\\simeq \\frac{\\eta_{\\rm pb}P_{\\rm abs}}{\\Delta}'),
('qp-responsivity', r'\\delta N_{\\rm qp}\\simeq \\frac{\\eta_{\\rm pb}\\tau_{\\rm qp}}{\\Delta}\\delta P_{\\rm abs}'),
('frequency-responsivity', r'\\mathcal R_x=\\frac{dx}{dP_{\\rm abs}}'),
('detector-transfer', r'H_{\\rm qp}(f)=\\frac{1}{1+j2\\pi f\\tau_{\\rm qp}}'),
('nep-definition', r'\\mathrm{NEP}(f)=\\frac{\\sqrt{S_x(f)}}{|dx/dP_{\\rm abs}|}'),
('photon-nep', r'\\mathrm{NEP}_{\\rm ph}^2\\simeq'),
('gr-nep', r'\\mathrm{NEP}_{\\rm GR}\\simeq'),
]
lookup7 = {x[0]: x[2:] for x in items7}
for key, anchor in md7anchors:
    ma,ph,en,va = lookup7[key]
    md = insert_after_md_display(md, CH7M, anchor, md_guide(ma,ph,en,va), key)

TEX_PATH.write_text(tex, encoding='utf-8')
MD_PATH.write_text(md, encoding='utf-8')

# Gates: Step 4-A+B retained, Step 4-C adds 15 guides.
tex_markers = tex.count('% STEP4C:')
md_markers = md.count('<!-- STEP4C:')
if tex_markers != 15 or md_markers != 15:
    raise SystemExit(f'Step 4-C marker mismatch: tex={tex_markers}, md={md_markers}')
if tex.count('\\formulaexplain') < 35:
    raise SystemExit('Expected at least 34 formula guides plus macro definition after Step 4-C')

AUDIT = ROOT / 'STEP4C_FORMULA_AUDIT.md'
AUDIT.write_text(textwrap.dedent(f'''\
# v0.10 Step 4-C — Resonator/readout and NEP formula pedagogy audit

- New four-layer formula explanations: **15**
- Chapters covered: **6–7**
- Earlier Step 4-A/B guides retained: **19**
- Reader-facing formula guides after this pass: **34**
- TeX Step 4-C markers: **{tex_markers}**
- Markdown Step 4-C markers: **{md_markers}**
- Core equations replaced: **NO** — explanatory/validity layer only

## Chapter 6 relations covered

1. first-principles quality factor definition;
2. loaded/internal/coupling-Q rate sum;
3. linewidth–Q relation;
4. energy vs amplitude ring-down factor of two;
5. ideal hanger/notch complex $S_{{21}}$;
6. ideal IQ-circle equation;
7. fixed-tone small-signal linearization;
8. measured-$S_{{21}}$ model with gain/delay/asymmetry.

## Chapter 7 relations covered

1. optical quasiparticle generation rate;
2. steady-state $dN_{{qp}}/dP_{{abs}}$;
3. frequency responsivity chain rule;
4. detector dynamic transfer function;
5. input-referred NEP definition;
6. photon-noise NEP;
7. generation–recombination NEP.

Compilation/layout status is filled by the Step 4-C workflow.
'''), encoding='utf-8')

notes = NOTES_PATH.read_text(encoding='utf-8')
if '## Step 4-C' not in notes:
    notes += textwrap.dedent('''

## Step 4-C — Resonator/readout + responsivity/noise

- 第 6 章补齐 Q、linewidth、ring-down、hanger S21、IQ circle、fixed-tone 与真实 VNA 模型的四层解释；
- 明确 energy lifetime 与 amplitude lifetime 的 factor-of-two 来源；
- 强调 notch 是相干路径干涉，不等于“全部功率被吸收”；
- 第 7 章把 $P_{abs}$、quasiparticle gain、responsivity、dynamic response、PSD/ASD 与 NEP 串成同一条量纲闭合链；
- 对 photon noise 和 GR noise 明确写出模型边界与 convention 风险。
''')
    NOTES_PATH.write_text(notes, encoding='utf-8')

print('Step 4-C transform complete')
