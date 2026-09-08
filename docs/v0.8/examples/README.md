# v0.8 examples

v0.8 新增两个复习用脚本：

- `capstone_chain_demo.py`：复现综合闭环题中的 150 GHz photon、Al pair-breaking threshold、Qr/linewidth、dark/light fixed-tone S21 数值。
- `iq_circle_workbook.py`：数值验证理想 hanger resonator 的 IQ-circle 方程，并检查 `S21(f0)=1-d`。

运行：

```bash
python capstone_chain_demo.py
python iq_circle_workbook.py
```

v0.7 的已有示例也继续复制到 v0.8 目录中，以保持版本自包含。
