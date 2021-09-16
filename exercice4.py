import math
#Note: km/h = 1000 m / 3600 s

def calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    vitesse_I = vitesseInitiale*(5/18) # en m/s
    vitesse_F = vitesseFinale*(5/18) # en m/s
    acceleration = (vitesse_F-vitesse_I)/ duree
    delta_x = (vitesse_I*duree)+(1/2 * acceleration * math.pow(duree,2))
    # TODO calculer la position finale, assigner la valeur à la variable "positionFinale"
    positionFinale = positionInitiale + delta_x

    return positionFinale

if __name__ == '__main__':
    positionInitiale = int(input("Entrez la position initiale en mètre: "))
    vitesseInitiale = int(input("Entrez la vitesse initiale en km/h: "))
    duree = int(input("Entrez la duree en secondes: "))
    vitesseFinale = int(input("Entrez la vitesse finale en km/h: "))
    print("La position finale est",calculerPosition(positionInitiale, vitesseInitiale, duree, vitesseFinale),"m")
