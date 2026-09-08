# GörüntüYUV'denRGB'ye

GörüntüYUVToRGB düğümü, görüntüleri YUV renk alanından RGB renk alanına dönüştürmek için tasarlanmıştır. Bu, görüntünün Y (aydınlatma), U (mavi projeksiyon) ve V (kırmızı projeksiyon) kanallarını temsil eden üç ayrı giriş görüntüsünü alarak bu kanalları renk alanı dönüşüm teknikleri kullanarak tek bir RGB görüntüsüne birleştirmek suretiyle yapılır.

## Genel Bakış

GörüntüYUVToRGB düğümü, YUV görüntüleri RGB görüntülere dönüştürmek için kullanılır. Bu, bu iki standart arasında renk alanı dönüşümü gerektiren uygulamalar için faydalıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|----------|-------|
| `Y`       | Görüntüün Y kanalı giriş görüntüsü, aydınlatma bilgilerini temsil eder. | GÖRÜNTÜ | Evet | - |
| `U`       | Görüntüün U kanalı giriş görüntüsü, mavi renk farkını temsil eder. | GÖRÜNTÜ | Evet | - |
| `V`       | Görüntüün V kanalı giriş görüntüsü, kırmızı renk farkını temsil eder. | GÖRÜNTÜ | Evet | - |

**Not:** Y, U ve V kanallarının birlikte sağlanması ve doğru dönüşüm sağlamak için aynı boyutlarda olması gerekmektedir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|-----------|-----------|
| `output`    | YUV'dan RGB'ye dönüşüm sonrası elde edilen sonuç görüntüsü. | GÖRÜNTÜ |

Çıkış görüntüsü, giriş Y, U ve V görüntülerinin aynı boyutlarında olacaktır, ancak renk bilgileri RGB renk alanında temsil edilecektir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/tr.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
