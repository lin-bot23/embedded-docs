# ByteDance İlk-Son-Kare'den Videoya

Bu düğüm, bir metin ipucu ve bir resmin ilk ve son karelerini kullanarak bir video oluşturur. İki kare arasında sorunsuz bir geçiş yaparak tam bir video sırası oluşturur. Düğüm, videoyun çözünürlüğü, en boy oranı, süresi ve ilave oluşturma parametrelerini özelleştirmek için çeşitli seçenekler sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturma için kullanılacak model. Mevcut seçeneklerden birini seçin (varsayılan: `"seedance-1-5-pro-251215"`). | COMBO | Evet | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `prompt` | Video oluşturma için kullanılacak metin ipucu. Bu ipucu, çözünürlük, orans, süre, seed, camerafixed veya watermark gibi belirli parametreler içermemelidir. | STRING | Evet | - |
| `ilk_kare` | Video için kullanılacak ilk kare. Resmin 300x300 ve 6000x6000 piksel arasında olmalı ve 0.4 ile 2.5 arasında bir en boy oranı olmalıdır. | IMAGE | Evet | - |
| `son_kare` | Video için kullanılacak son kare. Resmin 300x300 ve 6000x6000 piksel arasında olmalı ve 0.4 ile 2.5 arasında bir en boy oranı olmalıdır. | IMAGE | Evet | - |
| `çözünürlük` | Çıkış videoyun çözünürlüğü. Mevcut seçeneklerden birini seçin (varsayılan: `"480p"`). | COMBO | Evet | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `en_boy_oranı` | Çıkış videoyun en boy oranı. Mevcut seçeneklerden birini seçin (varsayılan: `"adaptive"`). | COMBO | Evet | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `süre` | Çıkış videoyun süresi saniye cinsinden (varsayılan: 5). `seedance-1-5-pro-251215` modeli için en düşük desteklenen süre 4 saniyedir. | INT | Evet | 3 - 12 |
| `tohum` | Oluşturma için kullanılacak seed (varsayılan: 0). Bu parametre isteğe bağlıdır. | INT | Hayır | 0 - 2147483647 |
| `sabit_kamera` | Video içinde kamerayı sabitlemeyi belirtir. Platform, ipucunuza kamera sabitleme talimatı ekler, ancak gerçek etkisi garantilenmez (varsayılan: False). | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI generated" su izi eklemeyi belirler (varsayılan: False). | BOOLEAN | Hayır | - |
| `ses_oluştur` | Bu parametre, `seedance-1-5-pro-251215` dışındaki tüm modeller için göz ardı edilir (varsayılan: False). | BOOLEAN | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

## Notlar

- `model` parametresi, video oluşturma sürecinin yetenekleri ve sınırlamalarını belirler.
- `prompt` yaratıcı ve açık olmalıdır, çünkü bu ipucu video oluşturmayı yönlendirecektir.
- `first_frame` ve `last_frame` kareleri, istenen video içeriğinin temsilcisi olmalıdır.
- `resolution` ve `aspect_ratio` parametreleri, son çıktı videoyun kalitesi ve boyutlarını etkileyecektir.
- `duration` parametresi, videoyun süresini ayarlar, en düşük 3 saniye ve en yüksek 12 saniye arasında olabilir.
- `seed` parametresi isteğe bağlıdır ve video oluşturma sürecinin tekrarlanabilirliğini sağlayabilir.
- `camera_fixed` parametresi, beklenen etkiyi her zaman sağlamayabilir olan ileri düzey bir seçenektir.
- `watermark` parametresi, videoya su izi eklemek için kullanılabilir ve bu, videoyun AI tarafından oluşturulduğunu belirtir.
- `generate_audio` parametresi, şu anda `seedance-1-5-pro-251215` dışındaki tüm modeller için göz ardı edilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
