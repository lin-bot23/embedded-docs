# Görüntüleri Normalleştir

Bu düğüm, bir giriş resminin piksel değerlerini matematiksel bir normalleştirme süreci kullanarak ayarlar. Her bir pikselden belirtilen ortalama değeri çıkarılır ve ardından sonuç standart sapma tarafından bölünür. Bu, diğer makine öğrenim modellerine hazırlık için yaygın bir ön işleme adımıdır. Eğer giriş resmi bir alpha kanalı içeriyorsa, alpha kanalı değişmez şekilde geçirilir ve şeffaflık korunur.

## Genel Bakış

Normalize Images düğümü, bir giriş resminin renklerini, ortalama ve standart sapma temel alınarak piksel değerlerini ayarlayarak normalleştirir. Bu süreç, makine öğrenim algoritmalarına uygulanmadan önce görüntü verilerini standartlaştırmak için kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image`   | Normalleştirilecek giriş resmi. | RESİM | Evet | - |
| `ortalama` | Normalleştirme için ortalama değeri. | FLOAT | Hayır | 0.0 - 1.0 (varsayılan: 0.5) |
| `std`     | Normalleştirme için standart sapma. | FLOAT | Hayır | 0.001 - 1.0 (varsayılan: 0.5) |

`mean` ve `std` parametreleri, giriş resminin piksel değerlerini normalleştirmek için kullanılır. Her iki parametrenin de varsayılan değerleri 0.5'tir ve bu, normalleştirmek için yaygın bir seçimdir.

## Çıktılar

| Çıkış Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `görüntüler`     | Normalleştirme sürecinin uygulanması sonrası elde edilen sonuç resmi. | RESİM |

Normalize Images düğümünden elde edilen çıktı, normalleştirilmiş resmdir. Piksel değerleri belirtilen ortalama ve standart sapma göre ayarlanır ve varsa alpha kanalı korunur.

## Not

Normalize Images düğümü, herhangi bir grup büyüklüğüne sahip resimleri işlemek için tasarlanmıştır, bu nedenle grup işleme görevleri için uygundur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/tr.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
