# MiniMax H3 Référence vers Vidéo

MiniMax H3 Reference to Video crée le conditionnement textuel et le latent audio-vidéo vide nécessaires à la génération reference-to-video de MiniMax H3. Vous fournissez une invite ainsi que des images, vidéos et clips audio de référence facultatifs, et le nœud encode ces références dans un conditionnement que le modèle peut utiliser lors de la génération. L'invite fait référence aux références avec les balises `<Picture i>`, `<Video k>` et `<Audio j>`.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP utilisé pour tokeniser l'invite et encoder les médias de référence en jetons de conditionnement. | CLIP | Oui | |
| `vae` | VAE vidéo utilisé pour encoder les images de référence et les frames des vidéos de référence. Sans lui, les images/vidéos de référence ne conditionnent que l'encodeur de texte. | VAE | Non | |
| `audio_vae` | VAE audio utilisé pour encoder l'audio de référence. L'audio est rééchantillonné au taux d'échantillonnage du VAE audio (32 kHz par défaut). Sans lui, l'audio de référence ne conditionne que l'encodeur de texte. | VAE | Non | |
| `invite` | Invite textuelle pour la vidéo. Les médias de référence peuvent être désignés avec les balises `<Picture i>`, `<Video k>` et `<Audio j>` (indexées à partir de 1 pour chaque type). Prend en charge les invites multilignes et dynamiques. | STRING | Oui | |
| `largeur` | Largeur de la vidéo générée en pixels (par défaut : 1344). | INT | Oui | 32 à 16384 (pas de 32) |
| `hauteur` | Hauteur de la vidéo générée en pixels (par défaut : 768). | INT | Oui | 32 à 16384 (pas de 32) |
| `longueur` | Nombre de frames à 24 fps ; 124 = ~5 s, la plage d'entraînement est d'environ 124-362 (par défaut : 124). | INT | Oui | 5 à 3600 (pas de 17) |
| `taille_image_référence` | Dimensionnement des images de référence. `match` réduit chaque image de référence uniquement, en conservant le ratio hauteur/largeur, à la zone en pixels de la génération ; `max` utilise le petit côté de 2048 px du pipeline de référence pour une meilleure fidélité de l'identité. Les jetons de référence traversent chaque étape d'échantillonnage, donc `max` peut être plusieurs fois plus lent (par défaut : `match`). | COMBO | Oui | `"match"`<br>`"max"` |
| `images_de_référence` | Emplacement extensible : connectez jusqu'à 9 images de référence (`ref_image_1` ... `ref_image_9`). Les images de référence sont réduites à un petit côté de 2048 px si elles sont plus grandes et ne sont jamais agrandies. | IMAGE | Non | 0 à 9 |
| `vidéos_de_référence` | Emplacement extensible : connectez jusqu'à 3 vidéos de référence (`ref_video_1` ... `ref_video_3`). Frames de vidéos de référence à 24 fps (2-15 s). | IMAGE | Non | 0 à 3 |
| `audios_vidéo_de_référence` | Emplacement extensible : connectez jusqu'à 3 bandes sonores (`ref_video_audio_1` ... `ref_video_audio_3`). Bande sonore de la vidéo de référence portant le même numéro. | AUDIO | Non | 0 à 3 |
| `audios_de_référence` | Emplacement extensible : connectez jusqu'à 3 clips audio de référence autonomes (`ref_audio_1` ... `ref_audio_3`). | AUDIO | Non | 0 à 3 |

Notes :

- L'invite fait référence aux médias de référence avec des balises indexées à partir de 1 par type : `<Picture i>` pour les images, `<Video k>` pour les vidéos et `<Audio j>` pour l'audio. Les références sont présentées au modèle dans un ordre fixe : les images, puis les vidéos (avec l'étiquette `<Audio j>` de chaque bande sonore juste avant sa `<Video k>`), puis l'audio autonome.
- Une bande sonore connectée à `ref_video_audio_N` est utilisée avec la vidéo de référence connectée à `ref_video_N`.
- Les vidéos de référence doivent contenir au moins 5 frames (~0,2 seconde à 24 fps), sinon le nœud lève une erreur. Les frames au-delà de la `length` demandée sont rognées, et le nombre de frames restant est ajusté à une valeur prise en charge par le modèle.
- La `length` demandée est alignée sur un nombre de frames pris en charge avant la création du latent.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `positif` | Conditionnement contenant l'invite encodée. Lorsque des médias de référence et les VAE correspondants sont fournis, il contient également le contenu encodé des images, vidéos et audios de référence utilisé par le modèle MiniMax H3. | CONDITIONING |
| `latent` | Latent audio-vidéo vide aux `width`, `height` et `length` (nombre de frames) demandés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
