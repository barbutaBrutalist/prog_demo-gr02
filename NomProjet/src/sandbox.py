# # taille: int = 5
# # tourX: bool = True
# # damier: str = ""

# # for i in range(taille):
# #     for j in range(taille):
# #         if tourX:
# #             print("X", end="")
# #         else:  
# #             print("O", end="")
# #         tourX = not tourX
# #     damier += "\n"

# # print(damier, end="")



# import random

# die: int = 0
# points: int = 1
# continuer: bool = True
# reponseContinuer: str

# while die != 1 and continuer:
#     die = random.randint(1, 6)
#     if die == 6:
#         points *= 2
#     else: points += 1
#     print(f"Résultat du dé: ", die, "\nPoints total: ", points)
#     if die != 1:
#         reponseContinuer = input("Voulez-vous continuer? O/N ")
#         continuer = reponseContinuer == "O" or reponseContinuer == "o"

# if die == 1:
#     print(f"Partie Perdue! Points final: {points}")


#print des chiffres de 1 à 10 une à une

i: int = 1

while i <= 11:
    print(i)
    i += 1