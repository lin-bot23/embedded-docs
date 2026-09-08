# Tripo: هدف‌گذاری مجدد مدل ریگ‌شده

گره TripoRetargetNode یک انیمیشن از پیش تنظیم‌شده را به یک مدل سه‌بعدی ریگ‌شده موجود اعمال می‌کند. این گره شناسه وظیفه (Task ID) مدلی را که قبلاً ریگ شده است دریافت می‌کند، درخواست ری‌تارگت (retarget) را به API Tripo ارسال می‌کند و فایل انیمیشن‌شده حاصل را دانلود می‌نماید. مدل انیمیشن‌شده می‌تواند به صورت GLB یا FBX برگردانده شود، با گزینه‌های اختیاری برای هندسه مش و پخش در محل.

## ورودی‌ها

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `شناسه وظیفه مدل اصلی` | شناسه وظیفه مدل سه‌بعدی ریگ‌شده قبلی برای ری‌تارگت. وظیفه مرجع باید یک وظیفه ریگ باشد؛ ریگی که با مشخصات Mixamo روی نسخه مدل v1.0 ساخته شده است نمی‌تواند برای ری‌تارگت استفاده شود. | RIG_TASK_ID | بله | - |
| `انیمیشن` | پیش‌تنظیم انیمیشن برای اعمال روی مدل ریگ‌شده. انیمیشن‌های `preset:*` با هر دو مدل ریگ کار می‌کنند؛ انیمیشن‌های `preset:biped:*` نیاز به ریگی دارند که با مدل v1.0-20240301 ساخته شده باشد. | COMBO | بله | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>به علاوه گزینه‌های اضافی `"preset:biped:*"` که در رابط کاربری نمایش داده می‌شوند |
| `out_format` | فرمت فایل خروجی؛ نتیجه در خروجی متناظر قرار می‌گیرد. (پیش‌فرض: glb) | COMBO | خیر | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | شامل کردن مش در خروجی؛ حالت خاموش فقط اسکلت انیمیشن‌شده را خروجی می‌گیرد. (پیش‌فرض: True) | BOOLEAN | خیر | True<br>False |
| `animate_in_place` | پخش انیمیشن در محل، بدون جابجایی ریشه (root displacement). (پیش‌فرض: False) | BOOLEAN | خیر | True<br>False |
| `auth_token_comfy_org` | توکن احراز هویت برای دسترسی به API Comfy.org (پارامتر پنهان). | AUTH_TOKEN_COMFY_ORG | خیر | - |
| `api_key_comfy_org` | کلید API برای دسترسی به سرویس Comfy.org (پارامتر پنهان). | API_KEY_COMFY_ORG | خیر | - |
| `unique_id` | شناسه یکتا برای ردیابی عملیات (پارامتر پنهان). | UNIQUE_ID | خیر | - |

نکته: انیمیشن‌های گروه `preset:*` با هر دو مدل ریگ کار می‌کنند، در حالی که انیمیشن‌های گروه `preset:biped:*` نیاز به ریگی دارند که با مدل v1.0-20240301 ساخته شده باشد. اگر ریگ مرجع با مشخصات Mixamo و نسخه مدلی که با `v1.0` شروع می‌شود ایجاد شده باشد، فراخوانی ری‌تارگت با خطا مواجه می‌شود.

## خروجی‌ها

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `فایل مدل` | فایل مدل سه‌بعدی انیمیشن‌شده تولید شده (فقط برای سازگاری معکوس). | STRING |
| `شناسه وظیفه ری‌تارگت` | شناسه وظیفه برای ردیابی عملیات ری‌تارگت. | RETARGET_TASK_ID |
| `GLB` | مدل سه‌بعدی انیمیشن‌شده در فرمت GLB. وقتی `out_format` برابر glb باشد مقدار می‌گیرد. | FILE3DGLB |
| `FBX` | مدل سه‌بعدی انیمیشن‌شده در فرمت FBX. وقتی `out_format` برابر fbx باشد مقدار می‌گیرد. | FILE3DFBX |

> این مستند با هوش مصنوعی تهیه شده است. اگر خطایی دیدید یا پیشنهادی برای بهبود دارید، خوشحال می‌شویم مشارکت کنید! [ویرایش در GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fa.md)

---
**Source fingerprint (SHA-256):** `e5417a8fa584285ba9e57526e65b091c2383374c70364df9053777a3ce09541a`
