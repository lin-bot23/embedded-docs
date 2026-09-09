# LTXVAddGeneratedKeyframes

```markdown
# LTXV Adicionar Chaves Geradas

## Visão Geral

O nó LTXV Adicionar Chaves Geradas anexa detalhes de chaves a um vídeo latente. Cada chave representa um quadro latente de tokens que span um único quadro de pixel, que são desnuvidos com o vídeo e não fazem parte da saída decodificada. A localização é determinada pelo parâmetro interval_frames, que especifica o passo do quadro de pixel para a localização automática.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condicionamento positivo aos quais as chaves são anexadas. | CONDITIONING | Sim | N/A |
| `negative` | Condicionamento negativo aos quais as chaves são anexadas. | CONDITIONING | Sim | N/A |
| `vae` | Usado apenas para ler os fatores de escala latentes. | VAE | Sim | N/A |
| `latent` | Vídeo latente plano 5D para gerar chaves ao lado. Adicione antes de Concat AV Latent. | LATENT | Sim | N/A |
| `interval_frames` | Passo do quadro de pixel para a localização automática. O padrão 24 é aproximadamente uma chave a cada segundo em 24 fps.像素已被占用则跳过。当frame_indices estiver definido, é ignorado. | INT | Não | 1-1024 |
| `keyframes` | Conteúdo opcional para inicializar novas chaves com. Conecte chaves de um Separar (mesmo tamanho espacial) anterior ou um vídeo latente plano para copiar o quadro mais próximo em cada novo slot (por exemplo, após o upscale temporal). Essas ainda são desnuvidas, não fixadas como guias. Índices gravados em um vídeo latente de chaves são ignorados a menos que frame_indices esteja definido. Tem efeito apenas quando a amostragem começa abaixo de sigma 1. | LATENT | Não | N/A |
| `frame_indices` | Índices de quadro de pixel opcionais. Deixe vazio para localizar a partir de interval_frames no canvas atual. Quando definido, essa lista é a localização (chaves conectadas são correspondidas na ordem). O último quadro é permitido; o quadro 0 não é (já é um token autônomo). | STRING | Não | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo com atenção de chave gerada anexada. | CONDITIONING |
| `negative` | Condicionamento negativo com atenção de chave gerada anexada. | CONDITIONING |
| `latent` | Vídeo latente com chaves geradas anexadas no T. | LATENT |

## Notas

- O parâmetro `interval_frames` determina o espaçamento das chaves no vídeo. Um valor mais alto resulta em menos chaves e uma taxa de quadros mais baixa.
- A entrada `keyframes` permite que você inicialize novas chaves com chaves existentes ou um vídeo latente. Se fornecido, essas chaves serão desnuvidas e anexadas ao vídeo latente.
- O parâmetro `frame_indices` permite que você especifique os índices exatos de quadro de pixel onde as chaves devem ser colocadas. Se fornecido, o parâmetro `interval_frames` é ignorado.
- As saídas `positive` e `negative` contêm o condicionamento com atenção de chave gerada anexada, que pode ser usado para processamento ou análise adicional.
- A saída `latent` contém o vídeo latente com chaves geradas anexadas no T, que pode ser usado para processamento ou análise adicional.
```

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
