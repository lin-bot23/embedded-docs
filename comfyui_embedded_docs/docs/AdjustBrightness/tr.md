# Parlaklığı Ayarla

Adjust Brightness düğümü, bir girdi görüntüsünün parlaklığını değiştirir. Her pikselin değerini belirtilen bir faktörle çarparak ve ardından sonuç değerlerini geçerli bir aralıkta kalacak şekilde sınırlayarak çalışır. 1.0 faktörü görüntüyü değiştirmez, 1.0'ın altındaki değerler onu koyulaştırır ve 1.0'ın üzerindeki değerler onu aydınlatır. Girdi görüntüsü bir alfa kanalı içeriyorsa, şeffaflığı korumak için alfa kanalı değiştirilmeden aktarılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Ayarlanacak girdi görüntüsü. | IMAGE | Evet | - |
| `faktör` | Parlaklık faktörü. 1.0 = değişiklik yok, <1.0 = koyulaştırır, >1.0 = aydınlatır. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görseller` | Parlaklığı ayarlanmış çıktı görüntüsü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/tr.md)

---
**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`
