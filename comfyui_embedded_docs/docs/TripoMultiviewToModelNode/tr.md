# Tripo: Çok Bakışlıdan Modele

Bu düğüm, Tripo'nun API'sini kullanarak, bir nesnenin farklı görünümlerini (ön, sol, arka, sağ) gösteren en fazla dört görüntüyü işleyerek 3D modelleri eşzamanlı olarak üretir. 3D model oluşturmak için bir ön görüntü ve en az bir ek görünüm (sol, arka veya sağ) gerekir. Doku, PBR malzeme, geometri kalitesi ve çıktı formatı düğümden kontrol edilebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | Nesnenin ön görünüm görüntüsü. | IMAGE | Evet | - |
| `sol_görüntü` | Nesnenin sol görünüm görüntüsü. | IMAGE | Hayır | - |
| `arka_görüntü` | Nesnenin arka görünüm görüntüsü. | IMAGE | Hayır | - |
| `sağ_görüntü` | Nesnenin sağ görünüm görüntüsü. | IMAGE | Hayır | - |
| `model_versiyonu` | Üretim için kullanılacak model sürümü. | COMBO | Hayır | Birden çok seçenek mevcut |
| `yönlendirme` | 3D model için yön ayarı (varsayılan: `"default"`). | COMBO | Hayır | Birden çok seçenek mevcut |
| `doku` | Doku haritaları oluşturur. Kapalıyken çıplak geometri döndürür ve pbr'yi yok sayar. (varsayılan: True) | BOOLEAN | Hayır | - |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). Doku gerektirir. (varsayılan: True) | BOOLEAN | Hayır | - |
| `model_tohumu` | Model üretimi için rastgele tohum (varsayılan: 42). | INT | Hayır | 0 ile 2,147,483,647 arası |
| `doku_tohumu` | Doku üretimi için rastgele tohum (varsayılan: 42). | INT | Hayır | 0 ile 2,147,483,647 arası |
| `doku_kalitesi` | Doku üretimi için kalite düzeyi (varsayılan: `"standard"`). `"detailed"` = HD dokular, `"extreme"` = 8K Ultra dokular. | COMBO | Hayır | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `doku_hizalama` | Dokuları modele hizalamak için kullanılan yöntem (varsayılan: `"original_image"`). | COMBO | Hayır | `"original_image"`<br>`"geometry"` |
| `yüz_sınırı` | Maksimum yüz sayısı. -1, Tripo'nun uyarlanabilir şekilde seçmesini sağlar (v3.x standard'da yaklaşık 1.4M yüz, detailed'da 2M). Tripo sessizce sınırlar: v2.5'te 500,000, dörtgen ağlarda 150,000. (varsayılan: -1) | INT | Hayır | -1 ile 2,000,000 arası |
| `dörtgen` | Dörtgen ağ çıktısı. Tripo, dörtgen ağları FBX olarak teslim eder; bu nedenle sonuç FBX çıktısında görünür ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Hayır | - |
| `geometry_quality` | Geometri üretimi için kalite düzeyi (varsayılan: `"standard"`). | COMBO | Hayır | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Temiz, el işçiliği tarzı topolojiye sahip düşük poli ağ (500-20,000 yüz, dörtgen ağlarda 500-10,000). Basit nesneler için en iyisidir; karmaşık olanlar başarısız olabilir. (varsayılan: False) | BOOLEAN | Hayır | - |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçeklendirir. Tripo, boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, rig'lendiğinde veya yeniden hedeflendiğinde bu boyutu kalıcı hale getirir; doku olmadan yok sayılır. (varsayılan: False) | BOOLEAN | Hayır | - |

**Not:** Ön görüntü (`image`) her zaman gereklidir ve `image_left`, `image_back` veya `image_right` görüntülerinden en az biri de sağlanmalıdır. `texture` kapatıldığında, `pbr` doku gerektirdiği için `pbr` de otomatik olarak kapanır. `smart_low_poly` etkinleştirildiğinde ve `face_limit` -1 değilse, `face_limit` üçgen ağlar için 500 ile 20,000 arasında veya dörtgen ağlar için 500 ile 10,000 arasında olmalıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3D model için dosya yolu veya tanımlayıcı (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_görev_id` | Model üretim sürecini izlemek için görev tanımlayıcı. | MODEL_TASK_ID |
| `GLB` | GLB formatında oluşturulan 3D model dosyası. `quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | FBX formatında oluşturulan 3D model dosyası. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `73f1259dcba75ce1d56aabb6f0435f11d21eee3268f93502c4c3293d562a6db0`
