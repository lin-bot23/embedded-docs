# Pixal3DConditioning

```markdown
# Pixal3DConditioning

## Aperçu

Le nœud Pixal3DConditioning est conçu pour préparer la conditionnement d'image pour le pipeline de génération 3D Trellis2. Il utilise un modèle de vision DINOv3 pour extraire les caractéristiques visuelles de l'image d'entrée à deux résolutions. Ces caractéristiques sont ensuite organisées en cartes de caractéristiques par étape, qui peuvent être optionnellement améliorées avec un modèle NAF. Le nœud intègre également les données de caméra dérivées du champ de vision horizontal pour calculer la matrice de transformation de projection. Il produit une paire de conditionnement positive qui inclut les cartes de caractéristiques dérivées de l'image et les données de projection, ainsi qu'une paire de conditionnement négative avec des tenseurs de caractéristiques zéroisés pour une guidance sans classificateur.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | Le modèle ClipVision DINOv3 ViT-L/16 utilisé pour l'extraction de caractéristiques. | CLIP_VISION | Oui | — |
| `image` | L'image prétraitée provenant du nœud ImageCropToMask, destinée à Pixal3D avec un facteur de pad de 1.1. | IMAGE | Oui | — |
| `camera_angle_x` | Le champ de vision horizontal en degrés. Ce paramètre peut être connecté à un nœud MoGeGeometryToFOV pour un champ de vision par image. Valeur par défaut : 49.13. | FLOAT | Oui | 1.0 – 170.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positif` | La sortie de conditionnement positive contenant les cartes de caractéristiques dérivées de l'image et les données de projection pour la génération Trellis2. | CONDITIONING |
| `négatif` | La sortie de conditionnement négative avec des tenseurs de caractéristiques zéroisés, utilisée pour une guidance sans classificateur. | CONDITIONING |

Note : La valeur `camera_angle_x` est convertie en radians internement et utilisée pour calculer la distance de la caméra pour la matrice de transformation de projection. Lorsque le modèle de vision fourni inclut une composante NAF, le nœud produit également des cartes de caractéristiques à haute résolution pour les étapes forme et texture.
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`
