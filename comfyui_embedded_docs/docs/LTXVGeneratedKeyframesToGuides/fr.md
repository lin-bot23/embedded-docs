# LTXVGeneratedKeyframesToGuides

## Aperçu

Le nœud LTXV Générés Clés à Guides fixe les clés générées à une étape précédente en tant que guides d'image figées sur un canevas ultérieur. Il décode les clés comme des images indépendantes, les redimensionne si nécessaire, et les écrit avec un masque de bruit à 0 pour éviter un débruitage supplémentaire. Les indices enregistrés sont étalonnés à partir du canevas où ils ont été générés vers le canevas cible, et vous pouvez remplacer les indices de cadre pour définir des positions explicitement.

## Entrées

| Paramètre                 | Description                                                                 | Type de données | Obligatoire | Gamme |
|---------------------------|-----------------------------------------------------------------------------|-----------------|--------------|-------|
| `positive`                | Conditionnement positif avec les clés fixées en tant que guides d'image.         | CONDITIONING    | Oui          |       |
| `negative`                | Conditionnement négatif avec les clés fixées en tant que guides d'image.         | CONDITIONING    | Oui          |       |
| `vae`                     | Le modèle VAE à utiliser pour décoder les clés.                               | MODEL           | Oui          |       |
| `latent`                  | La vidéo latente cible auxquelles ajouter les guides, par exemple, la version temporellement agrandie. | LATENT         | Oui          |       |
| `keyframes`               | Les clés en sortie de LTXV Séparer Générés Clés, qui contient l'index de cadre pixelique à chaque clé générée. | LATENT         | Oui          |       |
| `strength`                | Force du guide. 1.0 est un fixation rigide ; les valeurs inférieures le relâchent. | FLOAT           | Oui          | 0.0 - 10.0 |
| `override_frame_indices` | Optionnel — fixer à ces cadres pixeliques au lieu des positions enregistrées (ou étalonnées) automatiquement. Fournir un index par clé. Laisser vide pour réutiliser les positions enregistrées ou les étaler si nécessaire. | STRING          | Non          |       |

## Sorties

| Nom de sortie | Description                                                                 | Type de données |
|---------------|-----------------------------------------------------------------------------|-----------------|
| `positive`    | Conditionnement positif avec les clés fixées en tant que guides d'image.         | CONDITIONING    |
| `negative`    | Conditionnement négatif avec les clés fixées en tant que guides d'image.         | CONDITIONING    |
| `latent`      | Vidéo latente cible avec les clés ajoutées en tant que guides figés.               | LATENT          |

## Notes

- Le paramètre `strength` contrôle la force avec laquelle les clés sont fixées en tant que guides. Une valeur de 1.0 crée une fixation rigide, tandis que les valeurs inférieures la relâchent.
- Le paramètre `override_frame_indices` permet de spécifier les cadres pixeliques exacts où les clés doivent être fixées. Si laissé vide, le nœud utilisera les positions enregistrées ou les étalonnera si nécessaire.
- Le nœud suppose que la latente `keyframes` contient l'index de cadre pixelique pour chaque clé. Si ce n'est pas le cas, le nœud lèvera une `ValueError`.
- Le nœud ne prend en charge qu'une taille de lot de 1. Chaque guide est codé à partir d'une image, donc il ne peut pas différer entre les éléments du lot.
- Le nœud lèvera une `ValueError` si le tenseur `samples` dans l'entrée `latent` n'est pas un tenseur 5D ou si la taille de lot n'est pas de 1.
- Le nœud lèvera une `ValueError` si le tenseur `samples` dans l'entrée `keyframes` n'est pas un tenseur 5D ou si la taille de lot n'est pas de 1.
- Le nœud lèvera une `ValueError` si la forme du tenseur `samples` dans l'entrée `keyframes` ne correspond pas à la forme du tenseur `samples` dans l'entrée `latent` après redimensionnement.
- Le nœud lèvera une `ValueError` si le paramètre `strength` est en dehors de la gamme de 0.0 à 10.0.
- Le nœud lèvera une `ValueError` si le paramètre `override_frame_indices` n'est pas une liste de nombres entiers séparés par des virgules ou si le nombre d'indices ne correspond pas au nombre de clés.
- Le nœud lèvera une `ValueError` si l'un des indices dans le paramètre `override_frame_indices` est en dehors de la gamme de 1 à la nombre de cadres pixeliques dans le canevas cible.
- Le nœud lèvera une `ValueError` si l'index maximal dans le paramètre `override_frame_indices` est supérieur au nombre de cadres pixeliques dans le canevas cible.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/fr.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
