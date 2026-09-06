# LTXV Süre Tahmin Edici

Bu düğüm, ModelPatchLoader ile yüklenmiş bir LTX 2.4 duration head kullanarak bir metin istemi için doğal çekim süresini tahmin eder ve ardından sonucu VAE'nin 8k+1 kare ızgarasına hizalar. Tahmin; seçilen kare hızı ve minimum ile maksimum süre sınırları kullanılarak bir kare sayısına dönüştürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Metin yerleştirmelerini ön işlemek ve duration head'i çalıştırmak için kullanılan model. | MODEL | Evet | N/A |
| `positive` | Süre tahmini için istemin metin yerleştirmelerini ve meta verilerini sağlayan conditioning. | CONDITIONING | Evet | N/A |
| `duration_head` | ModelPatchLoader ile yüklenmiş LTX 2.4 duration head. Bir LTX duration head olmalıdır. | MODEL_PATCH | Evet | N/A |
| `frame_rate` | Saniyeleri karelere dönüştürmek için kullanılan, saniye başına kare cinsinden kare hızı (varsayılan: 24.0). | FLOAT | Evet | 1.0 ile 120.0 |
| `min_seconds` | Tahmini bir kare sayısına dönüştürürken kullanılan saniye cinsinden minimum süre (varsayılan: 1.0). | FLOAT | Evet | 0.5 ile 120.0 |
| `max_seconds` | Tahmini bir kare sayısına dönüştürürken kullanılan saniye cinsinden maksimum süre (varsayılan: 20.0). | FLOAT | Evet | 0.5 ile 120.0 |

Not: `duration_head` girdisi, bir LTX duration head içeren bir model patch olmalıdır. Bağlı model patch bir LTX duration head değilse, düğüm bir ValueError hatası fırlatır. Yalnızca ilk conditioning girdisi kullanılır — `positive`, birden fazla istem içeren bir batch içeriyorsa, düğüm yalnızca ilkini değerlendirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `num_frames` | Tahmin edilen sürenin bir kare sayısına dönüştürülmüş ve VAE'nin 8k+1 kare ızgarasına hizalanmış hali. | INT |
| `seconds` | Ham (sınırlandırılmamış) tahmin edilen süre. Bu değer, kare ızgarasına hizalanmadan önceki değerdir. | FLOAT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/tr.md)

---
**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`
