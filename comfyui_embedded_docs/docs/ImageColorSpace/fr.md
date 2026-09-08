# Convert Image Color Space

## Aperçu

Le nœud ImageColorSpace convertit les images entre différents espaces de couleur, y compris sRGB, HDR (Rec.2020 HLG) et HDR PQ (Rec.2020 PQ). Il permet de restreindre la luminance excessive des tons dans le lot et de compresser les couleurs hors de l'espace de couleur, et opère uniquement sur les canaux RGB, avec les canaux alpha passés en l'état.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `image` | L'image d'entrée à convertir. | IMAGE | Oui | Toute forme d'image valide. |
| `source` | L'espace de couleur des pixels d'entrée. | COMBO | Oui | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |
| `destination` | L'espace de couleur des pixels de sortie. | COMBO | Oui | <br> "sRGB" <br> "HDR" <br> "HDR PQ" |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `image` | L'image convertie dans l'espace de couleur de sortie spécifié. | IMAGE |

## Notes

- Le nœud utilise un blanc SDR de 203 nits et un affichage de référence HLG de 1000 nits pour les conversions.
- Les conversions sont calculées en float32 et renvoient l'appareil et le dtype intermédiaires.
- Le canal alpha est transmis en l'état, sans transformation de couleur.
- Le nœud prend en charge les conversions entre les espaces de couleur sRGB, HDR (Rec.2020 HLG) et HDR PQ (Rec.2020 PQ).
- Le nœud effectue un rétrécissement de la carte des tons et compresse les couleurs hors de l'espace de couleur pour assurer des conversions précises.
- Les canaux RGB sont utilisés pour les conversions, et le canal alpha (si présent) est transmis en l'état.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/fr.md)

---
**Source fingerprint (SHA-256):** `f0d38c6f5b524752a99d51b1a87f0e65c07f3ba36ecb0066d8d10c5b5032d36f`
