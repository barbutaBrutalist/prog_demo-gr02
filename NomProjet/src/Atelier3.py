# # # # age: int = 20
# # # # #12, 13, 15, 17, 20, 65, 70

# # # # if age < 13:
# # # #     print("\t- trop jeune pour créer un compte Facebook") #12

# # # # if age < 70:
# # # #     print("\t- trop jeune pour être le président des USA") #12, 13, 15, 17, 20, 65
# # # # else:
# # # #     print("\t- assez vieux pour être le président des USA") #70

# # # # if age < 16:
# # # #     print("\t- pas de permis de conduire") #12, 13, 15
# # # # elif age < 18:
# # # #     print("\t- permis de conduire avec accompagnateur") #17

# # # # if age < 13:
# # # #     print("\t- enfant") # 12
# # # # elif age < 18:
# # # #     print("\t- adolescent") # 12, 13, 15, 17
# # # # elif age < 65:
# # # #     print("\t- adulte") #20
# # # # else:
# # # #     print("\t- aîné") #65, 70

# # # #------------------------#

# # # heure: int = 14


# # # if heure >= 6 and heure < 12:
# # #     print("Bonjour")

# # # elif heure >= 12 and heure < 18:
# # #     print("Bon après-midi")

# # # elif heure >= 18 and heure < 22:
# # #     print("Bonsoir")

# # # else:
# # #     print("Bonne nuit")


# # # if not (heure >= 9 and heure < 17):
# # #     print("Le bureau est fermé")

# # # #idéalement sync les statements avec import.time, voir la page horloge.py
# # # #avec 14, ça serait bon après-midi. Dès que ça dit bonsoir, le bureau est fermé.


# # #---------------#

# # nombre: int = 0

# # if nombre > 0:
# #     print("Positif")
# # elif nombre < 0:
# #     print("Négatif")
# # elif nombre == 0:
# #     print("Zéro!")

# #-------------------#
# nombre: int = 6

# if nombre == 1:
#     print("Dimanche")
# elif nombre == 2:
#     print("Lundi")
# elif nombre == 3:
#     print("Mardi")
# elif nombre > 3 and nombre < 8:
#     print("Ça me tentait pas de continuer, mais valide")
# elif nombre >= 8:
#     print("Invalide! Nombre trop grand.")
# elif nombre <0:
#     print("Invalide! Nombre trop... négatif.")

ROCK: str = "r"
PAPER: str = "p"
SCISSORS: str = "s"
result: str

player1: str = ROCK
player2: str = SCISSORS

if player1 == player2:
    result = "DRAW!"
elif (player1 == ROCK and player2 == SCISSORS) or \
    (player1 == PAPER and player2 == ROCK) or \
    (player1 == SCISSORS and player2 == PAPER):
    result = "Player 1 wins!"
else:
    result = "Player 2 wins!"

print(result)