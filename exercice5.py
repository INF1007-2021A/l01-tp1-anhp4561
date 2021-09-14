def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    temps = distance/(v1+v2) # en unité de temps
    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"

    positionRencontre = temps * v1

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance),"unités de distance de la position initiale du véhicule 1")
