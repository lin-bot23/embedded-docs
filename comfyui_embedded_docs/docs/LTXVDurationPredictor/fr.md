# Prédicteur de durée LTXV

Ce nœud prédit la durée naturelle d’un plan pour un prompt texte à l’aide d’une tête de durée LTX 2.4 chargée avec ModelPatchLoader, puis ajuste le résultat sur la grille d’images 8k+1 du VAE. La prédiction est convertie en un nombre d’images à l’aide du taux d’images sélectionné et des limites de durée minimale et maximale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle utilisé pour prétraiter les plongements textuels et exécuter la tête de durée. | MODEL | Oui | N/A |
| `positive` | Le conditionnement qui fournit les plongements textuels du prompt et les métadonnées pour la prédiction de durée. | CONDITIONING | Oui | N/A |
| `duration_head` | Tête de durée LTX 2.4 chargée avec ModelPatchLoader. Doit être une tête de durée LTX. | MODEL_PATCH | Oui | N/A |
| `frame_rate` | Taux d’images par seconde utilisé pour convertir les secondes en images (défaut : 24.0). | FLOAT | Oui | 1.0 à 120.0 |
| `min_seconds` | Durée minimale en secondes utilisée lors de la conversion de la prédiction en nombre d’images (défaut : 1.0). | FLOAT | Oui | 0.5 à 120.0 |
| `max_seconds` | Durée maximale en secondes utilisée lors de la conversion de la prédiction en nombre d’images (défaut : 20.0). | FLOAT | Oui | 0.5 à 120.0 |

Remarque : L’entrée `duration_head` doit être un patch de modèle contenant une tête de durée LTX. Si le patch de modèle connecté n’est pas une tête de durée LTX, le nœud lève une ValueError. Seule la première entrée de conditionnement est utilisée — si `positive` contient un lot de plusieurs prompts, le nœud n’évalue que le premier.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `num_frames` | La durée prédite convertie en nombre d’images et ajustée sur la grille d’images 8k+1 du VAE. | INT |
| `seconds` | Durée prédite brute (non bornée). Cette valeur est celle d’avant l’ajustement sur la grille d’images. | FLOAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/fr.md)

---
**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`
