# 🧠 Exercice : Nombre positif ou négatif
# Objectif : Demander un nombre à l'utilisateur et indiquer s'il est positif, négatif ou nul.
# Pistes :
# - Utilise input() pour récupérer un nombre.
# - Compare avec 0 en utilisant if / elif / else.

number = int(input("Entre un nombre: "))

if number > 0:
    print(number, "est positif.")
elif number < 0:
    print(number, "est negatif.")
else:
    print("Le nombre est nul.")