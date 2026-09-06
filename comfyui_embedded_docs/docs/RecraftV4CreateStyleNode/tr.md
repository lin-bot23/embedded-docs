# Recraft V4 Stil Oluştur

Bu düğüm, 1 ila 10 referans görüntüden yeniden kullanılabilir bir Recraft V4 stili oluşturur. Döndürülen stil kimliği, aynı çıktı türündeki (raster veya vektör) tüm Recraft V4 ve V4.1 modelleriyle çalışır ve sonraki görüntü oluşturma adımlarında yeniden kullanılabilir. Tüm referans görüntülerin toplam boyutu 10 MB ile sınırlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Stilin oluşturulduğu model. Standard ve Pro tek bir stil havuzunu paylaşır: raster stiller tüm Recraft V4 ve V4.1 raster modelleriyle, vektör stiller (*_vector) ise tüm V4 ve V4.1 vektör modelleriyle çalışır. | COMBO | Evet | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | Stili tanımlayan referans görüntüler. Benzer referanslar eşleşmeyi keskinleştirir, çeşitli referanslar ise onu genişletir. Genişletilebilir yuva: 1 ila 10 görüntü bağlayın (`image_1` ile `image_10` arasında). | IMAGE | Evet | 1 ila 10 görüntü |

### Notlar

- En az bir referans görüntü gereklidir; hiçbir görüntü sağlanmazsa düğüm hata verir.
- En fazla 10 referans görüntüye izin verilir; daha fazlası sağlanırsa düğüm hata verir.
- Tüm referans görüntülerin toplam kodlanmış boyutu 10 MB'ı aşmamalıdır; sınır aşılırsa düğüm hata verir.
- Her referans görüntü, Recraft API'ye gönderilmeden önce en fazla 2048×2048 piksele küçültülür ve WebP olarak kodlanır.
- `_vector` ile biten modeller vektör stilleri oluşturur; diğer seçenekler raster stiller oluşturur. Standard ve Pro modeller, her çıktı türü içinde aynı stil havuzlarını paylaşır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `style_id` | Oluşturulan stilin benzersiz tanımlayıcısı; aynı çıktı türündeki tüm Recraft V4 ve V4.1 modelleriyle kullanılabilir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/tr.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
