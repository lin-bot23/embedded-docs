# Video Yükle

Load Video düğümü, video dosyalarını girdi klasöründen yükler ve iş akışında işlenmek üzere kullanılabilir hale getirir. Video dosyalarını belirlenen girdi klasöründen okur ve bunları diğer video işleme düğümlerine bağlanabilen video verisi olarak çıkarır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
| --- | --- | --- | --- | --- |
| `dosya` | Girdi klasöründen yüklenecek video dosyası. Açılır liste, ComfyUI girdi klasöründe bulunan tüm video dosyalarıyla dinamik olarak doldurulur; yeni video dosyaları doğrudan dosya seçici aracılığıyla da yüklenebilir. | COMBO | Evet | Multiple options available (all video files in the input directory) |

**Not:** `file` parametresi için mevcut seçenekler, girdi klasöründe bulunan video dosyalarından dinamik olarak oluşturulur. Yalnızca desteklenen içerik türlerine sahip video dosyaları görüntülenir. Ayrıca düğümün dosya seçici arayüzü aracılığıyla doğrudan yeni bir video dosyası yükleyebilirsiniz. Daha önce seçilmiş bir video dosyası artık bulunamıyorsa, düğüm geçersiz dosya hatası bildirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `video` | Daha fazla işleme veya analiz için diğer video işleme düğümlerine aktarılabilen yüklenmiş video verisi. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/tr.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
