# LTXVAddLatentGuide

```markdown
# LTXV Add Latent Guide

## Overview

The LTXV Add Latent Guide node pins an already-encoded latent as a guide, allowing for the use of a guide that comes out of an earlier stage rather than an image. This node avoids the VAE decode/encode round trip, and it can dilate a spatially smaller guide onto a sparse grid to cover the target canvas.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positive conditioning input. | CONDITIONING | Yes | N/A |
| `negative` | Negative conditioning input. | CONDITIONING | Yes | N/A |
| `vae` | The VAE model to use. | MODEL | Yes | N/A |
| `latent` | Target video latent the guide is pinned onto. | LATENT | Yes | N/A |
| `guiding_latent` | Guide latent. Its spatial size must divide the target's by the same whole number on both axes; equal size pins it as-is, half size is treated as an x2 IC-LoRA reference. | LATENT | Yes | N/A |
| `latent_idx` | Latent frame index to start the guide at, counted in latent frames rather than pixel frames. Negative values place the guide on frames before the start of the latent, not counted back from its end. | INT | Yes | -9999 to 9999 |
| `strength` | Capped at 1.0. A dilated guide marks its padding positions with a negative denoise mask so the model drops them; above 1.0 the kept positions would go negative too and the whole guide would be dropped. Amplify beyond 1.0 with attention_mask instead. | FLOAT | Yes | 0.0 to 1.0, step 0.01 |
| `attention_mask` | Optional pixel-space spatial mask. Controls per-region conditioning influence via self-attention, multiplied by strength. | MASK | No | N/A |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | Positive conditioning output. | CONDITIONING |
| `negative` | Negative conditioning output. | CONDITIONING |
| `latent` | Latent output with the guide applied. | LATENT |

## Notes

- The `guiding_latent` spatial size must divide the `latent` size by the same whole number on both axes.
- The `latent_idx` parameter allows for precise placement of the guide within the latent frames.
- The `strength` parameter controls the intensity of the guide, with values above 1.0 requiring the use of `attention_mask` to avoid negative positions.
- The `attention_mask` parameter is optional but can be used to fine-tune the influence of the guide in specific regions of the image.
```

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/en.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
