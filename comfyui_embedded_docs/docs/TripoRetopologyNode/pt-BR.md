# Tripo: Retopologia

Tripo: Retopology recebe um modelo 3D high-poly gerado por um nó Tripo anterior e o reconstrói como uma versão low-poly com topologia limpa. Ele envia o modelo ao serviço de retopologia da Tripo, aguarda a conclusão da tarefa, depois baixa o modelo finalizado e expõe seu ID de tarefa para uso por outros nós Tripo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID da tarefa do modelo high-poly de origem. Aceita um ID de tarefa de modelo de um nó de geração Tripo ou um ID de tarefa de segmento de Tripo: Segment Model. | STRING | Sim | ID de tarefa Tripo |
| `face_limit` | Contagem alvo de faces: 500-20.000 triângulos ou 500-10.000 quads. -1 permite que a Tripo escolha. (padrão: -1) | INT | Sim | -1 (automático)<br>500 a 20.000 (triângulos)<br>500 a 10.000 (quads) |
| `quad` | Saída de malha quad. A Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Sim | True<br>False (padrão) |
| `bake` | Faz o bake das texturas de origem na malha low-poly. (padrão: True) | BOOLEAN | Não | True (padrão)<br>False |
| `part_names` | Nomes de partes separados por vírgula de Tripo: Segment Model. Vazio processa o modelo inteiro. (padrão: "") | STRING | Não | Nomes de partes do modelo ou vazio |

Observação: Quando `face_limit` é definido como -1, a Tripo decide automaticamente a contagem de faces. Quando `quad` está habilitado, o limite máximo de faces é 10.000 quads em vez de 20.000 triângulos, e o resultado é fornecido como FBX (a saída GLB permanece vazia). Quando `part_names` está vazio, o modelo inteiro é processado. Se `face_limit` for algo diferente de -1 e estiver fora do intervalo permitido, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Saída compatível com versões anteriores que identifica o arquivo de modelo concluído. Fluxos de trabalho mais recentes devem usar as saídas GLB ou FBX. | STRING |
| `task_id do modelo` | ID da tarefa do resultado de retopologia finalizado. Pode ser passado para outros nós Tripo para referenciar este modelo. | STRING |
| `GLB` | O modelo low-poly retopologizado em formato GLB. Vazio quando `quad` está habilitado. | GLB FILE |
| `FBX` | O modelo low-poly retopologizado em formato FBX. Preenchido apenas quando `quad` está habilitado. | FBX FILE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b0e967eb4987a70242b6cfce93f09e0caffb7f4bdd3e4f1439e68f33f9138bb5`
