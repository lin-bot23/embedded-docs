# Metin Yer Paylaşımı Çiz

Bu düğüm, bir görüntünün veya görüntü grubunun üzerine metin çizer. Yapılandırılabilir yazı tipi boyutu, renk, dikey konum, yatay hizalama ve isteğe bağlı siyah anahat içeren bir metin katmanı oluşturur ve ardından bu katmanı orijinal görüntülerin üzerine bindirir.

## Girdiler

| Parametre | Açıklama | Veri Tipi | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntüler` | Metin çizilecek girdi görüntüsü veya görüntü grubu | IMAGE | Evet | |
| `metin` | Görüntüye yerleştirilecek metin (varsayılan: ""). Birden çok satırı destekler: `\n` ve `\t` kaçış dizileri satır sonu ve sekme karakterlerine dönüştürülür; uzun satırlar görüntü genişliğine sığacak şekilde otomatik olarak sarılır. | STRING | Evet | |
| `yazı tipi boyutu` | Görüntü yüksekliğinin yüzdesi olarak yazı tipi boyutu (varsayılan: 5.0) | FLOAT | Evet | 0.5 ila 50.0 (adım 0.5) |
| `renk` | Metnin rengi (varsayılan: "#ffffff") | STRING | Evet | |
| `konum` | Metnin görüntü üzerindeki dikey konumu (varsayılan: "top") | COMBO | Evet | "top"<br>"bottom" |
| `hizalama` | Metnin görüntü üzerindeki yatay hizalaması (varsayılan: "left") | COMBO | Evet | "left"<br>"center"<br>"right" |
| `dış çizgi` | Metnin çevresine siyah bir anahat çizilip çizilmeyeceği (varsayılan: True) | BOOLEAN | Evet | |

Not: `text` boşsa veya yalnızca boşluk karakterlerinden oluşuyorsa düğüm, girdi görüntülerini değiştirmeden döndürür. Metin katmanı bir kez oluşturulur ve gruptaki her görüntüye uygulanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Tipi |
|-------------|-------------|-----------|
| `görüntüler` | Üzerine metin katmanı eklenmiş girdi görüntüleri | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/tr.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
