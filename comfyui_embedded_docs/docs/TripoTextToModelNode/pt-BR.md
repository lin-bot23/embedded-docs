# Tripo: Texto para Modelo

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição textual do modelo 3D a ser gerado (multilinha). Este parâmetro é obrigatório e não pode estar vazio. | STRING | Sim | - |
| `negative_prompt` | Descrição textual do que evitar no modelo gerado (multilinha). Até 255 caracteres. Enviado para a API apenas quando não estiver vazio. | STRING | Não | Até 255 caracteres |
| `model_version` | Versão do modelo Tripo a ser usada para a geração (padrão: v3.1-20260211). | COMBO | Não | Múltiplas opções disponíveis |
| `style` | Estilo aplicado ao modelo gerado (padrão: Nenhum). Não mais suportado pela Tripo e ignorado; mantido para fluxos de trabalho mais antigos. | COMBO | Não | Múltiplas opções disponíveis |
| `texture` | Se gerar mapas de textura. Desligado retorna geometria nua e ignora `pbr` (padrão: Sim). | BOOLEAN | Não | Sim / Não |
| `pbr` | Se gerar mapas de material PBR (cor base, metálico, rugosidade, normal). Requer `texture`; forçado para desligado quando `texture` está desligado (padrão: Sim). | BOOLEAN | Não | Sim / Não |
| `image_seed` | Semente usada para a etapa de geração de imagem (padrão: 42). | INT | Não | 0 a 2147483647 |
| `model_seed` | Semente usada para a etapa de geração de modelo (padrão: 42). | INT | Não | 0 a 2147483647 |
| `texture_seed` | Semente usada para a etapa de geração de textura (padrão: 42). | INT | Não | 0 a 2147483647 |
| `texture_quality` | Qualidade dos mapas de textura gerados. detailed = texturas HD, extreme = texturas Ultra 8K (padrão: standard). | COMBO | Não | "standard"<br>"detailed"<br>"extreme" |
| `face_limit` | Número máximo de faces. -1 permite que a Tripo escolha adaptivamente (aproximadamente 1,4M faces na versão v3.x padrão, 2M na detalhada). A Tripo limita silenciosamente: v2.5 em 500.000, malhas quadrangulares em 150.000. (padrão: -1) | INT | Não | -1 a 2000000 |
| `quad` | Saída de malha quadrangular. A Tripo fornece malhas quadrangulares em FBX, então o resultado é entregue na saída FBX e a saída GLB permanece vazia. (padrão: Falso) | BOOLEAN | Não | Sim / Não |
| `geometry_quality` | Qualidade da geometria gerada (padrão: standard). | COMBO | Não | "standard"<br>"detailed" |
| `smart_low_poly` | Malha low-poly com拓扑 estilo manual limpa e bem construída (500-20.000 faces, quadrangular 500-10.000). Melhor para sujeitos simples; os complexos podem falhar. (padrão: Falso) | BOOLEAN | Não | Sim / Não |
| `auto_size` | Escalar modelos texturizados para o tamanho real do mundo em metros. A Tripo armazena o tamanho como a transformação da cena do modelo e cozinha-o quando o modelo é convertido, rigado ou retargetado; ignorado sem textura. (padrão: Sim) | BOOLEAN | Não | Sim / Não |

**Notas:**
- O parâmetro `prompt` é obrigatório: um prompt vazio faz com que o nó gere um erro.
- `pbr` requer `texture`. Quando `texture` está desligado, o nó força `pbr` para desligado e ignora seu valor. `auto_size` também não tem efeito sem `texture`.
- Quando `smart_low_poly` está ativado e `face_limit` é definido para um valor diferente de -1, o limite de faces deve estar entre 500 e 20.000 para saída triangular, ou entre 500 e 10.000 quando `quad` está ativado; caso contrário, o nó gera um erro.
- Quando `quad` está ativado, a malha quadrangular gerada é entregue como FBX, então a saída FBX é preenchida e a saída GLB permanece vazia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | O arquivo do modelo 3D gerado, mantido apenas para compatibilidade reversa. | STRING |
| `model task_id` | O identificador único da tarefa para o processo de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. Fica vazio quando `quad` está ativado. | FILE3DGLB |
| `FBX` | O modelo 3D gerado no formato FBX. Somente preenchido quando `quad` está ativado. | FILE3DFBX |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3f4bc09d125fedb6c30968f31804cfc7ec6d2f068a7c28d90b006137803020b0`
