# Tripo：轉換模型

此節點會將現有的 Tripo 3D 模型轉換為另一種 3D 檔案格式。它會取得先前由 Tripo 操作（例如模型生成、骨架綁定、動作重定向或分割）所建立或處理之模型的任務 ID，向 Tripo API 提交轉換任務，等待該任務完成，然後傳回轉換後的模型檔案。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `original_model_task_id` | 要轉換之 Tripo 模型的任務 ID。此 ID 必須來自先前的 Tripo 模型生成、骨架綁定、動作重定向或分割任務。若此 ID 遺失或為空，節點會拋出錯誤。 | STRING (Tripo task ID) | 是 | MODEL_TASK_ID<br>RIG_TASK_ID<br>RETARGET_TASK_ID<br>SEGMENT_TASK_ID |
| `format` | 轉換後 3D 模型的目標檔案格式。 | COMBO | 是 | GLTF<br>USDZ<br>FBX<br>OBJ<br>STL<br>3MF |
| `quad` | 啟用時，將三角形轉換為四邊形（預設值：False）。 | BOOLEAN | 否 | True or False |
| `face_limit` | 轉換後模型的面數上限。設為 -1 表示不限制（預設值：-1）。 | INT | 否 | -1 至 2000000 |
| `texture_size` | 輸出紋理的解析度（以像素為單位）（預設值：4096）。 | INT | 否 | 128 至 8192 |
| `texture_format` | 匯出紋理使用的檔案格式（預設值：JPEG）。 | COMBO | 否 | BMP<br>DPX<br>HDR<br>JPEG<br>OPEN_EXR<br>PNG<br>TARGA<br>TIFF<br>WEBP |
| `force_symmetry` | 啟用時，強制模型對稱（預設值：False）。 | BOOLEAN | 否 | True or False |
| `flatten_bottom` | 啟用時，將模型底部壓平（預設值：False）。 | BOOLEAN | 否 | True or False |
| `flatten_bottom_threshold` | 搭配 `flatten_bottom` 使用的壓平深度（預設值：0.01）。此值僅在啟用 `flatten_bottom` 時套用。 | FLOAT | 否 | 0.01 至 1.0 |
| `pivot_to_center_bottom` | 啟用時，將樞軸點移至模型的底部中心（預設值：False）。 | BOOLEAN | 否 | True or False |
| `scale_factor` | 套用至轉換後模型的縮放係數（預設值：1.0）。 | FLOAT | 否 | 0.01 and above |
| `with_animation` | 保留已骨架綁定或已進行動作重定向之模型的骨架與動畫（預設值：True）。 | BOOLEAN | 否 | True or False |
| `pack_uv` | 啟用時，重新打包 UV 座標（預設值：False）。 | BOOLEAN | 否 | True or False |
| `bake` | 將進階材質烘焙至基本紋理中，以獲得更大的相容性（預設值：True）。 | BOOLEAN | 否 | True or False |
| `part_names` | 要傳送至轉換作業的模型零件名稱清單，以逗號分隔。空項目會被忽略，重複名稱會被移除。保留空白以省略此選項（預設值：空）。 | STRING | 否 | 以逗號分隔的零件名稱清單 |
| `fbx_preset` | FBX 相容性預設。`bake_scale` 會將縮放變換烘焙至幾何中（預設值：blender）。 | COMBO | 否 | blender<br>mixamo<br>3dsmax<br>bake_scale |
| `export_vertex_colors` | 啟用時，匯出頂點色彩（預設值：False）。 | BOOLEAN | 否 | True or False |
| `export_orientation` | 匯出模型的前向軸。`default` 會保留 Tripo 的 +x（預設值：default）。 | COMBO | 否 | default<br>+x<br>-x<br>+y<br>-y |
| `animate_in_place` | 啟用時，讓模型在原地播放動畫（預設值：False）。 | BOOLEAN | 否 | True or False |

**注意：** 除了 `original_model_task_id` 與 `format` 之外，所有輸入皆為選用的進階設定。保留在預設值的設定會從轉換要求中省略，因此 Tripo API 會使用其標準行為。`flatten_bottom_threshold` 輸入只有在啟用 `flatten_bottom` 時才有意義。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `model_3d` | 以所要求格式轉換後的模型。OBJ 格式會由 Tripo 以 ZIP 壓縮檔形式提供（包含網格、材質與紋理）。 | FILE_3D |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoConversionNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5fd181d15025576083769e1ce31fb20cabb33096a01c67be50c3d9bb332739bf`
