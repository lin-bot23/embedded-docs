# OpenAI ChatGPT Gelişmiş Seçenekler

OpenAIChatConfig düğümü, OpenAI Chat Node'un yanıtları nasıl oluşturacağını kontrol eden gelişmiş seçenekler tanımlamanızı sağlar. Kırpma stratejisini belirleyebilir, çıktı token sayısını sınırlayabilir, özel talimatlar sağlayabilir ve modelin yanıt vermeden önce ne kadar akıl yürüteceğini seçebilirsiniz.

## Girdiler

| Parameter | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `kırpma` | Model yanıtı için kullanılacak kırpma stratejisi. auto: Bu yanıtın ve önceki yanıtların bağlamı, modelin bağlam penceresi boyutunu aşarsa, model, konuşmanın ortasındaki girdi öğelerini atarak yanıtı bağlam penceresine sığacak şekilde kırpar. disabled: Bir model yanıtı, söz konusu model için bağlam penceresi boyutunu aşarsa istek 400 hatasıyla başarısız olur (varsayılan: "auto") | COMBO | Evet | "auto"<br>"disabled" |
| `maksimum_çıktı_tokenları` | Bir yanıt için oluşturulabilecek token sayısının üst sınırı; görünür çıktı tokenleri ve akıl yürütme tokenleri dahildir (varsayılan: 4096) | INT | Hayır | 16 to 16384 |
| `talimatlar` | Modelin yanıtı nasıl oluşturacağına ilişkin talimatlar (çok satırlı girdi desteklenir) | STRING | Hayır | - |
| `reasoning_effort` | Modelin yanıtlamadan önce ne kadar akıl yürüteceği. "default", seçimi modele bırakır. Desteklenen düzeyler modele göre farklılık gösterir: GPT-6 Astra low-max, GPT-5.6 none-max (minimal düzeyi yok), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1 akıl yürütmeyi desteklemez. Desteklenmeyen düzeyler, istek gönderilmeden önce reddedilir. (varsayılan: "default") | COMBO | Hayır | "default"<br>"none"<br>"minimal"<br>"low"<br>"medium"<br>"high"<br>"xhigh"<br>"max" |

Not: `top_p` ve `temperature` API belirtiminde özellikler olarak listelenmiş olsa da tüm modellerde desteklenmez ve bu nedenle girdi olarak sunulmaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `OPENAI_CHAT_CONFIG` | OpenAI Chat Node ile kullanım için belirtilen ayarları içeren yapılandırma nesnesi | OPENAI_CHAT_CONFIG |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/tr.md)

---
**Source fingerprint (SHA-256):** `37d18a13b9d5bb36359603e5bab5918e7fea200ac552ea8439fff1488a88263c`
