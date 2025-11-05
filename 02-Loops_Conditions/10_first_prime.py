# 🧠 Exercice : Les 10 premiers nombres premiers
# Objectif : Afficher les 10 premiers nombres premiers.
# Pistes :
# - Utilise une boucle pour tester les nombres.
# - Crée une fonction is_prime() pour vérifier si un nombre est premier.
# - Arrête-toi après en avoir trouvé 10.

def is_prime(num):#fonction qui retourne vrai ou faux selon si le nombre est premier ou non
    for i in range(2, num ):
        if num % i == 0:
            return False
    return True

a = 2
c = 0
while c < 10:
    if is_prime(a) == True:
        print(a)
        c += 1
    a +=1