# LTXVAddGuide

```markdown
# Guide de LTXVAddGuide

Le nœud LTXVAddGuide est conçu pour ajouter une guidance de conditionnement vidéo aux séquences latentes en encodant des images ou des vidéos d'entrée et en intégrant les clés de frame dans les données de conditionnement. Il traite l'entrée à travers un encodeur VAE et place stratégiquement les latents obtenus à des positions de frame spécifiées tout en mettant à jour à la fois le conditionnement positif et négatif avec des informations de clé de frame. Le nœud gère les contraintes d'alignement de frame et permet de contrôler la force de l'influence de conditionnement.

## Aperçu

Le nœud LTXVAddGuide encode des images ou des vidéos d'entrée, les traite à travers un encodeur VAE et utilise les latents encodés pour conditionner une séquence vidéo latente. Il permet de spécifier un index de frame pour commencer le conditionnement et ajuste la force de l'influence de conditionnement. Le nœud prend également en charge des masques spatiaux optionnels pour chaque région de l'influence de conditionnement et peut gérer les paramètres IC-LoRA pour des ajustements de traitement de guide spécifiques.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrée de conditionnement positif à modifier avec la guidance de clé de frame | CONDITIONING | Oui | - |
| `négatif` | Entrée de conditionnement négatif à modifier avec la guidance de clé de frame | CONDITIONING | Oui | - |
| `vae` | Modèle VAE utilisé pour l'encodage des frames d'image ou de vidéo | VAE | Oui | - |
| `latent` | Séquence latente d'entrée qui recevra les frames de conditionnement | LATENT | Oui | - |
| `image` | Image ou vidéo à conditionner sur la séquence vidéo latente. Doit avoir 8*n + 1 frames. Si la vidéo n'a pas 8*n + 1 frames, elle sera rognée à la frame la plus proche de 8*n + 1. | IMAGE | Oui | - |
| `indice_de_l'image` | Index de frame pour commencer le conditionnement. Pour des images ou des vidéos avec 1-8 frames, tout valeur de frame_idx est acceptable. Pour des vidéos avec 9+ frames, frame_idx doit être divisible par 8, sinon il sera rogné à la valeur la plus proche multiple de 8. Les valeurs négatives sont comptées à partir de la fin de la vidéo. (par défaut : 0) | INT | Oui | -9999 à 9999 |
| `force` | Force de l'influence de conditionnement, où 1.0 applique un conditionnement complet et 0.0 applique aucun conditionnement (par défaut : 1.0) | FLOAT | Oui | 0.0 à 10.0 |
| `attention_mask` | Masque spatial optionnel pour chaque région. Contrôle l'influence de conditionnement par région via l'attention auto, multiplié par la force. | MASK | Non | - |
| `iclora_parameters` | Paramètres IC-LoRA optionnels d'un nœud Get IC-LoRA Parameters. Utilisés pour ajuster le traitement de guide selon les besoins de certains IC-LoRAs (par exemple, ceux avec un reference_downscale_factor > 1). Lors de la chaîne, chaque LTXVAddGuide utilise uniquement les paramètres connectés à lui. | IC_LORA_PARAMETERS | Non | - |

**Note:** L'image ou la vidéo d'entrée doit avoir un nombre de frames suivant le schéma 8*n + 1 (par exemple, 1, 9, 17, 25 frames). Si l'entrée dépasse ce schéma, elle sera automatiquement rognée à la frame la plus proche de ce schéma valide.

**Note sur `iclora_parameters`:** Lorsque des paramètres IC-LoRA avec un `reference_downscale_factor` supérieur à 1 sont utilisés, les dimensions spatiales latentes (largeur et hauteur) doivent être divisibles par ce facteur. Le nœud lève une erreur si cette condition n'est pas remplie.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `positive` | Conditionnement positif mis à jour avec des informations de guidance de clé de frame | CONDITIONING |
| `négatif` | Conditionnement négatif mis à jour avec des informations de guidance de clé de frame | CONDITIONING |
| `latent` | Séquence latente avec des frames de conditionnement intégrées et un masque de bruit mis à jour | LATENT |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddGuide/fr.md)

---
**Source fingerprint (SHA-256):** `031bc9030dafed85b5ff1cbceae36234e9d5f77f7f4b040267067ecd16a27929`
