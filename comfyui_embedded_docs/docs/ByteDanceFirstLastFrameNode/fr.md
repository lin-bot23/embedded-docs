# ByteDance Première-Dernière Image vers Vidéo

Ce nœud génère une vidéo à partir d’un prompt textuel ainsi que d’images de première et de dernière frame. Il utilise votre description et les deux images clés pour créer une séquence vidéo complète qui effectue une transition entre elles. Le nœud offre différentes options permettant de contrôler la résolution, le rapport hauteur/largeur, la durée et d’autres paramètres de génération de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle utilisé pour la génération vidéo (défaut : `"seedance-1-5-pro-251215"`). | COMBO | Oui | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `invite` | Le prompt textuel utilisé pour générer la vidéo. Ne doit pas être vide. | STRING | Oui | - |
| `première_image` | Première frame à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0.4 et 2.5. | IMAGE | Oui | - |
| `dernière_image` | Dernière frame à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0.4 et 2.5. | IMAGE | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio_d'aspect` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `durée` | La durée de la vidéo de sortie en secondes. Lorsque vous utilisez `seedance-1-5-pro-251215`, la durée minimale est de 4 secondes. (défaut : 5) | INT | Oui | 3 - 12 |
| `graine` | Graine (seed) à utiliser pour la génération. (défaut : 0) | INT | Non | 0 - 2147483647 |
| `camera_fixed` | Spécifie si la caméra doit être fixe. La plateforme ajoute une instruction pour fixer la caméra à votre prompt, mais ne garantit pas l’effet réel. (défaut : False) | BOOLEAN | Non | - |
| `watermark` | Indique si un filigrane « AI generated » doit être ajouté à la vidéo. (défaut : False) | BOOLEAN | Non | - |
| `générer_audio` | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215`. (défaut : False) | BOOLEAN | Non | - |

**Remarque :** Pour le modèle `seedance-1-5-pro-251215`, `duration` doit être d’au moins 4 secondes. `first_frame` et `last_frame` doivent tous deux être compris entre 300x300 et 6000x6000 pixels et avoir un rapport hauteur/largeur compris entre 0.4 et 2.5.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
