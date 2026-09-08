# Block Sparse Attention

## Aperçu

Le nœud Block Sparse Attention applique un mécanisme d'attention bloc-sparse à un modèle ComfyUI, réduisant les calculs d'attention en permettant à chaque bloc de requête d'attendre uniquement un sous-ensemble sélectionné de blocs de clé exactement.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle ComfyUI auquel appliquer l'attention bloc-sparse. | MODEL | Oui | N/A |
| `selection` | La méthode de sélection pour choisir quels blocs de clé attendre. | DYNAMIC_COMBO | Oui | Options : Sol-Attn (tau adaptatif), top-k (SLA), VSA (FastVideo) |
| `tau` | Le seuil en sigmas de distribution des scores pour la sélection Sol-Attn (tau adaptatif). | FLOAT | Non | par défaut : 1.3, min : 0.0, max : 4.0, étape : 0.05 |
| `keep_percent` | Le pourcentage de blocs de clé que chaque bloc de requête conserve exactement pour la sélection top-k (SLA). | FLOAT | Non | par défaut : 10.0, min : 0.5, max : 95.0, étape : 0.5 |
| `start_percent` | Le pourcentage du programme avant lequel le modèle utilise une attention dense. | FLOAT | Non | par défaut : 0.2, min : 0.0, max : 1.0, étape : 0.01 |
| `end_percent` | Le pourcentage du programme après lequel le modèle utilise une attention dense. | FLOAT | Non | par défaut : 1.0, min : 0.0, max : 1.0, étape : 0.01 |
| `dense_blocks` | Une chaîne représentant les blocs de transfo qui utilisent toujours une attention dense. | STRING | Non | par défaut : "" |
| `min_tokens` | Le nombre minimum de tokens dans une séquence pour lequel le modèle utilise une attention dense. | INT | Non | par défaut : 12288, min : 0, max : 1 << 20, étape : 512 |
| `extra_tokens` | Le nombre de tokens supplémentaires de haute note que chaque bloc de requête attend au-delà de ses blocs sélectionnés. | INT | Non | par défaut : 256, min : 0, max : 256, étape : 64 |
| `sink_conditioning` | Les lignes de conditionnement MiniMax-H3 à utiliser pour le conditionnement de puits. | COMBO | Non | Options : exact_kv, exact_kv_and_rows, off |
| `verbose` | Si activer le journalisation verbeuse. | BOOLEAN | Non | par défaut : False |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `model` | Le modèle ComfyUI avec l'attention bloc-sparse appliquée. | MODEL |

### Notes

- Le paramètre `selection` détermine comment les blocs de clé sont choisis. Les options sont :
  - Sol-Attn (tau adaptatif) : Chaque bloc de requête attend un sous-ensemble sélectionné de blocs de clé en fonction d'un seuil adaptatif.
  - top-k (SLA) : Chaque bloc de requête conserve un pourcentage fixe de blocs de clé exactement.
  - VSA (FastVideo) : Chaque bloc de requête conserve un pourcentage fixe de cubes vidéo exactement, en utilisant le tiling de cube et la branche grossière de FastH3-VSA.
- Le paramètre `dense_blocks` permet de spécifier les blocs de transfo qui utilisent toujours une attention dense.
- Le paramètre `min_tokens` définit le nombre minimum de tokens dans une séquence pour lequel le modèle utilise une attention dense.
- Le paramètre `extra_tokens` permet de spécifier le nombre de tokens supplémentaires de haute note que chaque bloc de requête attend au-delà de ses blocs sélectionnés.
- Le paramètre `sink_conditioning` détermine les lignes de conditionnement MiniMax-H3 à utiliser pour le conditionnement de puits.
- Le paramètre `verbose` active la journalisation verbeuse.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/fr.md)

---
**Source fingerprint (SHA-256):** `6a27aee45593883f5958ae1aac74a2077362742a0fdf74fc9dbfd68eddc6d259`
