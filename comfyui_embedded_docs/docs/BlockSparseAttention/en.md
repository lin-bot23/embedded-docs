# Block Sparse Attention

## Overview

The Block Sparse Attention node modifies a ComfyUI model to apply a block-sparse attention mechanism. This mechanism reduces the computational load by allowing each query block to focus on a subset of key blocks, rather than attending to all possible blocks, which is particularly beneficial for long sequences.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The ComfyUI model to apply the block-sparse attention to. | MODEL | Yes | N/A |
| `selection` | The method used to determine which key blocks to attend to. | DYNAMIC_COMBO | Yes | Options: sol-attn (adaptive tau), sla (top-k), vsa (Video Sparse Attention) |
| `tau` | The threshold in score-distribution sigmas for the sol-attn method. | FLOAT | No | default: 1.3, min: 0.0, max: 4.0, step: 0.05 |
| `keep_percent` | The percentage of key blocks each query block keeps exactly for the sla method. | FLOAT | No | default: 10.0, min: 0.5, max: 95.0, step: 0.5 |
| `start_percent` | The percentage point when sparse attention begins. | FLOAT | No | default: 0.2, min: 0.0, max: 1.0, step: 0.01 |
| `end_percent` | The percentage point when sparse attention ends. | FLOAT | No | default: 1.0, min: 0.0, max: 1.0, step: 0.01 |
| `dense_blocks` | A string representing the transformer blocks that always run dense attention. | STRING | No | default: "" |
| `min_tokens` | The minimum number of tokens in a sequence for which the model uses dense attention. | INT | No | default: 12288, min: 0, max: 1 << 20, step: 512 |
| `extra_tokens` | The number of extra top-scoring tokens each query block attends beyond its selected blocks. | INT | No | default: 256, min: 0, max: 256, step: 64 |
| `sink_conditioning` | The MiniMax-H3 conditioning rows to use for sink conditioning. | COMBO | No | Options: exact_kv, exact_kv_and_rows, off |
| `verbose` | Enables verbose logging. | BOOLEAN | No | default: False |

### Notes

- The `selection` parameter allows you to choose between different methods for selecting key blocks:
  - `sol-attn`: Uses an adaptive threshold to select key blocks based on the score distribution.
  - `sla`: Keeps a fixed percentage of the highest-scoring key blocks.
  - `vsa`: Applies Video Sparse Attention, which uses 3D video-cube tiling and a learned coarse attention branch.
- The `dense_blocks` parameter can be used to specify transformer blocks that should always use dense attention.
- The `min_tokens` parameter sets the minimum number of tokens in a sequence for which dense attention is used.
- The `extra_tokens` parameter allows you to specify the number of additional top-scoring tokens that each query block should attend to.
- The `sink_conditioning` parameter is relevant only for MiniMax-H3 models and determines how the conditioning rows are handled.
- The `verbose` parameter enables detailed logging, which can be useful for debugging.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model` | The ComfyUI model with block-sparse attention applied. | MODEL |

### Constraints and Limitations

- The `sol-attn` method requires a `tau` value between 0.0 and 4.0.
- The `sla` method requires a `keep_percent` value between 0.5 and 95.0.
- The `vsa` method is only compatible with MiniMax-H3 models and requires the model to have a `to_gate_compress` layer.
- The `min_tokens` parameter must be a non-negative integer (setting it to 0 keeps attention fully dense).
- The `extra_tokens` parameter must be a non-negative integer.
- The `sink_conditioning` options are only applicable to MiniMax-H3 models.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/en.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
