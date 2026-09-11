# ModelSamplingSD3

This node applies Stable Diffusion 3 style sampling settings to a model. It makes a copy of the model and replaces its sampling method with a flow-based sampling configuration that uses the given `shift` value, which controls how the sampling distribution is shaped.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | The input model to apply SD3 sampling parameters to | MODEL | Yes | - |
| `shift` | Controls the sampling shift parameter (default: 3.0) | FLOAT | Yes | 0.0 - 100.0 (step: 0.01) |

Note: The `shift` value is applied together with a fixed internal multiplier of 1000. If the original model has a noise scale setting, that value is carried over to the modified model. The original model is not changed; a cloned and patched copy is returned.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The modified model with SD3 sampling parameters applied | MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/en.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
