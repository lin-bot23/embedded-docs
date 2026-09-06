# Doku'yu Mesh'e Uygula

Bu düğüm, pişirilmiş doku görüntülerini bir ağın UV düzenine ekler; böylece SaveGLB düğümü tarafından ağ ile birlikte dışa aktarılabilirler. Pişirme için kullandığınız UV açılmış ağı, pişirilmiş görüntü haritalarıyla birlikte bağlayın. İsteğe bağlı metalik, pürüzlülük ve ortam tıkanıklığı haritaları tek bir ORM dokusunda paketlenir ve bir normal harita sağlanması, doğru gölgeleme için gereken düzgün normalleri ve teğetleri de saklar.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Pişirilmiş dokuların ekleneceği UV açılmış ağ. Pişirme sırasında kullanılan ağ ile aynı olmalıdır; ağda UV yoksa bir hata oluşturulur. | MESH | Evet | — |
| `base_color` | Pişirilmiş temel renk görüntüsü. Ağın dokusu olarak saklanır ve 0-1 aralığına sınırlanır. | IMAGE | Evet | — |
| `metallic` | Pişirilmiş metalik haritası. Birleşik ORM dokusunun mavi kanalı olarak kullanılır; sağlanmadığında varsayılan değeri 0'dır. | IMAGE | Hayır | — |
| `roughness` | Pişirilmiş pürüzlülük haritası. Birleşik ORM dokusunun yeşil kanalı olarak kullanılır; sağlanmadığında varsayılan değeri 1'dir. | IMAGE | Hayır | — |
| `occlusion` | Pişirilmiş ortam tıkanıklığı haritası. Birleşik ORM dokusunun kırmızı kanalı olarak kullanılır; sağlanmadığında varsayılan değeri 1'dir. Sağlandığında, ORM dokusu SaveGLB için ortam tıkanıklığı dokusu olarak da işaretlenir. | IMAGE | Hayır | — |
| `normal_map` | Pişirilmiş teğet uzayı normal haritası. Sağlandığında, düğüm tepe noktası başına teğet tabanını yeniden hesaplar ve normal haritanın doğru gölgelenmesi için düzgün tepe normalleri dışa aktarır. | IMAGE | Hayır | — |

Not: `metallic`, `roughness` veya `occlusion` öğelerinden herhangi biri bağlandığında, üçü de kanalları R = occlusion, G = roughness, B = metallic olan tek bir glTF ORM dokusunda paketlenir. Eksik haritalar varsayılan değerlerle doldurulur (occlusion 1, roughness 1, metallic 0) ve farklı çözünürlükteki haritalar en büyük genişlik ve yüksekliğe göre yeniden boyutlandırılır. `normal_map` bağlandığında, ağın normalleri hesaplanan düzgün tepe normalleriyle değiştirilir ve bir teğet tabanı eklenir. [0,1] aralığı dışında kalan UV koordinatları, en-boy oranı korunarak [0,1] aralığına ölçeklenir.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `mesh` | Doku görüntüleri UV düzenine eklenmiş, SaveGLB ile kaydedilmeye hazır giriş ağı. | MESH |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/tr.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
