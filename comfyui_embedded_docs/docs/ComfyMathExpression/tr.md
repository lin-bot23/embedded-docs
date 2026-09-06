# Matematiksel İfade

ComfyMathExpression düğümü, metin olarak yazdığınız matematiksel bir formülü değerlendirir. Formül, düğümün girdi değerlerine `a`, `b`, `c` gibi harf adlarıyla başvurabilir ve genişletilebilir `values` grubu aracılığıyla gerektiği kadar girdi değeri ekleyebilirsiniz. Hesaplama sonucu aynı anda bir kayan noktalı sayı, bir tam sayı ve bir boole değeri olarak döndürülür.

## Girdiler

| Parametre | Açıklama | Veri Türü | Zorunlu | Aralık |
|-----------|-------------|-----------|----------|-------|
| `ifade` | Değerlendirilecek matematiksel formül; metin olarak yazılır (örneğin `a + b`), girdi değerlerinin harf adlarını değişken olarak kullanır. Çok satırlı girdi. (varsayılan: "a + b") | STRING | Evet | N/A |
| `değerler` | İfade için değişkenleri sağlayan, genişletilebilir girdi değerleri grubu. Gruba eklenen her değer, `a`'dan başlayarak otomatik olarak sonraki küçük harf adını alır (`a`, `b`, `c`, ...) ve bu ad daha sonra `expression` içinde kullanılabilir. Her öğe bir sayı (INT veya FLOAT) veya bir boole (TRUE/FALSE) kabul eder. | FLOAT, INT, BOOLEAN | Evet | 1 ila 26 değer, `a` ile `z` arasında adlandırılır |

### Notlar ve kısıtlamalar

- `expression` boş olamaz veya yalnızca boşluk içeremez.
- İfade, sayısal bir sonuçla (INT veya FLOAT) sonuçlanmalıdır. Sonuç, metin gibi farklı bir türdeyse düğüm bir hata verir.
- Sayısal sonuç sonlu olmalı ve bir float değerine dönüştürülebilmelidir. Çok büyük veya sonlu olmayan sonuçlar hataya neden olur.
- Girdi değerlerinin tamamı, ifade içinde `values` değişken adı altında (bir liste olarak) da kullanılabilir; böylece `sum(values)` gibi ifadeler mümkündür.
- İfade içinde şu matematik işlevleri kullanılabilir: `sum`, `min`, `max`, `abs`, `round`, `pow`, `sqrt`, `ceil`, `floor`, `log`, `log2`, `log10`, `sin`, `cos`, `tan`, `int`, `float`.

## Çıktılar

| Çıktı Adı | Açıklama | Veri Türü |
|-------------|-------------|-----------|
| `FLOAT` | İfadenin kayan noktalı sayı olarak sonucu. | FLOAT |
| `INT` | İfadenin tam sayıya dönüştürülmüş sonucu; ondalık kısım atılır. | INT |
| `BOOL` | Boolean değerine dönüştürülmüş sonuç: sayısal sonuç sıfır olmadığında TRUE, sıfır olduğunda FALSE. | BOOLEAN |

> Bu belge yapay zeka tarafından oluşturulmuştur. Herhangi bir hata bulursanız veya iyileştirme önerileriniz varsa, katkıda bulunmaktan çekinmeyin! [GitHub'da Düzenle](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/tr.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
