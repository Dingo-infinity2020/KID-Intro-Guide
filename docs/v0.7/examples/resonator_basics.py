import numpy as np
import matplotlib.pyplot as plt


def s21_ideal(f, f0, Qi, Qc):
    Qr = 1.0 / (1.0 / Qi + 1.0 / Qc)
    x = (f - f0) / f0
    return 1.0 - (Qr / Qc) / (1.0 + 2j * Qr * x)


def main():
    f0 = 2.5e9
    Qi = 1.0e5
    Qc = 5.0e4
    Qr = 1.0 / (1.0 / Qi + 1.0 / Qc)
    linewidth = f0 / Qr
    f = np.linspace(f0 - 6 * linewidth, f0 + 6 * linewidth, 3000)
    s = s21_ideal(f, f0, Qi, Qc)

    f0_shifted = f0 - 10e3
    s_shifted = s21_ideal(f, f0_shifted, Qi, Qc)
    probe = f0
    s_dark = s21_ideal(np.array([probe]), f0, Qi, Qc)[0]
    s_light = s21_ideal(np.array([probe]), f0_shifted, Qi, Qc)[0]

    print(f"Qr = {Qr:.3f}")
    print(f"linewidth = {linewidth/1e3:.3f} kHz")
    print(f"tau_E = {Qr/(2*np.pi*f0)*1e6:.3f} us")
    print(f"tau_A = {Qr/(np.pi*f0)*1e6:.3f} us")
    print(f"fixed-tone dark  = {s_dark.real:+.6f} {s_dark.imag:+.6f}j")
    print(f"fixed-tone light = {s_light.real:+.6f} {s_light.imag:+.6f}j")
    print(f"delta S21        = {(s_light-s_dark).real:+.6f} {(s_light-s_dark).imag:+.6f}j")

    plt.figure(figsize=(7, 4.5))
    plt.plot((f-f0)/1e3, 20*np.log10(np.abs(s)), label='dark')
    plt.plot((f-f0)/1e3, 20*np.log10(np.abs(s_shifted)), label='f0 shifted -10 kHz')
    plt.xlabel('frequency offset from dark f0 (kHz)')
    plt.ylabel('|S21| (dB)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('resonator_notch.png', dpi=180)

    plt.figure(figsize=(5.5, 5.5))
    plt.plot(s.real, s.imag, label='dark sweep')
    plt.plot([s_dark.real, s_light.real], [s_dark.imag, s_light.imag], 'o-', label='fixed-tone response')
    plt.xlabel('Re(S21)')
    plt.ylabel('Im(S21)')
    plt.axis('equal')
    plt.legend()
    plt.tight_layout()
    plt.savefig('resonator_iq.png', dpi=180)


if __name__ == '__main__':
    main()
