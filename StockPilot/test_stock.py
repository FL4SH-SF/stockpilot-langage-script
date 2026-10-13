"""Tests reproductibles : chaque scénario utilise un stock neuf."""
from main import creer_stock, sortir_stock

CAS = [
    ("T01", "Normal", "P001", "4", True, 16, "Sortie enregistrée. Stock restant : 16."),
    ("T02", "Limite : stock épuisé", "P001", "20", True, 0, "Sortie enregistrée. Stock restant : 0. Alerte : produit à commander."),
    ("T03", "Limite : seuil atteint", "P001", "15", True, 5, "Sortie enregistrée. Stock restant : 5. Alerte : produit à commander."),
    ("T04", "Invalide : stock insuffisant", "P001", "21", False, 20, "Stock insuffisant : sortie refusée."),
    ("T05", "Invalide : zéro", "P001", "0", False, 20, "La quantité doit être supérieure à zéro."),
    ("T06", "Invalide : négatif", "P001", "-2", False, 20, "La quantité doit être supérieure à zéro."),
    ("T07", "Invalide : texte", "P001", "abc", False, 20, "La quantité doit être un entier."),
    ("T08", "Invalide : décimal", "P001", "2.5", False, 20, "La quantité doit être un entier."),
    ("T09", "Invalide : produit absent", "P999", "2", False, 20, "Produit inexistant."),
    ("T10", "Normal : espaces et minuscules", " p001 ", " 4 ", True, 16, "Sortie enregistrée. Stock restant : 16."),
    ("T11", "Invalide : saisie vide", "P001", "", False, 20, "La quantité doit être un entier."),
]


def executer_tests():
    for code, nature, identifiant, saisie, succes_attendu, restant, message_attendu in CAS:
        stock = creer_stock()
        avant = creer_stock()
        succes, message = sortir_stock(stock, identifiant, saisie)
        assert succes == succes_attendu, code
        assert stock["P001"]["quantite"] == restant, code
        assert message == message_attendu, code
        assert stock["P002"] == avant["P002"], code
        assert stock["P003"] == avant["P003"], code
        if not succes:
            assert stock == avant, f"{code} : un refus a modifié le stock"
        print(f"{code} | {nature} | stock P001={restant} | {message} | RÉUSSI")
    print(f"\n{len(CAS)}/{len(CAS)} tests réussis.")


if __name__ == "__main__":
    executer_tests()
