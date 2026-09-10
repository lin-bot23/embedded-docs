# Model Dikkat Arka Ucu

Bu düğüm, bir modelin dikkat hesaplamaları için kullandığı yoğun dikkat arka ucunu seçer. Verilen modeli kopyalar, seçilen arka ucu uygular ve yamalı kopyayı döndürür. Blok Seyrek Dikkat ile kullanıldığında, bu arka uç, seyrek dikkatin etkin olmadığı veya desteklenmediği durumlarda kullanılır. Seçilen arka uç kullanılamıyorsa, düğüm otomatik olarak PyTorch dikkatine geri döner.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Yamalanacak model. | MODEL | Evet |  |
| `dikkat` | Uygulanacak yoğun dikkat arka ucu (varsayılan: "pytorch attention"). Comfy Kitchen dikkati, nicelenmiş INT8 dikkat kullanır ve yalnızca Nvidia ve AMD GPU'larında kullanılabilir. Seçilen arka uç kullanılamıyorsa, geri dönüş olarak PyTorch dikkati kullanılır. | COMBO | Evet | "pytorch attention"<br>"comfy kitchen attention" |

Not: "comfy kitchen attention" seçeneği yalnızca geçerli ortamda Comfy Kitchen INT8 dikkat modülü mevcut olduğunda listelenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Seçilen dikkat arka ucu uygulanmış girdi modelinin bir kopyası. | MODEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/tr.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
