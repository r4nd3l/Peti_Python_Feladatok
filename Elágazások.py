gondolt_szám = 4
tipp = input('Gondoltam egy számra. Tippeld meg! ')
tipp = int(tipp)
if tipp == gondolt_szám:
    print('Ügyes!')
    print('Gratulálok.')
elif tipp == gondolt_szám + 1 or tipp == gondolt_szám - 1:
    print('Ó, csak eggyel tévedtél.')
else:
    print('Hosszan gondolkodtál rajta? ')
    print('Nem érte meg.')
print('Pápá.')