# Çözünürlük Seçici

Resolution Selector düğümü, seçilen en-boy oranına ve megapiksel cinsinden hedeflenen toplam çözünürlüğe göre piksel genişliğini ve yüksekliğini hesaplar. Empty Latent Image düğümü gibi diğer düğümler için tutarlı boyutlar üretmek amacıyla kullanışlıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `en_boy_orani` | Çıktı boyutları için en-boy oranı (varsayılan: `"1:1 (Square)"`). | COMBO | Evet | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `megapiksel` | Hedeflenen toplam megapiksel değeri. Kare için 1.0 MP ≈ 1024x1024 (varsayılan: 1.0). | FLOAT | Evet | 0.1 - 16.0 (step: 0.1) |
| `preview` | Hesaplanan çıktı çözünürlüğünün canlı önizlemesi. Bu salt okunur widget otomatik olarak güncellenir ve kullanıcı girdisi kabul etmez. | RESOLUTION_PREVIEW | Hayır | N/A |
| `kat` | Seçilen çözünürlüğün ayarlanacağı, hesaplanan sonucun en yakın katı (varsayılan: 8). | INT | Hayır | 8 - 128 (step: 4) |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `genislik` | Hesaplanan genişlik (piksel), seçilen kat değeriyle çarpılır. | INT |
| `yukseklik` | Hesaplanan yükseklik (piksel), seçilen kat değeriyle çarpılır. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/tr.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`
