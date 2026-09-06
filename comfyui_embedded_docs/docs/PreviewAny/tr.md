# Herhangi Bir Şeyi Önizle

PreviewAny, herhangi bir girdi değerini inceleyebilmeniz için okunabilir metne dönüştürür. String değerler değiştirilmeden geçer; sayılar ve boolean değerleri düz metne dönüştürülür; diğer veri türleri mümkün olduğunda JSON olarak serileştirilir (serileştirme başarısız olursa düz string biçimine geri dönülür). Elde edilen metin kullanıcı arayüzünde gösterilir ve ayrıca daha sonraki işlemler için bir string çıktısı olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `source` | Önizleme gösterimi için herhangi bir girdi veri türünü kabul eder. Değer sağlanmazsa önizleme 'None' gösterir. | ANY | Evet | Herhangi bir veri türü |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `result` | Metin biçimine dönüştürülen girdi değeri. Aynı metin kullanıcı arayüzünde de görüntülenir. | STRING |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/tr.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
