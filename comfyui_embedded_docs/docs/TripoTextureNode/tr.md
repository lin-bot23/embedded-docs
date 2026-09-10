# Tripo: Doku modeli

Tripo: Texture model (Legacy) düğümü, Tripo API aracılığıyla mevcut bir Tripo 3D modeline dokular ekler. Başka bir Tripo düğümü tarafından oluşturulan bir modelin görev kimliğini alır ve doku işi tamamlandığında dokulandırılmış bir GLB veya FBX modeli döndürür. Malzeme haritalarını, doku kalitesini, hizalamayı ve seed'i kontrol edebilir; dokuları bir metin istemi, bir stil görseli veya referans görsellerle yönlendirebilirsiniz. Bu düğüm, doku aracının eski (legacy) bir sürümüdür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_görev_id` | Dokulandırılacak modelin Tripo görev kimliği. Model görev kimliklerini ve segmentasyon görev kimliklerini kabul eder. | MODEL_TASK_ID, SEGMENT_TASK_ID | Evet | - |
| `doku` | Yok sayılır: bu düğüm her zaman dokular üretir. Eski iş akışları için tutulmuştur. (varsayılan: True) | BOOLEAN | Hayır | true<br>false |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal); kapalı olduğunda düz renkli bir doku verir. (varsayılan: True) | BOOLEAN | Hayır | true<br>false |
| `doku_tohumu` | Doku oluşturma için rastgele seed. (varsayılan: 42) | INT | Hayır | 0 – 2147483647 |
| `doku_kalitesi` | Doku çözünürlüğü kalitesi: detailed = HD dokular, extreme = 8K Ultra dokular. (varsayılan: "standard"). Yaklaşık maliyet: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `doku_hizalama` | Oluşturulan dokuları modele hizalamak için kullanılan yöntem. (varsayılan: "original_image") | COMBO | Hayır | "original_image"<br>"geometry" |
| `texture_prompt` | Dokulandırma için isteğe bağlı metin yönlendirmesi. İçe aktarılan modeller (Tripo: Import Model) için pratikte gereklidir; bu modellerde renklerin çıkarılacağı bir kaynak görsel bulunmaz. Referans görsellerle birlikte kullanılamaz. (varsayılan: "") | STRING | Hayır | - |
| `model_version` | Doku modeli: v3.x ile oluşturulan mesh'ler için v3.0, v2.5 ile oluşturulan mesh'ler için v2.5. (varsayılan: v3.0_20250812) | COMBO | Hayır | Birden fazla seçenek mevcut |
| `style_image` | Dokuların sanatsal stili için referans görsel. Yalnızca `texture_prompt` ile birlikte kullanılır. | IMAGE | Hayır | - |
| `referans` | Dokulara yönlendirme yapan referans görseller. `texture_prompt` veya `style_image` ile birlikte kullanılamaz. (varsayılan: "none") | DYNAMIC_COMBO | Hayır | "none"<br>"image"<br>"multiview" |
| `part_names` | Tripo: Segment Model'den dokulandırılacak virgülle ayrılmış parça adları. Boş bırakılırsa her parça dokulandırılır. (varsayılan: "") | STRING | Hayır | - |

### `image` Referans Girdileri

Bu girdiler, `reference` `"image"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Dokuların takip etmesi gereken tek referans görsel. | IMAGE | Evet | - |

### `multiview` Referans Girdileri

Bu girdiler, `reference` `"multiview"` olarak ayarlandığında kullanılabilir.

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Ön görünüm (0°). | IMAGE | Evet | - |
| `image_left` | Sol görünüm (90°). | IMAGE | Evet | - |
| `image_back` | Arka görünüm (180°). | IMAGE | Evet | - |
| `image_right` | Sağ görünüm (270°). | IMAGE | Evet | - |

**Not:** `"image"` ve `"multiview"` referans modları, boş olmayan bir `texture_prompt` veya `style_image` ile birlikte kullanılamaz. `style_image` girdisi, boş olmayan bir `texture_prompt` gerektirir. `texture_prompt` boş bırakıldığında, kaynak modelin kendi kaynak görseline zaten sahip olması gerekir (örneğin, metinden modele, görselden modele, çoklu görünümden modele veya daha önceki bir dokulandırma görevi tarafından üretilen modeller). Kaynak görsel taşımayan modeller — içe aktarılmış, segmentlenmiş, tamamlanmış veya yeniden topolojilendirilmiş modeller gibi — bir `texture_prompt` ile dokulandırılmalıdır; referans görseller yalnızca Tripo API'nin kendisinin oluşturduğu modeller için kabul edilir. Her parçayı dokulandırmak için `part_names` girdisi boş bırakılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_görev_id` | Tamamlanan doku oluşturma görevinin görev kimliği; diğer Tripo düğümleri için girdi olarak kullanılabilir. | MODEL_TASK_ID |
| GLB | GLB formatında oluşturulan dokulandırılmış model. Kaynak bir quad mesh veya FBX içe aktarımı olduğunda boştur. | FILE3DGLB |
| FBX | FBX formatında oluşturulan dokulandırılmış model. Tripo, quad mesh'ler ve FBX içe aktarımları için FBX döndürür; diğer durumlarda boştur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
