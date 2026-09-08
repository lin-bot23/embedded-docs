# ByteDance Metinden Videoya

ByteDance Metinten Video Düğümü, metin ipuçlarına dayalı olarak ByteDance modellerini kullanarak bir API üzerinden videolar oluşturur. Bir metin açıklaması ve çeşitli video ayarları alır, ardından sağlanan spesifikasyonlara uygun bir video oluşturur. Düğüm API iletişimini yönetir ve oluşturulan videoyu çıktı olarak döndürür.

## Genel Bakış

ByteDance Metinten Video Düğümü, metin ipuçlarını ByteDance'nin AI yetenekleri kullanarak videolara dönüştürmek için tasarlanmıştır. Kullanıcılar model, çözünürlük, en boy oranı, sürekli ve diğer parametreleri belirleyerek video oluşturma sürecini kontrol edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Kullanılacak ByteDance modeli. | STRING | Evet | 
  - "seedance-1-5-pro-251215"
  - "seedance-1-0-pro-250528"
  - "seedance-1-0-pro-fast-251015" |
| `prompt` | Videonun oluşturulmasında kullanılacak metin ipuçları. | STRING | Evet | Çok satırlı metin girdisi |
| `çözünürlük` | Çıktı videonun çözünürlüğü. | STRING | Evet | 
  - "480p"
  - "720p"
  - "1080p" |
| `en_boy_oranı` | Çıktı videonun en boy oranı. | STRING | Evet | 
  - "16:9"
  - "4:3"
  - "1:1"
  - "3:4"
  - "9:16"
  - "21:9" |
| `süre` | Çıktı videonun süresi saniye cinsinden. | INT | Evet | 3 ila 12 saniye |
| `tohum` | Kullanılacak semptom. | INT | Hayır | 0 ila 2,147,483,647 |
| `sabit_kamera` | Kamerayı sabitlemeyi belirtir. | BOOLEAN | Hayır | - |
| `filigran` | Videoya "AI oluşturuldu" su izi eklemeyi belirtir. | BOOLEAN | Hayır | - |
| `ses_oluştur` | Bu parametre, `seedance-1-5-pro-251215` modeli dışındaki tüm modeller için göz ardı edilir. | BOOLEAN | Hayır | - |

**Parametre Kısıtlamaları:**

- `prompt`, boşluk karakterlerinden arındırıldıktan sonra en az 1 karakter içermelidir.
- `prompt`, "resolution", "ratio", "duration", "seed", "camerafixed", "watermark" gibi metin parametrelerini içemez.
- `duration`, 3 ve 12 saniye arasında değerler alabilir.
- `seedance-1-5-pro-251215` modeli için en düşük desteklenen süre 4 saniyedir.
- `seed`, 0 ila 2,147,483,647 arasında değerleri kabul eder.
- `generate_audio` parametresi, `model` `seedance-1-5-pro-251215` olarak ayarlandığında etkili olur; diğer tüm modeller için göz ardı edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output` | Oluşturulan video dosyası. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
