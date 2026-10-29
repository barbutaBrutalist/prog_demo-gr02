import random
import time

ANSI_RESET: str = "\u001B[0m"
ANSI_RED: str = "\u001B[31m"
ANSI_BLUE: str = "\u001B[34m"
ANSI_GREEN: str = "\u001B[32m"

mise: int = 5

def lancerDe() -> int:
    """
    lance un dé qui roule de 1 à 6.
    retourne le résultat.
    """
    return random.randint(1,6)

def aDepasse(score) -> bool:
    """
    reçoit un score. si le score dépasse 11, retourne vrai. sinon, faux.
    retourne la valeur vraie ou fausse du "bust".
    """
    bust: bool = False
    
    if score > 11:
        bust = True
    return bust

def validerActionJoueur() -> str:
    """
    regarde si la réponse de l'utilisateur. si rien, relance le dé. si R, rester.
    n'importe quoi d'autre, montre une erreur et demande encore.
    """
    verifReponse: bool = True
    actionJoueur: str = ""
    
    while verifReponse:
        reponse: str = (input("Voulez-vouz relancer [Entrer], ou rester [R]?: "))
        reponse = reponse.lower()

        match reponse: 
            case "r":
                verifReponse = False
                actionJoueur = "Rester"
            case "":
                verifReponse = False
                actionJoueur = "Relancer"
            case _: print("Une erreure est survenue!") 
    return actionJoueur

def tourJoueur() -> int:
    """
    gère et calcule le tour du joueur.
    retourne le score final.
    """
    enjeu: bool = True
    score: int = 0

    while enjeu:
        print() # saute une ligne pour le rendre beau. chaque saut de ligne vide sera pour cette raison.
        print(f"Votre score: {score}")
        action = validerActionJoueur()
        if action == "Relancer":
            resultat = lancerDe()
            print(f"Vous avez lancé un {resultat}.")
            score += resultat
            bust = aDepasse(score)
            if bust: 
                enjeu = False
        elif action == "Rester":
            enjeu = False
    
    
    return score

def tourCroupier() -> int:
    """
    fait lancer le croupier automatiquement tant que son score est inférieur à 9, affiche chaque lancer.
    retourne le score final.
    un delai est ajouté pour un effet dynamique.
    retourne le score final du croupier.
    """
    score: int = 0
    
    print()    
    print("Tour du croupier...")
    while score < 9:
        time.sleep(0.2)
        resultat = lancerDe()
        score += resultat
        print(f"Le croupier a lancé un {resultat}. Score du croupier: {score}")

    print("Le croupier s'arrête.")
    return score

def afficherResultatManche(scoreJoueur, scoreCroupier, mise) -> str:
    """
    reçoit le score du joueur, du croupier et le montant de la mise.
    retourne et affiche le message de fin de manche, incluant les scores et l'effet sur la mise.
    """
    print()
    print(f"Votre score: {scoreJoueur} | Score du croupier: {scoreCroupier}")
    if scoreJoueur > 11:
        print(f"{ANSI_RED}Vous avez dépassé 11! Vous perdez la manche. (-{mise}$){ANSI_RESET}")
    elif scoreCroupier > 11:
        print(f"{ANSI_BLUE}Le croupier a dépassé 11! Vous gagnez la manche. (+{mise}$){ANSI_RESET}")
    elif scoreJoueur > scoreCroupier:
        print(f"{ANSI_BLUE}Vous gagnez la manche! (+{mise}$){ANSI_RESET}")
    elif scoreCroupier > scoreJoueur:
        print(f"{ANSI_RED}Le croupier gagne la manche. (-{mise}$){ANSI_RESET}")
    else: print("Égalité! Aucun changement à votre argent.")

def determinerResultat(scoreJoueur, scoreCroupier) -> int:
    """
    reçoit le score du joueur et croupier. 
    retourne 1 en cas de victoire du joueur, -1 en cas de défaite, 0 en cas d'égalité.
    """
    resultat: int

    if scoreJoueur > 11:
        resultat = -1
    elif scoreCroupier > 11:
        resultat = 1
    elif scoreJoueur > scoreCroupier:
        resultat = 1
    elif scoreJoueur < scoreCroupier:
        resultat = -1
    else: resultat = 0

    return resultat

def validerRejouer() -> bool:
    """
    demande au joueur s'il veut rejouer une manche.
    valide la saisie et retourne vrai ou faux.
    """
    verifReponse: bool = True
    choix: bool
    
    while verifReponse:
        print()
        reponse: str = (input("Voulez-vous rejouer? [Oui: o, Non: n]: "))
        reponse = reponse.lower()
        match reponse:
            case "o":
                choix = True
                verifReponse = False
            case "n":
                choix = False
                verifReponse = False
            case _: print("Une erreur est survenue!")
    return choix

def calculerTauxVictoire(victoires, manches) -> str:
    """
    reçoit le nombre de victoires et le nombre de manches jouées.
    retourne le pourcentage de victoire arrondi à 2 décimales.
    """
    return f"{round(victoires/manches * 100, 2)}%"

def afficherStatistiques(manches, victoires, defaites, egalites) -> None:
    """
    reçoit le nombre de manches jouées, victoires et défaites.
    calcule et affiche le résumé final.
    """
    print("--- Statistiques de la partie ---")
    print(f"Manches jouées: {manches}")
    print(f"Victoires: {victoires}")
    print(f"Défaites: {defaites}")
    print(f"Égalités: {egalites}")
    print(f"Taux de victoire: {calculerTauxVictoire(victoires, manches)}")

def jeu() -> None:
    """
    a boucle principale du jeu. la plus compliquée aussi..
    retourne rien, c'est la boucle.
    """
    boucleDeJeu: bool = True
    argent: int = 15
    victoires: int = 0
    defaites: int = 0
    egalites: int = 0
    manches: int = 0
    

    while boucleDeJeu:
        scoreJoueur: int = 0
        scoreCroupier: int = 0

        print(f"Argent: {argent}$ | Mise: {mise}$")
        scoreJoueur = tourJoueur()
        if scoreJoueur < 12:
            scoreCroupier = tourCroupier()
        else: scoreCroupier = "-"  # si le joueur a bust, le code n'a pas besoin d'éxécuter le tour du croupier, donc son score indique "-"
        afficherResultatManche(scoreJoueur, scoreCroupier, mise)
        resultat = determinerResultat(scoreJoueur, scoreCroupier)
        manches += 1
        match resultat: 
            case 1:
                victoires += 1
                argent += mise
            case -1:
                defaites += 1
                argent -= mise
            case 0:
                egalites += 1
        if argent == 0:
            print()
            print("Fin de la partie! Défaite, aucun argent restant.")
            afficherStatistiques(manches, victoires, defaites, egalites)
            valider = validerRejouer()
            if valider:
                argent = 15 # la boucle recommence en resettant l'argent.
                victoires = 0
                defaites = 0
                egalites = 0
                manches = 0
            else: boucleDeJeu = False
        
        elif argent == 30: 
            print()
            print("Fin de la partie! Victoire!")
            afficherStatistiques(manches, victoires, defaites, egalites)
            
            valider = validerRejouer()
            if valider:
                argent = 15 # la boucle recommence en resettant tout.
                victoires = 0
                defaites = 0
                egalites = 0
                manches = 0                
            else: boucleDeJeu = False

        
jeu()
