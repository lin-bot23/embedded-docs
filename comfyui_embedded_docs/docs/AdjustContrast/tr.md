# Kontrastı Ayarla

Adjust Contrast düğümü, bir girdi görüntüsünün kontrast düzeyini değiştirir. Bu, görüntünün açık ve koyu alanları arasındaki farkı ayarlayarak çalışır. 1.0 faktörü görüntüyü değiştirmez, 1.0'ın altındaki değerler kontrastı azaltır, 1.0'ın üzerindeki değerler ise artırır. Girdi görüntüsü bir alfa kanalı içeriyorsa, şeffaflığı korumak için alfa kanalı değiştirilmeden aktarılır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Kontrastı ayarlanacak girdi görüntüsü. | IMAGE | Evet | - |
| `faktör` | Kontrast faktörü. 1.0 = değişiklik yok, <1.0 = daha az kontrast, >1.0 = daha fazla kontrast. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görseller` | Kontrastı ayarlanmış sonuç görüntüsü. Piksel değerleri 0.0–1.0 aralığına sınırlandırılmıştır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/tr.md)

---
**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`
