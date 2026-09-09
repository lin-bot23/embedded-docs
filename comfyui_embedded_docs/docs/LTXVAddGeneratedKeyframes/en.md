# LTXVAddGeneratedKeyframes

## Overview

The LTXV Add Generated Keyframes node appends detailing keyframes to a video latent. Each keyframe represents one latent frame of tokens spanning a single pixel frame, which are denoised with the video and not part of the decoded output. Placement is determined by the interval_frames parameter, which specifies the pixel-frame stride for auto placement.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `positive` | Positive conditioning the keyframes are attached to. | CONDITIONING | Yes | N/A |
| `negative` | Negative conditioning the keyframes are attached to. | CONDITIONING | Yes | N/A |
| `vae` | Only used to read the latent scale factors. | VAE | Yes | N/A |
| `latent` | Plain 5D video latent to generate keyframes alongside. Add them before Concat AV Latent. | LATENT | Yes | N/A |
| `interval_frames` | Pixel-frame stride for auto placement. Default 24 is about one keyframe per second at 24 fps. Occupied pixels are skipped. Ignored when frame_indices is set. | INT | No | 1-1024 |
| `keyframes` | Optional content to initialize the new keyframes with. Connect keyframes from an earlier Separate (same spatial size), or a plain video latent to copy the nearest frame at each new slot (e.g. after temporal upscale). These are still denoised, not pinned as guides. Recorded indices on a keyframes latent are ignored unless frame_indices is set. Only has an effect when sampling starts below sigma 1. | LATENT | No | N/A |
| `frame_indices` | Optional pixel-frame indices. Leave empty to place from interval_frames on the current canvas. When set, this list is the placement (connected keyframes are matched in order). The last frame is allowed; frame 0 is not (it is already a standalone token). | STRING | No | N/A |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `positive` | Positive conditioning with generated-keyframe attention attached. | CONDITIONING |
| `negative` | Negative conditioning with generated-keyframe attention attached. | CONDITIONING |
| `latent` | Video latent with generated keyframes appended on T. | LATENT |

## Notes

- The `interval_frames` parameter determines the spacing of keyframes in the video. A higher value results in fewer keyframes and a lower frame rate.
- The `keyframes` input allows you to initialize the new keyframes with existing keyframes or a video latent. If provided, these keyframes will be denoised and appended to the video latent.
- The `frame_indices` parameter allows you to specify the exact pixel-frame indices where keyframes should be placed. If provided, the `interval_frames` parameter is ignored.
- The `positive` and `negative` outputs contain the conditioning with generated-keyframe attention attached, which can be used for further processing or analysis.
- The `latent` output contains the video latent with generated keyframes appended on T, which can be used for further processing or analysis.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/en.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
