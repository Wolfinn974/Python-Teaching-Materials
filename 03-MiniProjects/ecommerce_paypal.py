# 🧠 Mission 1 – E-commerce et PayPal 🛒
# Objectif : Calculer la commission PayPal et le montant final reçu par le vendeur.
# Détails :
# - Commission PayPal = 3.4% du prix + 0.35 €
# - Le montant final = prix - commission
# Exemple : si le produit coûte 50 €, combien touche le vendeur ?
# Pistes :
# - Utilise input() pour récupérer le prix.
# - Calcule la commission avec une simple formule mathématique.
# - Affiche le résultat arrondi à 2 décimales.

montant = float(input("Entrez le montant de la vente:"))
COMFIXE = 0.35

if (montant > 1):
    commission = COMFIXE + (montant * 0.034)
    reste = montant - commission
    print("la comission : ", commission)
    print("ce que le vendeur aura :", reste)
else :
    print("Le montant est trop petit")