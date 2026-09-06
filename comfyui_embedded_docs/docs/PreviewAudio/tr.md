# Sesi Önizle

The Preview Audio düğümü, sesi çıktı dizinine kaydetmeden doğrudan ComfyUI arayüzünde dinlemenizi sağlar. Ses verisini girdi olarak alır, varlığını doğrular ve geçici bir ses oynatıcısı göstererek sonucu duyabilmeniz için onu geçirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `audio` | Önizlenecek ses verisi. Kaynak videoda ses parçası yoksa girdi None olduğunda düğüm bir ValueError yükseltir. | AUDIO | Evet | - |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `audio` | Girdiden değiştirilmeden geçirilen ses verisi. | AUDIO |
| `ui` | Sesin önizlenmesi için arayüzde bir ses oynatıcı bileşeni görüntüler. | UI |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/tr.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
