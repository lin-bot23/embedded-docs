# 3D Önizleme (Gelişmiş)

Bu düğüm, dosyayı ComfyUI çıktı dizinine kaydetmeden kullanıcı arayüzünde bir 3D model önizlemesi görüntüler. Modeli geçici bir dosyaya kaydeder ve model verilerini, model bilgilerini, kamera bilgilerini ve önizleme boyutlarını daha sonraki işlem adımlarına iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir önceki 3D düğümünden alınan 3D model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ veya desteklenen herhangi bir 3D formatı |
| `model_3d_info` | İsteğe bağlı model bilgisi meta verisi. Gelişmiş seçenek. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgilerini içeren mevcut görünüm alanı durumu. | LOAD3D | Evet | - |
| `camera_info` | 3D görünümü için isteğe bağlı kamera yapılandırması. Gelişmiş seçenek. | LOAD3DCAMERA | Hayır | - |
| `width` | Önizleme genişliği piksel cinsinden. Varsayılan: 1024. | INT | Evet | 1 ile 4096 |
| `height` | Önizleme yüksekliği piksel cinsinden. Varsayılan: 1024. | INT | Evet | 1 ile 4096 |

Not: `camera_info` veya `model_3d_info` bağlanmadığında, değerleri mevcutsa `viewport_state` içinden alınır. `viewport_state` içinde kamera bilgisi yoksa `camera_info` değeri `None` olur. `viewport_state` içinde model bilgisi yoksa `model_3d_info` varsayılan olarak boş bir liste olur. `viewport_state` bir sözlük değilse boş kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Girdiden iletilen 3D model dosyası. | FILE3D |
| `model_3d_info` | Girdiden veya görünüm alanı durumundan alınan model bilgisi meta verisi. | LOAD3DMODELINFO |
| `camera_info` | Girdiden veya görünüm alanı durumundan alınan kamera yapılandırması. | LOAD3DCAMERA |
| `width` | Önizleme genişliği piksel cinsinden. | INT |
| `height` | Önizleme yüksekliği piksel cinsinden. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `46c14d6242cbcabd457e13ae193427bb4c1fed55e81e568d50719fff0f1a95a0`
