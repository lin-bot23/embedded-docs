# LTXVFreezeLatent

```markdown
# LTXV Freeze Latent

## Resumen

El nodo LTXV Freeze Latent está diseñado para establecer el noise_mask en 0 para un latente dado, asegurando que el latente permanezca limpio durante la muestreo. Es particularmente útil para congelar latentes de audio o video para evitar la desENOISE, que puede aplicarse antes de concatenar audio y video para la atención cruzada o para cualquier latente que no deba ser desenoisado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `latent` | Latente de video o audio que se debe congelar. El audio es de 4D; el video es de 5D. | LATENT | Sí | N/A |
| `samples` | El tensores que contiene las muestras latentes. | TENSO | Sí | Audio: 4D (batch, canales, cuadros, muestras); Video: 5D (batch, canales, altura, anchura, cuadros) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `latent` | El latente con un noise_mask establecido en 0, asegurando que permanezca limpio durante el muestreo. | LATENT |

## Notas

- El tensores `samples` debe ser un tensores plano y no un latente concatenado audio-video. Si es un latente concatenado, debe dividirse primero usando el nodo Separar Latente AV.
- La salida `latent` tendrá un noise_mask de ceros, lo que impide la desenoise para el latente especificado.
- El nodo admite tanto latentes de audio como de video, con diferentes formas tensoriales para cada uno.
- Si la forma del tensores `samples` no coincide con la forma esperada de audio o video, se lanzará un ValueError.
```

**Nota:** La implementación real puede tener restricciones o comportamientos adicionales no documentados aquí. Siempre referirse al código fuente más reciente para obtener la información más precisa.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/es.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
