# LTXVGeneratedKeyframesToGuides

## Visão Geral

O nó LTXV Gerados Keyframes para Guias fixa os keyframes gerados em uma etapa anterior como guias de imagem congelados em um canvas posterior. Ele decodifica os keyframes como quadros independentes, redimensiona-os se necessário e os escreve com uma máscara de ruído de 0 para evitar denoising adicional. Os índices registrados são escalados do canvas onde foram gerados para o canvas alvo, e você pode sobrescrever os índices de quadro para definir posições explicitamente.

## Entradas

| Parâmetro                 | Descrição                                                                 | Tipo de Dados | Obrigatório | Intervalo |
|---------------------------|-----------------------------------------------------------------------------|-----------|----------|-------|
| `positive`                | Condicionamento positivo com os keyframes fixados como guias de imagem.             | CONDITIONING | Sim      |       |
| `negative`                | Condicionamento negativo com os keyframes fixados como guias de imagem.             | CONDITIONING | Sim      |       |
| `vae`                     | O modelo VAE a ser usado para decodificar os keyframes.                           | MODEL      | Sim      |       |
| `latent`                  | O vídeo latente alvo para adicionar os guias, por exemplo, o temporariamente escalado. | LATENT     | Sim      |       |
| `keyframes`               | Saída de keyframes do LTXV Separar Gerados Keyframes, que carrega o índice de quadro de pixel em que cada keyframe foi gerado. | LATENT     | Sim      |       |
| `strength`                | Força do guia. 1.0 é um pin rígido; valores mais baixos relaxam.                   | FLOAT      | Sim      | 0.0 - 10.0 |
| `override_frame_indices` | Opcional — fixe em esses quadros de pixel em vez das posições registradas (ou escaladas) automaticamente. Forneça um índice por keyframe. Deixe em branco para reutilizar posições registradas ou para escalá-las quando o canvas alvo tiver um comprimento diferente (por exemplo, após temporal x2). | STRING    | Não      |       |

## Saídas

| Nome da Saída | Descrição                                                                 | Tipo de Dados |
|-------------|-----------------------------------------------------------------------------|-----------|
| `positive`  | Condicionamento positivo com os keyframes fixados como guias de imagem.             | CONDITIONING |
| `negative`  | Condicionamento negativo com os keyframes fixados como guias de imagem.             | CONDITIONING |
| `latent`    | Vídeo latente alvo com os keyframes adicionados como guias congelados.               | LATENT     |

## Notas

- O parâmetro `strength` controla a força com que os keyframes são fixados como guias. Um valor de 1.0 cria um pin rígido, enquanto valores mais baixos relaxam o pinning.
- O parâmetro `override_frame_indices` permite que você especifique os quadros de pixel exatos onde os keyframes devem ser fixados. Se deixado em branco, o nó usará as posições registradas ou as escalonará se necessário.
- O nó assume que o latente `keyframes` contém o índice de quadro de pixel para cada keyframe. Se isso não for o caso, o nó levantará um `ValueError`.
- O nó suporta apenas um tamanho de lote de 1. Cada guia é codificada a partir de uma imagem, então não pode diferir entre elementos do lote.
- O nó levantará um `ValueError` se o tensor `samples` na entrada `latent` não for um tensor 5D ou se o tamanho do lote não for 1.
- O nó levantará um `ValueError` se o tensor `samples` na entrada `keyframes` não for um tensor 5D ou se o tamanho do lote não for 1.
- O nó levantará um `ValueError` se a forma do tensor `samples` na entrada `keyframes` não coincidir com a forma do tensor `samples` na entrada `latent` após o redimensionamento.
- O nó levantará um `ValueError` se o parâmetro `strength` estiver fora do intervalo de 0.0 a 10.0.
- O nó levantará um `ValueError` se o parâmetro `override_frame_indices` não for uma lista de inteiros separados por vírgula ou se o número de índices não coincidir com o número de keyframes.
- O nó levantará um `ValueError` se algum dos índices no parâmetro `override_frame_indices` estiver fora do intervalo de 1 a o número de quadros de pixel no canvas alvo.
- O nó levantará um `ValueError` se o índice máximo no parâmetro `override_frame_indices` for maior que o número de quadros de pixel no canvas alvo.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
