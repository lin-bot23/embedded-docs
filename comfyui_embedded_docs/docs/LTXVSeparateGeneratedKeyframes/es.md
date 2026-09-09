# LTXVSeparateGeneratedKeyframes

## Resumen

El nodo LTXV Separar Claves Generadas elimina las claves generadas de un latente muestreado y la condición, permitiendo su manejo separado antes de escalar espacialmente el latente del video. Está diseñado para usarse antes de la escalada espacial y no debe ejecutarse después de LTXV Recortar Guías, ya que trata las claves generadas como guías desechables y las elimina.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condición positiva con los metadatos de claves generadas eliminados. | CONDITIONING | Sí | N/A |
| `negative` | Condición negativa con los metadatos de claves generadas eliminados. | CONDITIONING | Sí | N/A |
| `latent` | Latente del video con las claves generadas eliminadas. | LATENT | Sí | N/A |
| `keyframes_to_batch` | Devolver las claves como un lote de latentes de un solo cuadro. Dejarlo sin usar para obtener un latente multiframente, que es lo que esperan el escalador de latentes y el más tarde Agregar Claves Generadas. | BOOLEAN | No | predeterminado: Falso |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `positive` | Condición positiva con los metadatos de claves generadas eliminados. | CONDITIONING |
| `negative` | Condición negativa con los metadatos de claves generadas eliminados. | CONDITIONING |
| `latent` | Latente del video con las claves generadas eliminadas. | LATENT |
| `keyframes` | Las claves despojadas, etiquetadas con generated_keyframe_indices y generated_keyframe_num_frames. Alimentar estas a un más tarde Agregar Claves Generadas para inicializar nuevos espacios, o a Claves Generadas a Guías para fijarlas como guías de imagen congelada (los índices se reasignan si cambia la longitud del lienzo). | LATENT |

## Notas

- El parámetro `keyframes_to_batch` determina si las claves se devuelven como un lote de latentes de un solo cuadro o como un latente multiframente.
- El nodo asegura que las claves generadas se eliminen de la condición y el latente antes de cualquier procesamiento adicional.
- La salida `keyframes` se puede usar para inicializar nuevos espacios para las claves generadas o para fijarlas como guías de imagen congelada.
- El nodo lanza un `ValueError` si el latente no contiene claves generadas o si las claves no coinciden con el formato esperado.
- El nodo asume que las claves generadas se agregaron usando el nodo LTXV Agregar Claves Generadas y que son compatibles con el latente actual.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/es.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
