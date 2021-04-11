import random
import numpy as np

kiugrálások = []
# nyolcvanelemű, -5 és 3 közötti egész számokból álló lista
for _ in np.arange(-5, 3, 0.1):
    ugrás = random.choice(['vízfelszínen úszik', 'víz alatt úszik'])
    kiugrálások.append(ugrás)

print('A kiugrálások:', ', '.join(kiugrálások))

merülés = 0
for index, ugrás in enumerate(kiugrálások):
    if index > 0 and ugrás == 'vízfelszínen úszik' and kiugrálások[index-1] == 'vízfelszínen úszik':
        merülés += 1

print('Ennyiszer ugrott ki a vízből a delfin: ', merülés)