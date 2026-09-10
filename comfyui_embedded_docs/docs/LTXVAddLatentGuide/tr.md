# LTXVAddLatentGuide

## Özet

LTXV Add Latent rehberi, zaten kodlanmış bir gizli latenti bir rehber olarak sabitler ve daha erken bir aşamadan gelen bir rehber kullanmayı sağlar. Bu node, VAE decode/encode turunu önler ve daha küçük bir rehberi genişleterek hedef canvas'ı kapsayan bir azaltılmış ızgara üzerine yerleştirir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `positive` | Pozitif koşullandırma girdisi. | KOŞULLANDIRMA | Evet | N/A |
| `negative` | Negatif koşullandırma girdisi. | KOŞULLANDIRMA | Evet | N/A |
| `vae` | Kullanılacak VAE modeli. | MODEL | Evet | N/A |
| `latent` | Rehberin sabitleneceği hedef video gizli latenti. | LATENT | Evet | N/A |
| `guiding_latent` | Rehber latenti. Uzay boyutu, hedefin her iki eksende de aynı tam sayı ile bölünmelidir; eşit boyutta sabitlenir, yarım boyutta x2 IC-LoRA referans olarak işlenir. | LATENT | Evet | N/A |
| `latent_idx` | Rehberin başlayacağı latent çerçeve indeksi, latent çerçeveler olarak sayılır. Negatif değerler, gizli latentin sonundan geri sayılmadan başlangıçtan önceki çerçevelere yerleştirir. | INT | Evet | -9999 ile 9999 arasında |
| `strength` | 1.0 ile sınırlı. Genişletilmiş bir rehber, dolgu pozisyonlarını negatif denoising mask ile işaretler ve model bunları atar; 1.0'dan büyük değerler, tutulan pozisyonlar negatif olacaktır ve tüm rehber atılacaktır. 1.0'dan büyük artışları dikkat maskesi ile artırın. | FLOAT | Evet | 0.0 ile 1.0 arasında, adım 0.01 |
| `attention_mask` | Opsiyonel piksel alanı spesifik maskesi. Her bölgeye özel koşullandırma etkisini kendiliğinden dikkat ile çarpıp artırır. | MASK | Hayır | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `positive` | Pozitif koşullandırma çıktısı. | KOŞULLANDIRMA |
| `negative` | Negatif koşullandırma çıktısı. | KOŞULLANDIRMA |
| `latent` | Rehber uygulanmış latent çıktısı. | LATENT |

## Notlar

- `guiding_latent` uzay boyutu, `latent` boyutunu her iki eksende de aynı tam sayı ile bölünmelidir.
- `latent_idx` parametresi, rehberin latent çerçeveler içindeki yerleşimini kesin olarak belirler.
- `strength` parametresi, rehberin yoğunluğunu kontrol eder, 1.0'dan büyük değerler `attention_mask` kullanılarak kaçınılmalıdır.
- `attention_mask` parametresi opsiyoneldir ancak resmin belirli bölgelerindeki rehber etkisini ince ayarlamak için kullanılabilir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/tr.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
