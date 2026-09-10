# Tripo: 모델 분할

이 노드는 3D 모델을 개별 파트로 분할합니다. 모델을 Tripo 세그멘테이션 서비스로 전송하고 작업이 완료될 때까지 기다린 뒤, 분할된 모델을 GLB 형식으로 반환하며 쉼표로 구분된 파트 이름 목록도 함께 반환합니다. 이 파트 이름들은 Tripo: Complete Mesh Parts, Tripo: Retopology, Tripo: Convert model과 같은 후속 단계에 사용됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 파트로 분할할 3D 모델의 작업 ID입니다. | MODEL_TASK_ID | 예 | N/A |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model_file` | 분할된 GLB 모델의 출력 파일 이름이며 `<task_id>.glb` 형식입니다. 하위 호환성을 위해서만 유지됩니다. | STRING |
| `segment task_id` | 결과를 생성한 분할 작업의 작업 ID입니다. | SEGMENT_TASK_ID |
| `GLB` | 분할된 3D 모델이며 GLB 파일입니다. | GLB |
| `part_names` | 쉼표로 구분된 파트 이름입니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/ko.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
