# ImageYUVToRGB

Le nœud ImageYUVToRGB convertit des images de l'espace colorimétrique YUV vers l'espace colorimétrique RVB. Il prend trois images d'entrée distinctes correspondant aux composantes Y (luma), U (projection bleue) et V (projection rouge), puis les combine en une seule image RVB.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `Y` | Image d’entrée pour la composante Y (luma) | IMAGE | Oui | - |
| `U` | Image d’entrée pour la composante U (projection bleue) | IMAGE | Oui | - |
| `V` | Image d’entrée pour la composante V (projection rouge) | IMAGE | Oui | - |

**Remarque :** Les trois images d’entrée (Y, U et V) doivent être fournies ensemble et posséder des dimensions compatibles pour une conversion correcte.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L’image RVB convertie | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/fr.md)

---
**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`
