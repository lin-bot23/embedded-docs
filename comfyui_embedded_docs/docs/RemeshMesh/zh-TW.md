# 重新網格化網格（窄帶 DC）

Remesh Mesh 透過在原始表面周圍取樣窄帶距離場，並以 Dual Contouring 提取表面，重建出具有乾淨且均勻細分的網格。這可將混亂、非流形或自相交的拓撲正規化，並設計為在 Decimate Mesh 之前執行，以達到精確的面數。處理會在目前作用的計算裝置上執行，且輸出網格會維持焊接（welded）狀態。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要重新建構的輸入網格。 | MESH | 是 | — |
| `resolution` | 體素網格解析度（輸出密度）。256 ~ 100k 個面，512 ~ 1M 個面。若要達到精確的面數，請接著使用 Decimate Mesh。（預設值：512） | INT | 是 | 32 - 2048 |
| `sign_mode` | 表面提取模式。「udf」對混亂或非流形輸入具有穩健性；「sdf」則會產生乾淨的單一表面，具備 QEF（Quadratic Error Function，二次誤差函數）的銳利特徵還原能力，但需要一致的環繞方向。選取模式後會顯示其特定子選項。（預設值："udf"） | DYNAMIC_COMBO | 是 | "udf"<br>"sdf" |
| `band` | 窄帶寬度（以體素為單位）。在 UDF 模式下也會偏移表面。（進階，預設值：1.0） | FLOAT | 是 | 0.5 - 4.0 |
| `project_back` | 將頂點朝原始表面進行線性內插（0 = 純 DC，1 = 吸附至原始表面）。（進階，預設值：0.0） | FLOAT | 是 | 0.0 - 1.0 |
| `fix_poles` | 塌陷價數為 3 的頂點對（DC 的 T 型接點瑕疵）。（進階，預設值：false） | BOOLEAN | 是 | true / false |
| `smooth_iters` | Taubin 平滑迭代次數（0 = 關閉）。2-3 次可清除 DC 階梯狀的偽影；更高的次數會過度平滑 QEF 邊緣。（預設值：0） | INT | 是 | 0 - 20 |
| `drop_small_components` | 捨棄面數低於最大元件面數之指定比例的元件。0 表示停用。（進階，預設值：0.01） | FLOAT | 是 | 0.0 - 0.5 |
| `precluster_max_verts` | 在距離場查詢前限制輸入頂點數；若輸入頂點數超過此值，會先以叢集減面（cluster decimation）方式降至該值。避免大型網格造成 OOM。（進階，預設值：20,000,000） | INT | 是 | 0 - 100,000,000 |

### "udf" 模式輸入

當 `sign_mode` 設為 `"udf"` 時，會顯示這些參數。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `qef` | QEF（Quadratic Error Function，二次誤差函數）對偶頂點放置方式，用於產生較銳利的邊緣。（預設值：false） | BOOLEAN | 否 | true / false |
| `drop_inverted_components` | 捨棄法線朝內（負體積）的封閉元件，即 UDF 的內殼。（預設值：false） | BOOLEAN | 否 | true / false |
| `drop_enclosed_components` | 捨棄位於最大元件包圍盒（bbox）內、未通過 point-in-mesh 射線投射測試的元件。若是合法的巢狀零件，請停用此選項。（預設值：false） | BOOLEAN | 否 | true / false |

### "sdf" 模式輸入

當 `sign_mode` 設為 `"sdf"` 時，會顯示這些參數。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `qef` | 啟用時使用 QEF 的對偶頂點放置，可還原銳利特徵；停用時則使用 edge-crossing centroid（跨邊重心）。（預設值：true） | BOOLEAN | 否 | true / false |
| `manifold` | 流形 Dual Contouring：在多層片（multi-sheet）情況下，每個體素使用 1-4 個對偶頂點。速度較慢。（預設值：false） | BOOLEAN | 否 | true / false |

注意：`qef` 選項的預設值會依所選模式而不同——在 "udf" 模式為 false，在 "sdf" 模式為 true。當 `precluster_max_verts` 大於 0，且輸入網格的頂點數多於此值時，網格會在距離場查詢前先以叢集減面方式降至該目標值。處理完成後，節點上會顯示輸入到輸出的面數變化（例如："faces: 1.23M → 200K (-84%)"）。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `mesh` | 重新建構後的網格，具有均勻的細分與焊接拓撲。輸入若帶有頂點顏色則會保留；UV、法線與切線則不會沿用。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
