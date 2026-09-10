# Salvar 3D (Avançado)

Save3DAdvanced salva um modelo 3D em um arquivo no diretório de saída do ComfyUI e cria uma prévia da cena salva. Ele também repassa o modelo 3D, seu posicionamento na cena, informações da câmera e dimensões da viewport para os nós a jusante. Quando não há conexão para o posicionamento do modelo ou para as informações da câmera, o nó usa os valores armazenados no estado da viewport.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo de modelo 3D de um nó 3D a montante. | FILE3D | Sim | GLB<br>GLTF<br>FBX<br>OBJ<br>STL<br>USDZ<br>Any |
| `filename_prefix` | Prefixo usado para o nome do arquivo salvo (padrão: "3d/ComfyUI"). | STRING | Sim | Texto livre |
| `viewport_state` | Estado da viewport contendo informações de câmera e posicionamento do modelo, normalmente de um nó Load 3D. | LOAD3D | Sim | - |
| `model_3d_info` | Posicionamento de cada modelo na cena: posição, rotação e escala (espaço de mundo com Y para cima). Substitui o posicionamento do modelo armazenado em `viewport_state` quando conectado. | LOAD3DMODELINFO | Não | - |
| `camera_info` | Informações da câmera da viewport: posição, alvo de mira, zoom e tipo. Substitui as informações da câmera armazenadas em `viewport_state` quando conectado. | LOAD3DCAMERA | Não | - |
| `width` | Largura de renderização da viewport em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |
| `height` | Altura de renderização da viewport em pixels (padrão: 1024). | INT | Sim | 1 a 4096 |

Nota: `model_3d_info` e `camera_info` são opcionais. Quando qualquer uma das entradas não estiver conectada, o nó recorre aos valores correspondentes armazenados em `viewport_state`.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `model_3d` | O arquivo de modelo 3D repassado a partir da entrada. | FILE3D |
| `model_3d_info` | Posicionamento de cada modelo na cena: posição, rotação e escala (espaço de mundo com Y para cima). | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera da viewport: posição, alvo de mira, zoom e tipo. | LOAD3DCAMERA |
| `width` | O valor de largura de renderização repassado a partir da entrada. | INT |
| `height` | O valor de altura de renderização repassado a partir da entrada. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `27cb15c5cf382e6e5b8164cfd456993404222c61d59edff2d51f9f1c8e47b25f`
