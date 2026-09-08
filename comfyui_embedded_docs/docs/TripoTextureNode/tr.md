# Tripo: Doku modeli

TripoTextureNode, Tripo API'yi kullanarak mevcut bir Tripo 3D modeline dokular ekler. Başka bir Tripo düğümü tarafından oluşturulan bir modelin görev kimliğini (task ID) alır ve doku işi tamamlandıktan sonra dokulu bir GLB veya FBX modeli döndürür. Malzeme haritalarını, doku kalitesini, hizalamayı, seed'i kontrol edebilir ve dokuları bir metin istemi, bir stil görseli veya referans görsellerle yönlendirebilirsiniz.

## Girdiler

### Ortak Girdiler

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model_görev_id` | Dokulanacak modelin Tripo görev kimliği. Model görev kimliklerini ve segmentasyon görev kimliklerini kabul eder. | MODEL_TASK_ID | Evet | - |
| `doku` | Yoksayılır: bu düğüm her zaman dokular oluşturur. Eski iş akışları için korunmuştur. (varsayılan: True) | BOOLEAN | Hayır | true<br>false |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal); kapalı düz renk doku verir. (varsayılan: True) | BOOLEAN | Hayır | true<br>false |
| `doku_tohumu` | Doku oluşturma için rastgele seed. Aynı girdilerle aynı seed'i kullanmak aynı sonucu üretir. (varsayılan: 42) | INT | Hayır | 0 – 2147483647 |
| `doku_kalitesi` | Doku çözünürlük kalitesi: detailed = HD dokular, extreme = 8K Ultra dokular. (varsayılan: "standard"). Yaklaşık maliyet: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `doku_hizalama` | Oluşturulan dokuları modele hizalamak için kullanılan yöntem. (varsayılan: "original_image"). | COMBO | Hayır | "original_image"<br>"geometry" |
| `texture_prompt` | Dokulama için isteğe bağlı metin rehberi. Pratikte renk çıkarımı yapılacak kaynak görseli taşımayan içe aktarılan modeller (Tripo: Import Model) için gereklidir. Referans görsellerle kombinlenemez. (varsayılan: "") | STRING | Hayır | - |
| `model_version` | Doku modeli: v3.x ile oluşturulan mesh'ler için v3.0, v2.5 ile oluşturulan mesh'ler için v2.5. (varsayılan: en son v3.0 sürümü) | COMBO | Hayır | Multiple options available |
| `style_image` | Dokuların sanatsal stili için referans görsel. Yalnızca `texture_prompt` ile birlikte kullanılır. | IMAGE | Hayır | - |
| `referans` | Dokuları yönlendiren referans görseller. `texture_prompt` veya `style_image` ile kombinlenemez. (varsayılan: "none") | DYNAMIC_COMBO | Hayır | "none"<br>"image"<br>"multiview" |
| `part_names` | Dokulanacak Tripo: Segment Model'den virgülle ayrılmış parça adları. Boş bırakılırsa her parçayı dokular. (varsayılan: "") | STRING | Hayır | - |

### "image" Referans Girdileri

Bu girdiler `reference` `"image"` olarak ayarlandığında kullanılabilir.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `reference_image` | Dokuların takip etmesi gereken tek referans görsel. | IMAGE | Hayır | - |

### "multiview" Referans Girdileri

Bu girdiler `reference` `"multiview"` olarak ayarlandığında kullanılabilir.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image_front` | Ön görünüm (0°). | IMAGE | Hayır | - |
| `image_left` | Sol görünüm (90°). | IMAGE | Hayır | - |
| `image_back` | Arka görünüm (180°). | IMAGE | Hayır | - |
| `image_right` | Sağ görünüm (270°). | IMAGE | Hayır | - |

**Not:** `"image"` ve `"multiview"` referans modları, boş olmayan bir `texture_prompt` veya `style_image` ile kombinlenemez. `style_image` girdisi, boş olmayan bir `texture_prompt` gerektirir. `texture_prompt` boş bırakıldığında, kaynak modelin zaten kendi kaynak görseline sahip olması gerekir (örneğin, text-to-model, image-to-model, multiview-to-model veya önceki bir dokulama görevi tarafından üretilen modeller). Kaynak görsel taşımayan modeller — örneğin içe aktarılan, segmente edilen, tamamlanan veya retopolojize edilen modeller — bir `texture_prompt` ile dokulanmalıdır; referans görseller yalnızca Tripo API'nin kendi oluşturduğu modeller için kabul edilir.

## Çıktılar

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_görev_id` | Tamamlanan doku oluşturma görevinin görev kimliği, diğer Tripo düğümleri için girdi olarak kullanılabilir. | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan dokulu model. Kaynak bir quad mesh veya bir FBX içe aktarma ise boş olur. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan dokulu model. Tripo, quad mesh'ler ve FBX içe aktarmaları için FBX döndürür; aksi halde boş olur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/tr.md)

---
**Source fingerprint (SHA-256):** `815c22a9d8f4785ef5219789e0f2eee804776ec7e4752099ec0db0a2b5ad4bb2`
