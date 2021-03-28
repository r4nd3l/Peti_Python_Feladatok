kacatok = []

kacat = ''
while kacat != 'elfogyott':
        kacat = input ('Kérek egy kacatot! ')
        if kacat != 'elfogyott':
             kacatok.append(kacat)

kacatok_felsorolva = ', '.join(kacatok)
print('A kacatjaim: ', kacatok_felsorolva, '.', sep='')