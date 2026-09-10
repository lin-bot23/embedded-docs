# Görüntüleri Normalleştir

Bu düğüm, matematiksel bir normalleştirme süreci kullanarak girdi görüntüsünün piksel değerlerini ayarlar. Her pikselden belirtilen ortalama değeri çıkarır ve ardından sonucu belirtilen standart sapmaya böler. Bu, görüntü verilerini diğer makine öğrenimi modelleri için hazırlamak amacıyla yapılan yaygın bir ön işleme adımıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Normalleştirilecek girdi görüntüsü. | IMAGE | Evet | - |
| `ortalama` | Normalleştirme için ortalama değer (varsayılan: 0.5). | FLOAT | Hayır | 0.0 - 1.0 |
| `std` | Normalleştirme için standart sapma (varsayılan: 0.5). | FLOAT | Hayır | 0.001 - 1.0 |

Not: Girdi görüntüsü bir alfa (şeffaflık) kanalı içerdiğinde, alfa kanalı normalleştirilmez. Alfa, renk yerine şeffaflığı sakladığı için çıktıda değiştirilmeden korunur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görüntüler` | Normalleştirme süreci uygulandıktan sonra elde edilen görüntü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
