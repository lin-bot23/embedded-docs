# Superposer du texte

Ce nœud dessine du texte sur une image ou un lot d'images. Il crée une superposition de texte avec une taille de police, une couleur, une position, un alignement et un contour optionnel personnalisables, puis composite le texte sur les images originales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L'image ou le lot d'images d'entrée sur lequel dessiner le texte | IMAGE | Oui | |
| `texte` | Le texte à superposer sur l'image (par défaut : ""). Prend en charge plusieurs lignes ; les séquences d'échappement `\n` et `\t` sont converties en sauts de ligne et tabulations, et le texte est automatiquement renvoyé à la ligne pour tenir dans la largeur de l'image. | STRING | Oui | |
| `taille_de_police` | Taille de la police en pourcentage de la hauteur de l'image (par défaut : 5.0) | FLOAT | Oui | 0.5 à 50.0 (pas de 0.5) |
| `couleur` | Couleur du texte (par défaut : "#ffffff") | STRING | Oui | |
| `position` | Position verticale du texte sur l'image (par défaut : "top") | COMBO | Oui | `"top"`<br>`"bottom"` |
| `alignement` | Alignement horizontal du texte (par défaut : "left") | COMBO | Oui | `"left"`<br>`"center"`<br>`"right"` |
| `contour` | Dessiner un contour noir autour du texte (par défaut : True) | BOOLEAN | Oui | |
Remarque : si `text` est vide ou ne contient que des espaces, le nœud renvoie les images d'entrée inchangées. La même superposition de texte est appliquée à chaque image du lot. Pour les images avec un canal alpha (RGBA), le texte est composé avec un mélange alpha source-over, de sorte que la transparence existante est respectée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images d'entrée avec la superposition de texte composite dessus | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/fr.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
