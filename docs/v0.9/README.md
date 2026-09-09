# KID 入门讲义 v0.9

**主题：150 GHz 双偏振 LEKID 项目验证矩阵——从理论预测到可复现证据**

v0.9 保留 v0.1–v0.8 的完整理论与复习内容，并新增项目级 validation / traceability 章节。核心目标是把现有知识逐项映射到真实科研流程：geometry → Sonnet GHz → CST/HFSS optical → convergence/material/tolerance → fabrication → cryogenic VNA → optical/polarization calibration → final claim。

## 文件
- `KID入门讲义_v0.9.pdf`：正式阅读版（121 页）
- `KID入门讲义_v0.9.tex`：LaTeX 权威排版源
- `KID入门讲义_v0.9.md`：Markdown 内容源
- `CHANGELOG.md`：本版本修改记录
- `examples/`：完整继承前版示例，并新增 power closure、B0/B1 FOM、tolerance budget
- `templates/`：run manifest、validation matrix、pre-fabrication checklist

核心方法：`Claim + Observable + Method + Acceptance Rule + Evidence = 可审计验证`。

所有建议阈值和示例数据都明确属于项目规则或教学示例，不作为普适物理常数。
