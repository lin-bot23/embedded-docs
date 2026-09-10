# OpenAI GPT Görüntü 2

Bu düğüm, OpenAI'nin GPT Image API'sini kullanarak görüntüler üretir. Beş modeli destekler — `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` ve `gpt-image-1` — görüntü düzenleme için referans görüntüler eklemenize olanak tanır ve bir görüntünün hangi bölümlerinin değiştirileceğini belirtmek için maske kullanabilir.

## Girdiler

### Ortak Girdiler

Bu girdiler her zaman görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model` | Kullanılacak OpenAI GPT Image modeli. Bir model seçmek, o modele özgü ek parametreleri ortaya çıkarır. | DYNAMIC_COMBO | Evet | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `istem` | GPT Image için metin istemi (varsayılan: `""`). | STRING | Evet | N/A |
| `n` | Üretilecek görüntü sayısı (varsayılan: `1`). | INT | Evet | 1 ile 8 |
| `tohum` | Tekrarlanabilirlik için tohum (seed) değeri (varsayılan: `0`). Henüz arka uçta uygulanmadı. | INT | Evet | 0 ile 2147483647 |

### gpt-image-2.5-flare ve gpt-image-2.5-sunburst Girdileri

Bu girdiler, `model` `gpt-image-2.5-flare` veya `gpt-image-2.5-sunburst` olarak ayarlandığında görünür. Her iki model de aynı parametre kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `özel_genişlik` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 (adım 16) |
| `özel_yükseklik` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 (adım 16) |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). En fazla 16 görüntü. Ayrıntılar için Referans Girdileri bölümüne bakın. | IMAGE | Hayır | 0 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | N/A |

### gpt-image-2 Girdileri

Bu girdiler, `model` `gpt-image-2` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görüntü boyutu. Özel genişlik ve yüksekliği kullanmak için "Custom" seçin (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `özel_genişlik` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 (adım 16) |
| `özel_yükseklik` | Yalnızca `model.size` "Custom" olduğunda kullanılır. 16'nın katı olmalıdır (varsayılan: `1024`). | INT | Hayır | 480 ile 3840 (adım 16) |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"` |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). En fazla 16 görüntü. Ayrıntılar için Referans Girdileri bölümüne bakın. | IMAGE | Hayır | 0 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | N/A |

### gpt-image-1.5 ve gpt-image-1 Girdileri

Bu girdiler, `model` `gpt-image-1.5` veya `gpt-image-1` olarak ayarlandığında görünür. Her iki model de aynı parametre kümesini paylaşır.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `boyut` | Görüntü boyutu (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `arka_plan` | Görüntüyü arka planlı veya arka plansız döndürür (varsayılan: `"auto"`). | COMBO | Evet | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `kalite` | Görüntü kalitesi; maliyeti ve üretim süresini etkiler (varsayılan: `"low"`). | COMBO | Evet | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Görüntü düzenleme için isteğe bağlı referans görüntü(ler). En fazla 16 görüntü. Ayrıntılar için Referans Girdileri bölümüne bakın. | IMAGE | Hayır | 0 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | N/A |

### Referans Girdileri

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
| --- | --- | --- | --- | --- |
| `model.images` | Genişletilebilir yuva: 1..N öğe bağlayın (örn. `image_1`...`image_16`); tüm modeller için en fazla 16 referans görüntü. | IMAGE | Hayır | 1 ile 16 |
| `model.mask` | Inpainting için isteğe bağlı maske (beyaz alanlar değiştirilir). Tam olarak bir referans görüntü gerektirir. | MASK | Hayır | N/A |

**Parametre Kısıtlamaları ve Sınırlamalar:**

- `model.size` "Custom" olduğunda (yalnızca `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` ve `gpt-image-2`), `model.custom_width` ve `model.custom_height` değerlerinin her ikisi de 16'nın katı olmalı, en uzun kenar 3840'ı aşmamalı, en-boy oranı 3:1'i geçmemeli ve toplam piksel sayısı 655.360 ile 8.294.400 arasında olmalıdır.
- `model.mask`, `model.images` içinde tam olarak bir referans görüntü gerektirir: bir görüntü olmadan kullanılamaz ve birden fazla görüntüyle de kullanılamaz.
- `model.mask` kullanıldığında, maskenin yüksekliği ve genişliği referans görüntünün yüksekliği ve genişliğiyle eşleşmelidir.
- `model.images` sağlandığında düğüm, görüntü düzenleme modunda çalışır; `model.images` olmadan görüntüleri yalnızca istemden üretir.
- Referans görüntüler ve maske, API'ye gönderilmeden önce küçültülür.
- `"xhigh"` ve `"max"` kalite seviyeleri yalnızca `gpt-image-2.5-flare` ve `gpt-image-2.5-sunburst` için kullanılabilir.
- `"transparent"` arka plan seçeneği `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-1.5` ve `gpt-image-1` için kullanılabilir, ancak `gpt-image-2` için kullanılamaz.
- `seed` şu anda arka uçta uygulanmamıştır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
| --- | --- | --- |
| `image` | Üretilen görüntü veya görüntüler. Döndürülen tüm görüntüler tek bir grup (batch) halinde istiflenir; boyutları farklıysa, ilk görüntüyle eşleşecek şekilde yeniden boyutlandırılır. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/tr.md)

---
**Source fingerprint (SHA-256):** `4f77b79f9f432a1f2e0fd814012aebe7cc42a8aa983ee9a61f3b32984bf65148`
