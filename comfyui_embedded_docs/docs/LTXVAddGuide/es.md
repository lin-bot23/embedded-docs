# LTXVAddGuide

El nodo LTXVAddGuide está diseñado para agregar guía de condicionamiento de video a secuencias latentes mediante la codificación de imágenes o videos de entrada y la incorporación de los marcos clave como datos de condicionamiento. Procesa la entrada a través de un codificador VAE y coloca estratégicamente los latentes resultantes en posiciones de cuadro específicas mientras actualiza tanto el condicionamiento positivo como negativo con información de marcos clave. El nodo maneja las restricciones de alineación de cuadro y permite controlar la fuerza del influjo de condicionamiento.

## Resumen

El nodo LTXVAddGuide codifica imágenes o videos de entrada, los procesa a través de un codificador VAE y utiliza los latentes codificados para condicionar una secuencia de video latente. Permite especificar un índice de cuadro para comenzar el condicionamiento y ajusta la fuerza del influjo de condicionamiento. El nodo también admite máscaras espaciales optativas en el espacio de píxeles para influjo de condicionamiento por región y puede manejar parámetros IC-LoRA para ajustes de procesamiento de guía específicos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `positivo` | Entrada de condicionamiento positivo que se modificará con guía de marcos clave | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo que se modificará con guía de marcos clave | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar los marcos de entrada de imagen/video | VAE | Sí | - |
| `latente` | Secuencia latente de entrada que recibirá los marcos de condicionamiento | LATENT | Sí | - |
| `imagen` | Imagen o video para condicionar la secuencia de video latente. Debe tener 8*n + 1 marcos. Si el video no tiene 8*n + 1 marcos, se recortará al número más cercano de 8*n + 1 marcos. | IMAGE | Sí | - |
| `indice_fotograma` | Índice de cuadro para comenzar el condicionamiento. Para imágenes o videos con 1-8 marcos, cualquier valor de frame_idx es aceptable. Para videos con 9+ marcos, frame_idx debe ser divisible por 8, de lo contrario se redondeará hacia abajo al múltiplo más cercano de 8. Los valores negativos se contabilizan desde el final del video. (por defecto: 0) | INT | Sí | -9999 a 9999 |
| `fuerza` | Fuerza del influjo de condicionamiento, donde 1.0 aplica condicionamiento completo y 0.0 aplica ningún condicionamiento (por defecto: 1.0) | FLOAT | Sí | 0.0 a 10.0 |
| `attention_mask` | Máscara espacial optativa en el espacio de píxeles. Controla el influjo de condicionamiento por región a través de la atención autoregulada, multiplicada por la fuerza. | MASK | No | - |
| `iclora_parameters` | Parámetros IC-LoRA optativos de un nodo Get IC-LoRA Parameters. Usados para ajustar el procesamiento de guía según sea requerido por ciertos IC-LoRA (por ejemplo, aquellos con un reference_downscale_factor > 1). Cuando se encadenan, cada LTXVAddGuide utiliza solo los parámetros conectados a él. | IC_LORA_PARAMETERS | No | - |

**Nota:** La imagen o el video de entrada debe tener un recuento de marcos que siga el patrón 8*n + 1 (por ejemplo, 1, 9, 17, 25 marcos). Si la entrada excede este patrón, se recortará automáticamente al número más cercano de 8*n + 1 marcos.

**Nota sobre `iclora_parameters`:** Al usar parámetros IC-LoRA con un `reference_downscale_factor` mayor que 1, las dimensiones espaciales latentes (ancho y altura) deben ser divisibles por ese factor. El nodo generará un error si no se cumple esta condición.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positivo` | Condicionamiento positivo actualizado con información de guía de marcos clave | CONDITIONING |
| `negativo` | Condicionamiento negativo actualizado con información de guía de marcos clave | CONDITIONING |
| `latente` | Secuencia latente con marcos de condicionamiento incorporados y máscara de ruido actualizada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/es.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
