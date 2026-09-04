# KID 入门讲义 v0.1

文件：

- `KID入门讲义_v0.1.tex`：主 LaTeX 源文件，推荐用于长期迭代。
- `KID入门讲义_v0.1.md`：Markdown 版本，适合快速编辑、讨论和版本对比。
- `KID入门讲义_v0.1.pdf`：排版后的阅读版。

## 编译

推荐 XeLaTeX：

```bash
xelatex KID入门讲义_v0.1.tex
xelatex KID入门讲义_v0.1.tex
```

或使用 latexmk：

```bash
latexmk -xelatex KID入门讲义_v0.1.tex
```

后续建议持续以 `v0.x` 方式迭代，并在每一章加入：

1. 物理图景；
2. 正式推导；
3. 数值练习；
4. Python 仿真；
5. 对应到当前 LEKID 结构的工程问题。
