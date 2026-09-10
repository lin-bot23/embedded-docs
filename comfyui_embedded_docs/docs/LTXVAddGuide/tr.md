# LTXVRehberEkle

LTXVAddGuide düğümü, girdi görüntülerini veya videolarını kodlayıp bunları koşullandırma verisine ana kareler olarak ekleyerek latent dizilere video koşullandırma rehberliği ekler. Girdiyi bir VAE kodlayıcıdan geçirir ve elde edilen latentleri belirtilen kare konumlarına stratejik olarak yerleştirirken, hem pozitif hem de negatif koşullandırmayı ana kare bilgisiyle günceller. Düğüm, kare hizalama kısıtlamalarını yönetir ve koşullandırma etkisinin gücü üzerinde kontrol sağlar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `pozitif` | Ana kare rehberliğiyle değiştirilecek pozitif koşullandırma girdisi | CONDITIONING | Evet | - |
| `negatif` | Ana kare rehberliğiyle değiştirilecek negatif koşullandırma girdisi | CONDITIONING | Evet | - |
| `vae` | Girdi görüntü/video karelerini kodlamak için kullanılan VAE modeli | VAE | Evet | - |
| `gizli` | Koşullandırma karelerini alacak girdi latent dizisi | LATENT | Evet | - |
| `görüntü` | Latent videoyu koşullandırmak için kullanılacak görüntü veya video. 8*n + 1 kare olmalıdır. Video 8*n + 1 kare değilse, en yakın 8*n + 1 kare sayısına kırpılır. | IMAGE | Evet | - |
| `kare_indeksi` | Koşullandırmanın başlatılacağı kare dizini. Tek kare görüntüler veya 1-8 kare içeren videolar için herhangi bir frame_idx değeri kabul edilebilir. 9 veya daha fazla kare içeren videolar için frame_idx 8'e bölünebilir olmalıdır; aksi takdirde en yakın 8'in katına aşağı yuvarlanır. Negatif değerler videonun sonundan itibaren sayılır. (varsayılan: 0) | INT | Evet | -9999 - 9999 |
| `güç` | Koşullandırma etkisinin gücü; 1.0 tam koşullandırma uygular, 0.0 koşullandırma uygulamaz (varsayılan: 1.0) | FLOAT | Evet | 0.0 - 10.0 |
| `attention_mask` | İsteğe bağlı piksel uzayında uzamsal maske. Kendine dikkat (self-attention) mekanizması aracılığıyla bölge bazında koşullandırma etkisini kontrol eder; strength değeriyle çarpılır. | MASK | Hayır | - |
| `iclora_parameters` | Get IC-LoRA Parameters düğümünden alınan isteğe bağlı IC-LoRA parametreleri. Belirli IC-LoRA'ların gerektirdiği şekilde rehber işlemesini ayarlamak için kullanılır (örn. reference_downscale_factor > 1 olanlar). Zincirleme kullanımda her LTXVAddGuide yalnızca kendisine bağlı parametreleri kullanır. | IC_LORA_PARAMETERS | Hayır | - |

**Not:** Girdi görüntü/video, 8*n + 1 düzenini izleyen bir kare sayısına sahip olmalıdır (örn. 1, 9, 17, 25 kare). Girdi bu düzeni aşarsa, otomatik olarak en yakın geçerli kare sayısına kırpılır.

**`iclora_parameters` hakkında not:** `reference_downscale_factor` değeri 1'den büyük olan IC-LoRA parametreleri kullanıldığında, latent uzamsal boyutları (genişlik ve yükseklik) bu faktöre bölünebilir olmalıdır. Bu koşul sağlanmazsa düğüm bir hata verir.

**Not:** Kodlanmış rehber kareleri, seçilen kare konumunda latent dizinin içine sığmalıdır. Koşullandırılan kareler latent dizinin uzunluğunu aşarsa düğüm bir hata verir.

**Not:** Ses ve video kanallarını birleştiren bir latente rehber eklenmesi desteklenmez ve hata verir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `pozitif` | Ana kare rehberlik bilgisiyle güncellenmiş pozitif koşullandırma | CONDITIONING |
| `negatif` | Ana kare rehberlik bilgisiyle güncellenmiş negatif koşullandırma | CONDITIONING |
| `gizli` | Koşullandırma kareleri eklenmiş ve gürültü maskesi güncellenmiş latent dizi | LATENT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/tr.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
