# Tripo：文字轉模型

使用 Tripo 的 API 從文字描述生成完整的 3D 模型。此節點會等待生成完成，然後傳回模型檔案，並可選擇包含紋理與 PBR 材質。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 欲生成 3D 模型的文字描述（多行）。此參數為必填，且不能為空。 | STRING | 是 | - |
| `negative_prompt` | 要在生成的模型中避免出現之內容的文字描述（多行）。最多 255 個字元。僅在非空時才會傳送至 API。 | STRING | 否 | 最多 255 個字元 |
| `model_version` | 用於生成的 Tripo 模型版本（預設值：v3.1-20260211）。 | COMBO | 否 | 有多個選項可供選擇 |
| `style` | 套用到生成模型的樣式（預設值：None）。Tripo 已不再支援且會忽略此參數；僅為舊版工作流程保留。 | COMBO | 否 | 有多個選項可供選擇 |
| `texture` | 是否生成紋理貼圖。關閉時只會回傳不帶紋理的幾何模型，並忽略 `pbr`（預設值：True）。 | BOOLEAN | 否 | true / false |
| `pbr` | 是否生成 PBR 材質貼圖（基底色彩、金屬度、粗糙度、法線）。需要 `texture`；當 `texture` 關閉時會強制關閉（預設值：True）。 | BOOLEAN | 否 | true / false |
| `image_seed` | 用於影像生成階段的種子（預設值：42）。 | INT | 否 | 0 至 2147483647 |
| `model_seed` | 用於模型生成階段的種子（預設值：42）。 | INT | 否 | 0 至 2147483647 |
| `texture_seed` | 用於紋理生成階段的種子（預設值：42）。 | INT | 否 | 0 至 2147483647 |
| `texture_quality` | 生成紋理的品質。detailed = HD 紋理，extreme = 8K Ultra 紋理（預設值：standard）。 | COMBO | 否 | "standard"<br>"detailed"<br>"extreme" |
| `face_limit` | 最大面數。設為 -1 時由 Tripo 自適應選擇（在 v3.x 標準模式下約 1.4M 面，detailed 模式下約 2M 面）。Tripo 會靜默限制上限：v2.5 為 500,000，四邊形網格為 150,000。（預設值：-1） | INT | 否 | -1 至 2000000 |
| `quad` | 四邊形網格輸出。Tripo 以 FBX 格式提供四邊形網格，因此結果會出現在 FBX 輸出，而 GLB 輸出保持為空。（預設值：False） | BOOLEAN | 否 | true / false |
| `geometry_quality` | 生成幾何的品質（預設值：standard）。 | COMBO | 否 | "standard"<br>"detailed" |
| `smart_low_poly` | 具有乾淨、手工風格拓撲的低多邊形網格（500–20,000 個面，quad 模式為 500–10,000）。最適合簡單的主題；複雜的主題可能失敗。（預設值：False） | BOOLEAN | 否 | true / false |
| `auto_size` | 將帶有紋理的模型縮放到以公尺為單位的真實世界尺寸。Tripo 會將尺寸儲存為模型的場景轉換，並在模型轉換、綁定骨架或重新定向目標時將其烘焙進去；若無紋理則忽略此參數。（預設值：True） | BOOLEAN | 否 | true / false |

**附註：**
- `prompt` 參數為必填：若 `prompt` 為空，節點會引發錯誤。
- `pbr` 依賴 `texture`。當 `texture` 關閉時，節點會強制將 `pbr` 設為 off，並忽略其值。沒有 `texture` 時，`auto_size` 也無法生效。
- 啟用 `smart_low_poly` 且 `face_limit` 設為 -1 以外的值時，面數限制必須介於 500 到 20,000（三角輸出）之間；若啟用 `quad`，則必須介於 500 到 10,000 之間；否則節點會引發錯誤。
- 啟用 `quad` 時，生成的四邊形網格會以 FBX 格式提供，因此 FBX 輸出將有內容，而 GLB 輸出保持為空。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model_file` | 生成的 3D 模型檔案，僅為向下相容而保留。 | STRING |
| `model task_id` | 模型生成程序的唯一任務識別碼。 | MODEL_TASK_ID |
| `GLB` | 以 GLB 格式生成的 3D 模型。啟用 `quad` 時為空。 | FILE3DGLB |
| `FBX` | 以 FBX 格式生成的 3D 模型。僅在啟用 `quad` 時才會有內容。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3f4bc09d125fedb6c30968f31804cfc7ec6d2f068a7c28d90b006137803020b0`
