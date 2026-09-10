# Pixal3DMultiViewConditioning

## Genel Bakış

Pixal3D Çoklu Görüntüleme Koşullandırma düğümü, nesnenin ön, sol, arka ve sağ yanlarını 90 derecelik aralıklarla oluşturan sabit döngü aygıtıdır. Bu düğüm, nesnenin genişliğinin yaklaşık 1/1.1'ini kapsayan çerçeve içindeki çerçeve görünümleri oluşturmak için kullanılır ve her görüntüde aynı ölçekte kalır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision ile birlikte sunulan NAF ağırlıklarla birlikte gelen. | MODEL | Evet | N/A |
| `fov` | Görüntülerin çerçevede yer aldığı yatay FOV derecesi. | FLOAT | Evet | 1.0 - 170.0 |
| `front` | Nesnenin ön yüzünün kare görüntüsü, alfa ile veya siyah zemin üzerinde. | IMAGE | Evet | N/A |
| `left` | Nesnenin sol yüzünün kare görüntüsü, alfa ile veya siyah zemin üzerinde. | IMAGE | Seçimli | N/A |
| `back` | Nesnenin arka yüzünün kare görüntüsü, alfa ile veya siyah zemin üzerinde. | IMAGE | Seçimli | N/A |
| `right` | Nesnenin sağ yüzünün kare görüntüsü, alfa ile veya siyah zemin üzerinde. | IMAGE | Seçimli | N/A |

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `pozitif` | Pixal3D Çoklu Görüntüleme Koşullandırma düğümü için pozitif koşullandırma çıktısı. | CONDITIONING |
| `negatif` | Pixal3D Çoklu Görüntüleme Koşullandırma düğümü için negatif koşullandırma çıktısı. | CONDITIONING |

## Notlar

- `fov` parametresi, görüntülerin çerçevede yer aldığı yatay FOV derecesini kontrol eder. 20 derecelik bir değer, aygıt renderları ve çoğu çoklu görüntüleme oluşturucu için tipik bir değerdir.
- İlk bağlanan görüntü (ön, sol, arka, sağ sırası) ön olarak kabul edilir ve mesh bu görüntüye pozlandırılır.
- Ön görüntü sağlanmadığında, bir uyarı kaydedilir ve mesh ilk bağlanan görüntü olarak pozlandırılır.
- Bu düğüm, görüntülerin kare ve aygıt gibi çerçevelenmiş olduğunu varsayar. Nesnenin genişliğinin yaklaşık 1/1.1'ini kapsaması ve her görüntüde aynı ölçekte kalması gerekmektedir.
- Bu düğüm, pozitif ve negatif koşullandırma için iki Koşullandırma nesnesi çıktırır. Bu nesneler, Pixal3D modelleri veya Koşullandırma girdilerini kabul eden diğer düğümler için kullanılabilir.
```

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/tr.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
