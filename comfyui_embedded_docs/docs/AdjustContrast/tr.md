# Kontrastı Ayarla

Kontrast Ayarı düğümü, renk aralığının orta noktası etrafında açık ve koyu alanlar arasındaki farkı ölçekleyerek girdi görüntüsünün kontrastını ayarlar. 1.0 faktörü görüntüyü değiştirmez, 1.0'ın altındaki değerler kontrastı azaltır ve 1.0'ın üzerindeki değerler kontrastı artırır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `image` | Kontrastı ayarlanacak girdi görüntüsü. | IMAGE | Evet | - |
| `faktör` | Kontrast faktörü. 1.0 = değişiklik yok, <1.0 = daha az kontrast, >1.0 = daha fazla kontrast. (varsayılan: 1.0) | FLOAT | Hayır | 0.0 - 2.0 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `görseller` | Kontrastı ayarlanmış sonuç görüntüsü. Piksel değerleri 0.0–1.0 aralığına sınırlandırılır. Girdi görüntüsünün bir alfa kanalı varsa, bu kanal değiştirilmeden korunur. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/tr.md)

---
**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`
