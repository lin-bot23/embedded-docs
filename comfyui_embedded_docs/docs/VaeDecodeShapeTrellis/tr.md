# VaeDecodeShapeTrellis

Bu düğüm, Trellis2 şekil latent temsillerini 3B bir mesh'e dönüştürür. Seyrek şekil latent verilerini mesh geometrisine dönüştürmek için bir VAE kullanır ve ayrıca kod çözme sırasında üretilen şekil alt bölümleme verilerini çıkarır. Düğüm hem tek hem de toplu latent girdileri destekler ve mesh yönünü beklenen koordinat çerçevesine otomatik olarak ayarlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Kod çözülecek latent örnekler; örnek tensörünü ve seyrek koordinat verilerini içerir. Latent sözlüğü ayrıca şu isteğe bağlı alanları içerebilir: toplu şekiller için `coord_counts`, mesh çözünürlüğünü kontrol etmek için `coord_resolution` ve koordinat yönelimi için `model_frame`. | LATENT | Evet | None |
| `vae` | Şekil latentini bir mesh'e dönüştürmek için kullanılan VAE modeli. | VAE | Evet | None |

### `samples` Hakkında Notlar

- `samples` girdisi, `samples` tensörünü ve `coords` seyrek koordinatlarını içermesi gereken bir latent sözlüktür.
- `coord_counts` mevcutsa, negatif olmayan tamsayılardan oluşan 1B bir tensör olmalıdır ve tüm sayımların toplamı toplam koordinat satırı sayısına eşit olmalıdır. Her sayım, gruptaki bir şekli temsil eder.
- `coord_resolution` sağlanırsa, mesh çözünürlüğü `coord_resolution * 16` olarak hesaplanır. Aksi takdirde, VAE'nin yerleşik çözünürlük arabelleği kullanılır (varsayılan değer: 1024).
- `model_frame` `"z_up"` olarak ayarlanırsa, kod çözülen mesh köşeleri Z-up koordinat sisteminden glTF tarafından kullanılan Y-up kuralına döndürülür. Varsayılan değer `"y_up"`tir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Kod çözülen 3B mesh; köşe konumlarını ve yüz indekslerini içerir. Birden fazla şekil kod çözülürken, tümü aynı boyutlara sahipse mesh'ler tek bir yığılmış tensör olarak döndürülür; aksi takdirde değişken boyutlu paketlenmiş bir grup olarak döndürülür. | MESH |
| `shape_subdivides` | Kod çözme işleminin her aşamasında üretilen şekil alt bölümleme verileri. | SHAPE_SUBDIVIDES |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/tr.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
