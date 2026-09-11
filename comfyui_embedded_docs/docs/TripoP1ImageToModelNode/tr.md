# Tripo P1: Görüntüden Modele

Tripo P1: Image to Model, tek bir 2B görüntüyü Tripo P1 API'sini kullanarak 3B modele dönüştürür. Düşük poligonlu, oyuna hazır mesh'ler üretmek için optimize edilmiştir ve yalnızca geometriden oluşan bir mesh ile PBR haritaları içeren dokulu bir model arasında seçim yapmanızı sağlar. Tamamlanan model GLB dosyası olarak döndürülür.

## Girdiler

### Ortak Girdiler

Bu parametreler her zaman kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çıktı_modu` | Sonuç türünü seçer. "Geometry only" dokusuz bir mesh döndürür; "Textured" renk/PBR haritaları ekler ve ek doku ayarlarını gösterir. | DYNAMIC_COMBO | Evet | `"Geometry only"`<br>`"Textured"` |
| `görüntü` | 3B modeli oluşturmak için kullanılan kaynak 2B görüntü. Tek bir görüntü gereklidir; hiçbiri sağlanmazsa düğüm bir hata verir. | IMAGE | Evet | - |
| `görüntü_oto_düzeltme_aktif` | Daha iyi oluşturma kalitesi için giriş görüntüsünü ön işleme tabi tutar. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `yüz_sınırı` | Hedef yüz sayısı, 48-20000. -1, Tripo'nun uyarlamalı seçim yapmasını sağlar. (varsayılan: -1) | INT | Hayır | -1 ile 20000 arası |
| `model_tohumu` | Sonuçların yeniden üretilebilmesi için geometri oluşturmada kullanılan tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 arası |
| `oto_boyut` | Çıktıyı gerçek dünya metrelerine yaklaşık olacak şekilde ölçeklendirir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `uv_dışa_aktar` | Oluşturma sırasında UV açılımı yapar. Yalnızca geometri çalıştırmalarında daha hızlı olması için kapatın. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `geometriyi_sıkıştır` | meshopt geometri sıkıştırmasını uygular (EXT_meshopt_compression). Daha küçük dosyalar, ancak ComfyUI'nin 3B önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı açın. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### Yalnızca Geometri Girdileri

Ek parametre yok. Çıktı, dokusuz bir mesh'tir.

### Dokulu Girdiler

Bu parametreler `output_mode` "Textured" olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını dahil eder. Açıldığında, temel doku da zorunlu olarak açılır. (varsayılan: True) | BOOLEAN | Evet | True<br>False |
| `texture_quality` | detailed = HD dokular, extreme = 8K Ultra dokular. (varsayılan: "standard") | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Kaynak görüntüye görsel sadakati veya mesh geometrisine hizalamayı önceliklendirir. (varsayılan: "original_image") | COMBO | Evet | `"original_image"`<br>`"geometry"` |
| `orientation` | Çıktıyı kaynak görüntüyle eşleşecek şekilde döndürür. Yalnızca dokulu olduğunda uygulanır. (varsayılan: "default") | COMBO | Evet | `"default"`<br>`"align_image"` |
| `texture_seed` | Dokulu sonuçların yeniden üretilebilmesi için doku oluşturmada kullanılan tohum. (varsayılan: 42) | INT | Evet | 0 ile 2147483647 arası |

Not: `output_mode` "Geometry only" olduğunda, istek için dokulandırma devre dışı bırakılır. "Textured" modunda, her zaman bir renk dokusu istenir; `pbr` devre dışı bırakıldığında PBR haritaları kaldırılır ancak temel renk dokusu korunur, `pbr` etkinleştirildiğinde ise temel doku da zorunlu olarak açılır. `texture_alignment` ve `orientation` yalnızca "Textured" modunda kullanılabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan model dosya adını içeren bir dize (`<task_id>.glb`). Yalnızca geriye dönük uyumluluk için tutulmuştur. | STRING |
| `model_task_id` | Tamamlanan oluşturma işi için Tripo API tarafından döndürülen benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
