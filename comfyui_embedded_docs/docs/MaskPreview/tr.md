# MaskeÖnizleme

MaskPreview düğümü, maske verilerinin görsel bir önizlemesini çıktı dizinine kaydetmeden doğrudan ComfyUI arayüzünde görüntüler. Bu sayede maskeyi iş akışınızın herhangi bir noktasında inceleyebilirsiniz. Maske ayrıca düğümden değiştirilmeden geçtiği için iş akışının sonraki adımlarında kullanılmaya devam edebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `maske` | Önizlenecek maske verileri | MASK | Evet | - |
| `filename_prefix` | Önizleme için kullanılan dosya adı öneki (varsayılan: "ComfyUI") | STRING | Hayır | - |
| `prompt` | Meta veriler için istem bilgisi (otomatik sağlanır) | PROMPT | Hayır | - |
| `extra_pnginfo` | Meta veriler için ek PNG bilgisi (otomatik sağlanır) | EXTRA_PNGINFO | Hayır | - |

Yalnızca `mask` bağlanması gereken görünür bir girdidir. `filename_prefix`, `prompt` ve `extra_pnginfo` parametreleri sistem tarafından sağlanır: `filename_prefix` belirtilmediğinde varsayılan değeri kullanılır; `prompt` ve `extra_pnginfo` ise gizlidir ve ComfyUI çalışma zamanı tarafından otomatik olarak eklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mask` | Önizlenen maske verilerinin aynısıdır; değiştirilmeden döndürülür ve iş akışının başka yerlerinde kullanılabilir | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/tr.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
