# OpenAI GPT Image 2

Ce nœud génère des images à l'aide de l'API GPT Image d'OpenAI. Il prend en charge cinq modèles — `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` et `gpt-image-1` — vous permet de joindre des images de référence pour l'édition d'images et peut utiliser un masque pour spécifier les parties d'une image à remplacer.

## Entrées

### Entrées communes

Ces entrées sont toujours visibles.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle OpenAI GPT Image à utiliser. La sélection d'un modèle révèle des paramètres supplémentaires spécifiques à ce modèle. | DYNAMIC_COMBO | Oui | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Invite de texte pour GPT Image (par défaut : `""`). | STRING | Oui | N/A |
| `n` | Nombre d'images à générer (par défaut : `1`). | INT | Oui | 1 à 8 |
| `graine` | Graine pour la reproductibilité (par défaut : `0`). Pas encore implémentée dans le backend. | INT | Oui | 0 à 2147483647 |

### Entrées gpt-image-2.5-flare et gpt-image-2.5-sunburst

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-2.5-flare` ou `gpt-image-2.5-sunburst`. Les deux modèles partagent le même ensemble de paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `taille` | Taille de l'image. Sélectionnez « Custom » pour utiliser la largeur et la hauteur personnalisées (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largeur_personnalisée` | Utilisé uniquement lorsque `model.size` est réglé sur « Custom ». Doit être un multiple de 16 (par défaut : `1024`). | INT | Non | 480 à 3840 (pas de 16) |
| `hauteur_personnalisée` | Utilisé uniquement lorsque `model.size` est réglé sur « Custom ». Doit être un multiple de 16 (par défaut : `1024`). | INT | Non | 480 à 3840 (pas de 16) |
| `arrière-plan` | Renvoie l'image avec ou sans arrière-plan (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualité` | Qualité de l'image ; affecte le coût et le temps de génération (par défaut : `"low"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Image(s) de référence facultative(s) pour l'édition d'images. Jusqu'à 16 images. Voir Entrées de référence pour plus de détails. | IMAGE | Non | 0 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

### Entrées gpt-image-2

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-2`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `taille` | Taille de l'image. Sélectionnez « Custom » pour utiliser la largeur et la hauteur personnalisées (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largeur_personnalisée` | Utilisé uniquement lorsque `model.size` est réglé sur « Custom ». Doit être un multiple de 16 (par défaut : `1024`). | INT | Non | 480 à 3840 (pas de 16) |
| `hauteur_personnalisée` | Utilisé uniquement lorsque `model.size` est réglé sur « Custom ». Doit être un multiple de 16 (par défaut : `1024`). | INT | Non | 480 à 3840 (pas de 16) |
| `arrière-plan` | Renvoie l'image avec ou sans arrière-plan (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"` |
| `qualité` | Qualité de l'image ; affecte le coût et le temps de génération (par défaut : `"low"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Image(s) de référence facultative(s) pour l'édition d'images. Jusqu'à 16 images. Voir Entrées de référence pour plus de détails. | IMAGE | Non | 0 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

### Entrées gpt-image-1.5 et gpt-image-1

Ces entrées apparaissent lorsque `model` est défini sur `gpt-image-1.5` ou `gpt-image-1`. Les deux modèles partagent le même ensemble de paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `taille` | Taille de l'image (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `arrière-plan` | Renvoie l'image avec ou sans arrière-plan (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualité` | Qualité de l'image ; affecte le coût et le temps de génération (par défaut : `"low"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Image(s) de référence facultative(s) pour l'édition d'images. Jusqu'à 16 images. Voir Entrées de référence pour plus de détails. | IMAGE | Non | 0 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.images` | Connecteur extensible : connectez 1..N éléments (p. ex. `image_1`...`image_16`) ; jusqu'à 16 images de référence pour tous les modèles. | IMAGE | Non | 1 à 16 |
| `model.mask` | Masque facultatif pour l'inpainting (les zones blanches seront remplacées). Nécessite exactement une image de référence. | MASK | Non | N/A |

**Contraintes et limites des paramètres :**

- Lorsque `model.size` est réglé sur « Custom » (`gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` et `gpt-image-2` uniquement), `model.custom_width` et `model.custom_height` doivent tous deux être des multiples de 16, le côté le plus long ne doit pas dépasser 3840, le rapport hauteur/largeur ne doit pas dépasser 3:1, et le nombre total de pixels doit être compris entre 655 360 et 8 294 400.
- `model.mask` nécessite exactement une image de référence dans `model.images` : il ne peut pas être utilisé sans image, ni avec plus d'une image.
- Lorsque `model.mask` est utilisé, sa hauteur et sa largeur doivent correspondre à la hauteur et à la largeur de l'image de référence.
- Lorsque `model.images` est fourni, le nœud fonctionne en mode édition d'image ; sans `model.images`, il génère des images à partir de la seule invite.
- La résolution des images de référence et du masque est réduite avant leur envoi à l'API.
- Les niveaux de qualité `"xhigh"` et `"max"` sont uniquement disponibles pour `gpt-image-2.5-flare` et `gpt-image-2.5-sunburst`.
- L'option d'arrière-plan `"transparent"` est disponible pour `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-1.5` et `gpt-image-1`, mais pas pour `gpt-image-2`.
- `seed` n'est actuellement pas implémenté dans le backend.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image ou les images générées. Toutes les images renvoyées sont empilées dans un seul lot ; si leurs dimensions diffèrent, elles sont redimensionnées pour correspondre à la première image. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `4f77b79f9f432a1f2e0fd814012aebe7cc42a8aa983ee9a61f3b32984bf65148`
