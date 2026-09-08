# Tripo: 骨架模型

此節點接收現有的 Tripo 3D 模型，並建立其綁定版本，也就是為模型加入骨架，使其可以進行動畫。您需要提供要綁定之模型的任務 ID、選擇綁定版本、骨架類型、骨骼命名樣式與輸出檔案格式，節點會將作業傳送給 Tripo，等待其完成後，再回傳下載好的結果。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `原始模型任務ID` | 要綁定的原始 3D 模型的任務 ID。這通常是先前由 Tripo 模型生成節點所產生的 ID。 | MODEL_TASK_ID | 是 | - |
| `model_version` | 要使用的綁定模型版本。v1.0：僅限人形（雙足，即 biped）角色，提供超過 90 種動畫預設。v2.5：非人形生物（quadruped、hexapod、octopod、avian、serpentine、aquatic）。預設值：`v1.0-20240301`。 | COMBO | 否 | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | 骨架類型。"auto" 會先執行 Tripo 的免費綁定檢查，並使用建議的類型。其他值則強制指定特定骨架類型，例如人形角色可使用 biped。預設值："auto"。 | COMBO | 否 | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | 骨骼命名規則：Tripo 原生或與 Mixamo 相容。Tripo 無法將其動畫預設重定位到使用 mixamo 規範建立的 v1.0 綁定模型；若要搭配「Tripo: Retarget rigged model」，請使用 tripo。預設值："tripo"。 | COMBO | 否 | "tripo"<br>"mixamo" |
| `out_format` | 輸出檔案格式；結果會送至對應的輸出端。預設值："glb"。 | COMBO | 否 | "glb"<br>"fbx" |

**注意：** v1.0 模型版本（`v1.0-20240301`）僅支援雙足骨架（biped）。如果在這個版本上使用非 biped 的 `rig_type`，節點會產生錯誤，並提示您改用 `v2.5-20260210`。

**注意：** 當 `rig_type` 為 "auto" 時，Tripo 會先檢查模型是否能綁定，並選擇建議的骨架類型。如果 Tripo 回報模型無法綁定，節點會失敗並拋出錯誤。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `模型檔案` | 產生的綁定 3D 模型檔案。僅為回溯相容而保留。 | STRING |
| `綁定任務 ID` | 用於追蹤綁定生成流程的任務 ID。 | RIG_TASK_ID |
| `GLB` | 以 GLB 3D 檔案格式呈現的綁定模型。當 `out_format` 為 "glb" 時，此輸出會有值。 | FILE3DGLB |
| `FBX` | 以 FBX 3D 檔案格式呈現的綁定模型。當 `out_format` 為 "fbx" 時，此輸出會有值。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `54c3b0984835160b74884d2c30191ad6dac6ea447862e9276253ace7367bc419`
