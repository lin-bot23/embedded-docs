# Tripo: Metinden Modele

Tripo'nun API'sini kullanarak bir metin açıklamasından bitmiş 3D modeller üretir. Düğüm, üretimin tamamlanmasını bekler ve ardından model dosyasını, isteğe bağlı olarak dokular ve PBR malzemelerle birlikte döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `istek` | Oluşturulacak 3D modelin metin açıklaması (çok satırlı). Bu parametre zorunludur ve boş olamaz. | STRING | Evet | - |
| `olumsuz_istek` | Oluşturulan modelde kaçınılması gerekenlerin metin açıklaması (çok satırlı). En fazla 255 karakter. Yalnızca boş olmadığında API'ye gönderilir. | STRING | Hayır | Up to 255 characters |
| `model_versiyonu` | Üretim için kullanılacak Tripo modelinin sürümü (varsayılan: v3.1-20260211). | COMBO | Hayır | Multiple options available |
| `stil` | Oluşturulan modele uygulanan stil (varsayılan: None). Tripo tarafından artık desteklenmiyor ve yok sayılıyor; eski iş akışları için korunuyor. | COMBO | Hayır | Multiple options available |
| `doku` | Doku haritalarının oluşturulup oluşturulmayacağı. Kapalı, çıplak geometri döndürür ve `pbr` yok sayılır (varsayılan: True). | BOOLEAN | Hayır | true / false |
| `pbr` | PBR malzeme haritalarının (temel renk, metaliklik, pürüzlülük, normal) oluşturulup oluşturulmayacağı. `texture` gerektirir; `texture` kapalıyken zorla kapatılır (varsayılan: True). | BOOLEAN | Hayır | true / false |
| `görüntü_tohumu` | Görüntü oluşturma aşamasında kullanılan tohum (varsayılan: 42). | INT | Hayır | 0 ile 2147483647 |
| `model_tohumu` | Model oluşturma aşamasında kullanılan tohum (varsayılan: 42). | INT | Hayır | 0 ile 2147483647 |
| `doku_tohumu` | Doku oluşturma aşamasında kullanılan tohum (varsayılan: 42). | INT | Hayır | 0 ile 2147483647 |
| `doku_kalitesi` | Oluşturulan dokuların kalitesi. detailed = HD dokular, extreme = 8K Ultra dokular (varsayılan: standard). | COMBO | Hayır | "standard"<br>"detailed"<br>"extreme" |
| `yüz_sınırı` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı olarak seçmesini sağlar (v3.x standardında yaklaşık 1,4M yüz, detailed'da 2M). Tripo sessizce sınırlar: v2.5'te 500.000, dörtgen ağlarda 150.000. (varsayılan: -1) | INT | Hayır | -1 ile 2000000 |
| `dörtgen` | Dörtgen ağ çıktısı. Tripo dörtgen ağları FBX olarak teslim eder, böylece sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Hayır | true / false |
| `geometry_quality` | Oluşturulan geometrinin kalitesi (varsayılan: standard). | COMBO | Hayır | "standard"<br>"detailed" |
| `smart_low_poly` | Temiz, el yapımı tarzda topolojiye sahip düşük poligonlu ağ (500-20.000 yüz, dörtgen 500-10.000). Basit konular için en iyisi; karmaşık olanlar başarısız olabilir. (varsayılan: False) | BOOLEAN | Hayır | true / false |
| `auto_size` | Dokulu modelleri gerçek dünya boyutlarına metre cinsinden ölçekler. Tripo boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, donatıldığında veya yeniden hedeflendiğinde bunu kalıcı olarak uygular; doku olmadan yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | true / false |

**Notlar:**
- `prompt` parametresi zorunludur: boş bir prompt, düğümün hata vermesine neden olur.
- `pbr`, `texture` gerektirir. `texture` kapalıyken düğüm `pbr` değerini zorla kapatır ve yok sayar. `auto_size` da `texture` olmadan hiçbir etkiye sahip değildir.
- `smart_low_poly` etkinleştirildiğinde ve `face_limit` -1 dışında bir değere ayarlandığında, yüz sınırı üçgen çıktı için 500 ile 20.000 arasında veya `quad` etkinleştirildiğinde 500 ile 10.000 arasında olmalıdır; aksi takdirde düğüm hata verir.
- `quad` etkinleştirildiğinde, oluşturulan dörtgen ağ FBX olarak teslim edilir, bu nedenle FBX çıktısı doldurulur ve GLB çıktısı boş kalır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3D model dosyası, yalnızca geriye dönük uyumluluk için saklanır. | STRING |
| `model_görev_id` | Model oluşturma süreci için benzersiz görev tanımlayıcısı. | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3D model. `quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3D model. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `3f4bc09d125fedb6c30968f31804cfc7ec6d2f068a7c28d90b006137803020b0`
