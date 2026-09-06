# OpenAI ChatGPT

Bu düğüm, OpenAI modelinden metin yanıtları oluşturur. Bir metin ipucunu ve isteğe bağlı olarak resim veya dosyaları bağlam olarak kullanır ve ardından bu bilgileri OpenAI modeline gönderir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `komut` | Modelin yanıtı oluşturmak için kullanılan metin girdileri. Bu, modelin yanıt vermesini istediğiniz metindir. | STRING | Evet | - |
| `bağlamı_sürdür` | Bu parametre eski ve etkisi yoktur. Geriye dönük uyumluluk için içerilmiştir, ancak düğümün davranışını etkilemez. | BOOLEAN | Hayır | - |
| `model` | Yanıtı oluşturmak için kullanılan model. Kullanılabilir OpenAI modellerinden birini seçin. | COMBO | Evet | gpt-6-astra<br>gpt-5.6-sol<br>gpt-5.6-terra<br>gpt-5.6-luna<br>gpt-5.5-pro<br>gpt-5.5<br>gpt-5<br>gpt-5-mini<br>gpt-5-nano<br>gpt-4.1<br>gpt-4.1-mini<br>gpt-4.1-nano<br>o4-mini<br>o3<br>o1-pro<br>o1 |
| `görseller` | Model için bağlam olarak kullanılacak isteğe bağlı resim(ler). Çoklu resim içermek için Batch Images düğümünü kullanabilirsiniz. | IMAGE | Hayır | - |
| `dosyalar` | Model için bağlam olarak kullanılacak isteğe bağlı dosya(ya). OpenAI Chat Input Files düğümünden alınan girdileri kabul eder. | OPENAI_INPUT_FILES | Hayır | - |
| `gelişmiş_seçenekler` | Modelin davranışı için isteğe bağlı yapılandırma. OpenAI Chat Advanced Options düğümünden alınan girdileri kabul eder. | OPENAI_CHAT_CONFIG | Hayır | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `output_text` | OpenAI modeli tarafından oluşturulan metin yanıtı. Bu, girdi ipucu ve bağlam temel alınarak oluşturulan oluşturulan metindir. | STRING |

## Notlar

- `persist_context` parametresi eski ve etkisi yoktur. Geriye dönük uyumluluk için içerilmiştir, ancak kullanılmamalıdır.
- `images` girdisi model için ek bağlam sağlamak için kullanılabilir. Çoklu resim sağlanırsa, bu resimler Batch Images düğümü kullanılarak bağlanmalıdır.
- `files` girdisi ek bağlam olarak dosya sağlamak için kullanılabilir. Bu dosyalar OpenAI Chat Input Files düğümünden bağlanmalıdır.
- `advanced_options` girdisi modelin davranışı için daha ayrıntılı yapılandırma sağlamak için kullanılabilir. Bu girdi OpenAI Chat Advanced Options düğümünden bağlanmalıdır.
- Bu düğümün fiyatlandırması seçilen modele bağlıdır. Fiyat, model tarafından kullanılan token sayısına göre hesaplanır. Kesin maliyet, düğümün UI'sinde görüntülenir.
```

Bu belge, kaynak kodundaki değişiklikleri yansıtır, eski `persist_context` parametresinin kaldırılmasını ve `images` ve `files` girdilerinin eklenmesini içerir. Ayrıca, hala doğru olan mevcut belgeye ait insan yazılmış açıklamaları ve notları korur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/tr.md)

---
**Source fingerprint (SHA-256):** `687a6b1110518a2eaf23e240f43991b4ff91d6f01cae6c3ef55bcdac810e7a89`
