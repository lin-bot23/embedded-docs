# Tripo P1: Görüntüden Modele

Tripo P1: Image to Model, Tripo P1 API'sini kullanarak tek bir 2D görüntüyü 3D modele dönüştürür. Düşük poligonlu, oyuna hazır mesh'ler üretmek için optimize edilmiştir ve yalnızca geometri içeren bir mesh ile PBR haritalı dokulu bir model arasında seçim yapmanızı sağlar. Tamamlanan model GLB dosyası olarak döndürülür.

## Girdiler

### Ortak Girdiler

Bu parametreler her zaman kullanılabilir.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çıktı_modu` | Sonucun türünü seçer. "Geometry only" dokusuz bir mesh döndürür; "Textured" renk ve PBR haritaları ekler ve ek doku ayarlarını ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"Geometry only"`<br>`"Textured"` |
| `görüntü` | 3D modeli oluşturmak için kullanılan kaynak 2D görüntü. Düğüm tek bir görüntü gerektirir ve hiçbir görüntü sağlanmazsa hata verir. | IMAGE | Evet | - |
| `görüntü_oto_düzeltme_aktif` | Daha iyi üretim kalitesi için girdi görüntüsünü ön işler. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `yüz_sınırı` | Hedef yüz sayısı, 48-20000. -1 değeri Tripo'nun uyarlamalı seçim yapmasını sağlar. (varsayılan: -1) | INT | Hayır | -1 ile 20000 |
| `model_tohumu` | Sonuçların yeniden üretilebilmesi için geometri üretiminde kullanılan tohum değeri. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `oto_boyut` | Çıktıyı gerçek dünya metrelerine yaklaşık olarak ölçekler. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `uv_dışa_aktar` | Üretim sırasında UV açılımı (unwrap) uygular. Yalnızca geometri içeren işlemleri hızlandırmak için kapatın. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `geometriyi_sıkıştır` | meshopt geometri sıkıştırması (EXT_meshopt_compression) uygular. Dosyalar daha küçük olur ancak ComfyUI'nin 3D önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı çözün. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

### Dokulu Girdiler

Bu parametreler `output_mode` "Textured" olarak ayarlandığında görünür. "Geometry only" modunda ek parametre yoktur.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını dahil eder. Açıkken temel doku da zorunlu olarak açılır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `texture_quality` | Doku çözünürlük düzeyi. "detailed" = HD dokular, "extreme" = 8K Ultra dokular. (varsayılan: "standard") | COMBO | Hayır | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | Kaynak görüntüye görsel sadakati mi, yoksa mesh geometrisiyle uyumu mu önceliklendireceğini belirler. (varsayılan: "original_image") | COMBO | Hayır | `"original_image"`<br>`"geometry"` |
| `orientation` | Çıktıyı kaynak görüntüye uyacak şekilde döndürür. Yalnızca dokulu modda geçerlidir. (varsayılan: "default") | COMBO | Hayır | `"default"`<br>`"align_image"` |
| `texture_seed` | Dokulu sonuçların yeniden üretilebilmesi için doku üretiminde kullanılan tohum değeri. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |

Not: `output_mode` "Geometry only" olduğunda bu istek için dokulama devre dışıdır. "Textured" modunda her zaman renkli bir doku istenir; `pbr` kapatıldığında PBR haritaları kaldırılır ancak temel renk dokusu korunur, `pbr` açıldığında ise temel doku da zorunlu olarak açılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3D model sonucu. Yalnızca geriye dönük uyumluluk için saklanır. | STRING |
| `model_task_id` | Tripo API tarafından tamamlanan üretim işi için döndürülen benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3D model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `db5dc76518a4efcd28d388dc00ad0810f619481482f20fa456c4ff2478192aa3`
