# LTXVFreezeLatent

```markdown
# LTXV Freeze Latent

## Aperçu

Le nœud LTXV Freeze Latent est conçu pour définir le noise_mask sur 0 pour un latent donné, assurant ainsi que le latent reste propre pendant l'échantillonnage. Il est particulièrement utile pour geler les latents audio ou vidéo pour éviter le débruitage, qui peut être appliqué avant la concaténation audio et vidéo pour l'attention croisée ou pour tout latent qui ne devrait pas être débruité.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `latent` | Latent vidéo ou audio à geler. L'audio est 4D ; la vidéo est 5D. | LATENT | Oui | N/A |
| `samples` | Le tenseur contenant les échantillons latents. | TENSOR | Oui | Audio : 4D (batch, channels, frames, samples) ; Vidéo : 5D (batch, channels, height, width, frames) |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `latent` | Le latent avec un noise_mask défini sur 0, assurant ainsi qu'il reste propre pendant l'échantillonnage. | LATENT |

## Notes

- Le tenseur `samples` doit être un tenseur simple et non un latent audio-video concaténé. Si c'est un latent concaténé, il doit être divisé à l'aide du nœud Séparer le latent audio-video en premier.
- La sortie `latent` aura un noise_mask de zéros, ce qui empêche le débruitage pour le latent spécifié.
- Le nœud prend en charge à la fois les latents audio et vidéo, avec des formes de tenseurs différentes pour chacun.
- Si la forme du tenseur `samples` ne correspond pas à la forme audio ou vidéo attendue, une ValueError sera levée.
```

**Note:** La mise en œuvre réelle peut avoir des contraintes ou des comportements supplémentaires non explicitement documentés ici. Toujours vous référer au code source le plus récent pour obtenir les informations les plus précises.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/fr.md)

---
**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`
