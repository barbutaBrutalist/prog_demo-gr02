# calcuer un tarrif de stationnement, 12$ par heure, dès que l'heure est au dessus de 3, le tarif descend à 0.5 du prix.
# utiliser 5 heures et 12$

def tarifStationnement(tarif: float, temps: int) -> float:
    facture: float = 0
    
    for i in range(temps):
        if i > 3:
            tarif += tarif * 0.5
        else: facture += tarif
    
    
    
    return facture


print(tarifStationnement(12, 5))
