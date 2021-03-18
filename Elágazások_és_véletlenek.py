import random

egyik = random.randint(1,10)
másik = random.randint(1,10)
egyik_szövegként = str(egyik)
másik_szövegként = str(másik)
tipp = input('Mennyi' + egyik_szövegként + ' és ' + másik_szövegként + ' összege? ')
tipp = int(tipp)
öszzeg = egyik + másik
if tipp == összeg:
    print('Valóban annyi, ez igen!')