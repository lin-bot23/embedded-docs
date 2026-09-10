# GörüntüYUV'denRGB'ye

ImageYUVToRGB düğümü, YUV renk uzayı görüntülerini RGB renk uzayına dönüştürür. Y (parlaklık), U (mavi projeksiyon) ve V (kırmızı projeksiyon) bileşenlerini temsil eden üç ayrı girdi görüntüsünü alır ve bunları tek bir RGB görüntüsünde birleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `Y` | Y (parlaklık) bileşeni girdi görüntüsü | IMAGE | Evet | - |
| `U` | U (mavi projeksiyon) bileşeni girdi görüntüsü | IMAGE | Evet | - |
| `V` | V (kırmızı projeksiyon) bileşeni girdi görüntüsü | IMAGE | Evet | - |

**Not:** Üç girdi görüntüsünün tümü (Y, U ve V) birlikte sağlanmalı ve doğru dönüşüm için uyumlu boyutlara sahip olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `output` | Dönüştürülmüş RGB görüntüsü | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/tr.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
