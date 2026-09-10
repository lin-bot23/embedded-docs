# 3D Önizleme (Gelişmiş)

Bu düğüm, dosyayı ComfyUI çıktı dizinine kaydetmeden kullanıcı arayüzünde bir 3B model önizlemesi görüntüler. Modeli geçici bir dosyaya kaydeder ve model verilerini, model bilgilerini, kamera bilgilerini ve önizleme boyutlarını daha sonraki işlemler için iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Önceki 3B düğümünden gelen 3B model dosyası. | FILE3D | Evet | GLB, GLTF, FBX, OBJ, STL, USDZ veya desteklenen herhangi bir 3B format |
| `model_3d_bilgisi` | Sahnedeki her modelin yerleşimi: konum, dönüş ve ölçek (Y-up dünya uzayı). İsteğe bağlı. Gelişmiş seçenek. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | Kamera ve model bilgilerini içeren mevcut görünüm alanı durumu. | LOAD3D | Evet | - |
| `kamera_bilgisi` | Görünüm alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. İsteğe bağlı. Gelişmiş seçenek. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Görünüm alanının piksel cinsinden işleme genişliği. Varsayılan: 1024. | INT | Evet | 1 ile 4096 |
| `yükseklik` | Görünüm alanının piksel cinsinden işleme yüksekliği. Varsayılan: 1024. | INT | Evet | 1 ile 4096 |

Not: `camera_info` veya `model_3d_info` bağlı değilse, değerleri `viewport_state` içinde mevcut olduğunda oradan alınır. Eğer `viewport_state` kamera bilgisi içermiyorsa, `camera_info` None olur. Eğer `viewport_state` model bilgisi içermiyorsa, `model_3d_info` varsayılan olarak boş bir liste olur. Eğer `viewport_state` bir sözlük değilse, boş olarak kabul edilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Önceki 3B düğümünden gelen, değiştirilmeden iletilen 3B model dosyası (glb/obj/stl/vb.). | FILE3D |
| `kamera_bilgisi` | Sahnedeki her modelin yerleşimi: konum, dönüş ve ölçek (Y-up dünya uzayı). Girdi değerini kullanır; aksi durumda `viewport_state` içinde saklanan değere başvurur. | LOAD3DMODELINFO |
| `model_3d_bilgisi` | Görünüm alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. Girdi değerini kullanır; aksi durumda `viewport_state` içinde saklanan değere başvurur. | LOAD3DCAMERA |
| `genişlik` | Görünüm alanının piksel cinsinden işleme genişliği. | INT |
| `yükseklik` | Görünüm alanının piksel cinsinden işleme yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`
