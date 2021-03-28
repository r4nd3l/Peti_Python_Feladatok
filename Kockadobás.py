import random

dobások = []
for _ in range(1000000):
    dobás = random.randint(1,6)
    dobások.append(dobás)

ennyi_hatos = 0
for dobás in dobások:
    if dobás == 6:
        ennyi_hatos += 1

print('Összesn', ennyi_hatos, 'hatost dobtunk.')