# 3D Kaydet (Gelişmiş)

Save3DAdvanced, bir 3D modeli ComfyUI çıktı dizinindeki bir dosyaya kaydeder ve kaydedilen sahnenin bir önizlemesini oluşturur. Ayrıca 3D modeli, modelin sahnedeki yerleşimini, kamera bilgilerini ve görünüm alanı boyutlarını sonraki düğümlere iletir. Model yerleşimi veya kamera bilgileri bağlanmadığında, düğüm görünüm alanı durumunda saklanan değerleri kullanır.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `3D model` | Önceki bir 3D düğümünden gelen 3D model dosyası. | FILE3D | Evet | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `dosya adı ön eki` | Kaydedilen dosya adı için kullanılan önek (varsayılan: "3d/ComfyUI"). | STRING | Evet | Free text |
| `görünüm durumu` | Kamera ve model yerleşim bilgilerini içeren görünüm alanı durumu; genellikle bir Load 3D düğümünden gelir. | LOAD3D | Evet | - |
| `3D model bilgisi` | Sahnedeki her modelin yerleşimi: konum, dönüş ve ölçek (Y-up dünya uzayı). Bağlandığında `viewport_state` içinde saklanan model yerleşimini geçersiz kılar. | LOAD3DMODELINFO | Hayır | - |
| `kamera bilgisi` | Görünüm alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. Bağlandığında `viewport_state` içinde saklanan kamera bilgilerini geçersiz kılar. | LOAD3DCAMERA | Hayır | - |
| `genişlik` | Görünüm alanının piksel cinsinden render genişliği (varsayılan: 1024). | INT | Evet | 1 to 4096 |
| `yükseklik` | Görünüm alanının piksel cinsinden render yüksekliği (varsayılan: 1024). | INT | Evet | 1 to 4096 |

Not: `model_3d_info` ve `camera_info` isteğe bağlıdır. Bu girdilerden herhangi biri bağlanmadığında, düğüm `viewport_state` içinde saklanan karşılık gelen değerleri kullanır.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `3D model` | Girdiden olduğu gibi iletilen 3D model dosyası. | FILE3D |
| `3D model bilgisi` | Sahnedeki her modelin yerleşimi: konum, dönüş ve ölçek (Y-up dünya uzayı). | LOAD3DMODELINFO |
| `kamera bilgisi` | Görünüm alanı kamera bilgileri: konum, bakış hedefi, yakınlaştırma ve tür. | LOAD3DCAMERA |
| `genişlik` | Girdiden olduğu gibi iletilen render genişliği değeri. | INT |
| `yükseklik` | Girdiden olduğu gibi iletilen render yüksekliği değeri. | INT |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/tr.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
