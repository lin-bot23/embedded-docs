# LTXVFreezeLatent

## 개요

LTXV Freeze Latent 노드는 주어진 latent에 대해 noise_mask를 0으로 설정하여 샘플링 중에 latent이 깨끗하게 유지되도록 설계되었습니다. 오디오나 비디오 latent을 언뜨리는 것을 방지하기 위해 특히 유용하며, 이는 오디오와 비디오를 결합하여 � Cre-attention을 적용하거나 언뜨리지 않아야 할 모든 latent에 적용할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `latent` | 언뜨리기 위해 설정할 비디오나 오디오 latent. 오디오는 4D; 비디오는 5D입니다. | LATENT | 예 | N/A |
| `samples` | latent 샘플을 포함하는 텐서. | TENSOR | 예 | 오디오: 4D (batch, channels, frames, samples); 비디오: 5D (batch, channels, height, width, frames) |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `latent` | 샘플링 중에 noise_mask를 0으로 설정하여 깨끗하게 유지되도록 한 latent. | LATENT |

## 주의사항

- `samples` 텐서는 평면 텐서여야 하며, 결합된 오디오-비디오 latent이 아니어야 합니다. 결합된 latent이면 먼저 Separate AV Latent 노드를 사용하여 분리해야 합니다.
- 출력 `latent`은 zero noise_mask를 가지며, 지정된 latent에 대한 언뜨리기를 방지합니다.
- 노드는 오디오와 비디오 latent 모두를 지원하며, 각각 다른 텐서 형상을 가집니다.
- `samples` 텐서의 형상이 예상된 오디오나 비디오 형상과 일치하지 않으면 ValueError가 발생합니다.
- **Note:** 실제 구현은 여기에 명시되지 않은 추가 제약 사항이나 동작이 있을 수 있습니다. 가장 정확한 정보를 얻기 위해 항상 최신 소스 코드를 참조하세요.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/ko.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
