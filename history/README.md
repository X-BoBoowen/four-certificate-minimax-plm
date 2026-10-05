# 历史版本与内部审查

当前发布稿仍为 [`paper/`](../paper/) 中的 **Master-R24 / C22**。C23 是随后修改并生成 PDF、但尚未完成整合核验的草稿；本目录收录它以保留修订历史，不替换当前发布稿。

| 归档 | 收录范围 | 文件数 |
| --- | --- | ---: |
| [`manuscripts/master-revisions.zip`](manuscripts/master-revisions.zip) | 26 个 Master 版本目录：`master`、`master_r1`–`master_r24`，以及 `master_r8_r1` | 907 |
| [`manuscripts/submission-candidates.zip`](manuscripts/submission-candidates.zip) | 26 个 ICLR 投稿候选目录：`iclr2027`、`iclr2027_candidate_c1`–`iclr2027_candidate_c23`，以及 `iclr2027_candidate_c1_r1`、`iclr2027_candidate_c6_r1`；另含 `architecture/` 下 14 份 Markdown 规划文件 | 936 |
| [`reviews/internal-reviews.zip`](reviews/internal-reviews.zip) | 本项目的内部审查、审计与修订综合记录，以及审稿返回记录 | 832 |

下载并解压对应 ZIP 后，按原版本目录查找 `main.pdf` 或 `main.tex`。稿件归档保留各版本原有的源码、PDF、图表与版本台账（如有），省略缓存、TeX 编译中间文件和仅含校验信息的文件。`architecture/` 规划文件用于理解投稿稿件的结构演变。

内部审查归档保留实质性讨论与修订记录，不包含第三方已发表论文全文、重复稿件载荷、逐页渲染图、失效的旧暂存 ZIP 或打包与校验清单。

审查 ZIP 内按以下目录查找：

| 目录 | 内容 |
| --- | --- |
| `review/` | PLM 四证书研究及相关前期下界研究的内部审查、模拟审稿意见 |
| `audit/` | 审查返回、问题裁定、修订综合、证明与引用检查；包含后期 C18–C22 审查记录 |
| `working-returns/` | 各轮审查工作目录中保存的完整返回意见、表单和问题清单 |
| `returned-packages/` | 从原有 C3/C4/C5 返回包及 C11 定向核查包中展开的文字记录；按轮次和审查角色分组 |
| `review-inputs/` | C11–C14 的审稿输入说明、修订差异和核查任务上下文，不作为已返回的审查结论 |
| `project-notes/` | PLM 研究的原始主张台账 `CLAIM_LEDGER.md` |

同一报告在工作目录与正式返回包中可能各有一份，保留各自归档位置，便于核对不同交付阶段。

历史稿件、规划与报告可能包含已被后续修订取代的结论。内部、模拟或 AI 辅助审查不代表正式会议决定，也不构成当前稿件的验证结果；归档不表示已重新编译或逐一完成所有历史版本的数学核验。阅读当前结果与适用条件，请以 [`paper/main.pdf`](../paper/main.pdf) 为准。
