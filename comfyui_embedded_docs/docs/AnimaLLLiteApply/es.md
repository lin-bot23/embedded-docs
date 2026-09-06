# Aplicar Anima LLLite

```markdown
AnimaLLLiteApply aplica un parche de animación ligero a un modelo de difusión, lo que permite la generación controlada de imagen a imagen con fuerza y sincronización ajustables. Integra un parche de modelo preconfigurado con una imagen de entrada y una máscara opcional, modificando las capas de atención y MLP del modelo para influir en el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de difusión base al que se le aplicará el parche | MODEL | Sí | |
| `model_patch` | El parche de animación preconfigurado que se aplicará | MODEL_PATCH | Sí | |
| `image` | La imagen de referencia para guiar la generación. Solo se utilizan los primeros 3 canales de color (RGB) | IMAGE | Sí | |
| `strength` | La fuerza del efecto del parche (por defecto: 1.0) | FLOAT | Sí | -10.0 a 10.0 |
| `start_percent` | El porcentaje del proceso de denoizado en el que el parche comienza a surtir efecto (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `end_percent` | El porcentaje del proceso de denoizado en el que el parche deja de surtir efecto (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `mask` | Una máscara opcional para limitar el efecto del parche a áreas específicas de la imagen | MASK | No | |

**Nota sobre las restricciones de los parámetros:** Si el `model_patch` tiene 4 canales de entrada y no se proporciona una `mask`, se crea automáticamente una máscara cero para que coincida con las dimensiones de la imagen. Si el `model_patch` no tiene 4 canales de entrada, el parámetro `mask` se ignora y se establece en `None`. Este nodo está marcado como experimental en ComfyUI.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `MODEL` | El modelo de difusión modificado con el parche de animación aplicado | MODEL |
```

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/es.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
