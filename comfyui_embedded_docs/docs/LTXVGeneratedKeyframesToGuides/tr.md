# LTXVGeneratedKeyframesToGuides

## Genel Bakış

LTXV Oluşturulan Anahtar Kırmaların Rehberlere Dönüşüm düğümü, daha erken bir aşamadan oluşturulan anahtar kırmaları daha sonraki bir kanvasta dondurulmuş görüntü rehberleri olarak sabitler. Anahtar kırmaları bağımsız kareler olarak çözümler, gerekirse onları yeniden boyutlandırır ve 0 ile yazılan gürültü maskesi ile birlikte yazarlar. Kaydedilen indeksler, oluşturuldukları kanvasta hedef kanvasa ölçeklendirilir ve kare indekslerini açıkça belirlemek için geçersiz kılmak isteyebilirsiniz.

## Girdiler

| Parametre                 | Açıklama                                                                 | Veri Türü | Gerekli | Aralık |
|---------------------------|-----------------------------------------------------------------------------|-----------|----------|-------|
| `pozitif` | Anahtar kırmaları olarak sabitlenen pozitif koşullandırma. | CONDITIONING | Evet |  |
| `negatif` | Anahtar kırmaları olarak sabitlenen negatif koşullandırma. | CONDITIONING | Evet |  |
| `vae`                     | Anahtar kırmaları çözümlemek için kullanılacak VAE modeli.                   | MODEL      | Evet      |       |
| `latent`                  | Anahtar kırmaların eklenmesi istenen hedef video latenti, örneğin, zamanla yükseltilen bir tane. | LATENT     | Evet      |       |
| `anahtar kareler` | LTXV Ayrı Oluşturulan Anahtar Kırmaların çıkışında, her anahtar kırmaya hangi pixel kare indeksinde oluşturulduğunu taşıyan anahtar kırmalar. | LATENT     | Evet      |       |
| `güç` | Rehber güçlüğü. 1.0, sert bir sabitleme oluşturur; daha düşük değerler sabitlemeyi gevşetir. | FLOAT      | Evet      | 0.0 - 10.0 |
| `override_frame_indices` | Seçmeli — bu pixel karelerde sabitlenmek yerine kaydedilen (veya otomatik olarak ölçeklendirilen) konumlar. Her anahtar kırmaya bir indeks sağlayın. Boş bırakarak kaydedilen konumları yeniden kullanmak veya hedef kanvanın farklı uzunluğunda (örneğin, zamanla 2 kat arttırdıktan sonra) ölçeklemek için boş bırakın. | STRING    | Hayır       |       |

## Çıktılar

| Çıktı Adı | Açıklama                                                                 | Veri Türü |
|-------------|-----------------------------------------------------------------------------|-----------|
| `pozitif` | Anahtar kırmaları olarak sabitlenen pozitif koşullandırma. | CONDITIONING |
| `negatif` | Anahtar kırmaları olarak sabitlenen negatif koşullandırma. | CONDITIONING |
| `latent`    | Anahtar kırmaların eklendiği ve dondurulmuş rehber olarak kullanılan hedef video latenti. | LATENT     |

## Notlar

- `strength` parametresi, anahtar kırmaların rehber olarak sabitlenme güçlüğünü kontrol eder. 1.0 değeri sert bir sabitleme oluştururken, daha düşük değerler sabitlemeyi gevşetir.
- `override_frame_indices` parametresi, anahtar kırmaların sabitleneceği tam olarak belirtilen pixel karelerini belirlemenize olanak tanır. Boş bırakılırsa, düğüm kaydedilen konumları kullanır veya gerekirse onları ölçeklendirir.
- Düğüm, `keyframes` latentin her anahtar kırmaya hangi pixel kare indeksinde oluşturulduğunu içerdiğini varsayar. Bu durumda değilse, düğüm bir `ValueError` oluşturur.
- Düğüm, birim boyutlu bir grup destekler. Her rehber bir görüntüden kodlanır, bu yüzden grup elemanları arasında farklılık gösteremez.
- Düğüm, `latent` girdisindeki `samples` tensörünün 5D tensör olmadığı veya birim boyutlu olmadığı durumda bir `ValueError` oluşturur.
- Düğüm, `keyframes` girdisindeki `samples` tensörünün 5D tensör olmadığı veya birim boyutlu olmadığı durumda bir `ValueError` oluşturur.
- Düğüm, `keyframes` girdisindeki `samples` tensörünün `latent` girdisindeki `samples` tensörünün ölçeklendirildikten sonra şeklini tutmadığı durumda bir `ValueError` oluşturur.
- Düğüm, `strength` parametresi 0.0 ile 10.0 aralığında olmadığı durumda bir `ValueError` oluşturur.
- Düğüm, `override_frame_indices` parametresi virgülle ayrılmış bir integer listesi değilse veya indeks sayısı anahtar kırmaların sayısına eşit değilse bir `ValueError` oluşturur.
- Düğüm, `override_frame_indices` parametresindeki herhangi bir indeks hedef kanvanın pixel kare sayısının 1 ile 1 arasında olmadığı durumda bir `ValueError` oluşturur.
- Düğüm, `override_frame_indices` parametresindeki maksimum indeks hedef kanvanın pixel kare sayısından büyük olduğunda bir `ValueError` oluşturur.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/tr.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
