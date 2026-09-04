# KID 入门讲义 v0.3

本目录保存 **KID Intro Guide v0.3** 的完整交付文件。

## 本版本主题

v0.3 在 v0.2 的“从光子到 S21”与“动能电感”基础上，新增：

- 常规超导体的最小 BCS 物理图景；
- normal state / superconducting state 的低能激发差异；
- Cooper pair 的正确直觉；
- `Δ0 ≈ 1.764 kB Tc` 与 pair-breaking threshold；
- quasiparticle 激发谱与 BCS density of states；
- thermal quasiparticle density `nqp(T)` 的指数压低；
- optical pair breaking 与能量级联；
- generation–recombination 的最小速率模型；
- quasiparticle lifetime `τqp` 与 detector bandwidth；
- `T/Tc` 与 `hν/2Δ` 两条材料选择轴；
- 对当前 150 GHz 双偏振 LEKID 的直接材料映射。

## 文件

- `KID入门讲义_v0.3.pdf`：阅读版；
- `KID入门讲义_v0.3.tex`：权威排版源；
- `KID入门讲义_v0.3.md`：内容协作源；
- `CHANGELOG.md`：本版本变更记录。

## 编译

从仓库根目录执行：

```bash
make pdf
```

或：

```bash
./scripts/build_latest.sh
```

当前 `latest` 指向 v0.3。
