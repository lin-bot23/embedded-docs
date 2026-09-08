# Tripo: Görüntüden Modele

Tripo'nun API'sini kullanarak tek bir görüntüden eşzamanlı olarak 3B modeller üretir. Bir girdi görüntüsü sağlayın; düğüm, model sürümü, doku üretimi, ayrıntı düzeyi ve çıktı biçimi için isteğe bağlı kontrollerle bundan tamamlanmış bir 3B model oluşturur.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `görüntü` | 3B modeli üretmek için kullanılan girdi görüntüsü. Bir görüntü sağlanmalıdır, aksi takdirde düğüm bir hata oluşturur. | IMAGE | Evet | - |
| `model_sürümü` | Üretim için kullanılacak model sürümü. | COMBO | Hayır | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `stil` | Artık Tripo tarafından desteklenmiyor ve yok sayılıyor. Eski iş akışları için saklandı. (varsayılan: `"None"`) | COMBO | Hayır | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `doku` | Doku haritaları üretir. Kapalıyken yalnızca geometri döndürür ve `pbr` yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `pbr` | PBR malzeme haritaları (temel renk, metalik, pürüzlülük, normal). `texture` gerektirir. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |
| `model_tohumu` | Model üretimi için rastgele tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `yönlendirme` | Üretilen model için yön ayarı. (varsayılan: `"default"`) | COMBO | Hayır | `"default"`<br>`"front"`<br>`"back"`<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `doku_tohumu` | Doku üretimi için rastgele tohum. (varsayılan: 42) | INT | Hayır | 0 ile 2147483647 |
| `doku_kalitesi` | Doku üretimi için kalite düzeyi: `detailed` = HD dokular, `extreme` = 8K Ultra dokular. (varsayılan: `"standard"`) | COMBO | Hayır | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `doku_hizalama` | Doku haritalama için hizalama yöntemi. (varsayılan: `"original_image"`) | COMBO | Hayır | `"original_image"`<br>`"geometry"` |
| `yüz_sınırı` | Maksimum yüz sayısı. -1, Tripo'nun uyarlamalı olarak seçim yapmasını sağlar (v3.x standart sürümünde yaklaşık 1,4 milyon yüz, detaylı sürümde 2 milyon). Tripo sınırı sessizce uygular: v2.5 için 500.000, dörtgen ağlar için 150.000. (varsayılan: -1) | INT | Hayır | -1 ile 2000000 |
| `dörtlü` | Dörtgen ağ çıktısı. Tripo dörtgen ağları FBX olarak teslim eder; bu nedenle sonuç FBX çıktısına gelir ve GLB çıktısı boş kalır. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `geometry_quality` | Geometri üretimi için kalite düzeyi. (varsayılan: `"standard"`) | COMBO | Hayır | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | Temiz, el yapımı tarzda topolojiye sahip düşük poligonlu (low-poly) ağ (500-20.000 yüz, quad 500-10.000). Basit nesneler için idealdir; karmaşık olanlarda başarısız olabilir. (varsayılan: False) | BOOLEAN | Hayır | True<br>False |
| `auto_size` | Dokulu modelleri metre cinsinden gerçek dünya boyutlarına ölçekler. Tripo, boyutu modelin sahne dönüşümü olarak saklar ve model dönüştürüldüğünde, donatıldığında veya yeniden hedeflendiğinde bunu kalıcı olarak uygular; doku yoksa yok sayılır. (varsayılan: True) | BOOLEAN | Hayır | True<br>False |

Not: Bir `image` gereklidir; eksikse düğüm bir RuntimeError fırlatır. `texture` False olduğunda model yalnızca çıplak geometri içerir ve `pbr` False değerine zorlanır. `smart_low_poly` etkinleştirildiğinde, `face_limit` üçgen ağlar için 500 ile 20.000 arasında veya `quad` da etkinleştirilmişse 500 ile 10.000 arasında olmalıdır; sınır geçersizse düğüm bir ValueError fırlatır. `face_limit` değerinin -1 (varsayılan) olarak ayarlanması API'ye açık bir yüz sınırı göndermez ve Tripo'nun uyarlamalı olarak seçim yapmasını sağlar.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_dosyası` | Oluşturulan 3B model dosyası (yalnızca geriye dönük uyumluluk için). | STRING |
| `model_görev_id` | Model üretim sürecini izlemek için görev kimliği. | MODEL_TASK_ID |
| `GLB` | GLB biçiminde oluşturulan 3B model. `quad` etkinleştirildiğinde boştur. | FILE3DGLB |
| `FBX` | FBX biçiminde oluşturulan 3B model. Yalnızca `quad` etkinleştirildiğinde doldurulur. | FILE3DFBX |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/tr.md)

---
**Source fingerprint (SHA-256):** `79ebe76234036e8284640d7eaeee3a1220975b8adc043994de7de0ee161ccd45`
