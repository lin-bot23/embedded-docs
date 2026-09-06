# LTXV Bağlam Pencereleri

Bu düğüm, örnekleme sırasında LTXV benzeri modeller için bağlam pencereleri ayarlar. Video oluşturma sürecini çakışan pencerelere bölerek bellek kullanımını yönetir ve zamansal tutarlılığı artırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Örnekleme sırasında bağlam pencerelerinin uygulanacağı model. | MODEL | Evet | - |
| `context_length` | Bağlam penceresinin gerçek kareler cinsinden uzunluğu. 8*n + 1 olmalıdır. (varsayılan: 145) | INT | Evet | Minimum: 1<br>Maksimum: nodes.MAX_RESOLUTION<br>Adım: 8 |
| `context_overlap` | Bağlam penceresinin gerçek kareler cinsinden çakışma miktarı. (varsayılan: 40) | INT | Evet | Minimum: 0<br>Adım: 8 |
| `context_schedule` | Bağlam pencereleri için adıma bağlı zamanlama algoritması. (varsayılan: UNIFORM_STANDARD) | COMBO | Evet | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | Bağlam penceresinin adımı; yalnızca tekdüze zamanlamalar için geçerlidir. (varsayılan: 1) | INT | Hayır | Minimum: 1 |
| `closed_loop` | Bağlam penceresi döngüsünün kapatılıp kapatılmayacağı; yalnızca döngülü zamanlamalar için geçerlidir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `fuse_method` | Bağlam pencerelerini birleştirmek için kullanılacak yöntem. (varsayılan: PYRAMID) | COMBO | Evet | Options from comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | FreeNoise gürültü karıştırmanın uygulanıp uygulanmayacağı; pencere harmanlamasını iyileştirir. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `retain_first_frame` | Her bağlam penceresinde ilk latent kareyi korur (başlangıç referansının korunmasına yardımcı olabilir). (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `split_conds_to_windows` | Birden fazla koşullandırmanın (ConditionCombine tarafından oluşturulan) bölge indeksine göre her pencereye bölünüp bölünmeyeceği. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |

**Not:** `context_length` parametresi 8*n + 1 formülüne uymalıdır; burada n pozitif bir tam sayıdır. Düğüm, gerçek kareleri latent karelere dönüştürerek bu gereksinimi karşılamak için değeri otomatik olarak ayarlar. `context_overlap` da gerçek karelerden latent karelere dönüştürülür (8'e bölünür).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `MODEL` | Örnekleme için bağlam pencereleri uygulanmış model. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/tr.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
