# LTXVGeneratedKeyframesToGuides

## Resumen

El nodo LTXV Generados Claveframes a Guías fija los claveframes generados en una etapa anterior como guías de imagen congeladas en un lienzo posterior. Decodifica los claveframes como cuadros independientes, los redimensiona si es necesario y los escribe con una máscara de ruido de 0 para evitar el desenoising adicional. Los índices grabados se escalan desde el lienzo en el que se generaron al lienzo objetivo, y puedes anular los índices de cuadros para establecer posiciones explícitamente.

## Entradas

| Parámetro                 | Descripción                                                                 | Tipo de Datos | Requerido | Rango |
|---------------------------|-----------------------------------------------------------------------------|---------------|-----------|-------|
| `positive`                | Condicionamiento positivo con los claveframes fijados como guías de imagen.   | CONDITIONING  | Sí        |       |
| `negative`                | Condicionamiento negativo con los claveframes fijados como guías de imagen.   | CONDITIONING  | Sí        |       |
| `vae`                     | El modelo VAE a usar para decodificar los claveframes.                       | MODEL         | Sí        |       |
| `latent`                  | El video latente objetivo al que agregar las guías, por ejemplo, el temporalmente escalado. | LATENT       | Sí        |       |
| `keyframes`               | La salida claveframes de LTXV Separar Claveframes Generados, que lleva el índice de cuadro de píxeles en el que se generó cada claveframe. | LATENT       | Sí        |       |
| `strength`                | Fuerteza de la guía. 1.0 es un fijo duro; valores más bajos lo relajan.         | FLOAT         | Sí        | 0.0 - 10.0 |
| `override_frame_indices` | Opcional — fija en estos cuadros de píxeles en lugar de las posiciones grabadas (o escaladas automáticamente). Proporciona un índice por claveframe. Deja vacío para reutilizar las posiciones grabadas o para escalarlas cuando el lienzo objetivo tiene una longitud diferente (por ejemplo, después de temporal x2). | STRING       | No        |       |

## Salidas

| Nombre de Salida | Descripción                                                                 | Tipo de Datos |
|------------------|-----------------------------------------------------------------------------|---------------|
| `positive`       | Condicionamiento positivo con los claveframes fijados como guías de imagen.   | CONDITIONING  |
| `negative`       | Condicionamiento negativo con los claveframes fijados como guías de imagen.   | CONDITIONING  |
| `latent`         | Video latente objetivo con los claveframes agregados como guías congeladas. | LATENT        |

## Notas

- El parámetro `strength` controla cuán fuertemente los claveframes se fijan como guías. Un valor de 1.0 crea un fijo duro, mientras que valores más bajos relajan el fijo.
- El parámetro `override_frame_indices` permite especificar los cuadros de píxeles exactos donde deben fijarse los claveframes. Si se deja vacío, el nodo utilizará las posiciones grabadas o las escalará si es necesario.
- El nodo asume que el latente `keyframes` contiene el índice de cuadro de píxeles para cada claveframe. Si esto no es el caso, el nodo lanzará un `ValueError`.
- El nodo solo admite un tamaño de lote de 1. Cada guía se codifica a partir de una imagen, por lo que no puede diferir entre elementos del lote.
- El nodo lanzará un `ValueError` si la tensores `samples` en la entrada `latent` no es una tensores de 5D o si el tamaño del lote no es 1.
- El nodo lanzará un `ValueError` si la tensores `samples` en la entrada `keyframes` no es una tensores de 5D o si el tamaño del lote no es 1.
- El nodo lanzará un `ValueError` si la forma de la tensores `samples` en la entrada `keyframes` no coincide con la forma de la tensores `samples` en la entrada `latent` después de redimensionar.
- El nodo lanzará un `ValueError` si el parámetro `strength` está fuera del rango de 0.0 a 10.0.
- El nodo lanzará un `ValueError` si el parámetro `override_frame_indices` no es una lista de enteros separados por comas o si el número de índices no coincide con el número de claveframes.
- El nodo lanzará un `ValueError` si algún índice en el parámetro `override_frame_indices` está fuera del rango de 1 al número de cuadros de píxeles en el lienzo objetivo.
- El nodo lanzará un `ValueError` si el índice máximo en el parámetro `override_frame_indices` es mayor que el número de cuadros de píxeles en el lienzo objetivo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/es.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
