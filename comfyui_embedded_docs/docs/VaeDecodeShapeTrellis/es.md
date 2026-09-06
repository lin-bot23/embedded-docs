# VaeDecodeShapeTrellis

Este nodo decodifica representaciones latentes de forma de Trellis2 en una malla 3D. Utiliza un VAE para convertir datos latentes de forma dispersos en geometría de malla y también genera datos de subdivisión de forma producidos durante la decodificación. El nodo admite entradas latentes tanto individuales como por lotes y ajusta automáticamente la orientación de la malla al sistema de coordenadas esperado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `samples` | Las muestras latentes a decodificar, incluido el tensor de muestras y los datos de coordenadas dispersas. El diccionario latente también puede contener campos opcionales: `coord_counts` para formas por lotes, `coord_resolution` para controlar la resolución de la malla y `model_frame` para la orientación de las coordenadas. | LATENT | Sí | None |
| `vae` | El modelo VAE utilizado para decodificar el latente de forma en una malla. | VAE | Sí | None |

### Notas sobre `samples`

- La entrada `samples` es un diccionario latente que debe contener el tensor `samples` y las coordenadas dispersas `coords`.
- Si `coord_counts` está presente, debe ser un tensor 1D de enteros no negativos, y la suma de todos los conteos debe ser igual al número total de filas de coordenadas. Cada conteo representa una forma en el lote.
- Si se proporciona `coord_resolution`, la resolución de la malla se calcula como `coord_resolution * 16`. De lo contrario, se utiliza el búfer de resolución integrado del VAE (valor predeterminado: 1024).
- Si `model_frame` se establece en `"z_up"`, los vértices de la malla decodificada se rotan desde un sistema de coordenadas Z-up a la convención Y-up utilizada por glTF. El valor predeterminado es `"y_up"`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `mesh` | La malla 3D decodificada, que contiene posiciones de vértices e índices de caras. Al decodificar múltiples formas, las mallas se devuelven como un solo tensor apilado si todas comparten la misma forma, o como un lote empaquetado de tamaño variable en caso contrario. | MESH |
| `shape_subdivides` | Datos de subdivisión de forma producidos en cada etapa del proceso de decodificación. | SHAPE_SUBDIVIDES |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/es.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
