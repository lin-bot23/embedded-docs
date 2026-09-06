# Visualizar 3D (Avançado)

Este nó exibe uma prévia do modelo 3D na interface sem salvar o arquivo no diretório de saída do ComfyUI. Ele salva o modelo em um arquivo temporário e passa os dados do modelo, informações do modelo, informações da câmera e dimensões da prévia para processamento adicional a seguir.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo do modelo 3D proveniente de um nó 3D upstream. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ ou qualquer formato 3D suportado |
| `model_3d_info` | Metadados de informações do modelo opcional. Opção avançada. | LOAD3DMODELINFO | Não | - |
| `viewport_state` | O estado atual da vista, contendo informações da câmera e do modelo. | LOAD3D | Sim | - |
| `camera_info` | Configuração da câmera opcional para a vista 3D. Opção avançada. | LOAD3DCAMERA | Não | - |
| `width` | Largura da prévia em pixels. Padrão: 1024. | INT | Sim | 1 a 4096 |
| `height` | Altura da prévia em pixels. Padrão: 1024. | INT | Sim | 1 a 4096 |

Nota: Quando `camera_info` ou `model_3d_info` não estão conectados, seus valores são tomados do `viewport_state` quando disponíveis. Se `viewport_state` não contiver informações de câmera, `camera_info` é None. Se `viewport_state` não tiver informações de modelo, `model_3d_info` padrão é uma lista vazia. Se `viewport_state` não for um dicionário, é tratado como vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | Arquivo do modelo 3D passado pelo entrada. | FILE3D |
| `model_3d_info` | Metadados de informações do modelo, seja do entrada ou do estado da vista. | LOAD3DMODELINFO |
| `camera_info` | Configuração da câmera, seja do entrada ou do estado da vista. | LOAD3DCAMERA |
| `width` | Largura da prévia em pixels. | INT |
| `height` | Altura da prévia em pixels. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46c14d6242cbcabd457e13ae193427bb4c1fed55e81e568d50719fff0f1a95a0`
