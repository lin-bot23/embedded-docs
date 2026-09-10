# Parlaklığı Ayarla

Adjust Brightness düğümü, bir görüntünün ne kadar parlak göründüğünü değiştirir. Görüntünün renk değerlerini bir `factor` ile çarpar ve sonuçları geçerli 0.0 ile 1.0 aralığında tutar. 1.0 faktörü görüntüyü olduğu gibi bırakır; 1.0'ın altındaki değerler görüntüyü daha koyu, 1.0'ın üzerindeki değerler ise görüntüyü daha parlak yapar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Ayarlanacak girdi görüntüsü. Tek bir görüntü veya bir grup görüntü kabul eder. | IMAGE | Evet | - |
| `faktör` | Parlaklık faktörü. 1.0 = değişiklik yok, <1.0 = daha koyu, >1.0 = daha parlak. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

Not: Girdi görüntüsünde bir alfa kanalı (RGBA) varsa yalnızca renk kanalları ayarlanır. Alfa kanalı, renk değil saydamlık bilgisi sakladığı için girdiden değiştirilmeden kopyalanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görseller` | Parlaklığı ayarlanmış çıktı görüntüsü. Girdide alfa kanalı varsa, alfa değerleri değişmeden kalır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/tr.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
