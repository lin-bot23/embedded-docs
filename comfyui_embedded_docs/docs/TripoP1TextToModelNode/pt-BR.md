# Tripo P1: Texto para Modelo

Este nó gera um modelo 3D a partir de uma descrição de texto usando a API Tripo P1. Ele é otimizado para criar malhas de baixa poligonal, prontas para jogos com topologia estável, tornando-o adequado para aplicações em tempo real.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `output_mode` | Controla se o modelo gerado contém apenas geometria ou também texturas/PBR. Ao selecionar "Textured", adiciona entradas de textura abaixo. "Geometry only" retorna uma malha sem textura; "Textured" adiciona mapas de cor/PBR. | COMBO DINÂMICO | Sim | `"Geometry only"`<br>`"Textured"` |
| `prompt` | A descrição de texto do modelo 3D que você deseja gerar. Até 1024 caracteres. | STRING | Sim | Até 1024 caracteres |
| `negative_prompt` | Uma descrição de o que você não deseja no modelo gerado. Até 255 caracteres. | STRING | Não | Até 255 caracteres |
| `image_seed` | Um valor de semente para a geração de imagem, usado para controlar a aleatoriedade. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `face_limit` | Número alvo de faces, 48-20000. Um valor de -1 permite que o Tripo escolha adaptivamente. Padrão: -1. | INT | Não | -1 a 20000 |
| `model_seed` | Um valor de semente para a geração de modelo, usado para controlar a aleatoriedade. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `auto_size` | Escala a saída para aproximar metros do mundo real. Padrão: Falso. | BOOLEAN | Não | True / False |
| `export_uv` | Desempacotar UV durante a geração. Desative para execução mais rápida de geometria apenas. Padrão: True. | BOOLEAN | Não | True / False |
| `compress_geometry` | Aplicar compressão de geometria meshopt (EXT_meshopt_compression). Arquivos menores, mas o preview 3D do ComfyUI não pode exibi-los; descomprima antes de editar. Padrão: Falso. | BOOLEAN | Não | True / False |

### Entradas de geometria apenas

Não há entradas extras disponíveis quando `output_mode` é configurado para `"Geometry only"`. Parâmetros relacionados a textura não são enviados para o Tripo neste modo.

### Entradas texturizadas

Essas entradas aparecem apenas quando `output_mode` é configurado para `"Textured"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Incluir mapas PBR. Quando ativado, o mapa de base também é forçado. Padrão: True. | BOOLEAN | Sim | True / False |
| `texture_quality` | Preset de qualidade de textura. detailed = texturas HD, extreme = texturas Ultra 8K. Padrão: "standard". | COMBO | Sim | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Um valor de semente para a geração de textura, usado para controlar a aleatoriedade. Padrão: 42. | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | O caminho do arquivo para o modelo 3D gerado, mantido apenas para compatibilidade reversa. | STRING |
| `model task_id` | O ID de tarefa único para o pedido de geração de modelo. | ID_DE_TAREFA_DE_MODELO |
| `GLB` | O modelo 3D gerado no formato GLB. | ARQUIVO3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63781a990f892e6b1f241179039d1fb24778ba7aa7dccda7d14557cbf190b712`
