# MiniMax H3 İlk-Son-Kare'den Videoya

Bu düğüm, MiniMax H3 modellerini kullanarak bir ilk kare görüntüsünden ve isteğe bağlı olarak bir son kare görüntüsünden video oluşturur. `model` seçici, hangi oluşturma ayarlarının ve kısıtlamaların uygulanacağını belirler; oluşturulan videonun en-boy oranı sağlanan görüntülere uyar.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak model. Bir model seçmek, o modele özgü ayarları aşağıda ortaya çıkarır. | DYNAMIC_COMBO | Evet | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Video için ilk kare görüntüsü. Oluşturulan video, bu görüntünün en-boy oranına uyar. | IMAGE | Evet | - |
| `last_frame` | Video için isteğe bağlı son kare görüntüsü. Sağlandığında, video ilk kareden bu son kareye doğru oluşturulur. | IMAGE | Hayır | - |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek, benzer ancak birebir aynı olması garanti edilmeyen sonuçlar üretir. Bir "control after generate" seçeneği içerir. Varsayılan: 42. | INT | Evet | 0 ile 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği. Bu bir gelişmiş parametredir. Yalnızca `MiniMax H3` modeli tarafından desteklenir. Varsayılan: False. | BOOLEAN | Evet | True<br>False |

### MiniMax H3 Girdileri

Bu ayarlar, `model` seçicide `MiniMax H3` seçildiğinde gösterilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. En az bir boşluk olmayan karakter içermelidir. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "768P"<br>"2K" |
| `duration` | Çıktı videosunun saniye cinsinden süresi. Varsayılan: 5. | INT | Evet | 4 ile 15 |

### MiniMax H3 Max ve MiniMax H3 Max Turbo Girdileri

Bu ayarlar, `model` seçicide `MiniMax H3 Max` veya `MiniMax H3 Max Turbo` seçildiğinde gösterilir. Her iki model de aynı ayarları sunar.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video oluşturma için metin istemi. Boş veya yalnızca boşluk karakterlerinden oluşan bir metin olmamalıdır ve 50.000 karakterle sınırlıdır. | STRING | Evet | Çok satırlı metin |
| `resolution` | Çıktı videosunun çözünürlüğü. Varsayılan: 768P. | COMBO | Evet | "480P"<br>"768P" |
| `duration` | Çıktı videosunun saniye cinsinden süresi. Varsayılan: 5. | INT | Evet | 5 ile 15 |
| `prompt_expansion_mode` | Oluşturmadan önce istemin yeniden yazılması için ne kadar çaba harcandığı. Varsayılan: balanced. | COMBO | Evet | "balanced"<br>"quality" |

**Kısıtlamalarla ilgili notlar:**

- İstem metin içermelidir: boş veya yalnızca boşluk içeren istemler reddedilir.
- Sağlanan her kare görüntüsü en az 256 piksel genişliğinde ve 256 piksel yüksekliğinde olmalı ve en-boy oranı 0.4 ile 2.5 arasında (yaklaşık 2:5 ila 5:2) olmalıdır. Bu gereksinim `first_frame` ve sağlanması durumunda `last_frame` için de geçerlidir.
- `last_frame` belirtilmediğinde video yalnızca ilk kareden oluşturulur.
- Çıktı videosu, sağlanan görüntülerin en-boy oranına uyar.
- `watermark` yalnızca `MiniMax H3` tarafından desteklenir. `MiniMax H3 Max` veya `MiniMax H3 Max Turbo` ile etkinleştirilmesi hata verir.
- Süre, `MiniMax H3` için 4 ila 15 saniye arasında, `MiniMax H3 Max` ve `MiniMax H3 Max Turbo` için ise 5 ila 15 saniye arasında değişir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `video` | Seçilen MiniMax H3 modeli kullanılarak ilk kare ve isteğe bağlı son kareden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/tr.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
