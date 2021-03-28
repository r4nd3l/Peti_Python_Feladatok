versenyzők = []

versenyző = None
while versenyző != '':
    print('A versenyzők jelenleg:', ','.join(versenyzők))
    versenyző = input('Kérek egy versenyzőt! ')
    if versenyző != '':
        versenyzők.append(versenyző)

print('Az első helyezett: ', versenyzők[0])
print('Az második helyezett: ', versenyzők[1])
print('A harmedik helyezett: ', versenyzők[2])
print('A sereghajtó: ', versenyzők[-1])