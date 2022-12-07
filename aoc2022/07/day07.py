import os
from pathlib import Path

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day07.txt') as f:
    lines = f.readlines()

location = Path('/')
folder_size={}
folder_size[location]= 0

for line in lines:
    token = line.strip().split(' ')
    if token[0] == '$':
        if token[1] == "cd":
            if token[2] == "..":
                location = location.parent
            else:
                location = location / token[2]
                folder_size[location] = 0
    elif token[0][0].isnumeric():
        folder_size[location] += int(token[0])

sizes = {}
for key in folder_size.keys():
    sizes[key] = folder_size[key]
    for sub in folder_size.keys():
        if key in sub.parents:
            sizes[key] += folder_size[sub]
small_size = 0
for value in sizes.values():
    if value < 100000:
        small_size += value

print(small_size)

