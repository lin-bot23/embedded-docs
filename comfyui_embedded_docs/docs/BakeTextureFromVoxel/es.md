# Hornear textura desde vóxel

Este nodo hornea texturas PBR sobre una malla 3D utilizando la disposición de UV existente de la malla. Muestrea atributos de color y material de un volumen disperso de vóxeles en cada texel y genera una imagen de color base junto con mapas de metálico y rugosidad. No desenvuelve la malla, por lo que debe conectarse aguas arriba un nodo que desenvuelva las UV.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `mesh` | La malla 3D sobre la que se hornean las texturas. Debe tener ya una disposición de UV; un nodo que desenvuelva las UV debe estar conectado aguas arriba. | MESH | Sí | |
| `voxel_colors` | Volumen disperso de vóxeles que contiene colores por vóxel y atributos PBR opcionales (canales de metálico y rugosidad). | VOXEL | Sí | |
| `texture_size` | Resolución del atlas UV cuadrado (nombre mostrado: "resolution", valor por defecto: 2048). | INT | Sí | 64 a 8192 |
| `reference_mesh` | Malla densa opcional previa a la decimación; reproyecta cada texel sobre su superficie real antes de muestrear, eliminando el horneado facetado en mallas de baja resolución. | MESH | No | |

Notas:

- La malla de entrada debe tener UVs. Si no hay UVs, el nodo genera un error. Las UVs deben estar en proporción 1:1 con los vértices (una UV por vértice).
- Cuando las coordenadas de la malla y de los vóxeles contienen una dimensión de lote, cada elemento del lote se hornea por separado. Si un elemento del lote no tiene vóxeles ni caras, se omite y se emite una textura negra para ese elemento.
- Cuando se proporciona `reference_mesh` para un lote, se empareja por índice de lote, a menos que contenga una sola malla, en cuyo caso esa malla se usa para todos los elementos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `base_color` | Mapa de textura de color base en RGB. Los valores son de tipo float en el rango 0–1. | IMAGE |
| `metallic` | Mapa de metálico en escala de grises (float, 0–1). Negro cuando los colores de los vóxeles no contienen ningún canal de metálico. | IMAGE |
| `roughness` | Mapa de rugosidad en escala de grises (float, 0–1). Negro cuando los colores de los vóxeles no contienen ningún canal de rugosidad. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/es.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
