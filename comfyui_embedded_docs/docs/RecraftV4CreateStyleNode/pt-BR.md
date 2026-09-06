# Recraft V4 Criar Estilo

Este nó cria um estilo Recraft V4 reutilizável a partir de 1 a 10 imagens de referência. O ID de estilo retornado funciona com todos os modelos Recraft V4 e V4.1 do mesmo tipo de saída (raster ou vector), e pode ser reutilizado em etapas posteriores de geração de imagem. O tamanho total de todas as imagens de referência é limitado a 10 MB.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo para o qual o estilo é criado. Os modelos Standard e Pro compartilham o mesmo pool de estilos: estilos raster funcionam com todos os modelos Recraft V4 e V4.1 raster, estilos vector (*_vector) com todos os modelos V4 e V4.1 vector. | COMBO | Sim | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | Imagens de referência que definem o estilo. Referências semelhantes aprimoram o ajuste, referências variadas ampliam-no. Espaço crescente: conecte 1 a 10 imagens (`image_1` até `image_10`). | IMAGEM | Sim | 1 a 10 imagens |

### Notas

- Pelo menos uma imagem de referência é necessária; o nó gera um erro se nenhuma for fornecida.
- No máximo 10 imagens de referência são permitidas; o nó gera um erro se mais forem fornecidas.
- O tamanho total codificado de todas as imagens de referência não deve exceder 10 MB; o nó gera um erro se o limite for excedido.
- Cada imagem de referência é reduzida a no máximo 2048×2048 pixels e codificada como WebP antes de ser enviada para a API do Recraft.
- Modelos que terminam em `_vector` criam estilos vector; os outros opções criam estilos raster. Os modelos Standard e Pro compartilham o mesmo pool de estilos dentro de cada tipo de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `style_id` | Identificador único do estilo criado, utilizável com todos os modelos Recraft V4 e V4.1 do mesmo tipo de saída. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
