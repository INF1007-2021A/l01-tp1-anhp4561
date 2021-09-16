import math


def resoudreEquation(a = 0, b = 0, c = 0):
    # TODO: Calculer le discriminant et assigner la valeur
    #  dans la variable "delta"
    delta = float(b**2-4*a*c)
    # TODO: Déterminer la condition (bool) qui correspond à aucune solution
    #  de l'équation et mettre la valeur dans la variable "naPasDeSolution"
    if delta > int(0):
        naPasDeSolution = False
    elif delta < int(0):  # ces ligne de code seront executé si il y'a aucune racine
        # TODO: afficher sur l'écran "Aucune racine"
        naPasDeSolution = True
        print("Aucune racine")
        # ne pas modifier
        return None

    # TODO: Déterminer la condition (bool) qui correspond
    #  à une unique solution de l'équation et mettre la
    #  valeur dans "aUneSeuleSolution"
    aUneSeuleSolution = False
    if delta == 0:
        aUneSeuleSolution = True
    if aUneSeuleSolution == True:  # ces ligne de code seront executé si il y'a une seule racine
        # TODO: afficher sur l'écran "Une seule racine"
        print("Une seule racine")
        # TODO: assigner a la variable x1 la valeur de la racine
        x1 = (-b + delta ** (1/2))/(2*a)
        # ne pas modifier
        return x1

    # TODO: Déterminer la condition (bool) qui correspond à deux solutions
    #  de l'équation et mettre la valeur dans "aDeuxSolutions"
    aDeuxSolutions = False
    if delta > 0:
        aDeuxSolutions = True
    if aDeuxSolutions == True:
        # TODO: afficher sur l'écran "Deux racines"
        print("Deux racines")
        # TODO: calculer la premiere racine, assigner la a "x1"
        x1 = (-b + delta ** (1/2))/(2*a)
        # TODO: calculer la deuxieme racine, assigner la a "x2"
        x2 = (-b - delta**(1/2))/(2*a)
        # ne pas modifier cette ligne
        return x1, x2

if __name__ == '__main__':
    a = int(input("Entrez a, non nul: "))
    b = int(input("Entrez b: "))
    c = int(input("Entrez c: "))

    print(resoudreEquation(a, b, c))
