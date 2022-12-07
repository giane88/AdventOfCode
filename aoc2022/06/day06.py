import os
import numpy as np

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day06.txt') as f:
    lines = f.readlines()


"""
Soluzione parte 1
"""
for line in lines:
    line = line.strip()
    for i in range (4, len(line)):
        window = line[i-4: i]
        print(f'Window: {window} unique: {len(set(window))} size: {len(window)}')
        if len(set(window))== len(window):
            print(i)
            break


"""
Soluzione parte 2
"""
for line in lines:
    line = line.strip()
    for i in range (14, len(line)):
        window = line[i-14: i]
        print(f'Window: {window} unique: {len(set(window))} size: {len(window)}')
        if len(set(window))== len(window):
            print(i)
            break