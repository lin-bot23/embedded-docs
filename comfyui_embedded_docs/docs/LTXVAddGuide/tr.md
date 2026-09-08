# LTXVRehberEkle

LTXVAddGuide düğümü, gizli sıralara video koşullama rehberliği eklemek için tasarlanmıştır. Girdi resimlerini veya videolarını kodlayarak ve bunları koşullama verilerine anahtar kareler olarak entegre ederek işlem yapar. VAE kodlayıcı üzerinden girdiyi işler ve sonucu latent video sırasını koşullamak için kullanır. Koşullamayı başlatmak için belirli bir kare indeksi belirlemeyi ve koşullama etkisini ayarlamayı sağlar. Düğüm, kare hizalama sınırlarını işler ve koşullama etkisini kontrol etmeyi sağlar.

## Genel Bakış

LTXVAddGuide düğümü, girdi resimlerini veya videolarını kodlar, VAE kodlayıcı üzerinden işler ve kodlanmış latentleri latent video sırasını koşullamak için kullanır. Koşullamayı başlatmak için belirli bir kare indeksi belirlemeyi ve koşullama etkisini ayarlamayı sağlar. Düğüm, belirli bir bölgeye özel koşullama etkisini kontrol etmek için opsiyonel piksel alanı yerel maskeleri destekler ve belirli rehberleme işlemlerini ayarlamak için IC-LoRA parametrelerini işler.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pozitif` | Anahtar kare rehberliği ile değiştirilecek olumlu koşullama girdisi | KOŞULLAMA | Evet | - |
| `negatif` | Anahtar kare rehberliği ile değiştirilecek olumsuz koşullama girdisi | KOŞULLAMA | Evet | - |
| `vae` | Girdi resimleri veya videolarını kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `gizli` | Koşullama karelerini içeren girdi latent sırası | LATENT | Evet | - |
| `görüntü` | Latent videoyu koşullamak için kullanılacak resim veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın geçerli kare sayısına kesilir. | RESİM | Evet | - |
| `kare_indeksi` | Koşullamayı başlatmak için kullanılacak kare indeksi. Tek kareli resimler veya 1-8 kareli videolar için herhangi bir frame_idx değeri kabul edilir. 9+ kareli videolar için frame_idx, 8'e bölünmesi gereken bir değer olmalıdır, aksi takdirde en yakın 8'in katına yuvarlanır. Negatif değerler videoyun sonundan sayılır. (varsayılan: 0) | TAMSAYI | Evet | -9999 ila 9999 |
| `güç` | Koşullama etkisinin gücü, 1.0 tam koşullama ve 0.0 hiçbir koşullama uygular (varsayılan: 1.0) | TÜM | Evet | 0.0 ila 10.0 |
| `attention_mask` | Opsiyonel piksel alanı yerel maskesi. Self-attention yoluyla her bölgeye özel koşullama etkisini kontrol eder ve güç ile çarpılır. | MASK | Hayır | - |
| `iclora_parameters` | Get IC-LoRA Parametreleri düğümünden alınan opsiyonel IC-LoRA parametreleri. Belirli IC-LoRAlar tarafından gerekli olan rehberleme işlemlerini ayarlamak için kullanılır (örneğin, reference_downscale_factor > 1 olanlar). Zincirde kullanıldığında, her LTXVAddGuide sadece ona bağlanan parametreleri kullanır. | IC_LORA_PARİMERLER | Hayır | - |

**Not:** Girdi resim veya videosunun 8*n + 1 kare sayısına sahip olması gerekir (örneğin, 1, 9, 17, 25 kare). Girdi bu desenin üzerine çıkarsa, otomatik olarak en yakın geçerli kare sayısına kesilir.

**Not `iclora_parameters` hakkında:** reference_downscale_factor'ın 1'den büyük olduğu IC-LoRA parametreleri kullanıldığında, latent alan boyutları (genişlik ve yükseklik) bu faktöre bölünmelidir. Bu durumun yerine getirilmediği takdirde düğüm hata verecektir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Anahtar kare rehberliği bilgisi ile güncellenmiş olumlu koşullama | KOŞULLAMA |
| `negatif` | Anahtar kare rehberliği bilgisi ile güncellenmiş olumsuz koşullama | KOŞULLAMA |
| `gizli` | Koşullama karelerini içeren ve güncellenmiş gürültü maskesi ile latent sıra | LATENT |
```

Yukarıda sağlanan belge, kaynak koduna dayanmaktadır ve aşağıdaki güncellemeleri içerir:

- `frame_idx` parametresi, videosunun 9+ kareli olmaları durumunda `frame_idx`'in 8'e bölünmesi gereken bir değer olmasını gerektiren bir ipucu içerir.
- `iclora_parameters` parametresi, latent alan boyutlarının reference_downscale_factor'ın 1'den büyük olan IC-LoRA parametreleri kullanıldığında bu faktöre bölünmesi gerektiği konusunda bir not içerir.
- Genel Bakış bölümü, düğümün kaynak koduna dayalı işlevselliğini yansıtmak için güncellenmiştir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
