# 🧠 Exercice : Mot mystère
# Objectif : Faire deviner à l'utilisateur un mot choisi à l'avance.
# Pistes :
# - Crée une variable "mot_secret" avec le mot à deviner.
# - Utilise une boucle while tant que le mot n'est pas trouvé.
# - Donne un indice ou un message d'encouragement à chaque tentative.

import random

liste_mot = ["python", "robot", "algorithme", "ordinateur", "bug", "variable"]
mot = random.choice(liste_mot)
guess = ""

while guess != mot:
    guess = input("Devine le mot : ").lower()
    if guess == mot:
        print("Vous avez trouvez le mot mystère !")
    else:
        print("Raté ! Essaie encore")