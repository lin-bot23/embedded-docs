# Tripo: Modeli Dönüştür

Bu düğüm, mevcut bir Tripo 3B modelini başka bir 3B dosya biçimine dönüştürür. Daha önce bir Tripo işlemiyle (model oluşturma, rigging, retargeting veya segmentasyon gibi) oluşturulmuş veya işlenmiş bir modelin görev kimliğini alır, Tripo API'sine bir dönüştürme görevi gönderir, bu görevin tamamlanmasını bekler ve ardından dönüştürülmüş model dosyasını döndürür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Gerekli | Aralık |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | Dönüştürülecek Tripo modelinin görev kimliği. Daha önceki bir Tripo model oluşturma, rigging, retargeting veya segmentasyon görevinden gelmelidir. Kimlik eksik veya boşsa düğüm bir hata verir. | STRING (Tripo task ID) | Evet | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `format` | Dönüştürülmüş 3B model için hedef dosya biçimi. | COMBO | Evet | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | Etkinleştirildiğinde üçgenleri dörtgenlere dönüştürür (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `face_limit` | Dönüştürülen modeldeki azami yüz sayısı. Sınırsız için -1 olarak ayarlayın (varsayılan: -1). | INT | Hayır | -1 ile 2000000 |
| `texture_size` | Çıktı dokularının piksel cinsinden çözünürlüğü (varsayılan: 4096). | INT | Hayır | 128 ile 8192 |
| `texture_format` | Dışa aktarılan dokular için kullanılan dosya biçimi (varsayılan: JPEG). | COMBO | Hayır | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | Etkinleştirildiğinde modeli simetrik olmaya zorlar (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `flatten_bottom` | Etkinleştirildiğinde modelin altını düzleştirir (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `flatten_bottom_threshold` | `flatten_bottom` ile kullanılan düzleştirme derinliği (varsayılan: 0.01). Bu değer yalnızca `flatten_bottom` etkin olduğunda uygulanır. | FLOAT | Hayır | 0.01 ile 1.0 |
| `pivot_to_center_bottom` | Etkinleştirildiğinde pivot noktasını modelin alt merkezine taşır (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `scale_factor` | Dönüştürülen modele uygulanan ölçek faktörü (varsayılan: 1.0). | FLOAT | Hayır | 0.01 and above |
| `with_animation` | Rigging veya retargeting yapılmış modellerin iskeletini ve animasyonunu korur (varsayılan: True). | BOOLEAN | Hayır | True or False |
| `pack_uv` | Etkinleştirildiğinde UV koordinatlarını yeniden paketler (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `bake` | Daha geniş uyumluluk için gelişmiş malzemeleri temel dokulara işler (varsayılan: True). | BOOLEAN | Hayır | True or False |
| `part_names` | Dönüştürmeye gönderilecek model parça adlarının virgülle ayrılmış listesi. Boş girdiler yok sayılır ve yinelenen adlar kaldırılır. Bu seçeneği atlamak için boş bırakın (varsayılan: boş). | STRING | Hayır | Virgülle ayrılmış parça adları listesi |
| `fbx_preset` | FBX uyumluluk ön ayarı. bake_scale, ölçek dönüşümünü geometriye işler (varsayılan: blender). | COMBO | Hayır | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | Etkinleştirildiğinde köşe renklerini dışa aktarır (varsayılan: False). | BOOLEAN | Hayır | True or False |
| `export_orientation` | Dışa aktarılan modelin ileri ekseni. default değeri Tripo'nun +x yönünü korur (varsayılan: default). | COMBO | Hayır | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | Etkinleştirildiğinde modeli olduğu yerde canlandırır (varsayılan: False). | BOOLEAN | Hayır | True or False |

**Not:** `original_model_task_id` ve `format` dışındaki tüm girdiler isteğe bağlı gelişmiş ayarlardır. Varsayılan değerlerinde bırakılan ayarlar, dönüştürme isteğinden çıkarılır; böylece Tripo API standart davranışını kullanır. `flatten_bottom_threshold` girdisi yalnızca `flatten_bottom` etkinleştirildiğinde anlamlıdır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `model_3d` | İstenen biçimde dönüştürülmüş model. OBJ, Tripo tarafından ZIP arşivi olarak teslim edilir (mesh, malzeme ve dokular). | FILE_3D |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/tr.md)

---
**Source fingerprint (SHA-256):** `5fd181d15025576083769e1ce31fb20cabb33096a01c67be50c3d9bb332739bf`
