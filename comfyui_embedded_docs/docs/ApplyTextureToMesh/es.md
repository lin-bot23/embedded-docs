# Aplicar textura a malla

Este nodo adjunta imágenes de textura horneadas a la disposición UV de una malla para que puedan exportarse junto con la malla mediante el nodo SaveGLB. Conecte la misma malla con UV desplegadas que usó para el horneado, junto con los mapas de imagen horneados. Los mapas opcionales de metalizado, rugosidad y oclusión se empaquetan en una única textura ORM; además, al proporcionar un mapa normal, también se almacenan las normales suaves y las tangentes necesarias para un sombreado correcto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mesh` | La malla con UV desplegadas a la que se adjuntarán las texturas horneadas. Debe ser la misma malla utilizada durante el horneado; se genera un error si la malla no tiene UV. | MESH | Sí | — |
| `base_color` | La imagen de color base horneada. Se almacena como la textura de la malla y se limita al rango 0-1. | IMAGE | Sí | — |
| `metallic` | El mapa de metalizado horneado. Se usa como el canal azul de la textura ORM combinada; por defecto es 0 si no se proporciona. | IMAGE | No | — |
| `roughness` | El mapa de rugosidad horneado. Se usa como el canal verde de la textura ORM combinada; por defecto es 1 si no se proporciona. | IMAGE | No | — |
| `occlusion` | El mapa de oclusión ambiental horneado. Se usa como el canal rojo de la textura ORM combinada; por defecto es 1 si no se proporciona. Cuando se proporciona, la textura ORM también se marca como la textura de oclusión para SaveGLB. | IMAGE | No | — |
| `normal_map` | El mapa normal horneado en espacio tangente. Cuando se proporciona, el nodo recalcula la base tangente por vértice y exporta normales de vértice suaves para que el mapa normal sombree correctamente. | IMAGE | No | — |

Nota: Cuando se conecta cualquiera de `metallic`, `roughness` u `occlusion`, los tres se empaquetan en una única textura glTF ORM con los canales R = oclusión, G = rugosidad, B = metalizado. Los mapas faltantes se rellenan con los valores predeterminados (oclusión 1, rugosidad 1, metalizado 0), y los mapas con resoluciones diferentes se redimensionan al mayor ancho y alto. Cuando se conecta `normal_map`, las normales de la malla se reemplazan con normales de vértice suaves calculadas y se añade una base tangente. Las coordenadas UV que caen fuera del rango [0,1] se escalan uniformemente a [0,1] conservando la relación de aspecto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mesh` | La malla de entrada con las imágenes de textura adjuntas a su disposición UV, lista para ser guardada por SaveGLB. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/es.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
