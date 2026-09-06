# ByteDance Première-Dernière Image vers Vidéo

# ByteDance First-Last-Frame to Video

Ce nœud génère une vidéo en utilisant un texte d'invite ainsi que les premières et dernières images d'une image. Il crée une transition fluide entre les deux images, resulting in a complete video sequence. Le nœud offre une gamme d'options pour personnaliser la résolution, le ratio d'aspect, la durée et les paramètres de génération supplémentaires de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Gamme |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Le modèle à utiliser pour la génération de vidéo. Sélectionnez parmi les options disponibles (par défaut: `"seedance-1-5-pro-251215"`). | COMBO | Oui | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `invite` | Le texte d'invite utilisé pour la génération de la vidéo. Cet invite ne doit pas contenir de paramètres spécifiques tels que la résolution, le ratio, la durée, le seed, camerafixed ou watermark. | STRING | Oui | - |
| `première_image` | La première image à utiliser pour la vidéo. L'image doit être entre 300x300 et 6000x6000 pixels et avoir un ratio d'aspect entre 0.4 et 2.5. | IMAGE | Oui | - |
| `dernière_image` | La dernière image à utiliser pour la vidéo. L'image doit être entre 300x300 et 6000x6000 pixels et avoir un ratio d'aspect entre 0.4 et 2.5. | IMAGE | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. Choisissez parmi les options disponibles (par défaut: `"480p"`). | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio_d'aspect` | Le ratio d'aspect de la vidéo de sortie. Sélectionnez parmi les options disponibles (par défaut: `"adaptive"`). | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut: 5). Pour le modèle `seedance-1-5-pro-251215`, la durée minimale supportée est de 4 secondes. | INT | Oui | 3 - 12 |
| `graine` | Le seed à utiliser pour la génération (par défaut: 0). Ce paramètre est optionnel. | INT | Non | 0 - 2147483647 |
| `camera_fixed` | Détermine si la caméra doit être fixée dans la vidéo. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais l'effet réel n'est pas garanti (par défaut: False). | BOOLEAN | Non | - |
| `watermark` | Détermine si un filigrane "Généré par l'IA" doit être ajouté à la vidéo (par défaut: False). | BOOLEAN | Non | - |
| `générer_audio` | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215` (par défaut: False). | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | Le fichier vidéo généré. | VIDEO |

## Notes

- Le paramètre `model` détermine les capacités et les limites du processus de génération de vidéo.
- L'invite `prompt` doit être créative et claire, car elle guidera la génération de la vidéo.
- Les images `first_frame` et `last_frame` doivent être représentatives du contenu de la vidéo souhaitée.
- Les paramètres `resolution` et `aspect_ratio` affecteront la qualité et les dimensions finales de la vidéo de sortie.
- Le paramètre `duration` définit la longueur de la vidéo, avec un minimum de 3 secondes et un maximum de 12 secondes.
- Le paramètre `seed` est optionnel et peut être utilisé pour la répétabilité du processus de génération de vidéo.
- Le paramètre `camera_fixed` est une option avancée qui peut ne pas toujours donner l'effet attendu.
- Le paramètre `watermark` peut être utilisé pour ajouter un filigrane à la vidéo, indiquant qu'elle a été générée par une IA.
- Le paramètre `generate_audio` est actuellement ignoré pour tous les modèles sauf `seedance-1-5-pro-251215`.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
