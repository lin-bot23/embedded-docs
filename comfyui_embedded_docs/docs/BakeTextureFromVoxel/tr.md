# Voxel'den Doku İşle

Bu düğüm, PBR dokularını, ağın mevcut UV yerleşimini kullanarak 3B ağ üzerine pişirir. Her tekselde seyrek voksel hacminden renk ve malzeme niteliklerini örnekler ve temel renk görüntüsü ile metaliklik ve pürüzlülük haritalarını çıktı olarak verir. Ağı UV açılımına tabi tutmaz, bu nedenle yukarı akışa bir UV açma düğümü bağlanmış olmalıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Dokuların üzerine pişirileceği 3B ağ. Önceden bir UV yerleşimine sahip olmalıdır; yukarı akışa bir UV açma düğümü bağlanmış olmalıdır. | MESH | Evet | |
| `voxel_colors` | Voksel başına renkler ve isteğe bağlı PBR nitelikleri (metaliklik ve pürüzlülük kanalları) içeren seyrek voksel hacmi. | VOXEL | Evet | |
| `texture_size` | Kare UV atlas çözünürlüğü (görünen ad: "resolution", varsayılan: 2048). | INT | Evet | 64 ile 8192 |
| `reference_mesh` | İsteğe bağlı yoğun, inceltme öncesi ağ; örneklemeden önce her tekseli gerçek yüzeyine geri yansıtarak kaba ağlarda fasetli (faceted) pişirmeyi ortadan kaldırır. | MESH | Hayır | |

Notlar:

- Giriş ağı UV'lere sahip olmalıdır. UV yoksa düğüm hata verir. UV'ler köşelerle 1:1 olmalıdır (her köşe için bir UV).
- Ağ ve voksel koordinatları bir batch boyutu içerdiğinde, her batch öğesi ayrı ayrı pişirilir. Bir batch öğesinde voksel veya yüz yoksa, bu öğe atlanır ve onun için siyah bir doku üretilir.
- Bir batch için `reference_mesh` sağlandığında, yalnızca tek bir ağ içermediği sürece batch dizinine göre eşleştirilir; bu durumda bu ağ tüm öğeler için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `base_color` | RGB temel renk doku haritası. Değerler 0–1 aralığında float'tır. | IMAGE |
| `metallic` | Gri tonlamalı metaliklik haritası (float, 0–1). Voksel renkleri metaliklik kanalı içermediğinde siyahtır. | IMAGE |
| `roughness` | Gri tonlamalı pürüzlülük haritası (float, 0–1). Voksel renkleri pürüzlülük kanalı içermediğinde siyahtır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/tr.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
