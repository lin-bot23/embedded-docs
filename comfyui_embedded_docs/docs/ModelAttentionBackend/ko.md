# 모델 어텐션 백엔드

```markdown
# 모델어ention백엔드

## 개요

ModelAttentionBackend 노드는 모델에 사용할 다단계 주목력 구현을 선택할 수 있게 합니다. 이 노드는 선택한 주목력 백엔드로 모델을 패치하며, 사용 가능한 경우 PyTorch 주목력 또는 Comfy Kitchen 주목력을 사용할 수 있습니다. 이 노드는 희소 주목력이 비활성이거나 지원되지 않는 경우에 특히 유용하며, 모델이 지정된 다단계 주목력 기계로 작동하게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 선택한 주목력 백엔드로 패치될 모델. | MODEL | 예 |  |
| `attention` | 모델에 적용할 다단계 주목력 백엔드. 사용 가능한 옵션은 "pytorch attention"과 사용 가능한 경우 "comfy kitchen attention"입니다. | STRING | 예 | "pytorch attention"<br> "comfy kitchen attention" (when available) |

- "comfy kitchen attention" 옵션은 INT8 주목력을 사용하며, Nvidia와 AMD GPU에서만 지원됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model` | 선택한 주목력 백엔드가 적용된 입력 모델. | MODEL |

## 주의사항

- 선택한 주목력 백엔드가 사용 가능하지 않으면, 노드는 자동으로 PyTorch 주목력을 사용하며 경고 메시지를 로그에 기록합니다.
- ModelAttentionBackend 노드는 실험적이며, 향후 출시에서 변경될 수 있습니다.
```

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/ko.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
