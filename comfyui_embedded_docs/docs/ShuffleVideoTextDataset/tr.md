# Video-Metin Çiftlerini Karıştır

Bu düğüm, bir listedeki video-metin çiftlerinin sırasını rastgele karıştırır ve her videonun karşılık gelen metniyle eşleşmiş kalmasını sağlar. Eşit uzunlukta iki liste alır ve aynı rastgele permütasyonu her iki listeye de uygulayarak, orijinal eşleşmelerin karıştırma sonrasında korunmasını güvence altına alır. Bir seed değeri, karıştırma sırasını kontrol eder; böylece sonuçlar tekrarlanabilir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `videos` | Karıştırılacak videoların listesi. | VIDEO | Evet | Video öğeleri listesi |
| `texts` | Karıştırılacak metinlerin listesi (videolarla eşleştirilmiş açıklamalar). | STRING | Evet | Metin dizeleri listesi |
| `seed` | Karıştırma sırasını belirleyen rastgele seed değeri (varsayılan: 0). | INT | Evet | 0 ile 18446744073709551615 |

Not: `videos` ve `texts` aynı uzunlukta olmalıdır; düğüm her videoyu aynı konumdaki metinle eşleştirir ve bu eşleşmeleri karıştırma sırasında korur. Dahili olarak, `seed` değeri rastgele sıra oluşturulmadan önce 4294967295 (2^32 - 1) mod'una göre indirgenir; bu nedenle çok büyük seed değerleri, daha küçük olanlarla aynı karıştırmayı üretebilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `videos` | Yeni rastgele sırada karıştırılmış videolar. | VIDEO |
| `texts` | Videolarla aynı yeni sırada karıştırılmış metinler. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/tr.md)

---
**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`
