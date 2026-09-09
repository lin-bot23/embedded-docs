# 模型稀疏注意力

## 概述

块稀疏注意力节点通过应用块稀疏注意力机制来修改 ComfyUI 模型。这种机制通过允许每个查询块只关注关键块的子集，而不是关注所有可能的块，从而减少计算负载，这对于长序列特别有益。

## 输入

| 参数 | 描述 | 数据类型 | 必需 | 范围 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要应用块稀疏注意力的 ComfyUI 模型。 | MODEL | 是 | N/A |
| `selection` | 用于确定要关注哪些关键块的方法。 | 动态组合 | 是 | 选项：sol-attn（自适应 tau）、sla（top-k）、vsa（视频稀疏注意力） |
| `tau` | sol-attn 方法的分数分布 sigmas 中的阈值。 | 浮点数 | 否 | 默认：1.3，最小：0.0，最大：4.0，步长：0.05 |
| `keep_percent` | sla 方法中每个查询块精确保留的关键块百分比。 | 浮点数 | 否 | 默认：10.0，最小：0.5，最大：95.0，步长：0.5 |
| `start_percent` | 稀疏注意力开始时的百分比点。 | 浮点数 | 否 | 默认：0.2，最小：0.0，最大：1.0，步长：0.01 |
| `end_percent` | 稀疏注意力结束时的百分比点。 | 浮点数 | 否 | 默认：1.0，最小：0.0，最大：1.0，步长：0.01 |
| `dense_blocks` | 表示始终运行密集注意力的 Transformer 块的字符串。 | STRING | 否 | 默认："" |
| `min_tokens` | 模型使用密集注意力的序列中令牌的最小数量。 | INT | 否 | 默认：12288，最小：0，最大：1 << 20，步长：512 |
| `extra_tokens` | 每个查询块在其所选块之外关注的额外最高得分令牌的数量。 | INT | 否 | 默认：256，最小：0，最大：256，步长：64 |
| `sink_conditioning` | 用于下沉条件化的 MiniMax-H3 条件行。 | 组合 | 否 | 选项：exact_kv、exact_kv_and_rows、off |
| `verbose` | 启用详细日志记录。 | 布尔值 | 否 | 默认：False |

### 注意事项

- `selection` 参数允许您在以下不同的方法之间选择用于选择关键块：
  - `sol-attn`：使用自适应阈值根据分数分布选择关键块。
  - `sla`：保留固定百分比的最高得分关键块。
  - `vsa`：应用视频稀疏注意力，它使用 3D 视频立方体贴图和一个学习到的粗略注意力分支。
- `dense_blocks` 参数可以用来指定始终使用密集注意力的 Transformer 块。
- `min_tokens` 参数设置用于密集注意力的序列中令牌的最小数量。
- `extra_tokens` 参数允许您指定每个查询块应关注的额外最高得分令牌的数量。
- `sink_conditioning` 参数仅适用于 MiniMax-H3 模型，并确定如何处理条件行。
- `verbose` 参数启用详细日志记录，这对于调试可能很有用。

## 输出

| 输出名称 | 描述 | 数据类型 |
|-------------|-------------|-----------|
| `模型` | 应用了块稀疏注意力的 ComfyUI 模型。 | MODEL |

### 约束和限制

- `sol-attn` 方法需要介于 0.0 和 4.0 之间的 `tau` 值。
- `sla` 方法需要介于 0.5 和 95.0 之间的 `keep_percent` 值。
- `vsa` 方法仅与 MiniMax-H3 模型兼容，并要求模型具有 `to_gate_compress` 层。
- `min_tokens` 参数必须是非负整数（设为 0 时所有注意力都保持稠密）。
- `extra_tokens` 参数必须是非负整数。
- `sink_conditioning` 选项仅适用于 MiniMax-H3 模型。

> 本文档由 AI 生成。如果您发现任何错误或有改进建议，欢迎贡献！ [在 GitHub 上编辑](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/zh.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
