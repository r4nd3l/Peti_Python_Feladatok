autók = ['Trabant', 'T-Modell', 'Rolls-Royce']

while len (autók) > 0:
    print('Kölcsönözhető:', ', '.join(autók))
    mit = input('Melyik autót kölcsönzi ki? ')
    if mit in autók:
        autók.remove(mit)
    else:
         print('Ilyen autóval nem szolgálhatunk.')