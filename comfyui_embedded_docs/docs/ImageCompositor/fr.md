# Créer une image en couches

Ce nœud combine plusieurs calques d’image en une seule image composite. Il prend une pile de calques construite avec le nœud Add Layer et applique, le cas échéant, les paramètres de composition enregistrés depuis l’éditeur de composition, en fusionnant les calques selon leur position, leur taille, leur rotation, leur opacité et leur mode de fusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `layers` | Pile de calques à composer ; construisez-la avec Add Layer. Les éléments sont empilés par z_index, les images d’un lot à l’intérieur d’un élément se déploient en calques consécutifs, et la position, l’opacité et le mode de fusion de l’élément définissent la composition initiale. Sans canevas de document explicite, la taille correspond à une étendue maximale estimée des calques placés. Une composition enregistrée qui correspond aux entrées actuelles est prioritaire. | LAYERS | Oui | Maximum 50 calques |
| `compositor` | Composition en calques enregistrée par l’éditeur de composition. | COMPOSITOR | Non | None |

**Remarques sur les contraintes :**

- La pile de calques prend en charge un maximum de 50 calques (images déployées) ; en fournir davantage provoque une erreur.
- Seuls les calques raster sont actuellement pris en charge ; les autres types d’éléments de calque provoquent une erreur.
- La version du document `layers` doit être 1 ; les autres versions provoquent une erreur.
- L’état `compositor` enregistré n’est réappliqué que si les empreintes d’entrée enregistrées correspondent à la pile de calques actuelle. Si elles ne correspondent pas, le nœud revient à une composition basée sur les propriétés des calques et marque l’état enregistré comme périmé.
- L’opacité des calques est bornée à la plage de 0.0 à 1.0.
- Le positionnement horizontal/vertical des calques (`x`, `y`) est borné à la limite de résolution maximale.
- La largeur et la hauteur des calques reviennent à la taille naturelle de l’image lorsqu’elles sont définies à zéro ou moins, et sont plafonnées à la limite de résolution maximale.
- La taille du canevas composé ne doit pas dépasser la limite de résolution maximale.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Image composite. Comporte un canal alpha lorsque la composition présente des zones transparentes (par ex. un arrière-plan masqué), sinon RVB pur. | IMAGE |
| `MASK` | Transparence de la composition (1 = transparence totale). Toutes les valeurs sont nulles lorsque la composition est opaque. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/fr.md)

---
**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`
