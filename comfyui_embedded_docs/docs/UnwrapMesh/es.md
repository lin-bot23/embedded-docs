# Desplegar las UV de la malla

Genera un atlas UV para una malla 3D. La superficie de la malla se divide en islas, cada isla se aplana en dos dimensiones y las islas aplanadas se empaquetan en un atlas UV en el rango [0,1]. Los vértices en las costuras de las islas se duplican, por lo que la malla de salida puede contener más vértices que la malla de entrada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `malla` | La malla de entrada que se va a desenvolver. Acepta una sola malla o un lote de mallas. | MESH | Sí | — |
| `segmentador` | Algoritmo de particionado a utilizar. `pec`: particionado rápido por colapso de aristas paralelas en GPU. `adaptive`: CPU, más lento. (predeterminado: "pec") | COMBO | Sí | "pec"<br>"adaptive" |
| `resolución` | Resolución objetivo del atlas para la autoescala de densidad de texel (0 = ajustar al contenido). (predeterminado: 1024) | INT | Sí | 0 a 8192 (paso 256) |
| `relleno` | Relleno en texeles entre islas. (predeterminado: 1) | INT | Sí | 0 a 16 |
| `distancia de soldadura` | Radio de fusión de vértices coincidentes como fracción de la extensión de la malla (0 = automático). Auméntelo a ~0.001 si obtiene islas por triángulo (entrada sin soldar). (predeterminado: 0.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.0001) |

Nota: si la malla de entrada contiene vértices sin soldar, el nodo puede advertir que la adyacencia de caras es baja y generar islas UV por cara; aumentar `weld_distance` fusiona los vértices coincidentes antes del desplegado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `malla` | La malla de entrada con un atlas UV generado en el rango [0,1]. Los vértices de las costuras se duplican, por lo que el recuento de vértices de salida puede superar al de entrada. Se conservan los colores de vértice y la textura de la malla de entrada. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/es.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
