# MiniMax H3 Referanstan Videoya

MiniMax H3 Referanstan Videoya düğümü, MiniMax H3 referanstan videoya üretimi için gereken metin koşullandırmasını ve boş ses-video latentini oluşturur. Bir metin promptu ve isteğe bağlı referans görseller, videolar ve ses klipleri sağlarsınız; düğüm bu referansları, modelin üretim sırasında kullanabileceği koşullandırmaya kodlar. Prompt, referanslara `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle atıfta bulunur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip` | Promptu tokenize etmek ve referans medyayı koşullandırma tokenlarına kodlamak için kullanılan CLIP modeli. | CLIP | Evet | |
| `vae` | Referans görselleri ve referans video karelerini kodlamak için kullanılan Video VAE. Olmadan, referans görseller/videolar yalnızca metin kodlayıcıyı koşullandırır. | VAE | Hayır | |
| `audio_vae` | Referans sesi kodlamak için kullanılan Ses VAE. Ses, ses VAE örnekleme hızına (varsayılan 32 kHz) yeniden örneklenir. Olmadan, referans ses yalnızca metin kodlayıcıyı koşullandırır. | VAE | Hayır | |
| `prompt` | Video için metin promptu. Referans medyaya `<Picture i>`, `<Video k>` ve `<Audio j>` etiketleriyle (her tür için 1 tabanlı) atıfta bulunulabilir. Çok satırlı ve dinamik promptları destekler. | STRING | Evet | |
| `genişlik` | Üretilen videonun piksel cinsinden genişliği (varsayılan: 1344). | INT | Evet | 32 ila 16384 (adım 32) |
| `yükseklik` | Üretilen videonun piksel cinsinden yüksekliği (varsayılan: 768). | INT | Evet | 32 ila 16384 (adım 32) |
| `uzunluk` | 24 fps'de kare sayısı; 124 = ~5 sn, eğitilmiş aralık ~124-362'dir (varsayılan: 124). | INT | Evet | 5 ila 3600 (adım 17) |
| `ref_görüntü_boyutu` | Referans görsel boyutlandırması. `match`, her referans görselini en-boy oranını koruyarak yalnızca küçültüp üretimin piksel alanına ölçekler; `max`, en iyi kimlik doğruluğu için referans hattının 2048px kısa kenarını kullanır. Referans tokenları her örnekleme adımında taşındığından `max` birkaç kat daha yavaş olabilir (varsayılan: `match`). | COMBO | Evet | `"match"`<br>`"max"` |
| `ref_görüntüler` | Genişletilebilir yuva: en fazla 9 referans görseli bağlayın (`ref_image_1` ... `ref_image_9`). Referans görseller, daha büyüklerse 2048px kısa kenara küçültülür ve asla büyütülmez. | IMAGE | Hayır | 0 ila 9 |
| `ref_videolar` | Genişletilebilir yuva: en fazla 3 referans videosu bağlayın (`ref_video_1` ... `ref_video_3`). 24 fps'de (2-15 sn) referans video kareleri. | IMAGE | Hayır | 0 ila 3 |
| `ref_video_sesleri` | Genişletilebilir yuva: en fazla 3 film müziği bağlayın (`ref_video_audio_1` ... `ref_video_audio_3`). Aynı numaralı referans videosunun film müziği. | AUDIO | Hayır | 0 ila 3 |
| `ref_sesler` | Genişletilebilir yuva: en fazla 3 bağımsız referans ses klibi bağlayın (`ref_audio_1` ... `ref_audio_3`). | AUDIO | Hayır | 0 ila 3 |

Notlar:

- Prompt, referans medyaya her tür için 1 tabanlı etiketlerle atıfta bulunur: görseller için `<Picture i>`, videolar için `<Video k>` ve ses için `<Audio j>`. Referanslar modele sabit bir sırayla sunulur: görseller, ardından videolar (her filmin müziğinin `<Audio j>` etiketi, kendi `<Video k>` etiketinin hemen önünde), ardından bağımsız sesler.
- `ref_video_audio_N`'ye bağlı bir film müziği, `ref_video_N`'ye bağlı referans videosuyla birlikte kullanılır.
- Referans videolar en az 5 kare (~24 fps'de 0,2 saniye) içermelidir, aksi takdirde düğüm bir hata verir. İstenen `length` değerinin ötesindeki kareler kırpılır ve kalan kare sayısı model tarafından desteklenen bir değere ayarlanır.
- İstenen `length`, latent oluşturulmadan önce desteklenen bir kare sayısına hizalanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Kodlanmış promptu içeren koşullandırma. Referans medya ve ilgili VAE'ler sağlandığında, MiniMax H3 modeli tarafından kullanılan kodlanmış referans görsel, video ve ses içeriğini de içerir. | CONDITIONING |
| `latent` | İstenen `width`, `height` ve `length` (kare sayısı) değerlerinde boş ses-video latenti. | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/tr.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
