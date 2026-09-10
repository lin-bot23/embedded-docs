# Superposer du texte

Ce nœud dessine du texte par-dessus une image ou un lot d'images. Il crée une superposition de texte avec une taille de police configurable, une couleur, une position verticale, un alignement horizontal et un contour noir facultatif, puis applique la superposition sur les images d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|----------------|--------|-------|
| `images` | L'image ou le lot d'images d'entrée sur lequel dessiner du texte | IMAGE | Oui | |
| `texte` | Texte à superposer sur l'image (défaut : ""). Prend en charge plusieurs lignes : les séquences d'échappement `\n` et `\t` sont converties en sauts de ligne et en tabulations, et les lignes longues sont automatiquement renvoyées à la ligne pour tenir dans la largeur de l'image. | STRING | Oui | |
| `taille_de_police` | Taille de police en pourcentage de la hauteur de l'image (défaut : 5.0) | FLOAT | Oui | 0.5 to 50.0 (step 0.5) |
| `couleur` | Couleur du texte (défaut : "#ffffff") | STRING | Oui | |
| `position` | Position verticale du texte sur l'image (défaut : "top") | COMBO | Oui | "top"<br>"bottom" |
| `alignement` | Alignement horizontal du texte (défaut : "left") | COMBO | Oui | "left"<br>"center"<br>"right" |
| `contour` | Dessine un contour noir autour du texte (défaut : True) | BOOLEAN | Oui | |

Remarque : si `text` est vide ou ne contient que des espaces, le nœud renvoie les images d'entrée inchangées. La superposition de texte est créée une seule fois, puis appliquée à chaque image du lot.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images d'entrée avec la superposition de texte appliquée par-dessus | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/fr.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
