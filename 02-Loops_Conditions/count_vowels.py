# 🧠 Exercice : Compter les voyelles
# Objectif : Demander une phrase et compter le nombre de voyelles (a, e, i, o, u).
# Pistes :
# - Parcours chaque caractère de la phrase.
# - Compare avec la liste ['a', 'e', 'i', 'o', 'u'].
# - Incrémente un compteur à chaque voyelle trouvée.

sentence = input("Enter a sentence: ")
vowels = "aeiouyAEIOUY"
counter = 0

for letter in sentence:
    if letter in vowels:
        counter += 1

print(counter)