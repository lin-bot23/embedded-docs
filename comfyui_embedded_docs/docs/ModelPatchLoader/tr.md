# ModelPatchLoader

ModelPatchLoader düğümü, `model_patches` klasöründen bir model yaması dosyası yükler ve bunu bir iş akışında kullanılmak üzere hazırlar. Dosyada bulunan yamanın türünü otomatik olarak algılar, eşleşen mimariyi oluşturur, kayıtlı ağırlıkları yükler ve diğer modellere uygulanabilmesi için her şeyi bir ModelPatcher'a sarar. Ek ControlNet dalları, özellik katıştırıcı (feature embedder) modelleri, bağdaştırıcılar ve benzer modüller dahil olmak üzere birçok özel yama biçimini destekler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `ad` | `model_patches` dizininden yüklenecek model yaması dosyasının adı. Listede bulunan mevcut yama dosyalarından birini seçin. | COMBO | Evet | `model_patches` klasöründe bulunan tüm model yaması dosyalarının dinamik olarak oluşturulan listesi |

Not: Bu düğüm deneysel olarak işaretlenmiştir. Yama türü dosya içeriğinden otomatik olarak algılanır, bu nedenle manuel tür seçimi gerekmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `MODEL_PATCH` | ModelPatcher ile sarılmış, iş akışındaki bir modele uygulanmaya hazır yüklenmiş model yaması | MODEL_PATCH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/tr.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
