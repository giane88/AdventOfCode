import os

path = os.getcwd()
with open(f'{path}/aoc2022/01/day01.txt') as f:
    lines = f.readlines()


calories4Elf = [] 
sum = 0

for line in lines:
    if '\n' == line:
        calories4Elf.append(sum)
        sum = 0
    else:
        sum = sum + int(line)


if len(calories4Elf) == 0: calories4Elf.append(sum);

calories4Elf.sort(reverse=True)


print(f'Solution 1 {calories4Elf[0]}')
print(f'Solution 1 {calories4Elf[0]+calories4Elf[1]+calories4Elf[2]}')

