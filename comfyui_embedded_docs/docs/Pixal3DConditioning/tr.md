# Pixal3DConditioning

## Özet

Pixal3DConditioning düğümü, Trellis2 3D oluşturma pipeline'ı için görüntü koşullandırma hazırlamak için tasarlanmıştır. DINOv3 görsel modelini kullanarak girdi görüntüsünden iki çözünürlükte görsel özellikler çıkarır. Bu özellikler, isteğe bağlı olarak NAF modeli ile güçlendirilmiş olarak her aşamaya özel özellik haritalarına organize edilir. Düğüm, yatay açısal genişlikten elde edilen kamera verilerini kullanarak projeksiyon dönüş matrisini hesaplamak için entegre edilmiştir. Düğüm, görüntüden elde edilen özellik haritaları ve projeksiyon verilerini içeren pozitif koşullandırma çifti ile birlikte, sınıflandırıcısız rehberlik için sıfırlanmış özellik tensorları içeren negatif koşullandırma çifti üretir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | Görüntü özellik çıkarımı için kullanılan DINOv3 ViT-L/16 ClipVision modeli. | CLIP_VISION | Evet | — |
| `görüntü` | ImageCropToMask düğümünden gelen ön işlenmiş görüntü, Pixal3D için bir pad_factor'ı 1.1 olan amaçlanmıştır. | GÖRÜNTÜ | Evet | — |
| `camera_angle_x` | Derecelerde yatay açısal genişlik. Bu parametre, her görüntü için bir açısal genişlik için MoGeGeometryToFOV düğümüne bağlanabilir. Standart: 49.13. | FLOAT | Evet | 1.0 – 170.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Trellis2 oluşturma için görüntüden elde edilen özellik haritaları ve projeksiyon verilerini içeren pozitif koşullandırma çıktısı. | KOŞULLANDIRMA |
| `negatif` | Sınıflandırıcısız rehberlik için sıfırlanmış özellik tensorları içeren negatif koşullandırma çıktısı. | KOŞULLANDIRMA |

Not: `camera_angle_x` değeri içsel olarak radianlara dönüştürülür ve projeksiyon dönüş matrisi için kamera mesafesi hesaplanmak üzere kullanılır. Sağlanan görüntü modeli NAF bileşeni içeriyorsa, düğüm, şekil ve tekstür aşamaları için yüksek çözünürlüklü özellik haritaları da üretir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
