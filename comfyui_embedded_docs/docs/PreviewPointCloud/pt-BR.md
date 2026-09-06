# Pré-visualizar Nuvem de Pontos

### Visão Geral

O nó Ponto de Visão de Nuvem de Pontos permite visualizar um arquivo de nuvem de pontos 3D na interface ComfyUI sem salvá-lo no diretório de saída do ComfyUI. Ele salva a nuvem de pontos em um local temporário e a exibe em uma janela de pré-visualização 3D, além de passar os dados do modelo, informações do modelo, informações da câmera e dimensões da pré-visualização para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Arquivo de nuvem de pontos 3D (.ply) | FILE3D | Sim | - |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO | Não | - |
| `viewport_state` | Estado atual da visão 3D | LOAD3D | Sim | - |
| `camera_info` | Informações da câmera para a visão 3D | LOAD3DCAMERA | Não | - |
| `width` | Largura da janela de pré-visualização (padrão: 1024) | INT | Sim | 1 a 4096 |
| `height` | Altura da janela de pré-visualização (padrão: 1024) | INT | Sim | 1 a 4096 |

Nota: `model_3d_info` e `camera_info` são entradas avançadas opcionais. Quando não conectados, o nó recua para os valores correspondentes armazenados em `viewport_state`. O arquivo de nuvem de pontos é escrito no diretório temporário do ComfyUI em vez do diretório de saída. Este é um nó de saída (terminal), então é usado principalmente para exibir a pré-visualização na interface.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_3d` | Dados do modelo de nuvem de pontos | FILE3D |
| `model_3d_info` | Informações sobre o modelo 3D | LOAD3DMODELINFO |
| `camera_info` | Informações da câmera para a visão 3D | LOAD3DCAMERA |
| `width` | Largura da janela de pré-visualização | INT |
| `height` | Altura da janela de pré-visualização | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a0b13d9d5658343a6a7c25408d5e5cd9249c92264b76aa448a6553b370f4d782`
