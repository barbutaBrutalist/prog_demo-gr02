d: float = 1 / 3
i1: int = 10
i2: int = 100
i3: int = 1000
i4: int = 100

i1 * i1 # 100
i1 * d # 3.3333...
i1 + d # 10.3333...4
i1 / 0 # division par 0
i2 % 3 # 1 
i3 % 100 # 0
i4 - 100.0 # 0.0
i1 / 3 # 3.3333...5
i1 // 3 # 3

#-------------#

x: int = 5
y: int = 10

(x > 0) and (y > 0) # both true
(x > y) and (y == 10) # false
(x == 0) or (y == 0) # false
(x == 0) or (y == 10) # true
(x > 0) or (y > 0) # true
not(x > 0) # false
not not(y != 0) # true
not(x >= 0 and x <= 10) # False 
((x % 10 == 5) or (y % 10 == 0)) and (x + y > 100) # False
(x % 10 == 5) or (y % 10 == 0) and (x + y > 100) # False | True ??? à cause des paranthèses

#---------------#

nb1: int = 5
nb2: float = 2.5
nb3: int
test: bool = False
texte: str = "AB"
code: int = 3

nb1 + 4 % nb1 * 3 - 6 # 11, int
nb1 % 2 % 2 / 2 # 5, int
nb1 % 2 % 2 / 2.0
(nb2 / 2.5) == 1.0
test or (nb2 == (nb1 / 2))
nb1 / 2
nb1 / 2.5
nb1 + texte
(nb1 * 3 % 3) == 3
1 / (nb1 + nb2)
1 / (nb1 + 2)
(nb1 / nb2) != (nb1 / 2)
(nb1 > 2) and (nb1 < 5)
test or (nb1 == 5) and (nb2 > 2)
nb1 / code
nb2 - test
nb3 - 1
nbl / 5
5 % 2 * 7 + 6 / 2
(5 % 2 * 7 + 6) / 2
-nb1 % 2
nb1 / 5

#--------------#

# Transformer 72°F en °C

tempC: float
tempF: 72

tempC = (tempF - 32) * 5/9

print:(tempC)