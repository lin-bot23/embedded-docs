# LTXVAddGuide

El nodo LTXVAddGuide añade guía de condicionamiento de video a secuencias latentes codificando imágenes o videos de entrada e incorporándolos como fotogramas clave en los datos de condicionamiento. Procesa la entrada a través de un codificador VAE y coloca estratégicamente los latentes resultantes en posiciones de fotograma especificadas, actualizando tanto el condicionamiento positivo como el negativo con información de fotogramas clave. El nodo gestiona las restricciones de alineación de fotogramas y permite controlar la fuerza de la influencia del condicionamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo que se modificará con la guía de fotogramas clave. | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo que se modificará con la guía de fotogramas clave. | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar los fotogramas de imagen/video de entrada. | VAE | Sí | - |
| `latente` | Secuencia latente de entrada que recibirá los fotogramas de condicionamiento. | LATENT | Sí | - |
| `imagen` | Imagen o video para condicionar el video latente. Debe tener 8*n + 1 fotogramas. Si el video no tiene 8*n + 1 fotogramas, se recortará al número más cercano de 8*n + 1 fotogramas. | IMAGE | Sí | - |
| `indice_fotograma` | Índice de fotograma para iniciar el condicionamiento. Para imágenes de un solo fotograma o videos con 1-8 fotogramas, cualquier valor de frame_idx es aceptable. Para videos con 9 o más fotogramas, frame_idx debe ser divisible por 8; de lo contrario, se redondeará hacia abajo al múltiplo de 8 más cercano. Los valores negativos se cuentan desde el final del video. (por defecto: 0) | INT | Sí | -9999 a 9999 |
| `fuerza` | Fuerza de la influencia del condicionamiento, donde 1.0 aplica el condicionamiento completo y 0.0 no aplica condicionamiento (por defecto: 1.0) | FLOAT | Sí | 0.0 a 10.0 |
| `attention_mask` | Máscara espacial opcional en el espacio de píxeles. Controla la influencia del condicionamiento por región mediante la autoatención, multiplicada por strength. | MASK | No | - |
| `iclora_parameters` | Parámetros IC-LoRA opcionales de un nodo Get IC-LoRA Parameters. Se utilizan para ajustar el procesamiento de la guía según lo requerido por ciertos IC-LoRA (por ejemplo, aquellos con un reference_downscale_factor > 1). Cuando se encadenan, cada LTXVAddGuide utiliza solo los parámetros conectados a este. | IC_LORA_PARAMETERS | No | - |

**Nota:** La imagen/video de entrada debe tener un número de fotogramas que siga el patrón 8*n + 1 (por ejemplo, 1, 9, 17, 25 fotogramas). Si la entrada supera este patrón, se recortará automáticamente al número de fotogramas válido más cercano.

**Nota sobre `iclora_parameters`:** Al usar parámetros IC-LoRA con un `reference_downscale_factor` mayor que 1, las dimensiones espaciales del latente (ancho y alto) deben ser divisibles por ese factor. El nodo generará un error si no se cumple esta condición.

**Nota:** Los fotogramas de guía codificados deben caber dentro de la secuencia latente en la posición de fotograma seleccionada. Si los fotogramas condicionados exceden la longitud de la secuencia latente, el nodo generará un error.

**Nota:** No se admite agregar una guía a un latente que combine canales de audio y video; esto generará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo actualizado con información de guía de fotogramas clave. | CONDITIONING |
| `negativo` | Condicionamiento negativo actualizado con información de guía de fotogramas clave. | CONDITIONING |
| `latente` | Secuencia latente con fotogramas de condicionamiento incorporados y máscara de ruido actualizada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/es.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
