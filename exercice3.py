# Note : un an = 52 semaines ou 365 jours ou 8760 heures ou 525600 minutes ou 31536000 secondes
def decomposer(secondes):
    secondes_par_annee = 365 * 24 * 60 * 60 # en secondes (nombres de secondes dans une année)
    secondes_par_semaine = 7 * 24 * 60 * 60 # en secondes (nombres de secondes dans une semaine)
    secondes_par_jour = 24 * 60 * 60 # en secondes (nombres de secondes dans un jour)
    secondes_par_heure = 60 * 60 # en secondes (nombres de secondes dans une heure)
    secondes_par_minute = 60 # en secondes (nombres de secondes dans une minute)
    # TODO: Assigner à la variable "annees" le nombre d'années
    secondes_en_annees = secondes / secondes_par_annee
    annees = int(secondes_en_annees)
    annees_en_secondes = annees*secondes_par_annee
    reste_annees = secondes - annees_en_secondes

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    secondes_en_semaines = reste_annees / secondes_par_semaine
    semaines = int(secondes_en_semaines)
    semaines_en_secondes = semaines*secondes_par_semaine
    reste_semaines = reste_annees - semaines_en_secondes

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    secondes_en_jours = reste_semaines / secondes_par_jour
    jours = int(secondes_en_jours)
    jours_en_secondes = jours*secondes_par_jour
    reste_jours = reste_semaines - jours_en_secondes

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    secondes_en_heures = reste_jours / secondes_par_heure
    heures = int(secondes_en_heures)
    heures_en_secondes = heures*secondes_par_heure
    reste_heures = reste_jours - heures_en_secondes

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    secondes_en_minutes = reste_heures / secondes_par_minute
    minutes = int(secondes_en_minutes)
    minutes_en_secondes = minutes*secondes_par_minute
    reste_minutes = reste_heures - minutes_en_secondes

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes2 = int(reste_minutes)



    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(f"{secondes} secondes converties en années, semaines, jours, heures, minutes et secondes donne : {annees} années, {semaines} semaines, {jours} jours,\n "
          f"{heures} heures, {minutes} minutes et {secondes2} secondes")

    return (annees ,semaines ,jours ,heures ,minutes ,secondes2)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))