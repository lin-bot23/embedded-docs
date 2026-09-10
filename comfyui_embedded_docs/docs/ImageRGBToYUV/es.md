# ImageRGBToYUV

El nodo ImageRGBToYUV convierte una imagen RGB al espacio de color YUV. Divide la imagen en tres componentes — Y (luminancia o brillo), U (crominancia de diferencia de azul) y V (crominancia de diferencia de rojo) — y devuelve cada componente como una imagen separada del mismo tamaño que la imagen de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | La imagen RGB de entrada que se convertirá a YUV. Si la imagen contiene un canal alfa, solo se utilizan los primeros tres canales (RGB). | IMAGE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `Y` | El componente de luminancia (brillo) del espacio de color YUV. | IMAGE |
| `U` | El componente de crominancia de diferencia de azul del espacio de color YUV. | IMAGE |
| `V` | El componente de crominancia de diferencia de rojo del espacio de color YUV. | IMAGE |

Cada salida tiene el mismo ancho, alto y número de canales que la imagen de entrada. El componente Y, U o V correspondiente se repite en todos los canales para que cada salida se devuelva como una imagen estándar.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/es.md)

---
**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`
