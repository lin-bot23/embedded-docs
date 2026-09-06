# Anahtar

Switch düğümü, boolean bir koşula dayalı olarak iki olası girdi arasında seçim yapar. `switch` etkinleştirildiğinde (true), `on_true` girdisini çıktıya iletir; devre dışı bırakıldığında (false) ise `on_false` girdisini iletir. Yalnızca seçilen dal değerlendirilir, bu nedenle diğer girdinin bağlı olması gerekmez.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `switch` | Hangi girdinin iletileceğini belirleyen boolean koşul. Etkinleştirildiğinde (true), `on_true` girdisi seçilir. Devre dışı bırakıldığında (false), `on_false` girdisi seçilir. | BOOLEAN | Evet |  |
| `on_false` | `switch` devre dışıyken (false) çıktıya iletilecek veri. Bu girdi yalnızca `switch` false olduğunda gereklidir. | MATCH_TYPE | Hayır |  |
| `on_true` | `switch` etkinken (true) çıktıya iletilecek veri. Bu girdi yalnızca `switch` true olduğunda gereklidir. | MATCH_TYPE | Hayır |  |

**Girdi Gereksinimleri Notu:** `on_false` ve `on_true` girdileri koşullu olarak zorunludur. Düğüm, `on_true` girdisini yalnızca `switch` true olduğunda; `on_false` girdisini ise yalnızca `switch` false olduğunda ister. Her iki girdi de aynı veri tipinde olmalı ve çıktı veri tipiyle eşleşmelidir. Seçilen girdi bağlı değilse, düğüm değer üretmez.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
| --- | --- | --- |
| `output` | Seçilen veri. `switch` true olduğunda `on_true` girdisinden, `switch` false olduğunda ise `on_false` girdisinden alınan değerdir. | MATCH_TYPE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/tr.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
