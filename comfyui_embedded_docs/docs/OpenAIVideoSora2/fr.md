# OpenAI Sora - Vidéo

Le nœud OpenAIVideoSora2 génère des vidéos à l'aide des modèles Sora d'OpenAI. Il crée du contenu vidéo à partir d'un texte d'invite et d'une image de référence d'entrée facultative, puis fournit la vidéo générée comme sortie. Le nœud prend en charge différentes durées et résolutions vidéo selon le modèle sélectionné.

**AVIS D'OBSOLESCENCE :** OpenAI cessera de fournir l'API Sora v2 en septembre 2026. Ce nœud sera retiré de ComfyUI à ce moment-là.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle OpenAI Sora à utiliser pour la génération vidéo (défaut : "sora-2") | COMBO | Oui | "sora-2"<br>"sora-2-pro" |
| `prompt` | Texte d'orientation ; peut être vide si une image d'entrée est présente (défaut : vide) | STRING | Oui | - |
| `size` | La résolution de la vidéo générée (défaut : "1280x720") | COMBO | Oui | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" |
| `duration` | La durée de la vidéo générée en secondes (défaut : 8) | COMBO | Oui | 4<br>8<br>12 |
| `image` | Image de référence d'entrée facultative utilisée pour la génération vidéo (référence de tenue, de personnage, de scène, etc.) ; une seule image est prise en charge | IMAGE | Non | - |
| `seed` | Valeur seed pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la valeur seed (défaut : 0) | INT | Non | 0 à 2147483647 |

**Contraintes et limites :**

- Le modèle « sora-2 » ne prend en charge que les résolutions « 720x1280 » et « 1280x720 » ; les options « 1024x1792 » et « 1792x1024 » ne sont valides qu'avec le modèle « sora-2-pro »
- Lorsqu'une image est connectée, elle doit contenir exactement une image ; la connexion de plus d'une image génère une erreur
- Les résultats sont non déterministes quelle que soit la valeur seed

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré par OpenAI Sora | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/fr.md)

---
**Source fingerprint (SHA-256):** `d19eb6b65d7f712278828e4b1f7105068cc5e7cb72813b7549ab24520e7719fc`
