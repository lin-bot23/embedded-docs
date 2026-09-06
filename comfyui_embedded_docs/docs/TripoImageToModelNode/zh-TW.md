# Tripo：圖像轉模型

此節點使用 Tripo 的 API，依據單一影像同步生成 3D 模型。提供輸入影像後，節點會從中建立完整的 3D 模型，並可透過選用控制項調整模型版本、紋理生成、細節層級與輸出格式。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 用於生成 3D 模型的輸入影像。必須提供影像，否則節點會拋出錯誤。 | IMAGE | 是 | - |
| `model_version` | 用於生成的模型版本。 | COMBO | 否 | `"v1.4"`<br>`"v3.0"`<br>`"v3.5"`<br>`"v3.6"` |
| `style` | Tripo 已不再支援此參數，因此會予以忽略。保留此參數是為了相容較舊的工作流程。（預設值：`"None"`） | COMBO | 否 | `"None"`<br>`"realistic"`<br>`"cartoon"`<br>`"sculpture"`<br>`"low_poly"` |
| `texture` | 生成紋理貼圖。關閉時僅回傳未上紋理的幾何，並忽略 `pbr`。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `pbr` | PBR 材質貼圖（基礎色、金屬度、粗糙度、法線）。需要 `texture` 啟用。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `model_seed` | 用於模型生成的隨機種子。（預設值：42） | INT | 否 | 0 至 2147483647 |
| `orientation` | 生成模型的方位設定。（預設值：`"default"`） | COMBO | 否 | `"default"`<br>`"front"`<br>`"back"<br>`"left"`<br>`"right"`<br>`"top"`<br>`"bottom"` |
| `texture_seed` | 用於紋理生成的隨機種子。（預設值：42） | INT | 否 | 0 至 2147483647 |
| `texture_quality` | 紋理生成的品質等級：`detailed` 代表 HD 紋理，`extreme` 代表 8K Ultra 紋理。（預設值：`"standard"`） | COMBO | 否 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 紋理貼圖的對齊方式。（預設值：`"original_image"`） | COMBO | 否 | `"original_image"`<br>`"geometry"` |
| `face_limit` | 最大面數。設為 -1 時，由 Tripo 自適應決定（v3.x 標準模式約 140 萬個面，詳細模式約 200 萬個面）。Tripo 會自動限縮：v2.5 為 500,000，Quad 網格為 150,000。（預設值：-1） | INT | 否 | -1 至 2000000 |
| `quad` | Quad 網格輸出。Tripo 以 FBX 格式提供 quad 網格，因此結果會出現在 FBX 輸出，而 GLB 輸出保持空白。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `geometry_quality` | 幾何生成的品質等級。（預設值：`"standard"`） | COMBO | 否 | `"standard"`<br>`"detailed"` |
| `smart_low_poly` | 具有乾淨、手工風格拓撲的 Low-poly 網格（500 至 20,000 個面；quad 為 500 至 10,000）。最適合簡單的物體；複雜物體可能會失敗。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `auto_size` | 將含紋理的模型縮放至真實世界的公尺單位尺寸。Tripo 會將尺寸以場景變換形式儲存，並在模型進行轉換、綁定骨架或重新定向時將其烘焙進去；若未啟用紋理，此參數會被忽略。（預設值：True） | BOOLEAN | 否 | True<br>False |

注意：必須提供 `image`；若缺少影像，節點會拋出 RuntimeError。當 `texture` 為 False 時，模型只包含未上紋理的幾何，且 `pbr` 會被強制設為 False。當啟用 `smart_low_poly` 時，`face_limit` 必須介於 500 到 20,000 之間（三角形網格）；若同時啟用 `quad`，則必須介於 500 到 10,000 之間。若設定的限制無效，節點會拋出 ValueError。將 `face_limit` 設為 -1（預設值）時，不會向 API 傳送明確的面數限制，讓 Tripo 自適應決定。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `model_file` | 生成的 3D 模型檔案（僅供回溯相容）。 | STRING |
| `model task_id` | 用於追蹤模型生成過程的任務 ID。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。當啟用 `quad` 時此輸出為空白。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。僅在啟用 `quad` 時才會填入內容。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `79ebe76234036e8284640d7eaeee3a1220975b8adc043994de7de0ee161ccd45`
