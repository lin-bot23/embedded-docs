# Tripo: Riglenmiş Modeli Yeniden Hedefle

TripoRetargetNode, önceden riglenmiş bir 3D modele hazır bir animasyon uygular. Daha önce riglenmiş bir modelin görev kimliğini alır, Tripo API'sine bir yeniden hedefleme (retarget) isteği gönderir ve elde edilen animasyonlu dosyayı indirir. Animasyonlu model; isteğe bağlı mesh geometrisi ve isteğe bağlı yerinde oynatma ile GLB veya FBX olarak döndürülebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | Yeniden hedefleme yapılacak, daha önce riglenmiş 3D modelin görev kimliği. Referans verilen görev bir rig görevi olmalıdır; Mixamo spec ile model sürümü v1.0 üzerinde oluşturulmuş bir rig, yeniden hedefleme için kullanılamaz. | RIG_TASK_ID | Evet | - |
| `animation` | Riglenmiş modele uygulanacak animasyon ön ayarı. `preset:*` animasyonları her iki rig modeliyle de çalışır; `preset:biped:*` animasyonları, model v1.0-20240301 ile oluşturulmuş bir rig gerektirir. | COMBO | Evet | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>ayrıca UI'da gösterilen ek `"preset:biped:*"` seçenekleri |
| `out_format` | Çıktı dosyası biçimi; sonuç eşleşen çıktıya ulaşır. (varsayılan: glb) | COMBO | Hayır | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Dışa aktarıma mesh'i dahil eder; kapalıyken yalnızca animasyonlu iskelet dışa aktarılır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `animate_in_place` | Animasyonu, kök yer değiştirmesi olmadan yerinde oynatır. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `auth_token_comfy_org` | Comfy.org API erişimi için kimlik doğrulama token'ı (gizli parametre). | AUTH_TOKEN_COMFY_ORG | Hayır | - |
| `api_key_comfy_org` | Comfy.org hizmet erişimi için API anahtarı (gizli parametre). | API_KEY_COMFY_ORG | Hayır | - |
| `unique_id` | İşlemi izlemek için benzersiz tanımlayıcı (gizli parametre). | UNIQUE_ID | Hayır | - |

Not: `preset:*` grubundaki animasyonlar her iki rig modeliyle de çalışırken, `preset:biped:*` grubundaki animasyonlar model v1.0-20240301 ile oluşturulmuş bir rig gerektirir. Referans verilen rig, Mixamo spec ve `v1.0` ile başlayan bir model sürümü kullanılarak oluşturulmuşsa, yeniden hedefleme çağrısı bir hatayla başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_file` | Oluşturulan animasyonlu 3D model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `retarget task_id` | Yeniden hedefleme işlemini izlemek için görev kimliği. | RETARGET_TASK_ID |
| `GLB` | GLB biçiminde animasyonlu 3D model. `out_format` glb olduğunda doldurulur. | FILE3DGLB |
| `FBX` | FBX biçiminde animasyonlu 3D model. `out_format` fbx olduğunda doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/tr.md)

---
**Source fingerprint (SHA-256):** `e5417a8fa584285ba9e57526e65b091c2383374c70364df9053777a3ce09541a`
