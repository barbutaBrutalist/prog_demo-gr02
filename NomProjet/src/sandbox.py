import random

def lancerDe() -> int:
    """
    Lance un dé qui roule un nombre de 1 à 6 aléatoirement
    """
    return random.randint(1, 6)

def aDepasse() -> bool:
    """
    Reçoit un score. Si le score dépasse 11, retourne vrai. Sinon, faux.
    """
    if score > 11: 
        return True
    else: return False

def validerActionJoueur() -> str:
    """
    regarde si la réponse de l'utilisateur sera rien, un R (minuscule ou non), ou quelque chose d'autre.
    si rien, relancer le dé.
    si R, rester.
    quoique ce soit d'autre, erreur, et répéter.
    """
    

    reponse = False    
        
    while reponse == False:
        reponse: str = (input("Voulez vous continuer à rouler (Entrez), ou rester? (R): "))
        reponse.lower()
        
        if reponse == "r":
            reponse = True
        elif reponse == "":
            reponse = True
        else: print("Réponse invalide! Souhaitez-vous continuer à rouler? (Enter pour continuer, R pour rester): ")

    
    reponse.lower()

validerActionJoueur()
# def tourJoueur()



# def tourCroupier()



# def afficherResultatManche()



# def determinerResultat()



# def validerRejouer()



# def calculerTauxVictoire()



# def afficherStatistiques()


# aDepasse


# Reçoit un score, retourne vrai si le score dépasse 11, faux sinon.

# Tests :

#     Avec 10, donne False
#     Avec 11, donne False
#     Avec 12, donne True
