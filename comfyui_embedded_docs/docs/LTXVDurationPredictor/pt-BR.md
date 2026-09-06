# LTXV Duration Predictor

Este nó prevê a duração natural da cena para um prompt de texto usando uma cabeça de duração LTX 2.4 carregada com ModelPatchLoader, e então ajusta o resultado para a grade de quadros 8k+1 do VAE. A previsão é convertida em um número de quadros usando a taxa de quadros selecionada e os limites mínimos e máximos de duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo usado para pré-processar os embeddings de texto e executar a cabeça de duração. | MODEL | Sim | N/A |
| `positive` | A condição que fornece os embeddings de texto e os metadados para a previsão de duração. | CONDITIONING | Sim | N/A |
| `duration_head` | Cabeça de duração LTX 2.4 carregada com ModelPatchLoader. Deve ser uma cabeça de duração LTX. | MODEL_PATCH | Sim | N/A |
| `frame_rate` | Taxa de quadros em quadros por segundo usada para converter segundos em quadros (padrão: 24.0). | FLOAT | Sim | 1.0 a 120.0 |
| `min_seconds` | Duração mínima em segundos usada ao converter a previsão em um número de quadros (padrão: 1.0). | FLOAT | Sim | 0.5 a 120.0 |
| `max_seconds` | Duração máxima em segundos usada ao converter a previsão em um número de quadros (padrão: 20.0). | FLOAT | Sim | 0.5 a 120.0 |

Nota: A entrada `duration_head` deve ser um patch de modelo contendo uma cabeça de duração LTX. Se o patch de modelo conectado não for uma cabeça de duração LTX, o nó levanta um ValueError. Apenas a primeira entrada de condição é usada — se `positive` contiver um lote de mais de um prompt, o nó avalia apenas o primeiro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `num_frames` | A duração prevista convertida em um número de quadros e ajustada para a grade de quadros 8k+1 do VAE. | INT |
| `seconds` | Duração prevista bruta (não ajustada). Este é o valor antes de ajustar para a grade de quadros. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`
