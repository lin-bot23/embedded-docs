# Mélanger les paires Vidéo-Texte

Ce nœud mélange aléatoirement l’ordre des paires vidéo-texte dans une liste, en conservant chaque vidéo appariée avec son texte correspondant. Il prend deux listes de même longueur et applique la même permutation aléatoire aux deux, garantissant que les appariements d’origine sont préservés après le mélange. Une valeur de seed contrôle l’ordre du mélange afin que les résultats soient reproductibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `videos` | Liste des vidéos à mélanger. | VIDEO | Oui | Liste de vidéos |
| `texts` | Liste des textes à mélanger (les légendes appariées avec les vidéos). | STRING | Oui | Liste de chaînes de caractères |
| `seed` | Seed aléatoire qui détermine l’ordre du mélange (par défaut : 0). | INT | Oui | 0 à 18446744073709551615 |

Remarque : `videos` et `texts` doivent avoir la même longueur, car le nœud associe chaque vidéo au texte situé à la même position et préserve ces appariements lors du mélange. En interne, la valeur de `seed` est réduite modulo 4294967295 (2^32 - 1) avant que l’ordre aléatoire ne soit généré ; des valeurs de seed très grandes peuvent donc produire le même mélange que des valeurs plus petites.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `videos` | Vidéos mélangées dans le nouvel ordre aléatoire. | VIDEO |
| `texts` | Textes mélangés dans le même nouvel ordre que les vidéos. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoTextDataset/fr.md)

---
**Source fingerprint (SHA-256):** `834305718cd53a86211363750e887ffccdb54bc3b628dc17f049e546c234f9cb`
