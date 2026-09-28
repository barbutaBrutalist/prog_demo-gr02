# # # # a = 5
# # # # b = "chat"
# # # # c = 3.14

# # # # print(a, b, sep=" - ")
# # # # print(a, b, c, end=" FIN\n")
# # # # print(c)

# # # #--------------#

# # # # prix = 7
# # # # nom = "Alex"

# # # # print(f"{nom:>10}|")
# # # # print(f"{prix:05.2f}")
# # # # print(f"{prix:+d}")

# # # #-------------#

# # # # Entrez une température en Celsius: 22
# # # # Température en Fahrenheit: 71.6


# # # # celsius: float
# # # # fahrenheit: float

# # # # celsius = float (input ("Entrez la température en Celsius:"))
# # # # fahrenheit = (celsius * 9/5) + 32

# # # # print(f"Température en Fahrenheit: {fahrenheit:.1f}")


# # # #  	(50°C × 9/5) + 32 = F

# # # #-------------#
# # # # Numéro 4

# # # # Veuillez entrer une longueur: 10
# # # # Veuillez entrer une largeur: 10
# # # # C'est un carré
# # # # Aire de 100

# # # longueur: float
# # # largeur: float
# # # result: str = ""
# # # aire: float

# # # longueur = float (input("Entrez la longueur: "))
# # # largeur = float (input("Entrez la largeur: "))

# # # if largeur == longueur:
# # #     result = "carré"

# # # elif largeur != longueur:
# # #     result = "rectangle"

# # # else: print("Une erreur est survenue!") #ça sert à rien mais... je voulais mettre le != avant

# # # aire = longueur * largeur

# # # print(f"C'est un {result}.")
# # # print(f"Aire de {aire}")

# # #------------#

# # # Veuillez entrer un nombre de produits: 4
# # # Veuillez entrer un prix unitaire: 9.99

# # # Sous-total: 39.96
# # # TPS: 2.00
# # # TVQ: 3.99
# # # Total: 45.94

# # produits: int
# # prixUnitaire: float
# # sousTotal: float
# # prixTotal: float
# # tps: float
# # tvq: float

# # produits = int (input("Veuillez entrez un nombre de produits: "))
# # prixUnitaire = float (input("Entrez le prix unitaire: "))
# # sousTotal = produits * prixUnitaire

# # tps = sousTotal * 0.05
# # tvq = sousTotal * 0.09975

# # print(f"Sous-Total: {sousTotal:.2f} \nTPS: {tps:.2f} \nTVQ: {tvq:.2f} \nTotal: {sousTotal + tps + tvq:.2f}")

# #-------------#

# # Veuillez entrer la note #1: 75
# # Veuillez entrer la note #2: 92
# # Veuillez entrer la note #3: 41
# # Veuillez entrer la note #4: 60
# # Veuillez entrer la note #5: 88

# # La moyenne est de: 71.20%

# # moyenne: float

# # note1 = float (input("Entrez la première note: "))
# # note2 = float (input("Entrez la deuxième note: "))
# # note3 = float (input("Entrez la troisième note: "))
# # note4 = float (input("Entrez la quatrième note: "))
# # note5 = float (input("Entrez la cinqième note: "))

# # moyenne = (note1 + note2 + note3 + note4 + note5)/5

# # print(f"Moyenne: {moyenne:.2f}%")

# #------------#

# # Veuillez entrer un nombre: -5
# # Le nombre -5 est négatif et impair

# # Veuillez entrer un nombre: 42
# # Le nombre 42 est positif et pair


# even: str
# positif: str

# nombre = float (input("Entrez un nombre: "))

# if nombre < 0:
#     positif = "Négatif"
# elif nombre > 0:
#     positif = "Positif"
# else: positif = "Nul"

# if nombre % 2 == 0: # modulo de deux, donc s'il reste un nombre, ça veut dire que c'est impair
#     even = "Pair"
# else: even = "Impair"

# print(f"Votre nombre est {positif} et {even}.")


titre: str
prenom: str
nom: str
salutation: str

titre = input("Entrez le titre désiré (M,m,F,f,N,n): ")
prenom = input("Entrez le prénom: ")
nom = input("Entrez le nom: ")

match titre:
    case "M" | "m":
        salutation = "Bonjour monsieur"
    case "F" | "f":
        salutation = "Bonjour madame"
    case _:
        salutation = "Bonjour"

print(f"{salutation} {prenom} {nom}")