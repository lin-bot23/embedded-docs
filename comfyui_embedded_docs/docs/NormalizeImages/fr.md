# Normaliser les images

Ce nœud ajuste les valeurs des pixels d'une image d'entrée en utilisant un processus de normalisation mathématique. Il soustrait une valeur moyenne spécifiée de chaque pixel et divise ensuite le résultat par une déviation standard spécifiée. Il s'agit d'une étape de prétraitement courante pour préparer les données d'image pour d'autres modèles de machine learning. Si l'image d'entrée possède un canal alpha, ce canal est passé en tant que tel, ce qui préserve la transparence.

## Aperçu

Le nœud Normaliser les couleurs d'image normalise les couleurs d'une image d'entrée en ajustant ses valeurs de pixels en fonction d'une valeur moyenne et d'une déviation standard. Ce processus est utile pour standardiser les données d'image avant d'appliquer des algorithmes de machine learning.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `image`   | L'image d'entrée à normaliser. | IMAGE | Oui | - |
| `moyenne` | Valeur moyenne pour la normalisation. | FLOAT | Non | 0.0 - 1.0 (par défaut : 0.5) |
| `écart_type` | Déviation standard pour la normalisation. | FLOAT | Non | 0.001 - 1.0 (par défaut : 0.5) |

Les paramètres `mean` et `std` sont utilisés pour normaliser les valeurs des pixels de l'image d'entrée. Les valeurs par défaut pour les deux paramètres sont réglées sur 0.5, ce qui est une choix commun pour la normalisation.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `images`     | L'image résultante après que le processus de normalisation ait été appliqué. | IMAGE |

La sortie du nœud Normaliser les couleurs d'image est l'image normalisée. Les valeurs des pixels sont ajustées selon la valeur moyenne et la déviation standard spécifiées, et le canal alpha (si présent) est préservé.

## Note

Le nœud Normaliser les couleurs d'image est conçu pour gérer toute taille de lot d'images, ce qui le rend adapté aux tâches de traitement par lot.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/fr.md)

---
**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`
