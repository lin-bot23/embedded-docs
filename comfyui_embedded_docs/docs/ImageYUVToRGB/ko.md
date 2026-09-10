# ImageYUVToRGB

ImageYUVToRGB 노드는 YUV 색상 공간 이미지를 RGB 색상 공간으로 변환합니다. Y(휘도), U(청색 투영), V(적색 투영) 구성 요소를 각각 나타내는 세 개의 개별 입력 이미지를 가져와 단일 RGB 이미지로 결합합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `Y` | Y(휘도) 구성 요소 입력 이미지 | IMAGE | 예 | - |
| `U` | U(청색 투영) 구성 요소 입력 이미지 | IMAGE | 예 | - |
| `V` | V(적색 투영) 구성 요소 입력 이미지 | IMAGE | 예 | - |

**참고:** 세 입력 이미지(Y, U, V)는 모두 함께 제공되어야 하며 올바른 변환을 위해 호환 가능한 크기를 가져야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 변환된 RGB 이미지 | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/ko.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
