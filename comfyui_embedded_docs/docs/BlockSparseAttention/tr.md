# Model Seyrek Dikkat

## Genel Bakış

Blok Düzenli Dikkat düğümü, bir ComfyUI modeline blok-düzenli dikkat mekanizmasını uygulamak için kullanılır. Bu mekanizma, her sorgu bloğunun tüm olası bloklara değil, sadece belirli bir alt küme bloklara odaklanmasına izin vererek hesaplama yükünü azaltır ve uzun diziler için özellikle faydalıdır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `model` | Blok-düzenli dikkat uygulamak için kullanılacak ComfyUI modeli. | MODEL | Evet | N/A |
| `selection` | Anahtar blokları belirlemek için kullanılan yöntem. | DYNAMIC_COMBO | Evet | Seçenekler: sol-attn (uyumlu tau), sla (top-k), vsa (Video Düzenli Dikkat) |
| `tau` | sol-attn yönteminde puan dağılımı sigmalarında kullanılan eşiğin değeri. | FLOAT | Hayır | varsayılan: 1.3, min: 0.0, max: 4.0, adım: 0.05 |
| `keep_percent` | sla yönteminde her sorgu bloğunun kesin olarak tuttuğu anahtar blokların yüzdesi. | FLOAT | Hayır | varsayılan: 10.0, min: 0.5, max: 95.0, adım: 0.5 |
| `start_percent` | Düzenli dikkat başlamaya başladığı yüzdesi noktası. | FLOAT | Hayır | varsayılan: 0.2, min: 0.0, max: 1.0, adım: 0.01 |
| `end_percent` | Düzenli dikkat bittiği yüzdesi noktası. | FLOAT | Hayır | varsayılan: 1.0, min: 0.0, max: 1.0, adım: 0.01 |
| `dense_blocks` | Her zaman yoğun dikkat kullanacak transformer bloklarını temsil eden bir string. | STRING | Hayır | varsayılan: "", |
| `min_tokens` | Modelin yoğun dikkat kullanacağı dizideki en az token sayısı. | INT | Hayır | varsayılan: 12288, min: 0, max: 1 << 20, adım: 512 |
| `extra_tokens` | Her sorgu bloğunun seçili bloklarının ötesinde dikkat ettiği ekstra en yüksek puanlı token sayısı. | INT | Hayır | varsayılan: 256, min: 0, max: 256, adım: 64 |
| `sink_conditioning` | Kullanılacak MiniMax-H3 şartlandırma satırları. | COMBO | Hayır | Seçenekler: exact_kv, exact_kv_and_rows, off |
| `verbose` | Ayrıntılı günlüklemeyi etkinleştirir. | BOOLEAN | Hayır | varsayılan: False |

### Notlar

- `selection` parametresi, anahtar blokları seçmek için farklı yöntemler arasında seçim yapmanıza olanak tanır:
  - `sol-attn`: Puan dağılımına dayalı olarak anahtar blokları seçmek için uyumlu bir eşiği kullanır.
  - `sla`: En yüksek puanlı anahtar blokların sabit bir yüzdesini tutar.
  - `vsa`: 3B video-küp döşeme ve öğrenilmiş ince dikkat dalığını kullanarak Video Düzenli Dikkat uygular.
- `dense_blocks` parametresi, her zaman yoğun dikkat kullanacak transformer bloklarını belirtmek için kullanılır.
- `min_tokens` parametresi, yoğun dikkatin kullanılacağı dizideki en az token sayısını ayarlar.
- `extra_tokens` parametresi, her sorgu bloğunun seçili bloklarının ötesinde dikkat ettiği ekstra en yüksek puanlı token sayısını belirler.
- `sink_conditioning` parametresi yalnızca MiniMax-H3 modelleri için geçerlidir ve şartlandırma satırlarının nasıl ele alınacağını belirler.
- `verbose` parametresi, ayrıntılı günlüklemeyi etkinleştirir ve hata ayıklamada faydalı olabilir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model` | Blok-düzenli dikkat uygulandıktan sonra olan ComfyUI modeli. | MODEL |

### Kısıtlamalar ve Sınırlamalar

- `sol-attn` yöntemi için `tau` değeri 0.0 ile 4.0 arasında olmalıdır.
- `sla` yöntemi için `keep_percent` değeri 0.5 ile 95.0 arasında olmalıdır.
- `vsa` yöntemi yalnızca MiniMax-H3 modelleri ile uyumludur ve modelin `to_gate_compress` katmanına sahip olması gerekmektedir.
- `min_tokens` parametresi negatif olmayan bir tamsayı olmalıdır (0 ayarlanırsa tüm dikkat işlemi yoğun kalır).
- `extra_tokens` parametresi negatif olmayan bir tamsayı olmalıdır.
- `sink_conditioning` seçenekleri yalnızca MiniMax-H3 modelleri için geçerlidir.

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/tr.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
