# LTXVAddLatentGuide

## Resumen

El nodo Guía de Añadir Latente LTXV fija un latente ya codificado como una guía, permitiendo el uso de una guía que proviene de una etapa anterior en lugar de una imagen. Este nodo evita el viaje de decodificación/encodificación del VAE y puede dilatar una guía espacialmente más pequeña en una cuadrícula dispersa para cubrir el lienzo objetivo.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrada de condicionamiento positivo. | CONDITIONING | Sí | N/A |
| `negative` | Entrada de condicionamiento negativo. | CONDITIONING | Sí | N/A |
| `vae` | El modelo VAE a usar. | MODEL | Sí | N/A |
| `latent` | Latente de video objetivo al que se fija la guía. | LATENTE | Sí | N/A |
| `guiding_latent` | Latente de guía. Su tamaño espacial debe dividir el tamaño del objetivo por el mismo número entero en ambos ejes; un tamaño igual fija la guía tal cual, la mitad del tamaño se trata como una referencia IC-LoRA x2. | LATENTE | Sí | N/A |
| `latent_idx` | Índice de cuadro de latente para comenzar la guía, contado en cuadros latentes en lugar de cuadros de píxeles. Valores negativos colocan la guía en cuadros antes del inicio del latente, no contados hacia atrás desde su final. | INT | Sí | -9999 a 9999 |
| `strength` | Acotado en 1.0. Una guía dilatada marca sus posiciones de relleno con una máscara de desenoise negativa para que el modelo los descarte; valores por encima de 1.0 los posiciones mantenidas también serían negativas y toda la guía sería descartada. Amplifique más allá de 1.0 con attention_mask en su lugar. | FLOAT | Sí | 0.0 a 1.0, paso 0.01 |
| `attention_mask` | Máscara espacial opcional en espacio de píxeles. Controla la influencia de condicionamiento por región a través de auto-consideración, multiplicada por la fuerza. | MASK | No | N/A |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `positive` | Salida de condicionamiento positivo. | CONDITIONING |
| `negative` | Salida de condicionamiento negativo. | CONDITIONING |
| `latent` | Salida latente con la guía aplicada. | LATENTE |

## Notas

- El tamaño espacial del `guiding_latent` debe dividir el tamaño `latent` por el mismo número entero en ambos ejes.
- El parámetro `latent_idx` permite una colocación precisa de la guía dentro de los cuadros latentes.
- El parámetro `strength` controla la intensidad de la guía, con valores por encima de 1.0 que requieren el uso de `attention_mask` para evitar posiciones negativas.
- El parámetro `attention_mask` es opcional pero se puede usar para afinar la influencia de la guía en regiones específicas de la imagen.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/es.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
