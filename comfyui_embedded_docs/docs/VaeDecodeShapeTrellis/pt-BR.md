# VaeDecodeShapeTrellis

### Decodificação de Representações Latentes de Forma Trellis2 em Malha 3D

Este nó decodifica representações latentes de forma Trellis2 em uma malha 3D. Ele usa um VAE (Variational Autoencoder) para converter dados latentes de forma esparça em geometria de malha e também fornece dados de subdivisão de forma gerados durante o decodificação. O nó suporta tanto entradas latentes individuais quanto em lote e ajusta automaticamente a orientação da malha ao sistema de coordenadas esperado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `samples` | Amostras latentes a serem decodificadas, incluindo a tensor de amostra e dados de coordenadas esparças. O dicionário latente também pode conter campos opcionais: `coord_counts` para formas em lote, `coord_resolution` para controlar a resolução da malha e `model_frame` para orientação das coordenadas. | LATENT | Sim | Nenhum |
| `vae` | O modelo VAE usado para decodificar a forma latente em uma malha. | VAE | Sim | Nenhum |

### Notas sobre `samples`

- A entrada `samples` é um dicionário latente que deve conter a tensor de amostra e as coordenadas esparças `coords`.
- Se `coord_counts` estiver presente, deve ser uma tensor 1D de inteiros não negativos e a soma de todos os contadores deve igualar o número total de linhas de coordenadas. Cada contador representa uma forma no lote.
- Se `coord_resolution` for fornecida, a resolução da malha é calculada como `coord_resolution * 16`. Caso contrário, é usado o buffer de resolução interno do VAE (valor padrão: 1024).
- Se `model_frame` for configurado para `"z_up"`, os vértices decodificados da malha são rotacionados de um sistema de coordenadas Z-up para o convencional Y-up usado pelo glTF. O valor padrão é `"y_up"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha decodificada 3D, contendo posições de vértices e índices de faces. Quando decodificar múltiplas formas, as malhas são retornadas como uma única tensor empilhada se todas compartilharem a mesma forma, ou como uma variável de tamanho empacotado caso contrário. | MESH |
| `shape_subdivides` | Dados de subdivisão de forma produzidos em cada estágio do processo de decodificação. | SHAPE_SUBDIVIDES |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
