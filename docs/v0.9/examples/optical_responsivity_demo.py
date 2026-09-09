import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34
kB = 1.380649e-23


def gap_weak_bcs(Tc):
    return 1.764 * kB * Tc


def nqp_steady(P_abs, eta_pb, tau_qp, Delta):
    return eta_pb * P_abs * tau_qp / Delta


def main():
    Tc = 1.2
    eta_pb = 0.57
    tau_qp = 300e-6
    Delta = gap_weak_bcs(Tc)
    # Educational calibration coefficient. Replace with MB calculation or measurement.
    dx_dNqp = -4.0e-13

    P = np.logspace(-14, -11, 250)
    N = nqp_steady(P, eta_pb, tau_qp, Delta)
    x = dx_dNqp * N
    R_x = dx_dNqp * eta_pb * tau_qp / Delta

    print(f"Delta = {Delta/1.602176634e-22:.4f} meV")
    print(f"dx/dP_abs = {R_x:.3e} 1/W")
    print(f"Nqp at 1 pW = {nqp_steady(1e-12, eta_pb, tau_qp, Delta):.3e}")
    print(f"fractional shift at 1 pW = {dx_dNqp*nqp_steady(1e-12, eta_pb, tau_qp, Delta):.3e}")
    print(f"qp 3-dB bandwidth = {1/(2*np.pi*tau_qp):.1f} Hz")

    plt.figure(figsize=(7, 4.5))
    plt.loglog(P, np.abs(x))
    plt.xlabel('absorbed optical power (W)')
    plt.ylabel('|delta f0 / f0|')
    plt.tight_layout()
    plt.savefig('optical_responsivity.png', dpi=180)

    f = np.logspace(-1, 5, 800)
    plt.figure(figsize=(7, 4.5))
    for tau in [30e-6, 300e-6, 3e-3]:
        H = 1/np.sqrt(1+(2*np.pi*f*tau)**2)
        plt.loglog(f, H, label=f'tau_qp={tau*1e6:.0f} us')
    plt.xlabel('Fourier frequency (Hz)')
    plt.ylabel('|H_qp(f)|')
    plt.legend()
    plt.tight_layout()
    plt.savefig('qp_bandwidth.png', dpi=180)


if __name__ == '__main__':
    main()
