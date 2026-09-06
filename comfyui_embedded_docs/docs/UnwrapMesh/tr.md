# Mesh UV'lerini Aç

3B bir ağ için UV atlası oluşturur. Ağ yüzeyi parçalara ayrılır, her parça iki boyuta düzleştirilir ve düzleştirilmiş parçalar [0,1] UV atlasına paketlenir. Parça dikişlerindeki köşeler çoğaltılır, bu nedenle çıktı ağı, girdi ağından daha fazla köşe içerebilir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | UV açılımı yapılacak girdi ağı. Tek bir ağı veya bir grup ağı kabul eder. | MESH | Evet | — |
| `segmenter` | Kullanılacak parçalama algoritması. `pec`: GPU'da hızlı paralel-kenar-çökertme parçalama. `adaptive`: CPU, daha yavaş. (varsayılan: "pec") | COMBO | Evet | "pec"<br>"adaptive" |
| `resolution` | Texel yoğunluğu otomatik ölçekleme için hedef atlas çözünürlüğü (0 = içeriğe sığdır). (varsayılan: 1024) | INT | Evet | 0 ile 8192 (adım 256) |
| `padding` | Parçalar arası texel dolgusu. (varsayılan: 1) | INT | Evet | 0 ile 16 |
| `weld_distance` | Çakışık köşe birleştirme yarıçapı, ağ kapsamının bir kesri olarak (0 = otomatik). Üçgen başına parçalar elde ediyorsanız (kaynaşmamış girdi) yaklaşık 0.001'e yükseltin. (varsayılan: 0.0) | FLOAT | Evet | 0.0 ile 1.0 (adım 0.0001) |

Not: girdi ağı kaynaşmamış köşeler içeriyorsa, düğüm yüz bitişikliğinin düşük olduğunu belirten bir uyarı verebilir ve yüz başına UV parçaları üretebilir; `weld_distance` değerini artırmak, UV açılımından önce çakışık köşeleri birleştirir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Girdi ağı, [0,1] aralığında oluşturulmuş UV atlası ile birlikte. Dikiş köşeleri çoğaltılır, bu nedenle çıktı köşe sayısı girdiyi aşabilir. Girdi ağındaki köşe renkleri ve dokular korunur. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/tr.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
