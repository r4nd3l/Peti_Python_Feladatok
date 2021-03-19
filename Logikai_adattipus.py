import random

gondolt_szám = random.randint(1,6)
kitalálta = False
számláló = 0
while not kitalálta and számláló < 3:
    tipp = int(input('Szerinted?'))
    számláló +=1
    if tipp == gondolt_szám:
        kitalálta = True