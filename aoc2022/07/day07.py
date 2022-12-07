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

print(f'Soluzione 1 {small_size}')
free_space = 70000000 - sizes[Path('/')]
print(f'Free space: {free_space}')
small_directory_size = 30000000 - free_space
print(f'Small directory: {small_directory_size}')

min_dir_size = min([x for x in sizes.values() if x > small_directory_size])
print(f'Soluzione 2: {min_dir_size}')