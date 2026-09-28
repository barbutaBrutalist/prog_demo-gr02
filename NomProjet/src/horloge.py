import time
 
timestamp_secondes = int(time.time()-14400)

print(timestamp_secondes %60, " secondes") # Un modulo de 60 donne seulement les secondes.

print((timestamp_secondes //60) %60, " minutes") # diviser par 60 enlève les secondes, et on peut ensuite répeter la commande précédente pour les minutes.

print((timestamp_secondes // (60*60)) %24, " heures") # diviser par 60 fois 60 (qui donne une heure) donne la bonne heure, après avoir supprimer 14400 de l'heure de base