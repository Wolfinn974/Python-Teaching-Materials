# 🧠 Exercice : Mini calculatrice
# Objectif : Créer une calculatrice simple qui additionne, soustrait, multiplie ou divise deux nombres.
# Pistes :
# - Demande deux nombres et une opération (+, -, *, /).
# - Utilise if / elif / else pour déterminer le calcul à faire.
# - Gère les erreurs comme la division par zéro avec try / except.

test = True

while test:
    print("a. addition")
    print("b. soustraction")
    print("c. multiplication")
    print("d. division")
    print("q. quitter")
    choice = input("Enter your choice: ")
    match choice:
        case "a":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a + b
            print(result)
        case "b":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a - b
            print(result)
        case "c":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = a * b
            print(result)
        case "d":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0 :
                print("division impossible")
            else:
                result = a / b
                print(result)
        case "q":
            test = False
        case _:
            print("invalid choice")