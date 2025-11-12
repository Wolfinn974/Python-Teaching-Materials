# 🧠 Mission 2 – Convertisseur de devises 💶➡️💵
# Objectif : Convertir un montant d'euros en dollars.
# Détails :
# - Taux de conversion : 1 € = 1.07 $
# Pistes :
# - Utilise input() pour demander un montant.
# - Multiplie par 1.07 et affiche le résultat.


montant = float(input("montant a convertir :"))

def conv (x):
    rate = 1.07
    convert = x * rate
    print(x,"en dollars est :", convert)

conv(montant)
