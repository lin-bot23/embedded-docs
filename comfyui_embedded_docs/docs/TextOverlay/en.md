# Draw Text Overlay

This node draws text on top of an image or a batch of images. It builds a text overlay with a configurable font size, color, vertical position, horizontal alignment, and optional black outline, then composites the overlay onto the original images.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | The input image or batch of images to draw text on | IMAGE | Yes | |
| `text` | The text to overlay on the image (default: ""). Supports multiple lines: the `\n` and `\t` escape sequences are converted to newlines and tabs, and long lines are automatically wrapped to fit within the image width. | STRING | Yes | |
| `font_size` | Font size as a percentage of the image height (default: 5.0) | FLOAT | Yes | 0.5 to 50.0 (step 0.5) |
| `color` | Color of the text (default: "#ffffff") | STRING | Yes | |
| `position` | Vertical position of the text on the image (default: "top") | COMBO | Yes | "top"<br>"bottom" |
| `align` | Horizontal alignment of the text (default: "left") | COMBO | Yes | "left"<br>"center"<br>"right" |
| `outline` | Draw a black outline around the text (default: True) | BOOLEAN | Yes | |

Note: If `text` is empty or contains only whitespace, the node returns the input images unchanged. The text overlay is rendered once and applied to every image in the batch.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The input images with the text overlay composited on top | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/en.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
