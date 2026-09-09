# LTXVSeparateGeneratedKeyframes

```markdown
# LTXV 분리된 생성된 키프레임

## 개요

LTXV Separate Generated Keyframes 노드는 샘플된 latent과 조건부에서 생성된 키프레임을 제거하여, 공간적으로 업스케일링 전에 별도로 처리할 수 있도록 합니다. 공간 업스케일링 전에 사용되어야 하며, LTXV Crop Guides 이후에 실행되지 않도록 해야 합니다. 이 노드는 생성된 키프레임을 버리는 가이드로 처리하여 제거합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 생성된 키프레임 메타데이터가 제거된 긍정적인 조건부. | CONDITIONING | 예 | N/A |
| `negative` | 생성된 키프레임 메타데이터가 제거된 부정적인 조건부. | CONDITIONING | 예 | N/A |
| `latent` | 생성된 키프레임이 제거된 비디오 latent. | LATENT | 예 | N/A |
| `keyframes_to_batch` | 키프레임을 단일 프레임 latent의 배치로 반환합니다. 기본적으로 False로 설정되어 있으며, 여러 프레임의 latent으로 반환됩니다. | BOOLEAN | 아니요 | 기본값: False |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | 생성된 키프레임 메타데이터가 제거된 긍정적인 조건부. | CONDITIONING |
| `negative` | 생성된 키프레임 메타데이터가 제거된 부정적인 조건부. | CONDITIONING |
| `latent` | 생성된 키프레임이 제거된 비디오 latent. | LATENT |
| `keyframes` | 제거된 키프레임, `generated_keyframe_indices`와 `generated_keyframe_num_frames`로 레이블링됩니다. 이를 나중에 Add Generated Keyframes에 입력하여 새로운 슬롯을 초기화하거나, Generated Keyframes To Guides에 입력하여 고정된 이미지 가이드로 사용할 수 있습니다 (캔버스 길이가 변경되면 인덱스가 다시 매핑됩니다). | LATENT |

## 주의사항

- `keyframes_to_batch` 매개변수는 키프레임이 단일 프레임 latent의 배치로 반환되는지 여부를 결정합니다.
- 이 노드는 조건부와 latent에서 생성된 키프레임을 제거하기 전에 모든 추가적인 처리를 보장합니다.
- `keyframes` 출력은 생성된 키프레임의 새로운 슬롯을 초기화하거나, 고정된 이미지 가이드로 사용할 수 있습니다.
- latent이 생성된 키프레임을 포함하지 않거나, 키프레임이 예상된 형식과 일치하지 않으면 노드는 `ValueError`를 발생시킵니다.
- 노드는 LTXV Add Generated Keyframes 노드를 사용하여 추가된 생성된 키프레임이며, 현재 latent과 호환되는 것을 가정합니다.
```

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/ko.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
