# KID 入门讲义 v0.2 - 源文件说明

本目录是 v0.2 的增量交付，不是完整工程压缩包。

## 文件

- `KID入门讲义_v0.2.tex`：PDF 的权威排版源文件；流程图全部使用 TikZ，可直接编辑。
- `KID入门讲义_v0.2.md`：便于阅读、继续改写和交给其他 Agent 的 Markdown 内容源；关键流程图使用 Mermaid。
- `KID入门讲义_v0.2.pdf`：XeLaTeX 编译后的阅读版。
- `CHANGELOG.md`：相对 v0.1 的修改摘要。

## v0.2 流程图语义规范

1. 实线箭头：因果关系或真实信号流。
2. 虚线箭头：设计参数/材料参数对物理量的影响。
3. 无箭头连线或分组框：结构组成、互易耦合，不暗示单向因果。
4. 箭头统一从显式节点锚点出发/进入，避免箭头穿过方框或文字。

## 编译

需要 XeLaTeX 与常见 TeX Live 宏包：

```bash
xelatex KID入门讲义_v0.2.tex
xelatex KID入门讲义_v0.2.tex
```

第二次编译用于刷新目录和交叉引用。

## 版本定位

v0.2 在 v0.1 的“从光子到 S21”总图景基础上，新增完整的 kinetic inductance（动能电感）章节：

`载流子惯性 -> Lk -> London penetration depth -> sheet inductance -> alpha -> resonance frequency response -> Sonnet/CST 建模含义`。
