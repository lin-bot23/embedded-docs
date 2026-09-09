# LTXVGeneratedKeyframesToGuides

```markdown
# LTXV 생성된 키 프레임을 가이드로 변환

## 개요

LTXV Generated Keyframes to Guides 노드는 이전 단계에서 생성된 키 프레임을 나중에 캔버스에 고정된 이미지 가이드로 변환합니다. 키 프레임을 독립된 프레임으로 디코딩한 후 필요에 따라 크기를 조정하고, 더 이상의 데노이즈를 방지하기 위해 0의 노이즈 마스크로 기록합니다. 기록된 인덱스는 생성된 캔버스에서 타겟 캔버스로 스케일링되며, 프레임 인덱스를 명시적으로 설정할 수 있습니다.

## 입력

| 매개변수                 | 설명                                                                 | 데이터 타입 | 필수 | 범위 |
|---------------------------|-----------------------------------------------------------------------------|-----------|----------|-------|
| `positive`                | 키 프레임이 이미지 가이드로 고정된 긍정 조건.                             | CONDITIONING | 예      |       |
| `negative`                | 키 프레임이 이미지 가이드로 고정된 부정 조건.                             | CONDITIONING | 예      |       |
| `vae`                     | 키 프레임을 디코딩하는 데 사용할 VAE 모델.                                 | MODEL      | 예      |       |
| `latent`                  | 가이드를 추가할 목표 비디오 렌탈, 예를 들어 시간적으로 업스케일된 것. | LATENT     | 예      |       |
| `keyframes`               | LTXV Separate Generated Keyframes의 키 프레임 출력, 각 키 프레임이 생성된 픽셀 프레임 인덱스를 포함합니다. | LATENT     | 예      |       |
| `strength`                | 가이드 강도. 1.0은 단단한 고정; 낮은 값은 고정을 완화합니다.                   | FLOAT      | 예      | 0.0 - 10.0 |
| `override_frame_indices` | 선택적 — 이 픽셀 프레임에 고정합니다. 기록된 (또는 자동 스케일링된) 위치 대신 제공하십시오. 각 키 프레임당 하나의 인덱스를 제공합니다. 비어 있으면 기록된 위치를 재사용하거나 타겟 캔버스가 다른 길이일 때 (예: 시간적으로 x2 후) 스케일링합니다. | STRING    | 아님       |       |

## 출력

| 출력 이름 | 설명                                                                 | 데이터 타입 |
|-------------|-----------------------------------------------------------------------------|-----------|
| `positive`  | 키 프레임이 이미지 가이드로 고정된 긍정 조건.                             | CONDITIONING |
| `negative`  | 키 프레임이 이미지 가이드로 고정된 부정 조건.                             | CONDITIONING |
| `latent`    | 키 프레임이 추가된 렌탈로 변환된 목표 비디오.                               | LATENT     |

## 주의사항

- `strength` 매개변수는 키 프레임이 가이드로 고정되는 강도를 제어합니다. 1.0은 단단한 고정을 만들고, 낮은 값은 고정을 완화합니다.
- `override_frame_indices` 매개변수는 키 프레임이 고정될 정확한 픽셀 프레임을 지정할 수 있습니다. 비어 있으면 기록된 위치를 사용하거나 필요에 따라 스케일링합니다.
- 노드는 `keyframes` 렌탈이 각 키 프레임의 픽셀 프레임 인덱스를 포함하는 것을 가정합니다. 이렇지 않으면 노드는 `ValueError`를 발생시킵니다.
- 노드는 배치 크기가 1인 것만 지원합니다. 각 가이드는 하나의 이미지에서 인코딩되므로 배치 요소 간에 차이가 있을 수 없습니다.
- 노드는 `latent` 입력의 `samples` 텐서가 5D 텐서가 아니거나 배치 크기가 1이 아니면 `ValueError`를 발생시킵니다.
- 노드는 `keyframes` 입력의 `samples` 텐서가 5D 텐서가 아니거나 배치 크기가 1이 아니면 `ValueError`를 발생시킵니다.
- 노드는 `keyframes` 입력의 `samples` 텐서의 `samples` 텐서의 크기가 조정된 후 `latent` 입력의 `samples` 텐서의 크기와 일치하지 않으면 `ValueError`를 발생시킵니다.
- 노드는 `strength` 매개변수가 0.0에서 10.0 범위를 벗어나면 `ValueError`를 발생시킵니다.
- 노드는 `override_frame_indices` 매개변수가 콤마로 구분된 정수 목록이 아니거나 인덱스 수가 키 프레임 수와 일치하지 않으면 `ValueError`를 발생시킵니다.
- 노드는 `override_frame_indices` 매개변수의 인덱스가 타겟 캔버스의 픽셀 프레임 수 범위를 벗어나면 `ValueError`를 발생시킵니다.
- 노드는 `override_frame_indices` 매개변수의 최대 인덱스가 타겟 캔버스의 픽셀 프레임 수를 초과하면 `ValueError`를 발생시킵니다.
```

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/ko.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
