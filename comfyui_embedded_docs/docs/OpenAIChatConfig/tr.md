# OpenAI ChatGPT Gelişmiş Seçenekler

OpenAI ChatGPT Gelişmiş Seçenekleri düğümü, OpenAI Chat Düğmeleri için ek ayarlar belirlemenize olanak tanır. Bu düğüm, modelin yanıtlarını oluşturma şeklini kontrol eden kesme davranışı, çıktı uzunluk sınırları ve özel talimatlar gibi ileri düzey ayarlar sağlar.

## Genel Bakış

OpenAI ChatGPT Gelişmiş Seçenekleri düğümü, kullanıcıların ileri düzey yapılandırma seçeneklerini belirtmesine olanak tanıyan ve OpenAI Chat Düğmeleri'nin işlevselliğini artıran bir yapıdadır. Bu ayarlar, modelin yanıtlarını belirli gereksinimlere uyacak şekilde özelleştirmek için yardımcı olabilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kırpma` | Model yanıtının kullanılacak kesme stratejisi. auto: Bu yanıtın ve önceki yanıtların bağlamın modelin bağlam pencere boyutunu aşması durumunda, model konuşmanın ortasında girdi öğelerini atarak bağlam pencereye sığacak şekilde yanıtını keser. disabled: Bir model yanıtı bağlam pencere boyutunu aşarsa, istek 400 hatası ile başarısız olur (varsayılan: "auto") | STRING | Evet | "auto"<br>"disabled" |
| `maksimum_çıktı_tokenları` | Bir yanıt için oluşturulabilecek toplam token sayısının üst sınırları, görünen çıktı token'ları ve mantıksal token'ları içermektedir (varsayılan: 4096) | INT | Hayır | 16 ila 16384 |
| `talimatlar` | Modelin yanıt oluşturma konusunda vereceği talimatlar (çok satırlı girdi desteklenmektedir) | STRING | Hayır | - |
| `reasoning_effort` | Yanıta yanıt vermeden önce modelin ne kadar mantık yürüteceğini belirler. 'default' seçeneği modelin seçimine bırakır. Desteklenen seviyeler her model için farklıdır: GPT-6 Astra low-max, GPT-5.6 none-max (en az minimal), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1'de mantık yoktur. Desteklenmeyen seviyeler istek göndermeden önce reddedilir (varsayılan: "default") | STRING | Hayır | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | Belirtilen ayarları OpenAI Chat Düğmeleri ile kullanmak için içeren yapılandırma nesnesi | OPENAI_CHAT_CONFIG |

## Notlar

- `max_output_tokens` parametresi, toplam token sayısının üst sınırlarını belirler, bu da görünen çıktı token'ları ve mantıksal token'ları içermektedir.
- `reasoning_effort` parametresi, modelin yanıt oluşturma öncesinde ne kadar mantık yürüteceğini belirler. Desteklenen seviyeler her model için farklıdır.
- `instructions` parametresi, modelin yanıt oluşturma sürecini yönlendirmek için ayrıntılı talimatlar sağlayabilir.
- `truncation` parametresi, modelin bağlam pencere boyutunu aşarsa yanıtını otomatik olarak kesip kesmeyeceğini veya 400 hatası ile başarısız olacağını belirler.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/tr.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
