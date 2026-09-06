# GörüntüRGB'denYUV'ye

ImageRGBToYUV düğümü, RGB renk alanından YUV renk alanına dönüşüm yapar. Bir RGB görüntü girdisini alır ve bu görüntüyü YUV renk alanına dönüştürerek üç ayrı görüntü çıktısı üretir: Y (parlaklık), U (mavi-farklılık) ve V (kırmızı-farklılık).

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|----------|-------|
| `görüntü` | Dönüştürülecek olan girdi RGB görüntüsü. Bu, 3 kanallı bir görüntü olmalıdır. | GÖRÜNTÜ | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-----------|-----------|
| `Y`       | Görüntünün Y kanalı, görüntünün parlaklığını (aydınlatma) temsil eder. | GÖRÜNTÜ |
| `U`       | Görüntünün U kanalı, mavi-farklılık renk bileşenini temsil eder. | GÖRÜNTÜ |
| `V`       | Görüntünün V kanalı, kırmızı-farklılık renk bileşenini temsil eder. | GÖRÜNTÜ |

Çıktı görüntüleri, girdi görüntüsü ile aynı boyutlarda olacaktır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/tr.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
