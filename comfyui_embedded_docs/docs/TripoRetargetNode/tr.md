# Tripo: Riglenmiş Modeli Yeniden Hedefle

TripoRetargetNode, mevcut bir riglenmiş 3B modele ön ayarlı bir animasyon uygular. Daha önce riglenmiş bir modelin görev kimliğini alır, Tripo API'sine bir yeniden hedefleme isteği gönderir ve ortaya çıkan animasyonlu dosyayı indirir. Animasyonlu model, isteğe bağlı mesh geometrisi ve isteğe bağlı yerinde oynatma ile birlikte GLB veya FBX olarak döndürülebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `orijinal_model_görev_id` | Yeniden hedeflenecek, daha önce riglenmiş 3B modelin görev kimliği. Başvurulan görev bir rig görevi olmalıdır. | RIG_TASK_ID | Evet | - |
| `animasyon` | Riglenmiş modele uygulanacak animasyon ön ayarı. `preset:*` animasyonları her iki rig modeliyle de çalışır. `preset:biped:*` animasyonları model v1.0-20240301'den gelen rigler için yapılmıştır; bir v2.5 rig yalnızca chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn ve walk animasyonlarını kabul eder. | COMBO | Evet | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>ayrıca kullanıcı arayüzünde gösterilen ek `"preset:biped:*"` seçenekleri |
| `out_format` | Çıktı dosyası biçimi; sonuç eşleşen çıktıya gelir. (varsayılan: glb) | COMBO | Hayır | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Dışa aktarmaya mesh'i dahil et; kapalıyken yalnızca animasyonlu iskeleti dışa aktarır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `animate_in_place` | Animasyonu kök yer değiştirmesi olmadan yerinde oynat. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `auth_token_comfy_org` | Comfy.org API erişimi için kimlik doğrulama belirteci (gizli parametre). | AUTH_TOKEN_COMFY_ORG | Hayır | - |
| `api_key_comfy_org` | Comfy.org hizmet erişimi için API anahtarı (gizli parametre). | API_KEY_COMFY_ORG | Hayır | - |
| `unique_id` | İşlemi izlemek için benzersiz tanımlayıcı (gizli parametre). | UNIQUE_ID | Hayır | - |

Not: `preset:*` grubundaki animasyonlar her iki rig modeliyle de çalışır. `preset:biped:*` grubundaki animasyonlar model v1.0-20240301'den gelen rigler için yapılmıştır; bir v2.5 rig yalnızca chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn ve walk animasyonlarını kabul eder. Başvurulan rig Mixamo spesifikasyonuyla ve `v1.0` ile başlayan bir model sürümüyle oluşturulmuşsa, yeniden hedefleme çağrısı bir hatayla başarısız olur. İstenen çıktı biçimi GLB veya FBX olmalıdır; hizmet başka bir dosya türü döndürürse düğüm bir hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `retarget_görev_id` | Oluşturulan animasyonlu 3B model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `yeniden hedefleme task_id` | Yeniden hedefleme işlemini izlemek için görev kimliği. | RETARGET_TASK_ID |
| `GLB` | GLB biçimindeki animasyonlu 3B model. `out_format` glb olduğunda doldurulur. | FILE3DGLB |
| `FBX` | FBX biçimindeki animasyonlu 3B model. `out_format` fbx olduğunda doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/tr.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
