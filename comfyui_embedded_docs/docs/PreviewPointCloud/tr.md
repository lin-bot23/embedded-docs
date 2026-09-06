# Nokta Bulutu Önizleme

Preview Point Cloud düğümü, bir 3D nokta bulutu dosyasını ComfyUI çıktı dizinine kaydetmeden ComfyUI arayüzünde görüntülemenizi sağlar. Nokta bulutunu geçici bir konuma kaydeder ve 3D önizleme penceresinde görüntüler; ayrıca model verilerini, model bilgilerini, kamera bilgilerini ve önizleme boyutlarını daha sonraki işlemler için iletir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Nokta bulutu dosyası (.ply) | FILE3D | Evet | - |
| `model_3d_info` | 3D model hakkında bilgi | LOAD3DMODELINFO | Hayır | - |
| `viewport_state` | 3D görünüm alanının güncel durumu | LOAD3D | Evet | - |
| `camera_info` | 3D görünüm için kamera bilgisi | LOAD3DCAMERA | Hayır | - |
| `width` | Önizleme penceresinin genişliği (varsayılan: 1024) | INT | Evet | 1 ile 4096 |
| `height` | Önizleme penceresinin yüksekliği (varsayılan: 1024) | INT | Evet | 1 ile 4096 |

Not: `model_3d_info` ve `camera_info`, isteğe bağlı gelişmiş girdilerdir. Bağlı olmadıklarında düğüm, `viewport_state` içinde saklanan karşılık gelen değerleri kullanır. Nokta bulutu dosyası, çıktı dizinine değil ComfyUI geçici dizinine yazılır. Bu bir çıktı (terminal) düğümüdür; bu nedenle öncelikle arayüzde önizlemeyi görüntülemek için kullanılır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | Nokta bulutu model verileri | FILE3D |
| `model_3d_info` | 3D model hakkında bilgi | LOAD3DMODELINFO |
| `camera_info` | 3D görünüm için kamera bilgisi | LOAD3DCAMERA |
| `width` | Önizleme penceresinin genişliği | INT |
| `height` | Önizleme penceresinin yüksekliği | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/tr.md)

---
**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`
