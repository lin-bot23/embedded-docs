# Superponer texto

Este nodo dibuja texto sobre una imagen o un lote de imágenes. Crea una superposición de texto con un tamaño de fuente configurable, color, posición vertical, alineación horizontal y un contorno negro opcional, y luego compone la superposición sobre las imágenes originales.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imágenes` | La imagen o lote de imágenes de entrada sobre las que se dibujará el texto | IMAGE | Sí | |
| `texto` | El texto a superponer en la imagen (por defecto: ""). Admite múltiples líneas: las secuencias de escape `\n` y `\t` se convierten en saltos de línea y tabulaciones, y las líneas largas se ajustan automáticamente para caber dentro del ancho de la imagen. | STRING | Sí | |
| `tamaño de fuente` | Tamaño de fuente como porcentaje de la altura de la imagen (por defecto: 5.0) | FLOAT | Sí | 0.5 a 50.0 (paso 0.5) |
| `color` | Color del texto (por defecto: "#ffffff") | STRING | Sí | |
| `posición` | Posición vertical del texto en la imagen (por defecto: "top") | COMBO | Sí | "top"<br>"bottom" |
| `alineación` | Alineación horizontal del texto (por defecto: "left") | COMBO | Sí | "left"<br>"center"<br>"right" |
| `contorno` | Dibujar un contorno negro alrededor del texto (por defecto: True) | BOOLEAN | Sí | |

Nota: Si `text` está vacío o contiene solo espacios en blanco, el nodo devuelve las imágenes de entrada sin cambios. La superposición de texto se renderiza una vez y se aplica a cada imagen del lote.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `imágenes` | Las imágenes de entrada con la superposición de texto compuesta encima | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/es.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
