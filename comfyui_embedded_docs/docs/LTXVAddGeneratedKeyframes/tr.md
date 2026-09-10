# LTXVAddGeneratedKeyframes

## Genel Bakış

LTXV Oluşturulan Anahtar Çerçeveleri düğümü, bir video latentine ayrıntılı anahtar çerçeveler ekler. Her anahtar çerçeve, tek bir piksel çerçevesini kapsayan bir latent çerçevesi temsil eder ve bu çerçeveler video ile denoize edilir, ancak çözülen çıktının bir parçası değildir. Konumlandırma, interval_frames parametresi tarafından belirlenir ve bu parametre, otomatik konumlandırma için piksel çerçeve adımını belirtir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Anahtar çerçevelerin eklenmesi için pozitif koşullama. | KOŞULLAMA | Evet | N/A |
| `negative` | Anahtar çerçevelerin eklenmesi için negatif koşullama. | KOŞULLAMA | Evet | N/A |
| `vae` | Yalnızca latent ölçek faktörlerini okumak için kullanılır. | VAE | Evet | N/A |
| `latent` | Anahtar çerçevelerle birlikte oluşturulacak temiz 5D video latenti. Concat AV Latent öncesinde ekleyin. | LATENT | Evet | N/A |
| `interval_frames` | Otomatik konumlandırma için piksel çerçeve adımı. Standart 24, 24 fps'de bir saniyede bir anahtar çerçeve anlamına gelir. İşgal edilmiş pikseller atlanır. frame_indices ayarlandığında yoksayılmıştır. | INT | Hayır | 1-1024 |
| `keyframes` | Yeni anahtar çerçeveleri başlatmak için seçmeli içerik. Daha erken bir Ayır (aynı alan boyutu) veya temiz bir video latentine bağlanarak mevcut her yeni yuva için en yakın çerçeveyi kopyalayın (örneğin, zamansal yükseltme sonrası). Bu çerçeveler hala denoize edilir, rehber olarak sabitlenmez. Anahtar çerçeveler latentindeki kaydedilen indeksler, frame_indices ayarlandığında yoksayılmaz. Yalnızca sigma 1 altında başlangıçta örnek alındığında etkili olur. | LATENT | Hayır | N/A |
| `frame_indices` | Seçmeli piksel çerçeve indeksleri. Boş bırakarak mevcut canvas üzerinde interval_frames ile konumlandırma yapın. Ayarlandığında, bu liste konumlandırma (bağlantılı anahtar çerçeveler sırayla eşleştirilir). Son çerçeve izin verilir; çerçeve 0 izin verilmez (zaten bağımsız bir token). | STRING | Hayır | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Oluşturulan-anahtar çerçeve dikkatini eklediği pozitif koşullama. | KOŞULLAMA |
| `negative` | Oluşturulan-anahtar çerçeve dikkatini eklediği negatif koşullama. | KOŞULLAMA |
| `latent` | Oluşturulan anahtar çerçevelerle eklenen T'ye eklenen video latenti. | LATENT |

## Notlar

- `interval_frames` parametresi, videodaki anahtar çerçevelerin aralığını belirler. Daha yüksek bir değer, daha az anahtar çerçeve ve daha düşük kare hızı anlamına gelir.
- `keyframes` girdisi, mevcut anahtar çerçeveler veya video latenti ile yeni anahtar çerçeveleri başlatmanıza olanak tanır. Sağlandığında, bu çerçeveler denoize edilir ve video latentine eklenir.
- `frame_indices` parametresi, anahtar çerçevelerin yerleştirileceği kesin piksel çerçeve indekslerini belirlemenize olanak tanır. Ayarlandığında, `interval_frames` parametresi yoksayılmaz.
- `positive` ve `negative` çıktıları, oluşturulan-anahtar çerçeve dikkatini eklediği koşullamalar içerir ve bu çıktılar ileri işleme veya analiz için kullanılabilir.
- `latent` çıktısı, oluşturulan anahtar çerçevelerle eklenen video latenti içerir ve bu çıktı ileri işleme veya analiz için kullanılabilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/tr.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
