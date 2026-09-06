# Convert Image Color Space

## Genel Bakış

ImageColorSpace düğümü, sRGB, HDR (Rec.2020 HLG) ve HDR PQ (Rec.2020 PQ) gibi farklı renk alanları arasında görselleri dönüştürür. Bu düğüm, toplu içinde aşırı parlaklığı daraltma ve gam-out renkleri sıkıştırma gibi işlevleri destekler ve yalnızca RGB kanallarında çalışır, alpha kanalları değişmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-----------|-----------|----------|-------|
| `image` | Dönüştürülecek giriş görseli. | GÖRSEL | Evet | Herhangi geçerli görsel biçimi. |
| `source` | Giriş piksellerinin renk alanı. | COMBO | Evet | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |
| `destination` | Çıkış piksellerinin renk alanı. | COMBO | Evet | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |

## Çıktılar

| Çıkış Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Belirtilen çıkış renk alanında dönüştürülen görsel. | GÖRSEL |

## Notlar

- Bu düğüm, dönüştürmeler için 203 nit SDR beyaz ve 1000 nit HLG referans ekranı kullanır.
- Dönüşümler float32'de hesaplanır ve aracı cihaz ve dtype'yi döner.
- Doğrudan alpha renk dönüşümünden geçirilmez.
- Bu düğüm, sRGB, HDR (Rec.2020 HLG) ve HDR PQ (Rec.2020 PQ) renk alanları arasında dönüşümleri destekler.
- Bu düğüm, doğru dönüşümler sağlamak için ton-mapping daraltma ve gam-out renkleri sıkıştırma işlemleri gerçekleştirir.
- Dönüşümler RGB kanallarında yapılır ve varsa alpha kanalı değişmeden geçirilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/tr.md)

---
**Source fingerprint (SHA-256):** `f0d38c6f5b524752a99d51b1a87f0e65c07f3ba36ecb0066d8d10c5b5032d36f`
