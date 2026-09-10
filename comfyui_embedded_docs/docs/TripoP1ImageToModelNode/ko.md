# Tripo P1: 이미지에서 모델로

Tripo P1: Image to Model은 Tripo P1 API를 사용하여 단일 2D 이미지를 3D 모델로 변환합니다. 낮은 폴리곤의 게임용 메시 생성에 최적화되어 있으며, 지오메트리 전용 메시 또는 PBR 맵이 포함된 텍스처 모델 중에서 선택할 수 있습니다. 완성된 모델은 GLB 파일로 반환됩니다.

## 입력

### 공통 입력

이 매개변수들은 항상 사용할 수 있습니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `output_mode` | 결과 유형을 선택합니다. "Geometry only"는 텍스처가 없는 메시를 반환하고, "Textured"는 색상/PBR 맵을 추가하며 추가 텍스처 설정을 표시합니다. | DYNAMIC_COMBO | 예 | `"Geometry only"`<br>`"Textured"` |
| `image` | 3D 모델을 생성하는 데 사용되는 소스 2D 이미지입니다. 단일 이미지가 필요하며, 제공되지 않으면 노드에서 오류를 발생시킵니다. | IMAGE | 예 | - |
| `enable_image_autofix` | 더 나은 생성 품질을 위해 입력 이미지를 사전 처리합니다. (기본값: False) | BOOLEAN | 아니요 | True<br>False |
| `face_limit` | 목표 면 수로, 48-20000입니다. -1은 Tripo가 적응적으로 선택하도록 합니다. (기본값: -1) | INT | 아니요 | -1 to 20000 |
| `model_seed` | 결과를 재현할 수 있도록 지오메트리 생성에 사용되는 시드입니다. (기본값: 42) | INT | 아니요 | 0 to 2147483647 |
| `auto_size` | 출력을 실제 미터 단위에 가깝게 조정합니다. (기본값: False) | BOOLEAN | 아니요 | True<br>False |
| `export_uv` | 생성 중 UV 언랩을 수행합니다. 지오메트리 전용 실행을 더 빠르게 하려면 끄세요. (기본값: True) | BOOLEAN | 아니요 | True<br>False |
| `compress_geometry` | meshopt 지오메트리 압축(EXT_meshopt_compression)을 적용합니다. 파일은 더 작아지지만 ComfyUI의 3D 미리보기에서는 표시할 수 없으므로, 편집 전에 압축을 해제하세요. (기본값: False) | BOOLEAN | 아니요 | True<br>False |

### Geometry only 입력

추가 매개변수는 없습니다. 출력은 텍스처가 없는 메시입니다.

### Textured 입력

이 매개변수들은 `output_mode`가 "Textured"로 설정된 경우 나타납니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `pbr` | PBR 맵을 포함합니다. 켜면 기본 텍스처도 강제로 켜집니다. (기본값: True) | BOOLEAN | 예 | True<br>False |
| `texture_quality` | detailed = HD 텍스처, extreme = 8K Ultra 텍스처입니다. (기본값: "standard") | COMBO | 예 | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_alignment` | 소스 이미지에 대한 시각적 충실도를 우선시할지, 메시 지오메트리에 대한 정렬을 우선시할지 정합니다. (기본값: "original_image") | COMBO | 예 | `"original_image"`<br>`"geometry"` |
| `orientation` | 소스 이미지에 맞게 출력을 회전합니다. 텍스처가 있는 경우에만 적용됩니다. (기본값: "default") | COMBO | 예 | `"default"`<br>`"align_image"` |
| `texture_seed` | 텍스처 결과를 재현할 수 있도록 텍스처 생성에 사용되는 시드입니다. (기본값: 42) | INT | 예 | 0 to 2147483647 |

참고: `output_mode`가 "Geometry only"인 경우 해당 요청에서는 텍스처링이 비활성화됩니다. "Textured" 모드에서는 색상 텍스처가 항상 요청됩니다. `pbr`을 비활성화하면 PBR 맵은 제거되지만 기본 색상 텍스처는 유지되며, `pbr`을 활성화하면 기본 텍스처도 강제로 켜집니다. `texture_alignment`와 `orientation`은 "Textured" 모드에서만 사용할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model_file` | 생성된 모델 파일 이름(`<task_id>.glb`)을 포함하는 문자열입니다. 하위 호환성을 위해서만 유지됩니다. | STRING |
| `model task_id` | 완료된 생성 작업에 대해 Tripo API가 반환한 고유 작업 ID입니다. | MODEL_TASK_ID |
| `GLB` | GLB 형식으로 생성된 3D 모델입니다. | FILE3DGLB |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/ko.md)

---
**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`
