# تصاویر مرجع HiDream-O1

این گره تصاویر مرجع را به هر دو Conditioning مثبت و منفی متصل می‌کند تا گره‌های بعدی بتوانند از آن‌ها برای هدایت فرآیند تولید استفاده کنند. تصاویر مرجع به ترتیب عددی سوکت‌های ورودی خود اعمال می‌شوند. اگر هیچ تصویر مرجعی متصل نباشد، Conditioning مثبت و منفی بدون تغییر عبور می‌کنند.

## ورودی‌ها

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `positive` | Conditioning مثبت برای اتصال تصاویر مرجع به آن. | CONDITIONING | بله | - |
| `negative` | Conditioning منفی برای اتصال تصاویر مرجع به آن. | CONDITIONING | بله | - |
| `images` | تصاویر مرجع به ترتیب عددی سوکت استفاده می‌شوند. هنگامی که تصاویر ارائه می‌شوند، به هر دو Conditioning مثبت و منفی متصل می‌شوند. | IMAGE | خیر | ۰ تا ۱۰۰ تصویر (`image_1` تا `image_100`) |

**نکته درباره پارامتر `images`:** این یک ورودی autogrow است که سوکت‌های شماره‌گذاری شده `image_1` تا `image_100` را فراهم می‌کند. تصاویر به ترتیب عددی سوکت استفاده می‌شوند. این ورودی اختیاری است: اگر هیچ تصویر مرجعی متصل نباشد، گره Conditioningهای `positive` و `negative` را بدون تغییر باز می‌گرداند. هنگامی که تصاویر متصل می‌شوند، همان مجموعه تصاویر مرجع به هر دو خروجی متصل می‌شوند و Conditioning منفی نیز قبل از اتصال تصاویر، به عنوان منفی علامت‌گذاری می‌شود.

## خروجی‌ها

| Output Name | Description | Data Type |
| --- | --- | --- |
| `positive` | Conditioning مثبت با تصاویر مرجع متصل شده. | CONDITIONING |
| `negative` | Conditioning منفی با تصاویر مرجع متصل شده. | CONDITIONING |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/fa.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`
