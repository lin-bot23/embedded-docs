# ByteDance Görüntüden Videoya

ByteDance Görüntüden Video düğümü, girdi görsel ve metin prompt kullanarak ByteDance'nin API'si ile video oluşturur. Sunulan açıklamayı görsel olarak temsil eden bir video sırası oluşturur. Çıktının çözünürlüğü, en boy oranı, süresi ve diğer parametreleri özelleştirmek için seçenekler sunar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video oluşturmak için kullanılacak ByteDance modeli. Kullanılabilir seçenekler: <br>`"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` | STRING | Evet | Yukarıda listelenenler |
| `prompt` | Video oluşturmak için kullanılacak metin prompt. Boşlukları kesildikten sonra en az 1 karakter uzunluğunda olmalıdır. | STRING | Evet | - |
| `görüntü` | Video için kullanılacak ilk kare. Görsel 300x300 ve 6000x6000 piksel arasında olmalı, en boy oranı 0.4 ve 2.5 arasında olmalıdır. | GÖRSEL | Evet | - |
| `çözünürlük` | Çıktı videoyunun çözünürlüğü. Kullanılabilir seçenekler: <br>`"480p"`<br>`"720p"`<br>`"1080p"` | STRING | Evet | Yukarıda listelenenler |
| `en-boy oranı` | Çıktı videoyunun en boy oranı. Kullanılabilir seçenekler: <br>`"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | STRING | Evet | Yukarıda listelenenler |
| `süre` | Çıktı videoyunun süresi saniye cinsinden. `seedance-1-5-pro-251215` modeli için en düşük desteklenen süre 4 saniyedir. | INT | Evet | 3 - 12 |
| `seed` | Oluşturma için kullanılacak seed. Seçmeli, varsayılan değeri 0'dır. | INT | Hayır | 0 - 2147483647 |
| `sabit kamera` | Kamerayı sabitlemeyi belirtir. Platform, promptınıza kamerayı sabitleme talimatı ekler, ancak gerçek etkisini garanti etmez. Seçmeli, varsayılan değeri False'dır. | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI generated" su izi eklemeyi belirtir. Seçmeli, varsayılan değeri False'dır. | BOOLEAN | Hayır | - |
| `ses_oluştur` | Bu parametre, `seedance-1-5-pro-251215` modeli dışındaki herhangi bir model için göz ardı edilir. Seçmeli, varsayılan değeri False'dır. | BOOLEAN | Hayır | - |

**Not:** Prompt, aşağıdaki kelimeleri (büyük/küçük harfe duyarlı olmaksızın) içermemelidir: `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Bu parametreler, ilgili girdiler aracılığıyla ayarlanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Girdi görsel ve prompt parametrelerine dayalı olarak oluşturulan çıktı video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
