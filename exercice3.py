# Note : un an = 52 semaines ou 365 jours ou 8760 heures ou 525600 minutes ou 31536000 secondes
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    secondes_en_annees = secondes / 31536000 # en secondes
    annees = secondes_en_annees//1
    annees_en_secondes = annees*31536000
    reste_annees = secondes - annees_en_secondes

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    #annees_en_semaines = reste_annees * 52 # en semaines
    secondes_en_semaines = reste_annees / 604800 # en secondes
    semaines = secondes_en_semaines//1
    semaines_en_secondes = semaines*604800
    reste_semaines = reste_annees - semaines_en_secondes

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    #semaines_en_jours = reste_semaines * 7 # en jours
    secondes_en_jours = reste_semaines / 86400 # en secondes
    jours = secondes_en_jours//1
    jours_en_secondes = jours*86400
    reste_jours = reste_semaines - jours_en_secondes

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    #jours_en_heures = reste_jours * 24 # en heures
    secondes_en_heures = reste_jours / 3600 # en secondes
    heures = secondes_en_heures//1
    heures_en_secondes = heures*3600
    reste_heures = reste_jours - heures_en_secondes

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    #heures_en_minutes = reste_heures * 60 # en minutes
    secondes_en_minutes = reste_heures / 60 # en secondes
    minutes = secondes_en_minutes//1
    minutes_en_secondes = minutes*60
    reste_minutes = reste_heures - minutes_en_secondes

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = reste_minutes



    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(f"{annees} années ,{semaines} semaines ,{jours} jours ,{heures} heures ,{minutes} minutes et {secondes} secondes")

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))