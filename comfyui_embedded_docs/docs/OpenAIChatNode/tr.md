# OpenAI ChatGPT

Bu düğüm, bir OpenAI modelinden metin yanıtları üretir. Metin isteminizi ve isteğe bağlı olarak görselleri veya dosyaları bir OpenAI modeline gönderir ve üretilen metin yanıtını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `komut` | Yanıt üretmek için modele gönderilen metin girdileri (varsayılan: boş dize). | STRING | Evet | - |
| `bağlamı_sürdür` | Bu parametre kullanımdan kaldırılmıştır ve hiçbir etkisi yoktur (varsayılan: False). | BOOLEAN | Evet | - |
| `model` | Yanıtı üretmek için kullanılan model (varsayılan: `gpt-5`) | COMBO | Evet | `gpt-6-astra`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı görsel(ler). Birden fazla görsel eklemek için Batch Images düğümünü kullanabilirsiniz. | IMAGE | Hayır | - |
| `dosyalar` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(lar). OpenAI Chat Input Files düğümünden girdi kabul eder. | OPENAI_INPUT_FILES | Hayır | - |
| `gelişmiş_seçenekler` | Model için isteğe bağlı yapılandırma. OpenAI Chat Advanced Options düğümünden girdi kabul eder. | OPENAI_CHAT_CONFIG | Hayır | - |

Not: Akıl yürütme çabası (reasoning effort) belirleyen bir `advanced_options` yapılandırması bağlandığında, seçilen `model` bu çaba değerini desteklemelidir. Örneğin, gpt-4.1 model ailesi hiçbir akıl yürütme çabasını desteklemez; `gpt-5.5` none, low, medium, high ve xhigh değerlerini destekler; `gpt-5.5-pro` ise medium, high ve xhigh değerlerini destekler. Akıl yürütme çabası seçilen model tarafından desteklenmiyorsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output_text` | OpenAI modeli tarafından üretilen metin yanıtı. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
