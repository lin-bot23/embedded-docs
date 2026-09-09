# LTXVFreezeLatent

## Özet

LTXV Freeze Latent düğümü, belirli bir latent için noise_mask'ı 0'a ayarlayarak, latent'in örnekleme sırasında temiz kalmasını sağlamak üzere tasarlanmıştır. Özellikle, audio veya video latent'leri denoising'den korumak için kullanılır ve bu, audio ve videoyu cross-attention için birleştirmeden önce veya denoising'e tabi tutulmaması gereken herhangi bir latent için uygulanabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `latent` | Dondurulacak video veya audio latent. Audio 4D; video 5D. | LATENT | Evet | N/A |
| `samples` | Latent örneklerini içeren tensor. | TENSOR | Evet | Audio: 4D (batch, kanallar, kareler, örnekler); Video: 5D (batch, kanallar, yükseklik, genişlik, kareler) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `latent` | Örnekleme sırasında temiz kalmasını sağlamak için noise_mask'ı 0'a ayarlanmış latent. | LATENT |

## Notlar

- `samples` tensor'ı düz bir tensor olmalıdır ve birleştirilmiş audio-video latent olmamalıdır. Birleştirilmiş latentse, önce Ayır AV Latent düğümü kullanılarak bölünmelidir.
- Çıktı `latent`, belirtilen latent için denoising'i önlemek için noise_mask'ı sıfırlardan oluşur.
- Düğüm hem audio hem de video latent'lerini destekler ve her biri için farklı tensor şekilleri vardır.
- `samples` tensor'ının şekli audio veya video şekline uygun değilse, bir ValueError hatası alınacaktır.
```

**Not:** Gerçek uygulamanın burada açıkça belirtilmeyen ek kısıtlamaları veya davranışları olabilir. En doğru bilgi için her zaman en son kaynak koduna başvurun.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/tr.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
