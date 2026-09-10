# GörüntüRGB'denYUV'ye

ImageRGBToYUV düğümü, bir RGB görüntüsünü YUV renk uzayına dönüştürür. Görüntüyü üç bileşene ayırır — Y (parlaklık), U (mavi-fark kroma) ve V (kırmızı-fark kroma) — ve her bileşeni, girdiyle aynı boyutta ayrı bir görüntü olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|----------|-------|
| `görüntü` | YUV renk uzayına dönüştürülecek RGB girdi görüntüsü. Görüntü bir alfa kanalı içeriyorsa yalnızca ilk üç (RGB) kanal kullanılır. | IMAGE | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `Y` | YUV renk uzayının parlaklık bileşeni | IMAGE |
| `U` | YUV renk uzayının mavi-fark kroma bileşeni | IMAGE |
| `V` | YUV renk uzayının kırmızı-fark kroma bileşeni | IMAGE |

Her çıktı, girdi görüntüsüyle aynı genişliğe, yüksekliğe ve kanal sayısına sahiptir. İlgili Y, U veya V bileşeni tüm kanallara kopyalanır; böylece her çıktı standart bir görüntü olarak döndürülür.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/tr.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
