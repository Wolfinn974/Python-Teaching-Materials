# Exercice : Print alphabet
# Objectif : Afficher l'alphabet de a à z
# Astuces : utiliser range() et chr()

for i in range(97, 123): # 97 = a 122 = z
    print(chr(i))

# Exercice : Print alphabet inversé
# Objectif : Afficher l'alphabet de z à a
# Astuces : utiliser range() et chr() ou la fonction reversed()

for i in range(122, 96, -1): #descendant de 1 à chaque tour
    print(chr(i))