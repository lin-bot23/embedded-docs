# LTXVAddLatentGuide

```markdown
# LTXV 추가 잠재 지침

## 개요

LTXV Add Latent Guide 노드는 이미编码된 잠재 변수를 지침으로 고정하여, 이전 단계에서 나오는 지침을 사용할 수 있게 합니다. 이 노드는 VAE 디코딩/인코딩 라운드 트립을 피하고, 공간적으로 작은 지침을 희소 그리드에 확장하여 타겟 캔버스를 덮을 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 긍정적인 조건 입력. | CONDITIONING | 예 | N/A |
| `negative` | 부정적인 조건 입력. | CONDITIONING | 예 | N/A |
| `vae` | 사용할 VAE 모델. | MODEL | 예 | N/A |
| `latent` | 지침이 고정된 타겟 비디오 잠재 변수. | LATENT | 예 | N/A |
| `guiding_latent` | 지침 잠재 변수. 그 공간 크기는 타겟의 크기를 양쪽 축에서 같은 전체 수로 나누어야 합니다; 동일한 크기는 그대로 고정되고, 반 크기는 x2 IC-LoRA 참조로 처리됩니다. | LATENT | 예 | N/A |
| `latent_idx` | 지침을 시작할 잠재 프레임 인덱스, 잠재 프레임으로부터 계산됩니다. 픽셀 프레임보다 잠재 프레임을 기준으로 합니다. 음수 값은 잠재의 시작 이전의 프레임에 지침을 배치합니다. | INT | 예 | -9999 ~ 9999 |
| `strength` | 1.0으로 제한됩니다. 확장된 지침은 패딩 위치를 음수 데노이즈 마스크로 표시하여 모델이 그들을 제거합니다; 1.0 이상의 값은 유지된 위치가 음수가 되어 전체 지침이 제거됩니다. 1.0 이상의 값은 대신 attention_mask를 사용하여 증폭하세요. | FLOAT | 예 | 0.0 ~ 1.0, 단계 0.01 |
| `attention_mask` | 선택 사항입니다. 픽셀 공간 마스크입니다. 강도와 함께 지침의 영향을 지역별로 제어합니다. | MASK | 아님 | N/A |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | 긍정적인 조건 출력. | CONDITIONING |
| `negative` | 부정적인 조건 출력. | CONDITIONING |
| `latent` | 지침이 적용된 잠재 출력. | LATENT |

## 주의사항

- `guiding_latent`의 공간 크기는 `latent` 크기를 양쪽 축에서 같은 전체 수로 나누어야 합니다.
- `latent_idx` 매개변수는 지침이 잠재 프레임 내에서 정확하게 배치되도록 합니다.
- `strength` 매개변수는 지침의 강도를 제어하며, 1.0 이상의 값은 `attention_mask`를 사용하여 음수 위치를 피해야 합니다.
- `attention_mask` 매개변수는 선택 사항이지만, 이미지의 특정 지역에서 지침의 영향을 미세 조정할 수 있습니다.
```

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/ko.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
