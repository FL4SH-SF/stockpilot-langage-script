# Comprendre et présenter StockPilot

## Le besoin en 30 secondes
StockPilot aide les employés d'une petite boutique à consulter les quantités,
enregistrer une sortie et repérer les produits à commander. Une sortie invalide
est refusée sans changer les données. Le prototype utilise des produits fictifs.

## Les fonctions
| Fonction | Rôle |
|---|---|
| creer_stock | Retourner les trois produits fictifs de départ. |
| afficher_stock | Parcourir les produits et afficher tous les produits ou seulement les alertes. |
| sortir_stock | Valider une sortie, modifier le stock uniquement si elle est valide et retourner un résultat. |
| main | Afficher le menu en boucle et appeler la fonction correspondant au choix. |

## Pourquoi un dictionnaire ?
Chaque produit possède un identifiant : P001, P002 ou P003. L'identifiant permet
l'accès au produit ; son dictionnaire contient le nom, la quantité et le seuil.
`stock["P001"]["quantite"]` désigne la quantité du produit P001.

## Pourquoi valider avant de soustraire ?
Un produit inconnu, une saisie non entière, une quantité <= 0 ou une sortie supérieure
au stock doivent être refusés. La soustraction arrive seulement après ces vérifications.
Tous les refus retournent False et un message ; une sortie acceptée retourne True
et une confirmation. Le menu affiche le message.

## À quoi sert try / except ValueError ?
`int("abc")` ne peut pas produire un entier. Python déclenche ValueError.
Le programme intercepte précisément cette erreur pour répondre sans planter.
Une quantité décimale comme "2.5" est également refusée : les stocks sont comptés en unités.

## Quand apparaît une alerte ?
Quand quantité <= seuil. Avec 20 cahiers et un seuil de 5, une sortie de 15
laisse exactement 5 unités et déclenche l'alerte. Une sortie de 20 est permise
et laisse zéro unité ; une sortie de 21 est refusée.

## Pourquoi chaque test crée un stock neuf ?
Pour que le résultat d'un scénario ne dépende pas du précédent.
Les assertions vérifient les résultats. Une assertion qui échoue interrompt
le script avec une erreur : il faut alors chercher et corriger la cause.
Ne pas lancer les tests avec l'option Python -O, qui désactive les assertions.

## Limites à expliquer
Les données sont gardées en mémoire et sont réinitialisées à chaque lancement.
L'ajout de produits, les entrées, l'historique et la sauvegarde sont prévus pour
la soumission 2. Il ne s'agit pas d'un système commercial terminé.

## Démonstration
Suivre le scénario du README, puis essayer "abc" et une quantité négative.
Les trois membres devraient pouvoir refaire la démonstration et expliquer
les conditions, la boucle, le dictionnaire et le traitement d'une erreur.

## Petites modifications à savoir faire
- Modifier la quantité initiale d'un produit dans creer_stock.
- Modifier un seuil, puis constater le changement dans les alertes.
- Ajouter un produit fictif au dictionnaire initial.
Si les données initiales des tests changent, adapter aussi les résultats attendus.
