# Attention clairsemée par blocs du modèle

## Aperçu

Le nœud Bloc d'Attention Sparse modifie un modèle ComfyUI pour appliquer un mécanisme d'attention sparse par bloc. Ce mécanisme réduit la charge computationnelle en permettant à chaque bloc de requête de se concentrer sur un sous-ensemble de blocs de clé, plutôt que de s'attacher à tous les blocs possibles, ce qui est particulièrement bénéfique pour les séquences longues.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle ComfyUI auquel appliquer l'attention sparse par bloc. | MODEL | Oui | N/A |
| `selection` | La méthode utilisée pour déterminer quels blocs de clé doivent être pris en compte. | COMBO DYNAMIQUE | Oui | Options : sol-attn (tau adaptatif), sla (top-k), vsa (Video Sparse Attention) |
| `tau` | Le seuil en sigmas de distribution des scores pour la méthode sol-attn. | FLOAT | Non | par défaut : 1.3, min : 0.0, max : 4.0, pas : 0.05 |
| `keep_percent` | Le pourcentage de blocs de clé que chaque bloc de requête conserve exactement pour la méthode sla. | FLOAT | Non | par défaut : 10.0, min : 0.5, max : 95.0, pas : 0.5 |
| `start_percent` | Le pourcentage de point où l'attention sparse commence. | FLOAT | Non | par défaut : 0.2, min : 0.0, max : 1.0, pas : 0.01 |
| `end_percent` | Le pourcentage de point où l'attention sparse se termine. | FLOAT | Non | par défaut : 1.0, min : 0.0, max : 1.0, pas : 0.01 |
| `dense_blocks` | Une chaîne représentant les blocs de transformer qui doivent toujours utiliser l'attention dense. | STRING | Non | par défaut : "" |
| `min_tokens` | Le nombre minimum de tokens dans une séquence pour lequel le modèle utilise l'attention dense. | INTÉGRAL | Non | par défaut : 12288, min : 0, max : 1 << 20, pas : 512 |
| `extra_tokens` | Le nombre de tokens supplémentaires de score le plus élevé que chaque bloc de requête prend en compte au-delà de ses blocs sélectionnés. | INTÉGRAL | Non | par défaut : 256, min : 0, max : 256, pas : 64 |
| `sink_conditioning` | Les rangées de conditionnement MiniMax-H3 à utiliser pour le conditionnement de puits. | COMBO | Non | Options : exact_kv, exact_kv_and_rows, off |
| `verbose` | Active le journalisation verbale. | BOOLEEN | Non | par défaut : Faux |

### Notes

- Le paramètre `selection` vous permet de choisir entre différentes méthodes pour sélectionner les blocs de clé :
  - `sol-attn` : Utilise un seuil adaptatif pour sélectionner les blocs de clé en fonction de la distribution des scores.
  - `sla` : Conserve un pourcentage fixe des blocs de clé les plus bien notés.
  - `vsa` : Applique l'Attention Sparse Vidéo, qui utilise le tiling en cube vidéo 3D et une branche d'attention grossière apprise.
- Le paramètre `dense_blocks` peut être utilisé pour spécifier les blocs de transformer qui doivent toujours utiliser l'attention dense.
- Le paramètre `min_tokens` définit le nombre minimum de tokens dans une séquence pour lequel l'attention dense est utilisée.
- Le paramètre `extra_tokens` permet de spécifier le nombre de tokens supplémentaires de score le plus élevé que chaque bloc de requête doit prendre en compte.
- Le paramètre `sink_conditioning` est pertinent uniquement pour les modèles MiniMax-H3 et détermine comment les rangées de conditionnement sont traitées.
- Le paramètre `verbose` active la journalisation détaillée, ce qui peut être utile pour le débogage.

## Sorties

| Nom de la sortie | Description | Type de données |
|-------------|-------------|-----------|
| `model` | Le modèle ComfyUI auquel l'attention sparse par bloc a été appliquée. | MODEL |

### Contraintes et Limites

- La méthode `sol-attn` nécessite une valeur de `tau` entre 0.0 et 4.0.
- La méthode `sla` nécessite une valeur de `keep_percent` entre 0.5 et 95.0.
- La méthode `vsa` est compatible uniquement avec les modèles MiniMax-H3 et nécessite que le modèle ait une couche `to_gate_compress`.
- Le paramètre `min_tokens` doit être un entier positif ou nul (0 conserve toute l'attention en mode dense).
- Le paramètre `extra_tokens` doit être un entier non négatif.
- Les options `sink_conditioning` sont pertinentes uniquement pour les modèles MiniMax-H3.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/fr.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
