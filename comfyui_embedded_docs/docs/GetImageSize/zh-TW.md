# 取得圖片尺寸

GetImageSize 讀取輸入影像，並傳回其寬度、高度與批次大小。此節點也會直接在節點介面上顯示這些量測值。

## 輸入
| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 用來擷取寬度、高度與批次大小的輸入影像 | IMAGE | 是 | - |

## 輸出
| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `width` | 輸入影像的寬度（像素） | INT |
| `height` | 輸入影像的高度（像素） | INT |
| `batch_size` | 輸入批次中所包含的影像數量 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dc29add37a3362384e63cb1e57f03758a82f77811c78797fdffd486462cb19b8`
