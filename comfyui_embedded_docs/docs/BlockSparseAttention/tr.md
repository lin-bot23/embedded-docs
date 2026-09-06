# Block Sparse Attention

## Genel Bakış

Block Sparse Attention düğümü, bir ComfyUI modeline blok-sparse dikkat mekanizmasını uygular ve her sorgu bloğunun yalnızca seçilmiş bir anahtar blok kümesine dikkat etmesine izin vererek dikkat hesaplama işlemini azaltır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Blok-sparse dikkat mekanizmasını uygulamak için kullanılacak ComfyUI modeli. | MODEL | Evet | N/A |
| `selection` | Anahtar bloklara dikkat etmeyi seçmek için kullanılan seçim yöntemi. | DYNAMIC_COMBO | Evet | Seçenekler: Sol-Attn (uyumlu tau), top-k (SLA), VSA (FastVideo) |
| `tau` | Sol-Attn (uyumlu tau) seçimi için puan dağılım sigmalarındaki eşiğin değeri. | FLOAT | Hayır | varsayılan: 1.3, min: 0.0, max: 4.0, adım: 0.05 |
| `keep_percent` | Her sorgu bloğunun top-k (SLA) seçimi için kesin olarak tuttuğu anahtar blokların yüzdesi. | FLOAT | Hayır | varsayılan: 10.0, min: 0.5, max: 95.0, adım: 0.5 |
| `start_percent` | Modelin yoğun dikkat kullanmaya başlayacağı programın yüzdesi. | FLOAT | Hayır | varsayılan: 0.2, min: 0.0, max: 1.0, adım: 0.01 |
| `end_percent` | Modelin yoğun dikkat kullanmaya devam edeceği programın yüzdesi. | FLOAT | Hayır | varsayılan: 1.0, min: 0.0, max: 1.0, adım: 0.01 |
| `dense_blocks` | Her zaman yoğun dikkat çalıştıran transformer bloklarını temsil eden bir dizi. | STRING | Hayır | varsayılan: "", |
| `min_tokens` | Modelin yoğun dikkat kullanacağı dizideki en az token sayısı. | INT | Hayır | varsayılan: 12288, min: 0, max: 1 << 20, adım: 512 |
| `extra_tokens` | Her sorgu bloğunun seçilmiş bloklarının ötesinde dikkat ettiği ek en yüksek puanlı token sayısı. | INT | Hayır | varsayılan: 256, min: 0, max: 256, adım: 64 |
| `sink_conditioning` | Sink conditioning için kullanılacak MiniMax-H3 şartlandırma satırları. | COMBO | Hayır | Seçenekler: exact_kv, exact_kv_and_rows, off |
| `verbose` | Açıklamalı günlüklemeyi etkinleştirme. | BOOLEAN | Hayır | varsayılan: False |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Blok-sparse dikkat mekanizması uygulanmış ComfyUI modeli. | MODEL |

### Notlar

- `selection` parametresi, anahtar blokların nasıl seçileceğini belirler. Seçenekler:
  - Sol-Attn (uyumlu tau): Her sorgu bloğu, uyumlu bir eşiğe dayanarak seçilmiş bir anahtar blok kümesine dikkat eder.
  - top-k (SLA): Her sorgu bloğu, kesin olarak belirli bir yüzdedeki anahtar blokları tutar.
  - VSA (FastVideo): Her sorgu bloğu, FastH3-VSA'nın küp döşeme ve ince dal kullanarak kesin olarak belirli bir yüzdedeki video kübelerine dikkat eder.
- `dense_blocks` parametresi, her zaman yoğun dikkat çalıştıran transformer bloklarını belirtmenize olanak tanır.
- `min_tokens` parametresi, modelin yoğun dikkat kullanacağı dizideki en az token sayısını ayarlar.
- `extra_tokens` parametresi, her sorgu bloğunun seçilmiş bloklarının ötesinde dikkat ettiği ek en yüksek puanlı token sayısını belirler.
- `sink_conditioning` parametresi, sink conditioning için kullanılacak MiniMax-H3 şartlandırma satırlarını belirler.
- `verbose` parametresi, açıklamalı günlüklemeyi etkinleştirir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/tr.md)

---
**Source fingerprint (SHA-256):** `6a27aee45593883f5958ae1aac74a2077362742a0fdf74fc9dbfd68eddc6d259`
