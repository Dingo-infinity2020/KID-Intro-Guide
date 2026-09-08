import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34
kB = 1.380649e-23


def gap_weak_bcs(Tc):
    return 1.764 * kB * Tc


def photon_nep(P_abs, nu, optical_bw):
    return np.sqrt(2*h*nu*P_abs + 2*P_abs**2/optical_bw)


def gr_nep(P_abs, Delta, eta_pb):
    # Common low-frequency result under the one-sided PSD convention used in the guide.
    return np.sqrt(4*Delta*P_abs/eta_pb)


def main():
    nu = 150e9
    optical_bw = 30e9
    Tc = 1.2
    eta_pb = 0.57
    Delta = gap_weak_bcs(Tc)

    P = np.logspace(-14, -10, 300)
    nep_ph = photon_nep(P, nu, optical_bw)
    nep_gr = gr_nep(P, Delta, eta_pb)
    nep_quad = np.sqrt(nep_ph**2 + nep_gr**2)

    p0 = 1e-12
    print(f"At P_abs = {p0:.1e} W")
    print(f"photon NEP = {photon_nep(p0, nu, optical_bw):.3e} W/sqrt(Hz)")
    print(f"GR NEP     = {gr_nep(p0, Delta, eta_pb):.3e} W/sqrt(Hz)")

    measured_sqrt_Sx = 1e-9  # 1/sqrt(Hz)
    responsivity_x = 1e6     # 1/W
    print(f"Example measured NEP = {measured_sqrt_Sx/responsivity_x:.3e} W/sqrt(Hz)")

    plt.figure(figsize=(7, 4.5))
    plt.loglog(P, nep_ph, label='photon')
    plt.loglog(P, nep_gr, label='GR')
    plt.loglog(P, nep_quad, label='quadrature sum')
    plt.xlabel('absorbed optical power (W)')
    plt.ylabel('NEP (W / sqrt(Hz))')
    plt.legend()
    plt.tight_layout()
    plt.savefig('noise_budget.png', dpi=180)


if __name__ == '__main__':
    main()
