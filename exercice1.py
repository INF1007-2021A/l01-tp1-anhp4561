def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    if (n%3==0 and n%5==0):
        resultat = "fizzbuzz"
    elif (n%5==0):
        resultat = "buzz"
    elif (n%3==0):
        resultat = "fizz"
    else :
        resultat = f"{n} est ni fizz ni buzz"

    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
