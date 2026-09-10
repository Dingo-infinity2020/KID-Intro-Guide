from pathlib import Path
import textwrap

ROOT = Path("editorial/v0.10/step4")
TEX_PATH = ROOT / "KID入门讲义_v0.10_step4.tex"
MD_PATH = ROOT / "KID入门讲义_v0.10_step4.md"
AUDIT_PATH = ROOT / "STEP4B_FORMULA_AUDIT.md"

tex = TEX_PATH.read_text(encoding="utf-8")
md = MD_PATH.read_text(encoding="utf-8")


def insert_after_tex_display(text: str, scope: str, anchor: str, addition: str, sentinel: str) -> str:
    if sentinel in text:
        return text
    s = text.find(scope)
    if s < 0:
        raise SystemExit(f"Missing TeX scope: {scope}")
    a = text.find(anchor, s)
    if a < 0:
        raise SystemExit(f"Missing TeX anchor after {scope}: {anchor}")
    end = text.find(r"\]", a)
    if end < 0:
        raise SystemExit(f"Missing TeX display close after anchor: {anchor}")
    end += 2
    return text[:end] + "\n" + addition.rstrip() + "\n" + text[end:]


def insert_after_md_display(text: str, scope: str, anchor: str, addition: str, sentinel: str) -> str:
    if sentinel in text:
        return text
    s = text.find(scope)
    if s < 0:
        raise SystemExit(f"Missing Markdown scope: {scope}")
    a = text.find(anchor, s)
    if a < 0:
        raise SystemExit(f"Missing Markdown anchor after {scope}: {anchor}")
    end = text.find("$$", a)
    if end < 0:
        raise SystemExit(f"Missing Markdown display close after anchor: {anchor}")
    end += 2
    return text[:end] + "\n\n" + addition.rstrip() + "\n" + text[end:]


def insert_after_md_literal(text: str, scope: str, anchor: str, addition: str, sentinel: str) -> str:
    if sentinel in text:
        return text
    s = text.find(scope)
    if s < 0:
        raise SystemExit(f"Missing Markdown literal scope: {scope}")
    a = text.find(anchor, s)
    if a < 0:
        raise SystemExit(f"Missing Markdown literal anchor after {scope}: {anchor}")
    end = text.find("\n", a)
    if end < 0:
        end = len(text)
    return text[:end] + "\n\n" + addition.rstrip() + "\n" + text[end:]
def tex_guide(tag: str, math: str, physics: str, engineering: str, limits: str) -> str:
    return textwrap.dedent(rf"""
    % STEP4B:{tag}
    \formulaexplain
    {{{math}}}
    {{{physics}}}
    {{{engineering}}}
    {{{limits}}}
    """).strip()


def md_guide(tag: str, math: str, physics: str, engineering: str, limits: str) -> str:
    return textwrap.dedent(f"""
    <!-- STEP4B:{tag} -->
    > **公式怎么读：不要只背等号**  
    > **数学上：** {math}  
    > **物理上：** {physics}  
    > **工程上：** {engineering}  
    > **适用条件：** {limits}
    """).strip()


# 1) Weak-coupling zero-temperature gap
tex = insert_after_tex_display(
    tex,
    r"\section{BCS 能隙 $\Delta$：把材料与探测频率连接起来}",
    r"\boxed{\Delta_0\equiv\Delta(T=0)\approx1.764\,k_B T_c.}",
    tex_guide(
        "gap-tc",
        r"在弱耦合 BCS 极限，零温能隙 $\Delta_0$ 与临界温度 $T_c$ 成正比；比例系数约为 $1.764k_B$。",
        r"$T_c$ 和 $\Delta$ 都来自同一个配对能量尺度：升到 $T_c$ 附近时配对有序态消失，能隙也随之闭合。",
        r"只要先测到薄膜的 $T_c$，就能得到 $\Delta_0$ 的第一轮估计，并进一步估算 pair-breaking threshold $2\Delta_0/h$。这是材料筛选与 science band 匹配最便宜的一步。",
        r"$1.764$ 不是所有超导薄膜的普适常数。它对应常规、各向同性、弱耦合 $s$ 波 BCS 的零温极限；强耦合、非常规超导、薄膜无序和 proximity effect 都可能改变 $2\Delta_0/k_BT_c$。",
    ),
    "% STEP4B:gap-tc",
)

md = insert_after_md_display(
    md,
    "## 4.4 BCS 能隙",
    r"\boxed{\Delta_0\approx1.764k_BT_c.}",
    md_guide(
        "gap-tc",
        "在弱耦合 BCS 极限，零温能隙 $\\Delta_0$ 与临界温度 $T_c$ 成正比，比例系数约为 $1.764k_B$。",
        "$T_c$ 和 $\\Delta$ 来自同一个配对能量尺度；接近 $T_c$ 时配对有序态消失，能隙也随之闭合。",
        "测得薄膜 $T_c$ 后即可先估 $\\Delta_0$，再估 pair-breaking threshold $2\\Delta_0/h$，用于材料和 science band 的第一轮匹配。",
        "$1.764$ 对应常规、各向同性、弱耦合 $s$ 波 BCS 的零温极限；真实薄膜的强耦合、无序、proximity effect 等都可能改变该比值。",
    ),
    "<!-- STEP4B:gap-tc -->",
)

# 2) BCS quasiparticle dispersion
tex = insert_after_tex_display(
    tex,
    r"\section{准粒子：不是普通电子，而是超导体系的激发}",
    r"E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2}",
    tex_guide(
        "qp-dispersion",
        r"准粒子能量是 $\xi_{\mathbf{k}}$ 与 $\Delta$ 的平方和开根号，因此无论 $\xi$ 多接近零，都有 $E_{\mathbf{k}}\ge\Delta$。",
        r"超导转变不是把正常态能带简单平移，而是在费米面附近重构低能激发谱并打开能隙。准粒子因此是配对体系的激发，而不是一颗普通电子被单独“抬高”了能量。",
        r"这条色散关系解释了为什么热准粒子会被指数压低，也解释了 BCS density of states 和 Mattis--Bardeen 积分为什么在 $E\simeq\Delta$ 附近特别敏感。",
        r"这里使用理想、各向同性 $s$ 波 BCS 色散。真实薄膜中的 Dynes broadening、无序、proximity effect、非平衡分布或非常规配对会让理想能隙边缘被展宽或改变。",
    ),
    "% STEP4B:qp-dispersion",
)

md = insert_after_md_display(
    md,
    "## 4.5 准粒子",
    r"E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2}",
    md_guide(
        "qp-dispersion",
        "准粒子能量是 $\\xi_{\\mathbf{k}}$ 与 $\\Delta$ 的平方和开根号，所以总有 $E_{\\mathbf{k}}\\ge\\Delta$。",
        "超导态在费米面附近重构低能激发谱并打开能隙；准粒子是配对体系的激发，不是普通电子被简单抬高能量。",
        "它解释 thermal quasiparticle 的指数压低，也解释 BCS 态密度与 Mattis–Bardeen 为什么对 $E\\simeq\\Delta$ 附近最敏感。",
        "这是理想各向同性 $s$ 波 BCS 色散；无序、Dynes broadening、proximity effect、非平衡分布或非常规配对会改变理想图景。",
    ),
    "<!-- STEP4B:qp-dispersion -->",
)

# 3) Thermal quasiparticle density
tex = insert_after_tex_display(
    tex,
    r"\section{热准粒子：为什么降温如此有效？}",
    r"n_{\qp}^{\rm th}(T)",
    tex_guide(
        "thermal-qp",
        r"热平衡准粒子密度由一个缓慢变化的平方根前因子乘上 $\exp[-\Delta/(k_BT)]$；深低温时真正支配数量级的是指数项。",
        r"制造热准粒子必须付出跨越能隙的能量。当 $k_BT\ll\Delta$ 时，热浴中具备这份能量的涨落极少，因此准粒子人口被指数压低。",
        r"它把制冷指标从“多少 mK”改写成更有意义的 $T/T_c$ 或 $\Delta/k_BT$。可用它估算理想 dark quasiparticle baseline，并判断继续降温是否仍可能带来显著收益。",
        r"公式假设热平衡、理想 BCS 态密度且处于低温近似，并依赖 $N_0$ 的明确定义。真实 KID 往往存在 excess/non-equilibrium quasiparticles；此时继续降低 bath temperature 也可能看不到公式预测的指数下降。",
    ),
    "% STEP4B:thermal-qp",
)

md = insert_after_md_display(
    md,
    "## 4.6 热准粒子",
    r"n_{qp}^{\rm th}",
    md_guide(
        "thermal-qp",
        "热平衡准粒子密度由平方根前因子乘以 $\\exp[-\\Delta/(k_BT)]$；深低温时数量级主要由指数项决定。",
        "热激发要付出跨越能隙的能量；当 $k_BT\\ll\\Delta$，具有足够能量的热涨落极少，因此准粒子人口被指数压低。",
        "用 $T/T_c$ 或 $\\Delta/k_BT$ 而不是单独的 mK 数字判断制冷深度，并估算理想 dark-quasiparticle baseline。",
        "假设热平衡、理想 BCS 态密度和低温近似。excess/non-equilibrium quasiparticles 可能让真实器件在继续降温时出现饱和。",
    ),
    "<!-- STEP4B:thermal-qp -->",
)

# 4) Optical quasiparticle generation rate
tex = insert_after_tex_display(
    tex,
    r"\section{光子如何制造非平衡准粒子：从 pair breaking 到能量级联}",
    r"G_{\rm opt}",
    tex_guide(
        "optical-generation",
        r"准粒子产生率的量级等于“每秒真正吸收的能量”除以“形成低能准粒子所需的能量尺度 $\Delta$”，再乘能量转化效率 $\eta_{\rm pb}$。",
        r"一个高能光子首先产生高能激发，随后经电子--声子级联把能量重新分配；只有一部分吸收能量最终留在可被 KID 读出的低能准粒子池中。",
        r"它是从 optical simulation/光学标定得到的 $P_{\rm abs}$ 走向 responsivity 模型的入口：先把吸收功率转成 quasiparticle generation，再结合寿命得到稳态 $N_{\qp}$。",
        r"这是能量守恒的数量级表达，不是精确的微观级联公式。$\eta_{\rm pb}$ 依赖光子能量、材料、膜厚、声子逃逸/陷获等；且这里必须使用吸收功率 $P_{\rm abs}$，不能直接拿入射到系统前端的功率代入。",
    ),
    "% STEP4B:optical-generation",
)

md = insert_after_md_display(
    md,
    "## 4.7 光子如何制造非平衡准粒子",
    r"G_{\rm opt}",
    md_guide(
        "optical-generation",
        "产生率的量级是吸收功率除以准粒子能量尺度 $\\Delta$，再乘 pair-breaking efficiency $\\eta_{\\rm pb}$。",
        "高能光子经电子–声子级联重新分配能量，只有一部分最终进入可被读出的低能准粒子池。",
        "把 optical simulation/标定得到的 $P_{\\rm abs}$ 转成 quasiparticle generation，是从光学吸收到 responsivity 的入口。",
        "这是数量级能量守恒式；$\\eta_{\\rm pb}$ 随光子能量、材料、膜厚与声子逃逸/陷获而变，而且必须代入吸收功率而不是系统前端的 incident power。",
    ),
    "<!-- STEP4B:optical-generation -->",
)

# 5) Minimal generation-recombination rate equation
tex = insert_after_tex_display(
    tex,
    r"\section{recombination：为什么准粒子不会一直积累？}",
    r"\frac{dN_{\qp}}{dt}",
    tex_guide(
        "gr-rate-equation",
        r"$G$ 是源项，$\mathcal{R}N_{\qp}^2$ 是二次损失项；两者相等时得到稳态 $N_{\qp,\rm ss}\propto\sqrt{G}$。",
        r"两颗准粒子需要相遇才能复合回 Cooper-pair condensate，因此在最简均匀模型里复合事件率随准粒子人口的平方增长。人口越高，复合也越快，系统自然不会无限积累。",
        r"这个方程非常适合做第一版负载扫描、稳态估算和时域数值实验，也能直接解释为何 responsivity 与 optical loading 往往不是严格线性的。",
        r"这里把体积、材料常数和声子反馈压进一个有效 $\mathcal{R}$。真实器件可能需要 Rothwarf--Taylor 方程，并考虑 phonon trapping、traps、diffusion、空间非均匀和非平衡能量分布。",
    ),
    "% STEP4B:gr-rate-equation",
)

md = insert_after_md_display(
    md,
    "## 4.8 recombination",
    r"\frac{dN_{qp}}{dt}",
    md_guide(
        "gr-rate-equation",
        "$G$ 是源项，$\\mathcal{R}N_{qp}^2$ 是二次损失项；稳态时两者相等，因此 $N_{qp,\\rm ss}\\propto\\sqrt G$。",
        "两颗准粒子相遇后才能复合回凝聚态，所以最简均匀模型中的复合事件率随准粒子人口平方增加。",
        "可用于第一版负载扫描、稳态估算和时域数值实验，并解释 responsivity 对 optical loading 为什么常常不是严格线性。",
        "这是有效单池模型；真实器件可能需要 Rothwarf–Taylor 方程以及 phonon trapping、traps、diffusion、空间非均匀与非平衡分布。",
    ),
    "<!-- STEP4B:gr-rate-equation -->",
)

# 6) Quasiparticle lifetime
tex = insert_after_tex_display(
    tex,
    r"\section{准粒子寿命 $\tau_{\qp}$：把微观物理连接到探测器速度}",
    r"\delta N_{\qp}(t)",
    tex_guide(
        "qp-lifetime",
        r"小扰动按 $e^{-t/\tau_{\qp}}$ 衰减；经过一个 $\tau_{\qp}$，扰动剩下初值的 $1/e$。$\tau_{\qp}$ 因而直接定义恢复速度。",
        r"这是把非线性的 generation--recombination 动力学在某个稳态附近线性化后的结果：足够小的扰动看到一个局部的一阶恢复率。",
        r"从光脉冲、heater pulse 或加载阶跃的时间序列拟合 $\tau_{\qp}$，可以估计 detector bandwidth，并与 resonator ring-down time 比较究竟哪一环更慢。",
        r"单指数只在小扰动且存在一个主导时间常数时成立。强脉冲、空间扩散、多个准粒子池、声子陷获或读出链滤波都可能产生多指数或非指数恢复。",
    ),
    "% STEP4B:qp-lifetime",
)

md = insert_after_md_display(
    md,
    "## 4.9 准粒子寿命",
    r"\delta N_{qp}(t)=",
    md_guide(
        "qp-lifetime",
        "扰动按 $e^{-t/\\tau_{qp}}$ 衰减；一个 $\\tau_{qp}$ 后剩下初值的 $1/e$，因此它直接刻画恢复速度。",
        "它来自在某个稳态附近把 generation–recombination 动力学线性化；小扰动只看到局部的一阶恢复率。",
        "可从光脉冲、heater pulse 或加载阶跃拟合 $\\tau_{qp}$，再与 resonator ring-down time 比较哪一环限制 detector bandwidth。",
        "单指数只适用于小扰动和单主导时间常数；强脉冲、扩散、多准粒子池、phonon trapping 或读出滤波都可能导致多指数/非指数响应。",
    ),
    "<!-- STEP4B:qp-lifetime -->",
)

# 7) Complex conductivity
tex = insert_after_tex_display(
    tex,
    r"\chapter[复电导与 Mattis--Bardeen：把准粒子连接到 Lk 与 Qi]",
    r"\sigma(\omega,T)=\sigma_1(\omega,T)-i\sigma_2(\omega,T)",
    tex_guide(
        "complex-conductivity",
        r"$\sigma$ 是复数：$\sigma_1$ 与电场同相的部分承担净耗散，$\sigma_2$ 对应正交的反应性响应。",
        r"同一个超导电子系统既能真正吸收微波能量，也能把能量暂存在超流载流子的惯性中再返还给电磁场，所以一个实数电导不足以描述 GHz 响应。",
        r"这是从 BCS/准粒子物理进入器件仿真的接口。给定 $\sigma_1,\sigma_2$ 后，可以构造 surface impedance，再计算 $R_s$、$L_k$、$Q_i$ 和 resonance shift；也能明确 PEC 模型到底漏掉了什么。",
        r"虚部正负依赖采用 $e^{+i\omega t}$ 还是 $e^{-i\omega t}$ 的相量约定。还默认线性、局域交流响应；强驱动、非局域效应和明显非平衡分布需要更一般的电导模型。",
    ),
    "% STEP4B:complex-conductivity",
)

md = insert_after_md_display(
    md,
    "# 第 5 章：复电导与 Mattis",
    r"\sigma(\omega,T)=\sigma_1(\omega,T)-i\sigma_2(\omega,T)",
    md_guide(
        "complex-conductivity",
        "$\\sigma$ 是复数：$\\sigma_1$ 承担与电场同相的净耗散，$\\sigma_2$ 对应正交的反应性响应。",
        "同一个超导电子系统既会真正吸收微波能量，也会把能量暂存在超流载流子的惯性中再返还，因此实数电导不够描述 GHz 响应。",
        "由 $\\sigma_1,\\sigma_2$ 构造 surface impedance，再得到 $R_s$、$L_k$、$Q_i$ 与 resonance shift；这也是判断 PEC 模型漏掉哪层物理的接口。",
        "虚部正负取决于相量时间约定；这里还默认线性、局域交流响应，强驱动、非局域和明显非平衡情况需要更一般模型。",
    ),
    "<!-- STEP4B:complex-conductivity -->",
)

# 8) Average dissipated power density
tex = insert_after_tex_display(
    tex,
    r"\subsection{$\sigma_1$：为什么它代表损耗？}",
    r"\langle p\rangle=\frac12\sigma_1|E_0|^2",
    tex_guide(
        "sigma1-power",
        r"周期平均的耗散功率密度只含 $\sigma_1$，并与电场幅度平方成正比；$\sigma_2$ 不贡献净周期平均耗散。",
        r"与电场同相的电流分量在一个周期内持续从场中取走净能量，而相差四分之一周期的反应性分量只是先储能、后返还能量。",
        r"它给出 $\sigma_1\rightarrow R_s\rightarrow Q_i$ 这条损耗链最直接的物理依据，也提醒读出功率提高时内部耗散通常按场强平方迅速增长。",
        r"这里假设线性正弦稳态，并把 $E_0$ 当作峰值复幅度，因此出现 $1/2$。若使用 RMS 相量，前面的数值因子会变化；强非线性或空间非均匀时还需对体积/表面功率积分。",
    ),
    "% STEP4B:sigma1-power",
)

md = insert_after_md_literal(
    md,
    "# 第 5 章：复电导与 Mattis",
    r"\langle p\rangle=\tfrac12\sigma_1|E_0|^2",
    md_guide(
        "sigma1-power",
        "周期平均耗散功率密度只含 $\\sigma_1$，并与场幅平方成正比；$\\sigma_2$ 不贡献净周期平均耗散。",
        "同相电流分量持续从场中取走净能量；正交的反应性分量只是储能后再把能量返还。",
        "它是 $\\sigma_1\\rightarrow R_s\\rightarrow Q_i$ 的直接依据，也提醒高 readout field 会迅速增加内部耗散。",
        "假设线性正弦稳态，且 $E_0$ 是峰值复幅度，所以有 $1/2$；若采用 RMS 相量或存在强非线性/空间非均匀，表达式需相应调整。",
    ),
    "<!-- STEP4B:sigma1-power -->",
)

# 9) Mattis--Bardeen pair of integrals: insert after sigma2 integral
tex = insert_after_tex_display(
    tex,
    r"\section{Mattis--Bardeen 到底解决了什么问题？}",
    r"\frac{\sigma_2}{\sigma_n}",
    tex_guide(
        "mb-integrals",
        r"两个积分把允许的准粒子跃迁在能量轴上加权求和，输出归一化的 $\sigma_1/\sigma_n$ 与 $\sigma_2/\sigma_n$；$\Delta$、$f(E)$ 和 $\hbar\omega$ 分别控制可用态、占据和跃迁能量。",
        r"BCS density of states 与 coherence factor 决定每个能量区间对交流电流的贡献；已有准粒子可以吸收微波产生耗散，而凝聚态/虚跃迁共同产生强反应性响应。MB 做的正是把这些微观过程压缩成复电导。",
        r"数值计算 MB 后，可以从测得的 $T_c$、$R_{\Box,n}$ 和工作温度/频率构造超导 surface impedance，并预测温度扫中的 resonance shift 与 quasiparticle loss；反过来也可用低温 $S_{21}$ 数据约束材料参数。",
        r"这里展示的是常用的局域、BCS、平衡态且 $\hbar\omega<2\Delta$ 的形式。进入直接 pair-breaking 频段、强非平衡分布、明显 Dynes broadening、非局域/clean-limit 情况时，积分区间和响应模型都需要修改，不能把这两行公式当成万能黑箱。",
    ),
    "% STEP4B:mb-integrals",
)

md = insert_after_md_display(
    md,
    "## 2. Mattis–Bardeen 在做什么？",
    r"\frac{\sigma_2}{\sigma_n}",
    md_guide(
        "mb-integrals",
        "两个积分把允许的准粒子跃迁沿能量轴加权求和，输出 $\\sigma_1/\\sigma_n$ 和 $\\sigma_2/\\sigma_n$；$\\Delta$、$f(E)$、$\\hbar\\omega$ 分别控制可用态、占据和跃迁能量。",
        "BCS 态密度与 coherence factor 决定不同能量对交流电流的权重；MB 把微观跃迁统一压缩成可测的复电导。",
        "可由 $T_c$、$R_{\\Box,n}$、温度和读出频率构造 surface impedance，预测温度扫中的 resonance shift 与 quasiparticle loss，也可反向用低温 $S_{21}$ 约束材料参数。",
        "这里是常用局域、BCS、平衡态且 $\\hbar\\omega<2\\Delta$ 的形式；直接 pair breaking、强非平衡、Dynes broadening 或非局域/clean-limit 情况需要更一般模型。",
    ),
    "<!-- STEP4B:mb-integrals -->",
)

# 10) Thin-film sheet impedance
tex = insert_after_tex_display(
    tex,
    r"\section{从体电导 $\sigma$ 到实验真正“看到”的表面阻抗 $Z_s$}",
    r"Z_{\Box}",
    tex_guide(
        "sheet-impedance",
        r"薄膜每方块的复阻抗近似等于体复电导乘膜厚后的倒数，即 $Z_{\Box}\approx1/(t\sigma)$；实部和虚部分别给出 sheet resistance 与 sheet reactance。",
        r"当场和电流在膜厚方向近似均匀时，一个方块的横向几何尺寸会在电压/电流比中相消，只剩材料电导与厚度决定端口看到的复阻抗。",
        r"这是把 Mattis--Bardeen 输出喂给 Sonnet/CST/传输线模型的实用接口。相比把超导膜设成 PEC，surface-impedance 模型同时保留 kinetic inductance 与 conductor loss。",
        r"要求薄膜极限和近似均匀的厚度方向电流。膜厚与 penetration depth/skin depth 可比、非局域响应明显或多层 proximity structure 时，应使用更一般的有限厚度表面阻抗，而不是机械使用 $1/(t\sigma)$。",
    ),
    "% STEP4B:sheet-impedance",
)

md = insert_after_md_display(
    md,
    "## 4. 从 $\\sigma$ 到表面阻抗",
    r"Z_{\Box}",
    md_guide(
        "sheet-impedance",
        "薄膜每方块复阻抗近似为体复电导乘膜厚后的倒数：$Z_{\\Box}\\approx1/(t\\sigma)$。",
        "膜厚方向的场和电流近似均匀时，一个方块的横向几何尺度在电压/电流比中相消，剩下材料电导和厚度。",
        "把 Mattis–Bardeen 的 $\\sigma$ 转成 Sonnet/CST 或传输线模型可用的 surface impedance，同时保留 kinetic inductance 和 conductor loss。",
        "只适用于薄膜、局域且厚度方向近似均匀的情况；有限厚度、多层 proximity structure 或非局域响应应使用更一般的表面阻抗模型。",
    ),
    "<!-- STEP4B:sheet-impedance -->",
)

# 11) Kinetic inductance from sigma2
tex = insert_after_tex_display(
    tex,
    r"\section{终于闭环：从 $\sigma_2$ 再推一次 sheet kinetic inductance}",
    r"L_{k,\Box}",
    tex_guide(
        "lk-from-sigma2",
        r"在 $\sigma_2\gg\sigma_1$ 的薄膜极限，sheet reactance 近似为 $1/(t\sigma_2)$；再除以角频率 $\omega$ 就得到每方块动能电感。",
        r"$\sigma_2$ 越大，超流越容易建立反应性电流，因此同样电流需要的感性电压越小，等效 $L_k$ 也越小；准粒子增加使 $\sigma_2$ 下降，于是 $L_k$ 上升。",
        r"这条式子把 MB 的材料输出直接接回 GHz resonator：计算 $\sigma_2(T,P)$ 后即可更新 $L_{k,\Box}$、$\alpha$ 和 $f_0$，形成材料--器件闭环。",
        r"依赖薄膜、线性、局域响应以及 $\sigma_2\gg\sigma_1$。如果损耗不再很小，应从完整复数 $Z_{\Box}=1/(t\sigma)$ 提取 reactance，而不是只保留 $\sigma_2$。",
    ),
    "% STEP4B:lk-from-sigma2",
)

md = insert_after_md_display(
    md,
    "## 5. 从 $\\sigma_2$ 到 kinetic inductance",
    r"L_{k,\Box}",
    md_guide(
        "lk-from-sigma2",
        "在 $\\sigma_2\\gg\\sigma_1$ 的薄膜极限，sheet reactance 约为 $1/(t\\sigma_2)$；除以 $\\omega$ 就得到每方块动能电感。",
        "$\\sigma_2$ 越大，超流越容易建立反应性电流，因此等效 $L_k$ 越小；准粒子增加使 $\\sigma_2$ 下降，于是 $L_k$ 上升。",
        "由 MB 计算 $\\sigma_2(T,P)$ 后可直接更新 $L_{k,\\Box}$、$\\alpha$ 和 $f_0$，把材料模型接回 GHz resonator。",
        "依赖薄膜、线性、局域响应与 $\\sigma_2\\gg\\sigma_1$；损耗较大时应从完整 $Z_{\\Box}=1/(t\\sigma)$ 提取 reactance。",
    ),
    "<!-- STEP4B:lk-from-sigma2 -->",
)

# 12) Quasiparticle contribution to internal Q
tex = insert_after_tex_display(
    tex,
    r"\section{从 $\sigma_1$ 到 $Q_i$：损耗支路也闭环}",
    r"\frac{1}{Q_{i,\qp}}",
    tex_guide(
        "qi-from-sigma",
        r"准粒子导体损耗对内部品质因数的贡献近似为 $Q_{i,\qp}^{-1}\approx\alpha\,\sigma_1/\sigma_2$：损耗/储能比再乘 kinetic-inductance participation。",
        r"$\sigma_1$ 决定每周期真正耗掉多少能量，$\sigma_2$ 决定反应性储能尺度；而只有总储能中与超导动能相关的那部分以权重 $\alpha$ 强烈感受到这类准粒子损耗。",
        r"它允许把材料层的 $\sigma_1/\sigma_2$ 与器件层的 $Q_i$ 对接：做温度扫或光学加载扫时，可预测 quasiparticle loss 的方向和数量级，并与 TLS、radiation、vortex 等其他损耗项区分。",
        r"这是简化的薄膜/lumped 近似，默认 quasiparticle conductor loss 可单独定义且几何因子接近这里的形式。真实 $Q_i^{-1}$ 是多种损耗之和；复杂电流分布、有限厚度和界面效应可能引入额外 participation/geometric factor。",
    ),
    "% STEP4B:qi-from-sigma",
)

md = insert_after_md_display(
    md,
    "## 6. 从 $\\sigma_1$ 到 $Q_i$",
    r"\frac{1}{Q_{i,qp}}",
    md_guide(
        "qi-from-sigma",
        "准粒子导体损耗近似满足 $Q_{i,qp}^{-1}\\approx\\alpha\\,\\sigma_1/\\sigma_2$：损耗/储能比再乘 kinetic-inductance participation。",
        "$\\sigma_1$ 决定每周期耗掉多少能量，$\\sigma_2$ 决定反应性储能；$\\alpha$ 则表示总储能中有多少权重真正落在对超导态敏感的动能电感上。",
        "把材料层的 $\\sigma_1/\\sigma_2$ 与器件层的 $Q_i$ 对接，可在温度扫/光学加载扫中估算 quasiparticle loss，并与 TLS、radiation、vortex 等损耗区分。",
        "这是简化薄膜/lumped 近似；真实 $Q_i^{-1}$ 是多种损耗之和，复杂电流分布、有限厚度与界面还可能引入额外 participation/geometric factor。",
    ),
    "<!-- STEP4B:qi-from-sigma -->",
)

TEX_PATH.write_text(tex, encoding="utf-8")
MD_PATH.write_text(md, encoding="utf-8")

# Semantic gates: Step 4-A had 7 invocations + one macro definition. Step 4-B adds 12.
step4b_tex_tags = tex.count("% STEP4B:")
step4b_md_tags = md.count("<!-- STEP4B:")
if step4b_tex_tags != 12:
    raise SystemExit(f"Unexpected Step 4-B TeX tag count: {step4b_tex_tags}")
if step4b_md_tags != 12:
    raise SystemExit(f"Unexpected Step 4-B Markdown tag count: {step4b_md_tags}")
if tex.count(r"\formulaexplain") != 20:  # macro definition + 7 A + 12 B
    raise SystemExit("Unexpected total TeX formulaexplain count: " + str(tex.count(r"\formulaexplain")))
if md.count("**公式怎么读：不要只背等号**") != 19:
    raise SystemExit("Unexpected total Markdown formula-guide count: " + str(md.count("**公式怎么读：不要只背等号**")))

required = [
    r"\Delta_0\equiv\Delta(T=0)\approx1.764\,k_B T_c",
    r"E_{\mathbf{k}}=\sqrt{\xi_{\mathbf{k}}^2+\Delta^2}",
    r"n_{\qp}^{\rm th}(T)",
    r"G_{\rm opt}",
    r"\frac{dN_{\qp}}{dt}",
    r"\delta N_{\qp}(t)",
    r"\sigma(\omega,T)=\sigma_1(\omega,T)-i\sigma_2(\omega,T)",
    r"\langle p\rangle=\frac12\sigma_1|E_0|^2",
    r"\frac{\sigma_2}{\sigma_n}",
    r"Z_{\Box}",
    r"L_{k,\Box}",
    r"\frac{1}{Q_{i,\qp}}",
]
missing = [x for x in required if x not in tex]
if missing:
    raise SystemExit("Core Step 4-B relation unexpectedly missing: " + "; ".join(missing))

AUDIT_PATH.write_text(textwrap.dedent("""
# v0.10 Step 4-B — Superconducting response formula pedagogy audit

- New four-layer formula explanations: **12**
- Chapters covered: **4–5**
- Step 4-A formula guides retained: **7**
- Total formula-guide invocations in TeX: **19** (plus one macro definition)
- Total Markdown formula-guide blocks: **19**
- Core equations preserved: **PASS**
- Physics scope changed: **NO** — explanatory/validity layer only

## Relations covered in Step 4-B

1. weak-coupling $\\Delta_0$–$T_c$ relation;
2. BCS quasiparticle dispersion;
3. equilibrium thermal quasiparticle density;
4. optical quasiparticle generation rate;
5. minimal generation–recombination rate equation;
6. quasiparticle relaxation lifetime;
7. superconducting complex conductivity;
8. average dissipated microwave power density;
9. Mattis–Bardeen conductivity integrals as a model interface;
10. thin-film sheet impedance;
11. kinetic inductance from $\\sigma_2$;
12. quasiparticle contribution to internal quality factor.

Compilation/layout status is filled by the Step 4-B workflow.
""").lstrip(), encoding="utf-8")

print("Step 4-B superconducting-response formula pedagogy transform complete")
