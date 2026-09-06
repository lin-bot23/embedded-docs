# Tripo: Modeli Rigle

Bu düğüm, mevcut bir Tripo 3D modelini alır ve bu modelin riglenmiş bir sürümünü oluşturur; böylece model, animasyon yapılabilmesi için bir iskelete kavuşur. Riglenecek modelin görev kimliğini sağlar; rig sürümünü, iskelet türünü, kemik adlandırma stilini ve çıktı dosyası formatını seçersiniz. Düğüm işi Tripo’ya gönderir, tamamlanana kadar bekler ve indirilen sonucu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | Riglenecek orijinal 3D modelin görev kimliği. Bu genellikle daha önceki bir Tripo model oluşturma düğümü tarafından üretilen kimliktir. | MODEL_TASK_ID | Evet | - |
| `model_version` | Kullanılacak rig modeli sürümü. v1.0: yalnızca insansı (biped) karakterler; 90’dan fazla animasyon ön ayarı. v2.5: insansı olmayan canlılar (quadruped, hexapod, octopod, avian, serpentine, aquatic). Varsayılan: `v1.0-20240301`. | COMBO | Hayır | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | İskelet türü. "auto", önce Tripo’nun ücretsiz rig kontrolünü çalıştırır ve önerilen türü kullanır. Diğer değerler belirli bir iskelet türünü zorlar; örneğin insansı karakterler için biped. Varsayılan: "auto". | COMBO | Hayır | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Kemik adlandırma düzeni: Tripo native veya Mixamo uyumlu. Tripo, animasyon ön ayarlarını mixamo spec ile oluşturulmuş bir v1.0 rig üzerine retarget edemez; Tripo: Retarget rigged model için tripo kullanın. Varsayılan: "tripo". | COMBO | Hayır | "tripo"<br>"mixamo" |
| `out_format` | Çıktı dosyası formatı; sonuç eşleşen çıktıya gelir. Varsayılan: "glb". | COMBO | Hayır | "glb"<br>"fbx" |

**Not:** v1.0 model sürümü (`v1.0-20240301`) yalnızca biped iskeletlerini destekler. Bu sürümle biped olmayan bir `rig_type` kullanılırsa düğüm hata verir ve bunun yerine `v2.5-20260210` kullanmanızı söyler.

**Not:** `rig_type` "auto" olduğunda Tripo önce modelin riglenip riglenemeyeceğini kontrol eder ve önerilen iskelet türünü seçer. Tripo, modelin riglenemeyeceğini bildirirse düğüm hata vererek başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan riglenmiş 3D model dosyası. Yalnızca geriye dönük uyumluluk için korunur. | STRING |
| `rig task_id` | Rig oluşturma sürecini izlemek için görev kimliği. | RIG_TASK_ID |
| `GLB` | Riglenmiş model, GLB 3D dosyası olarak. `out_format` "glb" olduğunda doldurulur. | FILE3DGLB |
| `FBX` | Riglenmiş model, FBX 3D dosyası olarak. `out_format` "fbx" olduğunda doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/tr.md)

---
**Source fingerprint (SHA-256):** `54c3b0984835160b74884d2c30191ad6dac6ea447862e9276253ace7367bc419`
