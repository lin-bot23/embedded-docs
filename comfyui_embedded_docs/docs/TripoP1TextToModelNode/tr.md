# Tripo P1: Metinden Modele

Bu düğüm, Tripo P1 API'sini kullanarak bir metin açıklamasından 3B model üretir. Düşük poligonlu, oyuna hazır ve kararlı topolojiye sahip modeller oluşturmak için optimize edilmiştir; bu da onu gerçek zamanlı uygulamalar için uygun kılar.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `çıktı_modu` | Oluşturulan modelin yalnızca geometri mi yoksa renk/PBR dokuları mı içereceğini kontrol eder. "Textured" seçildiğinde aşağıya doku girdileri eklenir. "Geometry only" dokusuz bir ağ döndürür; "Textured" ise renk/PBR haritaları ekler. | DYNAMIC_COMBO | Evet | `"Geometry only"`<br>`"Textured"` |
| `istem` | Oluşturmak istediğiniz 3B modelin metin açıklaması. En fazla 1024 karakter. | STRING | Evet | Up to 1024 characters |
| `negatif_istem` | Oluşturulan modelde istemediklerinizi tanımlayan metin açıklaması. En fazla 255 karakter. | STRING | Hayır | Up to 255 characters |
| `görüntü_tohumu` | Görüntü üretimi için kullanılan ve rastgeleliği kontrol eden tohum değeri. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 |
| `yüz_sınırı` | Hedef yüz sayısı, 48-20000. -1 değeri Tripo'nun uyarlanabilir şekilde seçmesini sağlar. Varsayılan: -1. | INT | Hayır | -1 ile 20000 |
| `model_tohumu` | Model üretimi için kullanılan ve rastgeleliği kontrol eden tohum değeri. Varsayılan: 42. | INT | Hayır | 0 ile 2147483647 |
| `otomatik_boyut` | Çıktıyı yaklaşık gerçek dünya metrelerine ölçekler. Varsayılan: False. | BOOLEAN | Hayır | True / False |
| `uv_dışa_aktar` | Üretim sırasında UV açılımı yapar. Yalnızca geometri çalıştırmalarında hız için kapatın. Varsayılan: True. | BOOLEAN | Hayır | True / False |
| `geometriyi_sıkıştır` | meshopt geometri sıkıştırması uygular (EXT_meshopt_compression). Daha küçük dosyalar elde edilir, ancak ComfyUI'nin 3B önizlemesi bunları görüntüleyemez; düzenlemeden önce sıkıştırmayı açın. Varsayılan: False. | BOOLEAN | Hayır | True / False |

### Yalnızca Geometri Girdileri

`output_mode` parametresi `"Geometry only"` olarak ayarlandığında ek girdi bulunmaz. Bu modda doku ile ilgili parametreler Tripo'ya gönderilmez.

### Dokulu Girdiler

Bu girdiler yalnızca `output_mode` parametresi `"Textured"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR haritalarını dahil eder. Açıkken temel doku da zorunlu olarak açılır. Varsayılan: True. | BOOLEAN | Evet | True / False |
| `texture_quality` | Doku kalitesi ön ayarı. detailed = HD dokular, extreme = 8K Ultra dokular. Varsayılan: "standard". | COMBO | Evet | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Doku üretimi için kullanılan ve rastgeleliği kontrol eden tohum değeri. Varsayılan: 42. | INT | Evet | 0 ile 2147483647 |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3B modelin dosya yolu; yalnızca geriye dönük uyumluluk için korunur. | STRING |
| `model_görev_id` | Model oluşturma isteği için benzersiz görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. | FILE3DGLB |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `63781a990f892e6b1f241179039d1fb24778ba7aa7dccda7d14557cbf190b712`
