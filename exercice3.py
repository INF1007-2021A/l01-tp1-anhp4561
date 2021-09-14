# Note : un an = 52 semaines ou 365 jours ou 8760 heures ou 525600 minutes ou 31536000 secondes
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    secondes_en_annees = secondes / 31536000 # en secondes
    annees = secondes_en_annees//1
    reste_annees = secondes_en_annees%1

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    annees_en_semaines = (reste_annees * 52)+1/7 # en semaines
    semaines = annees_en_semaines//1
    reste_semaines = annees_en_semaines%1

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    semaines_en_jours = reste_semaines * 7 # en jours
    jours = semaines_en_jours//1
    reste_jours = semaines_en_jours%1

    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    jours_en_heures = reste_jours * 24 # en heures
    heures = jours_en_heures//1
    reste_heures = jours_en_heures%1

    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    heures_en_minutes = reste_heures * 60 # en minutes
    minutes = heures_en_minutes//1
    reste_minutes = heures_en_minutes%1

    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = reste_minutes * 60 # en secondes



    # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    print(f"{annees} années ,{semaines} semaines ,{jours} jours ,{heures} heures ,{minutes} minutes et {secondes} secondes")

    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
