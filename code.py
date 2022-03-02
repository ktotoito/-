import json
import sys


d = {'1': 'savannah', '2': 'desert', '3': 'forest'}
d1 = {"savannah": {}, "desert": {}, "forest": {}}
data = sys.stdin.readlines()
data = list(map(lambda x: x[:-1], data))
data = list(map(lambda x: x.split(";"), data))

for i in data:
    m = d[i[0]]
    d1[m][i[1]] = 0

for i in data:
    i1 = int(i[2])
    m = d[i[0]]
    d1[m][i[1]] += i1

with open("zambezi_animals.json", "w") as write_file:
    json.dump(d1, write_file)
