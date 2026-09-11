# Tripo P1: Çoklu Görünüşten Modele

Bu düğüm, bir nesnenin veya karakterin iki ila dört referans görüntüsünden 3D model oluşturur. Ön görünümü ve sol, arka ve sağ görünümlerden herhangi bir kombinasyonu sağlayın; düğüm, yeniden oluşturulan özneyi GLB mesh olarak döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Ön görünüm (0°). Gerekli. | IMAGE | Evet | - |
| `görüntü_sol` | Sol görünüm (90°), yani öznenin sol tarafı. | IMAGE | Hayır | - |
| `görüntü_arka` | Arka görünüm (180°). | IMAGE | Hayır | - |
| `görüntü_sağ` | Sağ görünüm (270°), yani öznenin sağ tarafı. | IMAGE | Hayır | - |
| `çıktı_modu` | Oluşturulacak model türünü seçin. `"Geometry only"` dokusuz bir mesh döndürür. `"Textured"` renk/PBR haritaları ekler. | DYNAMIC_COMBO | Evet | "Geometry only"<br>"Textured" |
| `yüz_sınırı` | Hedef yüz sayısı, 48-20000. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar. (varsayılan: -1) | INT | Hayır | -1 ile 20000 |
| `model_tohumu` | Tekrarlanabilir model oluşturma için tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `oto_boyut` | Çıktıyı yaklaşık gerçek dünya metrelerine göre ölçeklendirir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `uv_dışa_aktar` | Oluşturma sırasında UV açımı uygular. Daha hızlı yalnızca geometri çalıştırmaları için kapatın. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `geometriyi_sıkıştır` | meshopt geometri sıkıştırmasını uygular (EXT_meshopt_compression). Daha küçük dosyalar, ancak ComfyUI'nin 3D önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı açın. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### Yalnızca Geometri Girdileri

Bu mod için ek girdi gösterilmez. Oluşturulan model doku olmadan döndürülür.

### Dokulu Girdileri

Bu girdiler `output_mode` değeri `"Textured"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını dahil et. Açık olduğunda temel doku da zorunlu olarak açılır. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `texture_quality` | Doku kalite düzeyi. `detailed` = HD dokular, `extreme` = 8K Ultra dokular. (varsayılan: "standard") | COMBO | Evet | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Kaynak görüntüye görsel sadakati ya da mesh geometrisine hizalamayı önceliklendirir. (varsayılan: "original_image") | COMBO | Evet | "original_image"<br>"geometry" |
| `orientation` | Çıktıyı kaynak görüntüyle eşleşecek şekilde döndürür. Yalnızca dokulu olduğunda geçerlidir. (varsayılan: "default") | COMBO | Evet | "default"<br>"align_image" |
| `texture_seed` | Doku oluşturmada kullanılan tohum. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 |

**Not:** En az 2 görüntü sağlamalısınız: ön görünüm (`image`) artı diğer görünümlerden (`image_left`, `image_back` veya `image_right`) en az biri. 2'den az görüntü sağlanırsa düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan GLB modelinin dosya adı (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_task_id` | Bu model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3D model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `1153f74ac76603829142959844e701f3c8f16be080e3de849951cffdda322d12`
