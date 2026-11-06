#!/usr/bin/env python

from math import sqrt

#Exo 2
def est_pair(n: int):
    if n % 2 == 0:
        return True
    return False

#Exo3
def nombre_maxi(liste: list):
    if len(liste) == 0:
        return None
    if len(liste) == 1:
        return liste[0]
    x = liste[0]
    for n in liste[1:]:
        if n > x:
            x = n
    return x

#Exo4
def nombre_trier(liste: list):
    if len(liste) < 2:
        return liste
    on_a_permuter = True
    while on_a_permuter:
        on_a_permuter = False
        for i in range(len(liste) - 2):
            if liste[i] > liste[i+1]:
                permuter = liste[i]
                liste[i] = liste[i+1]
                liste[i+1] = permuter
                on_a_permuter = True
    return liste

#Exo5
def resoudre_premier_degre(a: float, b: float):
    if a == 0:
        if b != 0:
            print("Aucune solution")
        else:
            print("Une infinité de solutions")
    else:
        x = -b/a
        print(f"La solution est x = {x}")

def resoudre_second_degre(a: float, b: float, c: float):
    if a == 0:
        resoudre_premier_degre(b, c)
    else:
        delta = (b**2) - (4*a*c)
        if delta < 0:
            print("Aucune solution réelle")
        elif delta == 0:
            x0 = -b/(2*a)
            print(f"Une solution double : x0 = {x0}")
        else:
            x1 = (-b - sqrt(delta))/(2*a)
            x2 = (-b + sqrt(delta))/(2*a)
            print(f"Deux solutions : x1 = {x1} et x2 = {x2}")


if __name__ == "__main__":
    #Exercice 2
    """print("#Exercice 2")
    nombre = int(input("Saisir un nombre : "))
    print(est_pair(nombre))

    print()"""

    liste = [11]

    #Exercice 3
    print("#Exercice 3")
    print(nombre_maxi(liste))

    print()

    #Exercice 4
    print("#Exercice 4")
    print(nombre_trier(liste))

    print()

    #Exercice 5
    print("#Exercice 5")
    resoudre_premier_degre(4, 0)

    print()

    #Exercice 6
    print("#Exercice 6")
    resoudre_second_degre(-1, -4, -21)
