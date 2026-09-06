# ByteDance Image en vidéo

# Nœud Image à Vidéo de ByteDance

Le nœud Image à Vidéo de ByteDance génère une vidéo à partir d'une image d'entrée et d'un texte d'indication en utilisant l'API de ByteDance. Il crée une séquence vidéo qui représente visuellement la description fournie, avec des options pour personnaliser la résolution, le rapport d'aspect, la durée et d'autres paramètres de la sortie.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Le modèle ByteDance à utiliser pour la génération de vidéo. Les options disponibles sont : <br>`"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` | STRING | Oui | Comme listé ci-dessus |
| `prompt` | Le texte d'indication utilisé pour générer la vidéo. Doit contenir au moins 1 caractère après l'élimination des espaces. | STRING | Oui | - |
| `image` | La première image à utiliser pour la vidéo. L'image doit être entre 300x300 et 6000x6000 pixels, avec un rapport d'aspect entre 0,4 et 2,5. | IMAGE | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. Les options disponibles sont : <br>`"480p"`<br>`"720p"`<br>`"1080p"` | STRING | Oui | Comme listé ci-dessus |
| `ratio_d'aspect` | Le rapport d'aspect de la vidéo de sortie. Les options disponibles sont : <br>`"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | STRING | Oui | Comme listé ci-dessus |
| `durée` | La durée de la vidéo de sortie en secondes. Pour le modèle `seedance-1-5-pro-251215`, la durée minimale supportée est de 4 secondes. | INT | Oui | 3 - 12 |
| `graine` | Grain à utiliser pour la génération. Optionnel, avec une valeur par défaut de 0. | INT | Non | 0 - 2147483647 |
| `caméra_fixe` | Spécifie si la caméra doit être fixée. La plateforme ajoute une instruction pour fixer la caméra à votre indication, mais ne garantit pas l'effet réel. Optionnel, avec une valeur par défaut de False. | BOOLEAN | Non | - |
| `filigrane` | Si ajouter une marque d'eau "Généré par l'IA" à la vidéo. Optionnel, avec une valeur par défaut de False. | BOOLEAN | Non | - |
| `générer_audio` | Ce paramètre est ignoré pour tout modèle sauf `seedance-1-5-pro-251215`. Optionnel, avec une valeur par défaut de False. | BOOLEAN | Non | - |

**Note :** L'indication ne doit pas contenir les mots suivants (sensibilité aux majuscules et minuscules) : `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Ces paramètres sont définis via leurs entrées dédiées.

## Sorties

| Nom de la sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | Le fichier vidéo généré sur la base de l'image d'entrée et des paramètres de l'indication. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `9f4ad18642533689f9c664f2ca6a4ce8e92c8698754cdf9b6bb2d2735bc80415`
