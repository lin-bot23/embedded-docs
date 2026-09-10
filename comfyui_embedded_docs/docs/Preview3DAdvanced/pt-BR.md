# Visualizar 3D (Avançado)

Este nó exibe uma pré-visualização de modelo 3D na interface do usuário sem salvar o arquivo no diretório de saída do ComfyUI. Ele salva o modelo em um arquivo temporário e repassa os dados do modelo, as informações do modelo, as informações da câmera e as dimensões da pré-visualização para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo_3d` | Arquivo de modelo 3D de um nó 3D de origem. | FILE3D | Sim | GLB, GLTF, FBX, OBJ, STL, USDZ ou qualquer formato 3D compatível |
| `info_modelo_3d` | Posicionamento de cada modelo na cena: posição, rotação e escala (espaço de mundo com Y para cima). Opcional. Opção avançada. | LOAD3DMODELINFO | Não | - |
| `estado_da_janela_de_visualização` | O estado atual da viewport contendo informações de câmera e modelo. | LOAD3D | Sim | - |
| `info_câmera` | Informações da câmera da viewport: posição, alvo de visualização, zoom e tipo. Opcional. Opção avançada. | LOAD3DCAMERA | Não | - |
| `largura` | Largura de renderização da viewport em pixels. Padrão: 1024. | INT | Sim | 1 a 4096 |
| `altura` | Altura de renderização da viewport em pixels. Padrão: 1024. | INT | Sim | 1 a 4096 |

Observação: Quando `camera_info` ou `model_3d_info` não estão conectados, seus valores são obtidos de `viewport_state` quando disponíveis. Se `viewport_state` não contiver informações de câmera, `camera_info` será None. Se `viewport_state` não tiver informações de modelo, `model_3d_info` será uma lista vazia por padrão. Se `viewport_state` não for um dicionário, ele será tratado como vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `arquivo_modelo` | Arquivo de modelo 3D (glb/obj/stl/etc.) de um nó 3D de origem, repassado sem alterações. | FILE3D |
| `info_câmera` | Posicionamento de cada modelo na cena: posição, rotação e escala (espaço de mundo com Y para cima). Usa o valor de entrada ou recorre ao valor armazenado em `viewport_state`. | LOAD3DMODELINFO |
| `info_modelo_3d` | Informações da câmera da viewport: posição, alvo de visualização, zoom e tipo. Usa o valor de entrada ou recorre ao valor armazenado em `viewport_state`. | LOAD3DCAMERA |
| `largura` | Largura de renderização da viewport em pixels. | INT |
| `altura` | Altura de renderização da viewport em pixels. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f2d3d35ed35fe68edebcde8fd8421d26850b04e3ae5b7147f1020c8ed904c480`
