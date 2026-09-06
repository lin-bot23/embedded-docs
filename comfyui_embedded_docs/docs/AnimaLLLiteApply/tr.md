# Anima LLLite Uygula

AnimaLLLiteApply, bir difüzyon modeline hafif bir animasyon yaması uygulayarak ayarlanabilir güç ve zamanlama ile kontrollü görüntüden görüntüye üretim sağlar. Önceden yapılandırılmış bir model yamasını, bir giriş görseli ve isteğe bağlı bir maske ile bütünleştirir; modelin dikkat ve MLP katmanlarını değiştirerek üretim sürecini etkiler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yamanın uygulanacağı temel difüzyon modeli | MODEL | Evet | |
| `model_patch` | Uygulanacak önceden yapılandırılmış animasyon yaması | MODEL_PATCH | Evet | |
| `image` | Üretimi yönlendirmek için kullanılan referans görsel. Yalnızca ilk 3 renk kanalı (RGB) kullanılır | IMAGE | Evet | |
| `strength` | Yama etkisinin gücü (varsayılan: 1.0) | FLOAT | Evet | -10.0 ila 10.0 |
| `start_percent` | Yamanın etkili olmaya başladığı gürültü giderme işleminin yüzdesi (varsayılan: 0.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `end_percent` | Yamanın etkisinin sona erdiği gürültü giderme işleminin yüzdesi (varsayılan: 1.0) | FLOAT | Evet | 0.0 ila 1.0 |
| `mask` | Yama etkisini görselin belirli alanlarıyla sınırlamak için kullanılan isteğe bağlı maske | MASK | Hayır | |

**Parametre kısıtlamalarına ilişkin not:** `model_patch` 4 giriş kanalına sahipse ve `mask` sağlanmazsa, görsel boyutlarıyla eşleşecek şekilde otomatik olarak sıfır maskesi oluşturulur. `model_patch` 4 giriş kanalına sahip değilse, `mask` parametresi yok sayılır ve `None` olarak ayarlanır. Bu düğüm ComfyUI'de deneysel olarak işaretlenmiştir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Animasyon yaması uygulanmış difüzyon modeli | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/tr.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
