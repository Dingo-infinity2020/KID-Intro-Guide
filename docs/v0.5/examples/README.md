# v0.5 Python examples

## 1. `resonator_basics.py`

生成理想 hanger/notch resonator 的幅频曲线、IQ circle，并演示 `f0` 发生 -10 kHz 位移时固定 probe tone 的复数 `ΔS21`。

依赖：`numpy`, `matplotlib`。

## 2. `resonator_fit_demo.py`

生成包含 complex gain、cable delay、有效 asymmetry 和复高斯噪声的 synthetic VNA 数据，再用 `scipy.optimize.least_squares` 拟合回参数。

依赖：`numpy`, `scipy`。

> 这是教学模型。真实实验可进一步加入频率相关 baseline、complex coupling quality factor、邻近模态、功率非线性与参数不确定度估计。
