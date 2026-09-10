# Tripo: Importar Modelo

Este nó importa um modelo 3D externo para o Tripo, para que os nós de pós-processamento do Tripo, como Texture, Rig e Convert, possam usá-lo. O nó envia o arquivo para o Tripo e retorna um ID de tarefa que identifica o modelo importado para uso por esses nós. O GLB é recomendado porque as texturas são preservadas apenas quando incorporadas ao arquivo, e a texturização de um modelo importado requer um prompt de textura. Este nó é gratuito para uso.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Modelo 3D a importar (GLB / FBX / OBJ / STL, até 150 MB). Arquivos OBJ e STL não contêm texturas incorporadas. | FILE3D | Sim | GLB<br>FBX<br>OBJ<br>STL<br>Any 3D format |

**Observação:** Apenas os formatos GLB, FBX, OBJ e STL são suportados. GLTF (.gltf) não pode ser importado porque faz referência a arquivos externos; exporte um GLB de arquivo único em vez disso. O arquivo de modelo deve ter 150 MB ou menos. O GLB é recomendado porque as texturas sobrevivem à importação apenas quando estão incorporadas ao arquivo. Arquivos OBJ e STL não carregam texturas incorporadas. A texturização de um modelo importado requer um prompt de textura.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model task_id` | Um ID de tarefa que identifica o modelo importado, para uso com nós de pós-processamento do Tripo | MODEL_TASK_ID |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`
