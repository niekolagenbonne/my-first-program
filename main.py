from multiprocessing import Condition


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        print("merci de votre reponse!")
        print()
        try:
            age_int = int(age_str)
        except:
            print("Erreur: Vous devez rentrer un nombre pour l'age")
        return age_int

def afficher_information_personne(nom, age, taille=0):
    print("-------------------------")
    print("-Vous vous appelez: " + nom + " et vous avez: " + str(age) + " ans")
    print()
    print("-L'an prochain vous aurez " + str(age + 1) + " ans")
    print()

    Condition = age >= 18 
    if age == 17:
        print("-Vous êtes presque majeur")
    elif 12<= age < 18:
        print("-Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("-Vous êtes un bebe")
    elif age == 18:
        print("-Tout juste majeur : félicitation!!")
    elif age > 60:
        print ("-Vous êtes sénior")
    elif age < 10:
         print("-Vous êtes enfant")
    elif Condition:
        print("-Vous êtes majeur")
    else:
        print("-Vous êtes mineur")
   
    #afficher la taille de la personne
    if not taille == 0:
        print()
        print("-Votre taille: " + str(taille) + "m")


    print("-------------------------")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
        print("merci de votre reponse!")
        print()
    return reponse_nom

#demander nom
#nom1 = demander_nom()

#nom2 = demander_nom()
#nom1 = "nieko1"
#nom2 = "nieko2"
######demander l'age
#age1 = demander_age(nom1)
#age2 = demander_age(nom2)
#age1 = 9
#age2 = 65

#######afficher les resultats:
#afficher_information_personne(nom1, age1)
#afficher_information_personne(nom2, age2)

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i + 1)
    age = demander_age(nom)
    afficher_information_personne(nom, age, 0.80)




