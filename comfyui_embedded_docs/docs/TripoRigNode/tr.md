# Tripo: Modeli Rigle

Bu düğüm, mevcut bir Tripo 3D modelini alır ve onun riglenmiş bir sürümünü oluşturur; yani model, canlandırılabilmesi için bir iskelet kazanır. Riglenecek modelin görev kimliğini sağlar, rig sürümünü, iskelet türünü, kemik adlandırma stilini ve çıktı dosyası biçimini seçersiniz; düğüm işi Tripo'ya gönderir, tamamlanmasını bekler ve ardından indirilen sonucu döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `orijinal_model_görev_id` | Riglenecek orijinal 3D modelin görev kimliği. Bu genellikle daha önceki bir Tripo model oluşturma düğümü tarafından üretilen kimliktir. | MODEL_TASK_ID | Evet | - |
| `model_version` | Kullanılacak rig model sürümü. v1.0: yalnızca insansı (biped) karakterler, 90+ animasyon ön ayarı. v2.5: insan dışı yaratıklar (quadruped, hexapod, octopod, avian, serpentine, aquatic). Varsayılan: `v1.0-20240301`. | COMBO | Hayır | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | İskelet türü. "auto", önce Tripo'nun ücretsiz rig kontrolünü çalıştırır ve önerilen türü kullanır. Varsayılan: "auto". | COMBO | Hayır | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Kemik adlandırma: Tripo yerel veya Mixamo uyumlu. Tripo, animasyon ön ayarlarını mixamo spec ile oluşturulmuş bir v1.0 rig üzerine yeniden hedefleyemez; Tripo: Retarget rigged model için tripo kullanın. Varsayılan: "tripo". | COMBO | Hayır | "tripo"<br>"mixamo" |
| `out_format` | Çıktı dosyası biçimi; sonuç eşleşen çıktıya gelir. Varsayılan: "glb". | COMBO | Hayır | "glb"<br>"fbx" |

**Not:** v1.0 model sürümü (`v1.0-20240301`) yalnızca biped iskeletleri destekler. Bu sürümle biped olmayan bir `rig_type` kullanılırsa, düğüm bir hata verir ve bunun yerine `v2.5-20260210` kullanmanızı söyler.

**Not:** `rig_type` "auto" olduğunda, Tripo önce modelin riglenip riglenemeyeceğini kontrol eder ve önerilen iskelet türünü seçer. Tripo modelin riglenemeyeceğini bildirirse, düğüm bir hatayla başarısız olur.

**Not:** Düğüm, Tripo'nun bir GLB veya FBX dosyası döndürmesini bekler. Tripo başka bir dosya türü döndürürse, düğüm bir hata verir.

**Not:** Yalnızca `out_format` ile eşleşen çıktı doldurulur: `out_format` "glb" olduğunda `GLB`, `out_format` "fbx" olduğunda `FBX`. Diğer 3D çıktısı boş kalır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan riglenmiş model dosyası adı (görev kimliği artı biçim uzantısı). Yalnızca geriye dönük uyumluluk için tutulur. | STRING |
| `rig_görev_id` | Rig oluşturma sürecini izlemek için görev kimliği. | RIG_TASK_ID |
| `GLB` | GLB 3D dosyası olarak riglenmiş model. `out_format` "glb" olduğunda doldurulur. | FILE3DGLB |
| `FBX` | FBX 3D dosyası olarak riglenmiş model. `out_format` "fbx" olduğunda doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/tr.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
