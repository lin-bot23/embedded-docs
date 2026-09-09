# LTXVAddLatentGuide

## Aperçu

Le nœud LTXV Add Latent Guide fixe un latent déjà encodé comme guide, permettant d'utiliser un guide provenant d'une étape précédente plutôt qu'une image. Ce nœud évite le voyage d'encodage/décodage du VAE et peut dilater un guide spatialement plus petit sur une grille rare pour couvrir le canevas cible.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrée de conditionnement positive. | CONDITIONING | Oui | N/A |
| `negative` | Entrée de conditionnement négative. | CONDITIONING | Oui | N/A |
| `vae` | Le modèle VAE à utiliser. | MODEL | Oui | N/A |
| `latent` | Latent vidéo cible sur lequel le guide est fixé. | LATENT | Oui | N/A |
| `guiding_latent` | Latent guide. Sa taille spatiale doit diviser la taille du cible par le même nombre entier sur les deux axes ; une taille égale le fixe tel quel, une moitié de taille est traitée comme une référence IC-LoRA x2. | LATENT | Oui | N/A |
| `latent_idx` | Index de trame latent pour commencer le guide, compté en trames latentes plutôt qu'en trames pixel. Les valeurs négatives placent le guide sur des trames avant le début du latent, non comptées à partir de sa fin. | INT | Oui | -9999 à 9999 |
| `strength` | Limité à 1.0. Un guide dilaté marque ses positions de remplissage avec un masque de débruit négatif afin que le modèle les ignore ; au-delà de 1.0, les positions conservées deviendraient négatives et tout le guide serait ignoré. Amplifiez au-delà de 1.0 à l'aide de attention_mask. | FLOAT | Oui | 0.0 à 1.0, pas 0.01 |
| `attention_mask` | Masque spatial optionnel en espace pixel. Contrôle l'influence de conditionnement par région via l'auto-attention, multiplié par la force. | MASK | Non | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | Sortie de conditionnement positive. | CONDITIONING |
| `negative` | Sortie de conditionnement négative. | CONDITIONING |
| `latent` | Sortie latente avec le guide appliqué. | LATENT |

## Notes

- La taille spatiale du `guiding_latent` doit diviser la taille `latent` par le même nombre entier sur les deux axes.
- Le paramètre `latent_idx` permet de placer précisément le guide au sein des trames latentes.
- Le paramètre `strength` contrôle l'intensité du guide, avec des valeurs au-delà de 1.0 nécessitant l'utilisation de `attention_mask` pour éviter des positions négatives.
- Le paramètre `attention_mask` est optionnel mais peut être utilisé pour affiner l'influence du guide dans des régions spécifiques de l'image.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/fr.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
