# Tripo: 骨架模型

此節點會取得現有的 Tripo 3D 模型，並為其建立帶有骨架（rig）的版本，也就是讓模型擁有骨架，以便進行動畫製作。您需提供要製作骨架的模型 task ID，選擇 rig 版本、骨架類型、骨骼命名風格與輸出檔案格式，節點會將工作送至 Tripo，等待完成後回傳下載的結果。

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `原始模型任務ID` | 要製作骨架的原始 3D 模型 task ID。這通常是先前的 Tripo 模型生成節點所產生的 ID。 | MODEL_TASK_ID | 是 | - |
| `model_version` | 要使用的 rig 模型版本。v1.0：僅支援人形（雙足）角色，內含 90 種以上的動畫預設。v2.5：非人形生物（四足、六足、八足、鳥類、蛇形、水生）。預設值：`v1.0-20240301`。 | COMBO | No | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | 骨架類型。"auto" 會先執行 Tripo 的免費 rig 檢查，並採用建議的類型。預設值："auto"。 | COMBO | No | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | 骨骼命名方式：Tripo 原生或相容於 Mixamo。Tripo 無法將其動畫預設重定向（retarget）到使用 mixamo 規格的 v1.0 rig 上；若要搭配 Tripo 使用，請採用 tripo：Retarget rigged model。預設值："tripo"。 | COMBO | No | "tripo"<br>"mixamo" |
| `out_format` | 輸出檔案格式；結果會出現在對應的輸出上。預設值："glb"。 | COMBO | No | "glb"<br>"fbx" |

**注意：** v1.0 模型版本（`v1.0-20240301`）僅支援雙足骨架。若此版本搭配非雙足的 `rig_type` 使用，節點會擲回錯誤，並提示您改用 `v2.5-20260210`。

**注意：** 當 `rig_type` 為 "auto" 時，Tripo 會先檢查該模型是否可製作骨架，並挑選建議的骨架類型。若 Tripo 回報該模型無法製作骨架，節點會以錯誤結束。

**注意：** 節點預期 Tripo 回傳 GLB 或 FBX 檔案。若 Tripo 回傳任何其他檔案類型，節點會擲回錯誤。

**注意：** 只有與 `out_format` 相符的輸出會被填入資料：當 `out_format` 為 "glb" 時填入 `GLB`，當 `out_format` 為 "fbx" 時填入 `FBX`。另一個 3D 輸出則為空。

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `模型檔案` | 所生成的帶骨架模型檔案名稱（task ID 加上格式副檔名）。僅為回溯相容性而保留。 | STRING |
| `綁定任務 ID` | 用於追蹤 rig 生成流程的 task ID。 | RIG_TASK_ID |
| `GLB` | 以 GLB 3D 檔案形式呈現的帶骨架模型。當 `out_format` 為 "glb" 時填入。 | FILE3DGLB |
| `FBX` | 以 FBX 3D 檔案形式呈現的帶骨架模型。當 `out_format` 為 "fbx" 時填入。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
