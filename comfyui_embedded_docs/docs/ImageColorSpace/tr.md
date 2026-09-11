# Görüntü Renk Uzayını Dönüştür

ImageColorSpace düğümü, görüntüleri sRGB (Rec.709), doğrusal Rec.709, HDR (Rec.2020 HLG) ve HDR PQ (Rec.2020 PQ) renk uzayları arasında dönüştürür. Renk uzayını daraltırken, toplu iş boyunca fazla parlaklığı ton eşler ve gam dışı renkleri sıkıştırır. Dönüşümler float32'de hesaplanır ve varsa alfa kanalı değiştirilmeden geçirilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Dönüştürülecek giriş görüntüsü. | IMAGE | Evet | Herhangi bir geçerli görüntü. |
| `source` | Giriş piksellerinin renk uzayı. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | Çıkış piksellerinin renk uzayı. Kaydetme düğümünü de aynı renk uzayına ayarlayın. Varsayılan: "sRGB". | COMBO | Evet | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `image` | Belirtilen hedef renk uzayındaki dönüştürülmüş görüntü. | IMAGE |

## Notlar

- Linear 1.0, sRGB ile aynı 203 nit referans beyazını kullanır; HLG ise 1000 nit referans ekran kullanır.
- Linear çıktı ve Linear'dan HDR'ye dönüşümler, ton eşleme olmadan genişletilmiş değerleri korur.
- SDR çıktısı ve PQ'dan HLG'ye dönüşüm, toplu iş boyunca fazla parlaklığı ton eşler (pozlamanın kare kare değişmemesi için tek bir beyaz noktasını paylaşır) ve gam dışı renkleri sıkıştırır.
- Dönüşümler float32'de hesaplanır ve ara aygıt ile dtype değerini döndürür.
- Straight alfa renk dönüşümüne uğratılmaz; yalnızca RGB kanalları dönüştürülür.
- `source` ve `destination` aynıysa, hiçbir renk dönüşümü uygulanmaz — görüntü yalnızca ara aygıt ve dtype'a taşınır.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/tr.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
