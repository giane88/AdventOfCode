import os
import numpy as np

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day01.txt') as f:
    lines = f.readlines()

calories4Elf = [] 
sum = 0

for line in lines:
    if line.strip():
        sum += int(line)
    else:
        calories4Elf.append(sum)
        sum = 0

calories4Elf.sort(reverse=True)

print(f'Solution 1 {calories4Elf[0]}')
print(f'Solution 2 {np.sum(calories4Elf[:3])}')

