# Mesh'i Yeniden Oluştur (Dar Bant DC)

Remesh Mesh, orijinal yüzeyin çevresindeki dar bantlı bir mesafe alanını örnekleyip bu alandan yüzeyi Dual Contouring ile çıkararak bir mesh'i temiz ve düzgün bir mozaiklemeyle yeniden oluşturur. Bu, dağınık, manifold olmayan veya kendi kendini kesen topolojiyi normalleştirir; tam bir yüz sayısına ulaşmak için Decimate Mesh'ten önce çalıştırılması amaçlanır. İşlem, etkin hesaplama aygıtında çalışır ve çıktı mesh'i kaynaklı (welded) kalır.

## Girdiler

### Ortak Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Remesh uygulanacak girdi mesh'i. | MESH | Evet | — |
| `çözünürlük` | Voksel ızgara çözünürlüğü (çıktı yoğunluğu). 256 ~ 100 bin yüz, 512 ~ 1 milyon. Tam bir yüz sayısı için ardından Decimate Mesh kullanın. (varsayılan: 512) | INT | Evet | 32 - 2048 |
| `sign_mode` | Yüzey çıkarma modu. "udf", dağınık/manifold olmayan girdilere karşı dayanıklıdır; "sdf", QEF (İkinci Dereceden Hata Fonksiyonu) keskin özellik kurtarma ile temiz bir tek yüzey üretir, ancak tutarlı bir yüzey yönlendirmesi (winding) gerektirir. Bir mod seçildiğinde, o moda özel alt seçenekler görüntülenir. (varsayılan: "udf") | DYNAMIC_COMBO | Evet | "udf"<br>"sdf" |
| `band` | Voksel birimi cinsinden dar bant genişliği. UDF modunda yüzeyi de öteler. (gelişmiş, varsayılan: 1.0) | FLOAT | Evet | 0.5 - 4.0 |
| `project_back` | Köşeleri orijinal yüzeye doğru doğrusal olarak enterpole eder (0 = saf DC, 1 = orijinal yüzeye oturtulmuş). (gelişmiş, varsayılan: 0.0) | FLOAT | Evet | 0.0 - 1.0 |
| `fix_poles` | Valansı 3 olan köşe çiftlerini çökertir (DC T-kesişim artefaktı). (gelişmiş, varsayılan: false) | BOOLEAN | Evet | true / false |
| `smooth_iters` | Taubin yumuşatma yineleme sayısı (0 = kapalı). 2-3, DC merdiven benzeri artefaktları temizler; daha yüksek değerler QEF kenarlarını aşırı yumuşatır. (varsayılan: 0) | INT | Evet | 0 - 20 |
| `drop_small_components` | En büyük bileşenin yüz sayısının bu oranının altındaki bileşenleri atar. 0 devre dışı bırakır. (gelişmiş, varsayılan: 0.01) | FLOAT | Evet | 0.0 - 0.5 |
| `precluster_max_verts` | Alan sorgularından önce girdi köşe sayısını sınırlar; bu değerin üzerindeki girdiler önce bu hedef değere küme küçültme (cluster-decimate) uygulanarak düşürülür. Büyük mesh'lerde OOM'u (bellek yetersizliği) önler. (gelişmiş, varsayılan: 20,000,000) | INT | Evet | 0 - 100,000,000 |

### "udf" Modu Girdileri

Bu parametreler, `sign_mode` değeri `"udf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qef` | Daha keskin kenarlar için QEF (İkinci Dereceden Hata Fonksiyonu) tabanlı dual köşe yerleşimi. (varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_inverted_components` | İçe dönük normal (negatif hacimli) kapalı bileşenleri — UDF iç kabuğunu — atar. (varsayılan: false) | BOOLEAN | Hayır | true / false |
| `drop_enclosed_components` | En büyük bileşenin sınır kutusu (bbox) içinde kalan ve mesh-içinde-nokta ışın testini geçemeyen bileşenleri atar. Geçerli iç içe parçalar için devre dışı bırakın. (varsayılan: false) | BOOLEAN | Hayır | true / false |

### "sdf" Modu Girdileri

Bu parametreler, `sign_mode` değeri `"sdf"` olarak ayarlandığında görünür.

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `qef` | Kenar kesişim merkezine (centroid) kıyasla QEF (İkinci Dereceden Hata Fonksiyonu) ile dual köşe yerleşimi (keskin özellikleri kurtarır). (varsayılan: true) | BOOLEAN | Hayır | true / false |
| `manifold` | Manifold Dual Contouring: çok katmanlı durumlar için voksel başına 1-4 dual köşe. Daha yavaştır. (varsayılan: false) | BOOLEAN | Hayır | true / false |

Not: `qef` seçeneğinin varsayılan değeri seçilen moda göre farklıdır — "udf" modunda false, "sdf" modunda true. `precluster_max_verts` değeri 0'dan büyükse ve girdi mesh'i bu değerden daha fazla köşe içeriyorsa, alan sorgularından önce mesh, bu hedef değere küme küçültme (cluster-decimate) uygulanarak düşürülür. İşlemden sonra düğüm, girdiden çıktıya yüz sayısı değişimini üzerinde görüntüler (örneğin, "faces: 1.23M → 200K (-84%)").

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `ağ` | Düzgün mozaiklemeli ve kaynaklı topolojiye sahip, yeniden oluşturulmuş mesh. Girdide mevcut olduğunda köşe renkleri korunur; UV'ler, normaller ve teğetlerin hiçbiri aktarılmaz. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/tr.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
