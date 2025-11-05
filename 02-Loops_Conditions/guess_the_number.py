# 🧠 Exercice : Guess the Number Game 🎲
# Objectif : Faire deviner à l'utilisateur un nombre choisi aléatoirement entre 1 et 100.
# Pistes :
# - Utilise la librairie random pour générer le nombre secret.
# - Utilise une boucle while jusqu'à ce que la réponse soit correcte.
# - Indique "Trop petit !" ou "Trop grand !" selon le cas.

import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 100: "))
    score = 0

    if guess == num:
        print("congratulations! you won! your score is :", score)
        break
    elif guess > num:
        print("+ petit")
        score += 1
    elif guess < num:
        print("plus grand")
        score += 1