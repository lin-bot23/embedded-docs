# Crear imagen por capas

Este nodo combina múltiples capas de imagen en una única imagen compuesta. Toma una pila de capas creada con el nodo Add Layer y, opcionalmente, aplica la configuración de composición guardada desde el editor de compositor, fusionando las capas según su ubicación, tamaño, rotación, opacidad y modo de fusión.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `capas` | Pila de capas para componer; créela con Add Layer. Los elementos se apilan según z_index, los fotogramas del lote dentro de un elemento se expanden a capas consecutivas, y la ubicación, opacidad y modo de fusión del elemento definen la composición inicial. Sin un lienzo de documento explícito, el tamaño es una extensión máxima calculada de las capas colocadas. Una composición guardada que coincida con las entradas actuales tiene prioridad. | LAYERS | Sí | Máximo 50 capas |
| `compositor` | Composición en capas guardada por el editor de compositor. | COMPOSITOR | No | Ninguno |

**Notas sobre las restricciones:**

- La pila de capas admite un máximo de 50 capas (fotogramas expandidos); si se proporcionan más, se produce un error.
- Actualmente solo se admiten capas ráster; otros tipos de elementos de capa generan un error.
- La versión del documento de `layers` debe ser 1; otras versiones generan un error.
- El estado guardado de `compositor` solo se reproduce cuando las huellas de entrada registradas coinciden con la pila de capas actual. Si no coinciden, el nodo recurre a componer a partir de las propiedades de las capas y marca el estado guardado como obsoleto.
- La opacidad de la capa se limita al rango de 0.0 a 1.0.
- La ubicación horizontal/vertical de la capa (`x`, `y`) se limita al límite máximo de resolución.
- El ancho y alto de la capa recurren al tamaño natural de la imagen cuando se establecen en cero o menos, y se limitan al máximo de resolución.
- El tamaño del lienzo compuesto no debe superar el límite máximo de resolución.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `IMAGE` | Imagen compuesta. Contiene un canal alfa cuando la composición tiene áreas transparentes (por ejemplo, fondo oculto); de lo contrario, RGB sin transparencia. | IMAGE |
| `MASK` | Transparencia de la composición (1 = totalmente transparente). Todo ceros cuando la composición es opaca. | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/es.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
