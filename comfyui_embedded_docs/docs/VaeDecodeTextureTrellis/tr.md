# VaeDecodeTextureTrellis

Bu düğüm, bir VAE kullanarak Trellis2 doku latent verisini voksel renklerine kodunu çözer. Girdi latent verisi, koordinatlarla birlikte seyrek özellik örnekleri içerir; düğüm, her voksel için rengi yeniden oluşturur ve sonucu, PaintMesh gibi aşağı akış düğümlerinin bir 3D mesh'i renklendirmek için kullanabileceği bir voksel ızgarası olarak döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `samples` | Kodu çözülecek doku latent verisi. Örnek özellikleri ve seyrek koordinatları içerir ve koordinat sayıları, model çerçevesi ve koordinat çözünürlüğü gibi isteğe bağlı meta veriler içerebilir. | LATENT | Evet | — |
| `vae` | Doku latent verisini voksel renklerine kodunu çözmek için kullanılan Trellis2 VAE. | VAE | Evet | — |
| `shape_subdivides` | Kod çözme sırasında daha yüksek detaylı yeniden oluşturmayı yönlendirmek için kullanılan şekil bilgisi. Daha yüksek çözünürlüklerde yapı tutarlılığını korumaya yardımcı olur. | SHAPE_SUBDIVIDES | Evet | — |

Not: `samples` latent verisi koordinat sayıları içerdiğinde, sayılar negatif olmamalı, toplamı koordinat satır sayısıyla eşleşmeli ve her batch beklenen satır sayısına tam olarak sahip olmalıdır; aksi takdirde düğüm bir hata oluşturur. Latent verisinin model çerçevesi "z_up" ise, kodu çözülen voksel koordinatları mesh köşeleriyle hizalanması için Y-up olarak yeniden eşlenir. Bir koordinat çözünürlüğü sağlandığında, çıktı doku çözünürlüğü bu değerin 16 ile çarpılmasıyla elde edilir; aksi takdirde en büyük voksel koordinatından çıkarılır ve 256, 512, 1024, 1536 veya 2048 değerlerinden birine yukarı yuvarlanır (koordinat mevcut olmadığında 1024).

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `voxel_colors` | Koordinatları, renk özelliklerini ve doku çözünürlüğünü içeren kodu çözülmüş voksel verisi. Her vokselin 6 renk kanalı vardır: temel renk (RGB), metalik, pürüzlülük ve alfa, hepsi [0, 1] aralığındadır. PaintMesh gibi vertex-color tüketicileri ilk 3 kanalı kullanır. | VOXEL |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/tr.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
