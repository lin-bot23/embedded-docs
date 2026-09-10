# LTXVSeparateGeneratedKeyframes

## Genel Bakış

LTXV Ayrı Oluşturulan Anahtar Kırmızılar düğümü, örneklenen latent ve koşullamadan oluşturulan anahtar kırmızıları çıkararak, video latent'in uzayda yükseltmeden önce ayrı olarak işlemesine olanak tanır. Uzayda yükseltmeden önce kullanılmak üzere tasarlanmıştır ve LTXV Kesim Rehberleri'nden sonra çalıştırılmamalıdır, çünkü oluşturulan anahtar kırmızıları atıl rehberler olarak görür ve onları atar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pozitif` | Oluşturulan-anahtar-kırmızı metadata'sız pozitif koşullama. | CONDITIONING | Evet | N/A |
| `negatif` | Oluşturulan-anahtar-kırmızı metadata'sız negatif koşullama. | CONDITIONING | Evet | N/A |
| `latent` | Oluşturulan anahtar kırmızıları çıkarılmış video latent. | LATENT | Evet | N/A |
| `keyframes_to_batch` | Anahtar kırmızıları tek çerçeve latent'ler olarak bir grup olarak döndür. Grup olarak döndürmek için kaldırın, bu da latent yükseltici ve daha sonra Oluşturulan Anahtar Kırmızıları Ekle düğme tarafından beklenen tek çerçeve latent'tir. | BOOLEAN | Hayır | varsayılan: False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Oluşturulan-anahtar-kırmızı metadata'sız pozitif koşullama. | CONDITIONING |
| `negatif` | Oluşturulan-anahtar-kırmızı metadata'sız negatif koşullama. | CONDITIONING |
| `latent` | Oluşturulan anahtar kırmızıları çıkarılmış video latent. | LATENT |
| `anahtar kareler` | Çıkarılan anahtar kırmızılar, generated_keyframe_indices ve generated_keyframe_num_frames ile etiketlenmiş. Bu anahtar kırmızıları daha sonra Oluşturulan Anahtar Kırmızıları Ekle düğmesine beslemek için yeni slotlar oluşturmak veya dondurulmuş resim rehberleri olarak pinlemek için kullanın (çerçeve uzunluğu değiştiğinde indeksler yeniden haritalandırılır). | LATENT |

## Notlar

- `keyframes_to_batch` parametresi, anahtar kırmızılarının tek çerçeve latent'ler olarak bir grup olarak döndürülüp döndürülmediğini belirler.
- Düğüm, oluşturulan anahtar kırmızının koşullamadan ve latent'ten çıkarıldığını sağlar.
- `keyframes` çıktısı, yeni oluşturulan anahtar kırmızıları için yeni slotlar oluşturmak veya dondurulmuş resim rehberleri olarak pinlemek için kullanılabilir.
- Düğüm, latent'te oluşturulan anahtar kırmızının olmadığı veya kırmızının beklenen formatta olmadığı durumda bir `ValueError` yükseltir.
- Düğüm, oluşturulan anahtar kırmızının LTXV Oluşturulan Anahtar Kırmızıları düğmesi kullanılarak eklendiğini ve mevcut latent ile uyumlu olduğunu varsayar.
```

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/tr.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
