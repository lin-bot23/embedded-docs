# MiniMax H3 Referans ile Videoya

Bu düğüm, MiniMax H3 modellerini kullanarak referans görsellere, videolara ve seslere koşullu olarak bir video üretir. Referanslara, istemde bağlantı sırasına göre "Image 1", "Image 2", "Video 1", "Audio 1" vb. şeklinde atıfta bulunulur. İki model mevcuttur: "MiniMax H3" ve "MiniMax H3 Max".

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `model` | Video oluşturma için kullanılacak model (varsayılan: "MiniMax H3"). "MiniMax H3" seçildiğinde aşağıdaki MiniMax H3 oluşturma ve referans girdileri sunulur. "MiniMax H3 Max" seçildiğinde aşağıdaki MiniMax H3 Max oluşturma ve referans girdileri sunulur. | DYNAMIC_COMBO | Evet | "MiniMax H3"<br>"MiniMax H3 Max" |
| `seed` | Rastgele tohum. Aynı tohumla yapılan aynı istek benzer sonuçlar verir; ancak sonuçların birebir aynı olması garanti edilmez (varsayılan: 42). | INT | Evet | 0 ile 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği (varsayılan: false). Yalnızca MiniMax H3 modeli tarafından desteklenir. | BOOLEAN | Hayır | true<br>false |

### MiniMax H3 Girdileri

Bu girdiler, model olarak "MiniMax H3" seçildiğinde kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Video oluşturma için metin istemi. Referans medyaya sırayla atıfta bulunulabilir; örneğin "Image 1", "Image 2", "Video 1" veya "Audio 1". | STRING | Evet | En az 1 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "768P"<br>"2K" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "adaptive"). | COMBO | Evet | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 4 ile 15 |

### MiniMax H3 Max Girdileri

Bu girdiler, model olarak "MiniMax H3 Max" seçildiğinde kullanılabilir.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `prompt` | Video oluşturma için metin istemi. Referans medyaya sırayla atıfta bulunulabilir; örneğin "Image 1", "Image 2", "Video 1" veya "Audio 1". | STRING | Evet | 1 ila 50000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "adaptive"). | COMBO | Evet | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (varsayılan: 5). | INT | Evet | 5 ile 15 |
| `prompt_expansion_mode` | Oluşturmadan önce istemin yeniden yazılmasına ne kadar çaba harcanacağı (varsayılan: "balanced"). | COMBO | Evet | "balanced"<br>"quality" |
| `reference_detail` | Referans görsellerin gönderildiği ayrıntı düzeyi. "high" seçeneği, görselleri modelin kullandığı en büyük boyutta (kısa kenar 2048 piksele kadar) gönderir; "standard" seçeneği ise referans maliyetini azaltmak amacıyla bunları en fazla 2048x1024 boyutuna küçültür (varsayılan: "standard"). | COMBO | Evet | "high"<br>"standard" |

### Referans Girdileri

Bu referans girdileri her iki model tarafından da paylaşılır. Her biri genişletilebilir bir yuvadır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|----------|-----------|---------|--------|
| `reference_images` | Genişletilebilir yuva: en fazla 9 öğe bağlayın (`image_1`...`image_9`). Bağlantı sırasına göre istemde "Image 1".."Image 9" olarak belirtilen konu veya stil referans görselleri. En fazla 9 görsel. | IMAGE | Hayır | 0 ila 9 görsel |
| `reference_videos` | Genişletilebilir yuva: en fazla 3 öğe bağlayın (`video_1`...`video_3`). Bağlantı sırasına göre istemde "Video 1".."Video 3" olarak belirtilen hareket veya sahne referans videoları. Her biri 2-15 saniye olmak üzere toplamda en fazla 15 saniyelik 3 videoya kadar. | VIDEO | Hayır | 0 ila 3 video |
| `reference_audios` | Genişletilebilir yuva: en fazla 3 öğe bağlayın (`audio_1`...`audio_3`). Bağlantı sırasına göre istemde "Audio 1".."Audio 3" olarak belirtilen ses referansları. Her biri 2-15 saniye olmak üzere toplamda en fazla 15 saniyelik 3 ses klibine kadar. Bir referans görseli veya videosu olmadan kullanılamaz. | AUDIO | Hayır | 0 ila 3 ses klibi |

### Parametre Kısıtlamaları

- En az bir referans görseli veya bir referans videosu gereklidir. Yalnızca referans sesi kabul edilmez.
- Her referans görseli, yaklaşık 0.4 ile 2.5 (2:5 ile 5:2) arasında bir en-boy oranına ve en az 256 piksel genişlik ve yüksekliğe sahip olmalıdır.
- Her referans videosu, saniyede 23.976 ile 60 kare (FPS) arasında bir kare hızıyla 2 ile 15 saniye arasında olmalıdır. Tüm referans videolarının toplam süresi 15 saniyeyi aşamaz.
- Her referans ses klibi 2 ile 15 saniye arasında olmalıdır. Tüm referans ses kliplerinin toplam süresi 15 saniyeyi aşamaz.
- "MiniMax H3 Max" seçildiğinde `watermark` ayarı devre dışı bırakılmalıdır.
- "MiniMax H3 Max" seçildiğinde toplam referans dosyası sayısı (görseller, videolar ve sesler birlikte) 12'yi aşamaz.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-----------|----------|-----------|
| `video` | Oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/tr.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
