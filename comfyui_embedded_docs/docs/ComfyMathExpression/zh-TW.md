# 數學運算式

ComfyMathExpression 節點會評估您以文字編寫的數學公式。公式可以使用字母名稱，例如 `a`、`b`、`c`，來引用節點的輸入值，而且您可以透過可擴充的 `values` 群組，依需求新增任意數量的輸入值。計算結果會同時以浮點數、整數和布林值的形式回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `運算式` | 要評估的數學公式，以文字編寫（例如 `a + b`），使用輸入值的字母名稱作為變數。多行輸入。（預設值："a + b"） | STRING | 是 | N/A |
| `數值` | 可擴充的輸入值群組，為公式提供變數。群組中新增的每個值會自動依序取得下一個小寫字母名稱，從 `a` 開始（`a`、`b`、`c`……），然後該名稱便可在 `expression` 中使用。每個項目接受數字（INT 或 FLOAT）或布林值（TRUE/FALSE）。 | FLOAT, INT, BOOLEAN | 是 | 1 至 26 values, named `a` to `z` |

### 注意事項與限制

- `expression` 不能為空，也不能僅包含空白字元。
- 公式必須求值為數字結果（INT 或 FLOAT）。如果結果是其他型別（例如文字），節點會引發錯誤。
- 數字結果必須是有限數值，且可轉換為浮點數。太大或非有限的結果會導致錯誤。
- 所有輸入值也會以變數名稱 `values`（作為清單）提供給公式使用，因此可以編寫如 `sum(values)` 的運算式。
- 公式內可使用以下數學函數：`sum`、`min`、`max`、`abs`、`round`、`pow`、`sqrt`、`ceil`、`floor`、`log`、`log2`、`log10`、`sin`、`cos`、`tan`、`int`、`float`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `FLOAT` | 公式結果以浮點數形式輸出。 | FLOAT |
| `INT` | 公式結果轉換為整數，小數部分會被截斷。 | INT |
| `BOOL` | 結果轉換為布林值：當數值結果不為零時為 TRUE，為零時則為 FALSE。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
