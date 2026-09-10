# LTXVAddGeneratedKeyframes

## Aperçu

Le nœud LTXV Add Generated Keyframes ajoute des keyframes détaillés à un latent vidéo. Chaque keyframe représente un cadre latent de tokens couvrant un cadre de pixels unique, qui sont débruités avec la vidéo et ne font pas partie de la sortie décodée. Le placement est déterminé par le paramètre interval_frames, qui spécifie le pas de cadre de pixels pour le placement automatique.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `positive` | Conditionnement positif auxquels les keyframes sont attachés. | CONDITIONING | Oui | N/A |
| `negative` | Conditionnement négatif auxquels les keyframes sont attachés. | CONDITIONING | Oui | N/A |
| `vae` | Utilisé uniquement pour lire les facteurs de scale latents. | VAE | Oui | N/A |
| `latent` | Latent vidéo 5D brut pour générer des keyframes en même temps. Ajoutez-les avant Concat AV Latent. | LATENT | Oui | N/A |
| `interval_frames` | Pas de cadre de pixels pour le placement automatique. La valeur par défaut 24 correspond à environ un keyframe par seconde à 24 ips. Les pixels occupés sont ignorés. Ignoré lorsque frame_indices est défini. | INT | Non | 1-1024 |
| `keyframes` | Contenu optionnel pour initialiser les nouveaux keyframes. Connectez les keyframes d'un Séparer (même taille spatiale) précédent ou un latent vidéo brut pour copier le cadre le plus proche à chaque nouveau emplacement (par exemple, après un upscale temporel). Ces keyframes sont toujours débruités, mais pas fixés comme guides. Les indices enregistrés sur un latent keyframes sont ignorés sauf si frame_indices est défini. Ne prend effet que lorsque le sampling commence en dessous de sigma 1. | LATENT | Non | N/A |
| `frame_indices` | Indices de cadre de pixels optionnels. Laissez vide pour placer à partir de interval_frames sur le canevas actuel. Lorsque défini, cette liste est le placement (les keyframes connectés sont alignés dans l'ordre). Le dernier cadre est autorisé ; le cadre 0 ne l'est pas (il est déjà un token autonome). | STRING | Non | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | Conditionnement positif avec l'attention des keyframes générés attachée. | CONDITIONING |
| `negative` | Conditionnement négatif avec l'attention des keyframes générés attachée. | CONDITIONING |
| `latent` | Latent vidéo avec des keyframes générés ajoutés sur T. | LATENT |

## Notes

- Le paramètre `interval_frames` détermine l'espacement des keyframes dans la vidéo. Une valeur plus élevée entraîne moins de keyframes et une fréquence d'images inférieure.
- L'entrée `keyframes` vous permet d'initialiser les nouveaux keyframes avec des keyframes existants ou un latent vidéo. Si fourni, ces keyframes seront débruités et ajoutés au latent vidéo.
- Le paramètre `frame_indices` permet de spécifier les indices de cadre de pixels exacts où les keyframes doivent être placés. Si fourni, le paramètre `interval_frames` est ignoré.
- Les sorties `positive` et `negative` contiennent le conditionnement avec l'attention des keyframes générés attachée, ce qui peut être utilisé pour une traitement ou une analyse ultérieure.
- La sortie `latent` contient le latent vidéo avec des keyframes générés ajoutés sur T, ce qui peut être utilisé pour une traitement ou une analyse ultérieure.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGeneratedKeyframes/fr.md)

---
**Source fingerprint (SHA-256):** `43053d15eceb61f37223c46dd46417c71f0503ef3a412ee50a3b2f764f310a64`
