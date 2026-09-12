# 建立影片

Create Video 節點會將一系列影像結合成影片。你可以設定播放速度（以每秒影格數為單位），可選擇加入音訊，並選擇輸出影片的壓縮格式、位元深度與色彩空間。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 要據以建立影片的影像。 | IMAGE | 是 | - |
| `每秒影格數` | 影片播放速度的每秒影格數（預設：30.0）。 | FLOAT | 是 | 1.0 - 120.0 |
| `音訊` | 要加入影片的音訊。 | AUDIO | 否 | - |
| `bit_depth` | Auto 會針對 sRGB 使用 8 位元、針對 HDR 與 HDR PQ 使用 10 位元。明確選擇 8 位元與 10 位元時，會與色彩空間無關。（預設："auto"） | COMBO | 否 | `"auto"`<br>8<br>10 |
| `color_space` | 輸入影像的色彩空間。HDR 會選用 BT.2020/HLG，HDR PQ 會選用 BT.2020/PQ。（預設："sRGB"） | COMBO | 否 | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `codec` | 可選擇立即編碼影片。None 會將影像保持為張量形式；Auto 會使用 H.264。（預設："none"） | COMBO | 否 | `"none"`<br>可從視訊編碼器清單取得的可用視訊編碼器選項（例如 `"auto"` 及其他支援的編碼器） |

注意：當 `bit_depth` 設為 `"auto"` 時，節點會自動針對 HDR 與 HDR PQ 色彩空間使用 10 位元，並針對 sRGB 使用 8 位元。

注意：`codec` 參數是進階選項。當其保留為 `"none"` 時，輸出會保持為張量形式；選擇任何其他編碼器都會立即編碼影片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 產生的影片，包含輸入影像與可選的音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9274559caabbafbcaad47883bf017967f9685f155ea1031e66cf22ee8d0d14c3`
