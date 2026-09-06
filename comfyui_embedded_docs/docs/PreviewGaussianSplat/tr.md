# Splat Önizleme

PreviewGaussianSplat düğümü, bir 3B gaussian splat dosyasını ComfyUI çıktı dizinine kaydetmeden bir önizleme penceresinde görüntüler. Çeşitli gaussian splat formatlarındaki bir 3B model dosyasını kabul eder, önizleme için geçici bir kopya kaydeder ve model verilerini iş akışında daha sonraki işlemler için olduğu gibi iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Bir gaussian splat 3B dosyası. | FILE3D | Evet | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | 3B model hakkında isteğe bağlı meta veri bilgisi. Bağlı olmadığında düğüm, `viewport_state` içindeki model bilgisini kullanır. | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | 3B görünüm alanının kamera ve model bilgisi dahil geçerli durumu. | LOAD3D | Evet | - |
| `camera_info` | Önizleme için isteğe bağlı kamera bilgisi. Bağlı olmadığında düğüm, `viewport_state` içindeki kamera bilgisini kullanır. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Önizleme çıktısının piksel cinsinden genişliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |
| `yükseklik` | Önizleme çıktısının piksel cinsinden yüksekliği (varsayılan: 1024). | INT | Evet | 1 ila 4096 |

Not: `camera_info` veya `model_3d_info` sağlanmadığında düğüm, `viewport_state` içinde saklanan kamera ve model bilgilerini kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Girdi olarak verilen 3B gaussian splat dosyası, değiştirilmeden iletilir. | FILE3D |
| `model_3d_info` | 3B model hakkında meta veri bilgisi; girdiden veya görünüm alanı durumundan elde edilir. | LOAD3DMODELINFO |
| `camera_info` | Önizleme için kamera bilgisi; girdiden veya görünüm alanı durumundan elde edilir. | LOAD3DCAMERA |
| `genişlik` | Önizleme çıktısının genişliği. | INT |
| `yükseklik` | Önizleme çıktısının yüksekliği. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/tr.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
