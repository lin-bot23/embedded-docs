# Tripo: Görüntüden Çoklu Görünüme

Tek bir giriş görüntüsünden Tripo API'sini kullanarak konunun ön, sol, arka ve sağ görünümlerini üretir. Görüntü yüklenir, bir çoklu görünüm oluşturma görevi başlatılır ve tamamlanana kadar yoklanır; elde edilen dört görünüm görev kimliğiyle birlikte döndürülür. Bu, yaklaşık 0,10 USD olarak faturalandırılan ücretli bir görevdir.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `image` | Tripo'nun ön, sol, arka ve sağ görünümleri ürettiği konunun kaynak görüntüsü. Bir toplu iş sağlansa bile istek için yalnızca bir görüntü kullanılır. | IMAGE | Evet | Single image |

Not: Düğüm, Tripo'nun bulut API'sini çağırır ve oluşturma görevinin tamamlanmasını bekler. Tipik bir görev yaklaşık 25 saniye sürer. Kimlik doğrulama, düğümün gizli girdileri aracılığıyla otomatik olarak gerçekleştirilir; bu nedenle iş akışında herhangi bir Tripo API anahtarı sağlanmasına gerek yoktur. Düğüm, Tripo yanıtındaki dört görünüm URL'sinin tümünü gerektirir (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); herhangi bir görünüm eksikse yürütme bir hatayla başarısız olur.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-----------|-----------|
| `multiview task_id` | Tripo tarafından çoklu görünüm görüntü oluşturma isteği için döndürülen görev tanımlayıcısı. Tamamlanan göreve başvurmak için kullanılabilir; örneğin görünümleri Tripo: Edit Multiview ile iyileştirirken. | MULTIVIEW_TASK_ID |
| `ön` | Konunun oluşturulan ön görünümü. | IMAGE |
| `sol` | Konunun oluşturulan sol yan görünümü. | IMAGE |
| `arka` | Konunun oluşturulan arka görünümü. | IMAGE |
| `sağ` | Konunun oluşturulan sağ yan görünümü. | IMAGE |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/tr.md)

---
**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`
