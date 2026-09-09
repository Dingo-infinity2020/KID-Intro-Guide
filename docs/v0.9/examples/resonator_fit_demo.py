import numpy as np
from scipy.optimize import least_squares


def s21_model(f, f0, Qr, Qc, phi, amp, phase, tau):
    x = (f - f0) / f0
    resonator = 1.0 - (Qr / Qc) * np.exp(1j * phi) / (1.0 + 2j * Qr * x)
    gain = amp * np.exp(1j * phase) * np.exp(-2j * np.pi * (f - f.mean()) * tau)
    return gain * resonator


def pack_residual(p, f, data):
    f0, logQr, logQc, phi, logamp, phase, tau = p
    model = s21_model(f, f0, np.exp(logQr), np.exp(logQc), phi, np.exp(logamp), phase, tau)
    r = model - data
    return np.concatenate([r.real, r.imag])


def main():
    rng = np.random.default_rng(1234)
    truth = dict(f0=2.5e9, Qr=3.3e4, Qc=5.0e4, phi=0.08, amp=0.93, phase=0.35, tau=18e-9)
    span = 500e3
    f = np.linspace(truth['f0']-span, truth['f0']+span, 2501)
    clean = s21_model(f, **truth)
    sigma = 2.0e-3
    data = clean + sigma*(rng.normal(size=f.size)+1j*rng.normal(size=f.size))

    p0 = np.array([2.50003e9, np.log(3.0e4), np.log(5.5e4), 0.0, np.log(1.0), 0.0, 10e-9])
    fit = least_squares(pack_residual, p0, args=(f, data), max_nfev=4000)
    f0, logQr, logQc, phi, logamp, phase, tau = fit.x
    Qr, Qc, amp = np.exp(logQr), np.exp(logQc), np.exp(logamp)
    Qi = 1.0 / (1.0/Qr - 1.0/Qc)

    print('Recovered parameters')
    print(f'f0  = {f0:.3f} Hz')
    print(f'Qr  = {Qr:.2f}')
    print(f'Qc  = {Qc:.2f}')
    print(f'Qi  = {Qi:.2f}')
    print(f'phi = {phi:.5f} rad')
    print(f'amp = {amp:.5f}')
    print(f'phase = {phase:.5f} rad')
    print(f'tau = {tau*1e9:.3f} ns')
    print(f'RMS complex residual = {np.sqrt(np.mean(np.abs(s21_model(f, f0, Qr, Qc, phi, amp, phase, tau)-data)**2)):.4e}')


if __name__ == '__main__':
    main()
