"""StockPilot : premier prototype en console, avec des données fictives."""


def creer_stock():
    return {
        "P001": {"nom": "Cahier", "quantite": 20, "seuil": 5},
        "P002": {"nom": "Stylo", "quantite": 8, "seuil": 3},
        "P003": {"nom": "Classeur", "quantite": 2, "seuil": 2},
    }


def afficher_stock(stock, alertes_seulement=False):
    print("\nID     Produit          Quantité  Seuil  État")
    trouve = False
    for identifiant, produit in stock.items():
        faible = produit["quantite"] <= produit["seuil"]
        if not alertes_seulement or faible:
            etat = "À commander" if faible else "Disponible"
            print(f'{identifiant:<7}{produit["nom"]:<17}{produit["quantite"]:<10}'
                  f'{produit["seuil"]:<7}{etat}')
            trouve = True
    if not trouve:
        print("Aucun produit à commander.")


def sortir_stock(stock, identifiant, saisie_quantite):
    """Refuse toute sortie invalide avant de modifier les données."""
    identifiant = identifiant.strip().upper()
    if identifiant not in stock:
        return False, "Produit inexistant."
    try:
        quantite = int(saisie_quantite)
    except ValueError:
        return False, "La quantité doit être un entier."
    if quantite <= 0:
        return False, "La quantité doit être supérieure à zéro."
    produit = stock[identifiant]
    if quantite > produit["quantite"]:
        return False, "Stock insuffisant : sortie refusée."
    produit["quantite"] -= quantite
    message = f'Sortie enregistrée. Stock restant : {produit["quantite"]}.'
    if produit["quantite"] <= produit["seuil"]:
        message += " Alerte : produit à commander."
    return True, message


def main():
    stock = creer_stock()
    while True:
        print("\nSTOCKPILOT - Soumission 1")
        print("1. Consulter le stock\n2. Enregistrer une sortie")
        print("3. Afficher les alertes\n0. Quitter")
        choix = input("Votre choix : ").strip()
        if choix == "1":
            afficher_stock(stock)
        elif choix == "2":
            identifiant = input("Identifiant du produit : ")
            quantite = input("Quantité à sortir : ")
            succes, message = sortir_stock(stock, identifiant, quantite)
            print(message)
        elif choix == "3":
            afficher_stock(stock, True)
        elif choix == "0":
            print("Au revoir. Les données de ce prototype ne sont pas sauvegardées.")
            break
        else:
            print("Choix invalide : saisir 0, 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nApplication fermée. Aucune sauvegarde dans ce prototype.")
