# Katmanlı Görsel Oluştur

Bu düğüm, birden çok görüntü katmanını tek bir birleşik görüntüde birleştirir. Add Layer düğümüyle oluşturulan katman yığınını alır ve isteğe bağlı olarak compositor düzenleyicisinden kaydedilmiş kompozisyon ayarlarını uygulayarak katmanları; yerleşim, boyut, dönüş, opaklık ve karıştırma moduna göre harmanlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `katmanlar` | Birleştirilecek katman yığını; Add Layer ile oluşturun. Öğeler z_index’e göre yığılır, bir öğe içindeki toplu kareler ardışık katmanlara genişler ve öğe yerleşimi, opaklığı ve karıştırma modu ilk kompozisyonu tanımlar. Belirli bir belge tuvali yoksa boyut, yerleştirilen katmanların olabildiğince geniş kapsamı olarak belirlenir. Geçerli girdilerle eşleşen kayıtlı bir kompozisyon önceliğe sahiptir. | LAYERS | Evet | En fazla 50 katman |
| `kompozitör` | Compositor düzenleyicisi tarafından kaydedilmiş katmanlı kompozisyon. | COMPOSITOR | Hayır | Yok |

**Kısıtlamalarla ilgili notlar:**

- Katman yığını en fazla 50 katmanı (genişletilmiş kareler) destekler; daha fazla sağlanırsa hata oluşturur.
- Şu anda yalnızca raster katmanlar desteklenir; diğer katman öğesi türleri hata oluşturur.
- `layers` belge sürümü 1 olmalıdır; diğer sürümler hata oluşturur.
- Kaydedilmiş `compositor` durumu yalnızca, kaydedilen girdi parmak izleri geçerli katman yığınıyla eşleştiğinde yeniden uygulanır. Eşleşmezse düğüm, katman özelliklerinden kompozisyon oluşturmaya geri döner ve kaydedilmiş durumu geçerliliğini yitirmiş olarak işaretler.
- Katman opaklığı 0.0 ile 1.0 aralığına sınırlandırılır.
- Katmanın yatay/dikey yerleşimi (`x`, `y`) maksimum çözünürlük sınırına kısıtlanır.
- Katman genişliği ve yüksekliği, sıfır veya daha düşük ayarlandığında doğal görüntü boyutuna geri döner ve maksimum çözünürlük sınırıyla sınırlandırılır.
- Birleştirilmiş tuval boyutu maksimum çözünürlük sınırını aşmamalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `IMAGE` | Birleştirilmiş görüntü. Birleşik görüntüde şeffaf alanlar varsa (ör. gizli arka plan) bir alfa kanalı taşır; aksi takdirde yalnızca RGB. | IMAGE |
| `MASK` | Birleşik görüntünün şeffaflığı (1 = tamamen şeffaf). Birleşik görüntü opak olduğunda tüm değerler sıfırdır. | MASK |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/tr.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
