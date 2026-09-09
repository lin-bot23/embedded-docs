# LTXVFreezeLatent

```markdown
# LTXV Freeze Latent

## Overview

The LTXV Freeze Latent node is designed to set the noise_mask to 0 for a given latent, ensuring that the latent remains clean during sampling. It is particularly useful for freezing audio or video latents to prevent denoising, which can be applied before concatenating audio and video for cross-attention or for any latent that should not be denoised.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `latent` | Video or audio latent to freeze. Audio is 4D; video is 5D. | LATENT | Yes | N/A |
| `samples` | The tensor containing the latent samples. | TENSOR | Yes | Audio: 4D (batch, channels, frames, samples); Video: 5D (batch, channels, height, width, frames) |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `latent` | The latent with a noise_mask set to 0, ensuring it remains clean during sampling. | LATENT |

## Notes

- The `samples` tensor must be a plain tensor and not a concatenated audio-video latent. If it is a concatenated latent, it should be split using the Separate AV Latent node first.
- The output `latent` will have a noise_mask of zeros, which prevents denoising for the specified latent.
- The node supports both audio and video latents, with different tensor shapes for each.
- If the shape of the `samples` tensor does not match the expected audio or video shape, a ValueError will be raised.
```

**Note:** The actual implementation may have additional constraints or behaviors not explicitly documented here. Always refer to the latest source code for the most accurate information.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/en.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
