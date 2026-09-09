# LTXVSeparateGeneratedKeyframes

## Aperçu

Le nœud LTXV Séparer les Keyframes Générés supprime les keyframes générés d'un latent échantillonné et de la condition, permettant un traitement séparé avant l'upscale spatiale du latent vidéo. Il est conçu pour être utilisé avant l'upscale spatiale et ne doit pas être exécuté après LTXV Coupe des Guides, car il traite les keyframes générés comme des guides jetables et les supprime.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `positive` | Condition positive avec les métadonnées des keyframes générés supprimées. | CONDITIONING | Oui | N/A |
| `negative` | Condition négative avec les métadonnées des keyframes générés supprimées. | CONDITIONING | Oui | N/A |
| `latent` | Latent vidéo avec les keyframes générés enlevés. | LATENT | Oui | N/A |
| `keyframes_to_batch` | Retourner les keyframes sous forme de lot de latents d'image unique. Laisser vide pour obtenir un latent multi-image, ce que le latent upsampler et un Add Generated Keyframes ultérieur attendent. | BOOLEEN | Non | par défaut : False |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | Condition positive avec les métadonnées des keyframes générés supprimées. | CONDITIONING |
| `negative` | Condition négative avec les métadonnées des keyframes générés supprimées. | CONDITIONING |
| `latent` | Latent vidéo avec les keyframes générés enlevés. | LATENT |
| `keyframes` | Les keyframes pelés, étiquetés avec generated_keyframe_indices et generated_keyframe_num_frames. Alimentez ces données à un Add Generated Keyframes ultérieur pour initialiser de nouveaux emplacements, ou à Generated Keyframes To Guides pour les fixer comme guides d'image figées (les indices sont remapés si la longueur du canevas a changé). | LATENT |

## Notes

- Le paramètre `keyframes_to_batch` détermine si les keyframes sont retournés sous forme de lot de latents d'image unique ou sous forme d'un latent multi-image.
- Le nœud assure que les keyframes générés sont supprimés de la condition et du latent avant tout traitement ultérieur.
- La sortie `keyframes` peut être utilisée pour initialiser de nouveaux emplacements pour les keyframes générés ou pour les fixer comme guides d'image figées.
- Le nœud lève une `ValueError` si le latent ne contient pas de keyframes générés ou si les keyframes ne correspondent pas au format attendu.
- Le nœud suppose que les keyframes générés ont été ajoutés à l'aide du nœud LTXV Add Generated Keyframes et qu'ils sont compatibles avec le latent actuel.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateGeneratedKeyframes/fr.md)

---
**Source fingerprint (SHA-256):** `295e49181e87445a1c47b2e9413d95b20585b12e89f26f13129ac5d97f913007`
