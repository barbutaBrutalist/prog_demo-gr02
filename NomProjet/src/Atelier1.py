#1
    -18.0 #.0 non nécéssaire, peut être un int
    123 #int
    -10 #int
    007 #syntaxe invalide. mettre un 0 demande une autre valeur après, mettre un autre 0 ne fait aucun sens.
    3.012 #float
    .5 #float, manque 0
    0.123 #float
    2 #int
    3. #int, manque une décimale pour faire un float | Python le prends comme un float car il attend une décimale, mais c'est une mauvaise pratique
    3,442 #techniquement un int..? avec le standard américain au moins. Un typo, c'est un point à la place d'une virgule
    vrai #rien, il faut que ce soit en anglais pour faire un bool
    True #bool
    true #minuscule, bool raté
    False #bool
    'Allo' #string avec une commande manquante
    "'" #string dans un string..?
    "il fait "CHAUD"" #string avec syntaxe invalide, une paire de guillemets de trop | Ou mettre un différent type de guillemet. \"x\" fonctionne aussi.
    1_048_323 #int | Le underscore fait en sorte que ce soit plus lisible pour un humain. Mettre un espace plante le programme. 
    1.23E-24  #float
    0b101 #valeur pour 5, donc int | 0 avec un b après indique que c'est binaire
    0x1A5 #valeur pour 421, donc int | 0 avec un x après indique que c'est hexadécimal.
    # Une commande qui commence avec 0 est un changement de base.
#2
    Vous achetez un café à 3.50$. # Café=String, 3.50=float

    Au restaurant vous commandez pour 50$, vous donnez 5% de pourboire, quel est le total? #3.50=float, 5=int | Pourcentage est idéalement un float, juste le convertir en décimales

    Vous commandez un gâteau au chocolat, glacage rose et sans écriture. #gâteau au chocolat typeDessert=string, chocolat saveur=string, glaçage rose glacage=string, écriture=string OU bool
    L ordinateur possède un processeur i9, 16 Go de ram ainsi que 1 To de SSD. #i9=string, 16=int

    Je m appel Philippe Girard, mon DA est 1234567, je suis étudiant en informatique. #1234567=int, étudiant en informatique=string

    J ai roulé 100 km avec ma Nissan Versa, ça m a couté 42.32$ d essence. Par chance elle n est pas tombé en panne #100=int, Nissan Versa=String, 42.32=float

    Le colis de 2.3 kg a été expédié à l adresse 452 rue des Érables, avec le numéro de suivi 004829. Il est arrivé endommagé après 3 jours. #2.3=float, adresse=string, 004829=string, vu que ça commence avec des zéros, 3=int
#3
    2eNote #variable ne peux pas commencer avec un chiffre
    mon-age #monAge serait la bonne syntaxe
    for #reservé
    classe #oui
    numéroDeCompte #oui | éviter accents hors des commentaires
    mon age #Non, Espace
    nomComplet #Oui
    p #oui, mais trop vague
    True #non, reservé
    int #non, reservé
    _age #non, mauvaise syntaxe
    age2024 #oui
    mon.age #non, mauvaise syntaxe
    NomDeFamille #oui
    donnee #oui, mais trop vague
    print #non, reservé
#4
    nom: str             # Jean Peuplu # Vrai
    2eMembre: str        # 00452 # FAUX, devrait être un int, nombre plein. Un string ne peut pas commencer avec un nombre, donc faux dans deux sens. | Erreur, commence avec 00, dont string
    prixAbonnement: str  # 89.99$ # FAUX, devrait être un float, (float pour les calculs?) et enlever le $
    carteVIP: str        # a une carte VIP # Ça dépend. Y a-t-il plusieurs types de carte? Si oui, vrai. Est-ce que la carte VIP est la seule? Faux, la valeur est booléène.
    Entraineur: str      # Jules # Mauvaise syntaxe, devrait être entraineur. Commencer toujours avec un miniscule, suivi d'une majuscule pour d'autre mots
    nb_visites: int      # 3 fois par semaine # Mauvais syntaxe, contient un underscore, devrait être nbVisites