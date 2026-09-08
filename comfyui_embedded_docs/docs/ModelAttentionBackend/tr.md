# Model Dikkat Arka Ucu

## Özet

ModelAttentionBackend düğümü, modelinize seçtiğiniz yoğun dikkat uygulamasını seçmenize olanak tanır. Modeli seçilen dikkat arka planı ile onarır, bu da PyTorch dikkat veya mevcutsa Comfy Kitchen dikkat olabilir. Bu düğüm, az yoğun dikkat pasif veya desteklenmemiş olduğunda özellikle kullanışlıdır ve modelin belirtilen yoğun dikkat mekanizması ile çalışmasını sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Seçilen dikkat arka planı ile onarılacak model. | MODEL | Evet |  |
| `dikkat` | Modele uygulanacak yoğun dikkat arka planı. Mevcut seçenekler "pytorch dikkat" ve mevcutsa ortamda "comfy kitchen dikkat"'dir. | STRING | Evet | "pytorch dikkat"<br> "comfy kitchen dikkat" (mevcutsa) |

- "comfy kitchen dikkat" seçeneği, INT8 dikkat ile ölçeklendirilmiş dikkat kullanır ve sadece Nvidia ve AMD GPU'larında desteklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Seçilen dikkat arka planı ile uygulanmış girdi modeli. | MODEL |

## Not

- Seçilen dikkat arka planı mevcutsa olmayabilirse, düğüm otomatik olarak PyTorch dikkat kullanmaya geçiş yapar ve bir uyarı kaydeder.
- ModelAttentionBackend düğümü deneyimseldir ve gelecekteki sürümlerde değişikliklere maruz kalabilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/tr.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
