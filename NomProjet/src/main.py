# # # # # # nb: int = int(input("Entrez le nombre du dé: "))

# # # # # # match nb:
# # # # # #     case 1:
# # # # # #         print("Nope")
# # # # # #     case 2:
# # # # # #         print("nah")
# # # # # #     case 3:
# # # # # #         print ("Bof")
# # # # # #     case 4:
# # # # # #         print ("Bof")
# # # # # #     case 5:
# # # # # #         print("Nice")
# # # # # #     case 6:
# # # # # #         print("Parfait")

# # # # # # # Le case est majoritairement utilisé comme un elif pour de la répétition sous une même variable.


# # # # # total: int = 0

# # # # # for i in range(1, 5):
# # # # #     total = total + i

# # # # # print(total)

# # # # # #----------#


# # # # for i in range(10, 0, -2):
# # # #     print(i)

# # # # # 10 à 0 est le range, -2 étant le calcul à répéter pour s'y rendre

# # # for i in range(1, 15):
# # #     print(i)






# # nbLignes: int
# # etoiles: str = "*"

# # nbLignes = int(input("Combien de lignes?: "))

# # for i in range(nbLignes):
# #     print(etoiles)
# #     etoiles += "*"


# nb: int = 1
# resultat = ""

# while nb <= 10:
#     resultat += str(nb) + " - " if nb < 10 else ""
#     nb+=1

# print(resultat)


seuil: int = 1000
somme: int = 0
nb: int = 1

while somme < seuil:
    somme += nb
    nb += 1

print(somme)