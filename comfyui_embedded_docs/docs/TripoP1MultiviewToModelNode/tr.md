# Tripo P1: Çoklu Görünüşten Modele

Bu node, bir nesnenin veya karakterin iki ila dört referans görüntüsünden 3D model oluşturur. Ön görünümü ve sol, arka, sağ görünümlerin herhangi bir kombinasyonunu sağlayın; node, yeniden oluşturulan nesneyi GLB mesh olarak döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Ön görünüm (0°). Zorunlu. | IMAGE | Evet | - |
| `image_left` | Sol görünüm (90°), yani nesnenin sol tarafı. | IMAGE | Hayır | - |
| `image_back` | Arka görünüm (180°). | IMAGE | Hayır | - |
| `image_right` | Sağ görünüm (270°), yani nesnenin sağ tarafı. | IMAGE | Hayır | - |
| `output_mode` | Oluşturulacak modelin türünü seçin. "Geometry only" dokusuz bir ağ döndürür. "Textured" renk/PBR haritaları ekler. | DYNAMIC_COMBO | Evet | "Geometry only"<br>"Textured" |
| `face_limit` | Hedef yüz sayısı, 48-20000. -1, Tripo'nun uyarlanabilir şekilde seçmesini sağlar. (varsayılan: -1) | INT | Hayır | -1 ile 20000 arası |
| `model_seed` | Tekrarlanabilir model üretimi için tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |
| `auto_size` | Çıktıyı gerçek dünya metrelerine yaklaşık olarak ölçeklendirir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `export_uv` | Üretim sırasında UV açılımı yapar. Yalnızca geometri çalıştırmaları için daha hızlı olması amacıyla kapatın. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `compress_geometry` | Meshopt geometri sıkıştırması uygular (EXT_meshopt_compression). Dosyalar küçülür, ancak ComfyUI'nin 3D önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı açın. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### Yalnızca Geometri Girdileri

Bu mod için ek girdi gösterilmez. Oluşturulan model doku olmadan döndürülür.

### Dokulu Girdiler

Bu girdiler, `output_mode` `"Textured"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını dahil eder. Açıkken temel doku da zorunlu olarak açılır. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `texture_quality` | Doku kalite seviyesi. `detailed` = HD dokular, `extreme` = 8K Ultra dokular. (varsayılan: "standard") | COMBO | Evet | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Kaynak görsele görsel doğruluğa mı yoksa ağ geometrisine hizalamaya mı öncelik verileceğini belirtir. (varsayılan: "original_image") | COMBO | Evet | "original_image"<br>"geometry" |
| `orientation` | Çıktıyı kaynak görsele uyacak şekilde döndürür. Yalnızca doku eklendiğinde geçerlidir. (varsayılan: "default") | COMBO | Evet | "default"<br>"align_image" |
| `texture_seed` | Doku üretimi için kullanılan tohum. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

**Not:** En az 2 görsel sağlamalısınız: ön görünüm (`image`) ve diğer görünümlerden en az biri (`image_left`, `image_back` veya `image_right`). 2'den az görsel sağlanırsa node bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan GLB modelinin dosya adı (yalnızca geriye dönük uyumluluk içindir). | STRING |
| `model_task_id` | Bu model üretim isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `c26bf9d46f6b95ec57e4eb663cb6c602035c3ad00682e7f9622ce575ff54d228`
