# Pixal3DMultiViewConditioning

## 概述

Pixal3D 多視角條件設定節點是一個固定軌道裝置，以90度間隔生成物體的前視、左視、後視和右視。它用於為 Pixal3D 應用程序創建框選視角，其中物體在其最寬處佔據約 1/1.1 的畫面，並在每個視角中保持相同的比例。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 范圍 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision 配備內置的 NAF 重量。 | MODEL | 是 | N/A |
| `視野角` | 视角框選中的水平視野角（度）。 | FLOAT | 是 | 1.0 - 170.0 |
| `前方` | 物體前側的方形視圖，帶有 alpha 通道或黑色背景。 | IMAGE | 是 | N/A |
| `左側` | 物體左側的方形視圖，帶有 alpha 通道或黑色背景。 | IMAGE | 選擇性 | N/A |
| `後方` | 物體後側的方形視圖，帶有 alpha 通道或黑色背景。 | IMAGE | 選擇性 | N/A |
| `右側` | 物體右側的方形視圖，帶有 alpha 通道或黑色背景。 | IMAGE | 選擇性 | N/A |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | Pixal3D 多視角條件設定節點的正向條件輸出。 | CONDITIONING |
| `負向` | Pixal3D 多視角條件設定節點的負向條件輸出。 | CONDITIONING |

## 記錄

- `fov` 參數控制視角框選中的視野角。對於裝置渲染和大多數多視角生成器，20 度的值是典型的。
- 第一個連接的視角（前、左、後、右的順序）被視為前視，並將網格設定為此視角。
- 如果沒有提供前視，將記錄警告，並將網格設定為第一個連接的視角作為其前視。
- 節點假設視角是方形的，並像裝置一樣框選。物體在其最寬處應該佔據約 1/1.1 的畫面，並在每個視角中保持相同的比例。
- 節點輸出兩個 CONDITIONING 對象，一個用於正向條件，一個用於負向條件。這些可以用於條件化 Pixal3D 模型或其他接受 CONDITIONING 輸入的節點。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`
