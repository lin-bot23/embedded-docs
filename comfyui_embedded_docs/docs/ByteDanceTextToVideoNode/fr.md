# ByteDance Texte vers Vidéo

# Nœud Texte vers Vidéo ByteDance

Le nœud Texte vers Vidéo ByteDance génère des vidéos à l'aide des modèles ByteDance via une API basée sur des prompts textuels. Il prend une description textuelle et divers réglages vidéo en entrée, puis crée une vidéo correspondant aux spécifications fournies. Le nœud gère la communication API et retourne la vidéo générée.

## Aperçu

Le nœud Texte vers Vidéo ByteDance est conçu pour convertir des prompts textuels en vidéos en utilisant les capacités IA de ByteDance. Les utilisateurs peuvent spécifier le modèle, la résolution, le ratio d'aspect, la durée et d'autres paramètres pour contrôler le processus de génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle ByteDance à utiliser pour la génération. | STRING | Oui | 
  - "seedance-1-5-pro-251215"
  - "seedance-1-0-pro-250528"
  - "seedance-1-0-pro-fast-251015" |
| `prompt` | Le prompt textuel utilisé pour générer la vidéo. | STRING | Oui | Entrée de texte multiligne |
| `resolution` | La résolution de la vidéo de sortie. | STRING | Oui | 
  - "480p"
  - "720p"
  - "1080p" |
| `aspect_ratio` | Le ratio d'aspect de la vidéo de sortie. | STRING | Oui | 
  - "16:9"
  - "4:3"
  - "1:1"
  - "3:4"
  - "9:16"
  - "21:9" |
| `duration` | La durée de la vidéo de sortie en secondes. | INT | Oui | 3 à 12 secondes |
| `seed` | Graine à utiliser pour la génération. | INT | Non | 0 à 2,147,483,647 |
| `camera_fixed` | Spécifie si la caméra doit être fixée. | BOOLEAN | Non | - |
| `filigrane` | Indique si un filigrane "Généré par IA" doit être ajouté à la vidéo. | BOOLEAN | Non | - |
| `générer_audio` | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215`. | BOOLEAN | Non | - |

**Contraintes des paramètres :**

- Le `prompt` doit contenir au moins 1 caractère après suppression des espaces.
- Le `prompt` ne peut pas contenir les paramètres textuels suivants : "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- La `duration` est limitée aux valeurs entre 3 et 12 secondes.
- Pour le modèle `seedance-1-5-pro-251215`, la durée minimale supportée est de 4 secondes.
- Le `seed` accepte des valeurs de 0 à 2,147,483,647.
- Le paramètre `generate_audio` ne prend effet que lorsque le `model` est réglé sur `seedance-1-5-pro-251215` ; il est ignoré pour tous les autres modèles.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | Le fichier vidéo généré. | VIDÉO |

**Note :** Le nœud Texte vers Vidéo ByteDance est un nœud API et nécessite des jetons d'authentification et des clés API pour fonctionner correctement. Ces éléments sont fournis via les entrées cachées `auth_token_comfy_org` et `api_key_comfy_org`.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`
