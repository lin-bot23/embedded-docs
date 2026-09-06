# MiniMax H3 Metinden Videoya

Bu düğüm; MiniMax H3, MiniMax H3 Max ve MiniMax H3 Max Turbo modellerini içeren MiniMax H3 model ailesini kullanarak bir metin isteminden video oluşturur. Modeli seçersiniz, metin istemini girersiniz ve çözünürlük, en-boy oranı ve süre gibi ayarları belirlersiniz. Düğüm, isteği MiniMax API'ye gönderir, üretim görevinin tamamlanmasını bekler ve sonuçta oluşan videoyu döndürür.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Video üretimi için kullanılacak model (varsayılan: "MiniMax H3"). Bir model seçmek, aşağıdaki bölümlerde açıklanan modele özel ayarları da gösterir. | DYNAMIC_COMBO | Evet | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `seed` | Rastgele tohum. Aynı istek aynı tohumla tekrarlandığında benzer sonuçlar üretir; ancak sonuçların birebir aynı olması garanti edilmez (varsayılan: 42). | INT | Evet | 0 ila 4294967295 |
| `watermark` | Videoya bir AIGC filigranı eklenip eklenmeyeceği (varsayılan: false). Etkinleştirildiğinde yalnızca "MiniMax H3" modeli desteklenir. | BOOLEAN | Hayır | true<br>false |

### MiniMax H3 Girdileri

Bu ayarlar, "MiniMax H3" modeli seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Boşluk olmayan en az bir karakter içermelidir. | STRING | Evet | Herhangi bir metin |
| `resolution` | Çıktı videosunun çözünürlüğü. | COMBO | Evet | "768P"<br>"2K" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (4-15) (varsayılan: 5). | INT | Evet | 4 ila 15 |

### MiniMax H3 Max ve MiniMax H3 Max Turbo Girdileri

Bu ayarlar, "MiniMax H3 Max" ve "MiniMax H3 Max Turbo" modelleri tarafından paylaşılır ve bu modellerden herhangi biri seçildiğinde görünür.

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Video üretimi için metin istemi. Boşluk olmayan en az bir karakter içermeli ve en fazla 50.000 karakter uzunluğunda olabilir. | STRING | Evet | En fazla 50000 karakter |
| `resolution` | Çıktı videosunun çözünürlüğü (varsayılan: "768P"). | COMBO | Evet | "480P"<br>"768P" |
| `ratio` | Çıktı videosunun en-boy oranı (varsayılan: "16:9"). | COMBO | Evet | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Çıktı videosunun saniye cinsinden süresi (5-15) (varsayılan: 5). | INT | Evet | 5 ila 15 |
| `prompt_expansion_mode` | Üretimden önce istemin yeniden yazılması için ne kadar çaba harcandığı (varsayılan: "balanced"). | COMBO | Evet | "balanced"<br>"quality" |

### Notlar

- Tüm modellerde istem, boşluk olmayan en az bir karakter içermelidir.
- `watermark` ayarı yalnızca "MiniMax H3" tarafından desteklenir. "MiniMax H3 Max" veya "MiniMax H3 Max Turbo" ile etkinleştirilmesi hataya neden olur.
- "MiniMax H3 Max" ve "MiniMax H3 Max Turbo" modelleri istemi 50.000 karakterle sınırlar.
- Çözünürlük ve süre sınırları seçilen modele bağlıdır: "MiniMax H3", "768P" ve "2K" çözünürlüğü ve 4-15 saniyelik videoları desteklerken; "MiniMax H3 Max" ve "MiniMax H3 Max Turbo", "480P" ve "768P" çözünürlüğü ve 5-15 saniyelik videoları destekler.
- Bu düğüm için gösterilen tahmini fiyat; seçilen modele, çözünürlüğe ve süreye göre hesaplanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `VIDEO` | Sağlanan metin isteminden oluşturulan video. | VIDEO |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/tr.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
