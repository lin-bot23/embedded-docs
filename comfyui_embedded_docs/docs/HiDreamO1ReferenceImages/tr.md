# HiDream-O1 Referans Görselleri

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `positive` | Referans görüntülerin ekleneceği pozitif conditioning. | CONDITIONING | Evet | - |
| `negative` | Referans görüntülerin ekleneceği negatif conditioning. | CONDITIONING | Evet | - |
| `images` | Referans görüntüler sayısal soket sırasına göre kullanılır. Görüntüler sağlandığında, hem pozitif hem de negatif conditioning'e eklenir. | IMAGE | Hayır | 0 ila 100 görüntü (`image_1` - `image_100`) |

**`images` parametresi hakkında not:** Bu, `image_1`'den `image_100`'e kadar numaralandırılmış soketler sağlayan otomatik büyüyen bir girdidir. Görüntüler sayısal soket sırasına göre kullanılır. Girdi isteğe bağlıdır: hiçbir referans görüntüsü bağlanmazsa, düğüm `positive` ve `negative` conditioning'i değiştirmeden döndürür. Görüntüler bağlandığında, aynı referans görüntü seti her iki çıktıya da eklenir ve negatif conditioning, görüntüler eklenmeden önce negatif olarak işaretlenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `positive` | Referans görüntülerin eklendiği pozitif conditioning. | CONDITIONING |
| `negative` | Referans görüntülerin eklendiği negatif conditioning. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/tr.md)

---
**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`
