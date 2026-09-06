# OpenAI Sora - Video

OpenAIVideoSora2 düğümü, OpenAI'nin Sora modellerini kullanarak videolar oluşturur. Bir metin istemine ve isteğe bağlı bir referans giriş görseline dayalı olarak video içeriği üretir ve ardından oluşturulan videoyu çıktı olarak sunar. Düğüm, seçilen modele bağlı olarak farklı video sürelerini ve çözünürlüklerini destekler.

**KULLANIMDAN KALDIRMA BİLDİRİMİ:** OpenAI, Eylül 2026'da Sora v2 API'sine hizmet vermeyi durduracaktır. Bu düğüm, o tarihte ComfyUI'dan kaldırılacaktır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Video oluşturma için kullanılacak OpenAI Sora modeli (varsayılan: "sora-2") | COMBO | Evet | "sora-2"<br>"sora-2-pro" |
| `prompt` | Yönlendirici metin; bir giriş görseli mevcutsa boş olabilir (varsayılan: boş) | STRING | Evet | - |
| `size` | Oluşturulan videonun çözünürlüğü (varsayılan: "1280x720") | COMBO | Evet | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | Oluşturulan videonun saniye cinsinden süresi (varsayılan: 8) | COMBO | Evet | 4<br>8<br>12 |
| `image` | Video oluşturma için kullanılan isteğe bağlı referans giriş görseli (fit, karakter, sahne referansı vb.); yalnızca tek bir görsel desteklenir | IMAGE | Hayır | - |
| `seed` | Düğümün yeniden çalıştırılıp çalıştırılmayacağını belirleyen seed değeri; gerçek sonuçlar seed değerinden bağımsız olarak deterministik değildir (varsayılan: 0) | INT | Hayır | 0 - 2147483647 |

**Sınırlamalar ve Kısıtlamalar:**

- "sora-2" modeli yalnızca "720x1280" ve "1280x720" çözünürlüklerini destekler; "1024x1792" ve "1792x1024" seçenekleri yalnızca "sora-2-pro" modeliyle geçerlidir
- Bir görsel bağlandığında, tam olarak bir görsel içermelidir; birden fazla görsel bağlamak hata oluşturur
- Sonuçlar, seed değeri ne olursa olsun deterministik değildir

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | OpenAI Sora tarafından oluşturulan video dosyası | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/tr.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
