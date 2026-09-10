# Pixal3DConditioning

Bu düğüm, Trellis2 3D üretim hattı için görüntü koşullandırmasını hazırlar. Girdi görüntüsünden, DINOv3 görü modeliyle iki çözünürlükte görsel öznitelikler çıkarır; bunları aşama başına öznitelik haritaları halinde düzenler (isteğe bağlı olarak bir NAF modeliyle geliştirilir) ve yatay görüş alanından türetilen kamera verileriyle birleştirir. Sınıflandırıcısız yönlendirme için negatif tarafın sıfırlanmış öznitelikler kullandığı bir pozitif ve bir negatif koşullandırma çifti çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Evet | — |
| `görüntü` | ImageCropToMask çıktısı olan ön işlenmiş görüntü (Pixal3D için pad_factor=1.1). | IMAGE | Evet | — |
| `camera_angle_x` | Derece cinsinden yatay görüş alanı (görünen ad: fov). Görüntü başına FoV için bir MoGeGeometryToFOV (axis='horizontal', unit='degrees') bağlayın (üst akış varsayılanıyla uyumludur). Varsayılan: 49.13. | FLOAT | Evet | 1.0 – 170.0 |

Not: `camera_angle_x` değeri dahili olarak radyana dönüştürülür ve projeksiyon dönüşüm matrisi için kamera mesafesini hesaplamakta kullanılır. Sağlanan görü modeli bir NAF bileşeni içerdiğinde, düğüm ayrıca şekil ve doku aşamaları için yüksek çözünürlüklü öznitelik haritaları üretir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Trellis2 üretimi için görüntüden türetilmiş öznitelik haritalarını ve projeksiyon verilerini içeren pozitif koşullandırma. | CONDITIONING |
| `negatif` | Sınıflandırıcısız yönlendirme için kullanılan, sıfırlanmış öznitelik tensörlerine sahip negatif koşullandırma. | CONDITIONING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
