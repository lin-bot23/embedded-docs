# ModelAttentionBackend

## Overview

The ModelAttentionBackend node allows you to select a dense attention implementation for a model. It patches the model with the chosen attention backend, which can be either PyTorch attention or Comfy Kitchen attention when available. This node is particularly useful when sparse attention is inactive or unsupported, ensuring that the model operates with the specified dense attention mechanism.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model` | The model that will be patched with the selected attention backend. | MODEL | Yes |  |
| `attention` | The dense attention backend to apply to the model. Available options are "pytorch attention" and "comfy kitchen attention" if the latter is available in the environment. | STRING | Yes | "pytorch attention"<br> "comfy kitchen attention" (when available) |

- The "comfy kitchen attention" option utilizes quantized INT8 attention and is supported only on Nvidia and AMD GPUs.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model` | The input model with the selected attention backend applied. | MODEL |

## Note

- If the selected attention backend is not available, the node will automatically fall back to using PyTorch attention and log a warning.
- The ModelAttentionBackend node is experimental and may be subject to changes in future releases.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/en.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
