import os
import numpy as np

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day02.txt') as f:
    lines = f.readlines()

pointsFigure={
    "X":1,
    "Y":2,
    "Z":3,
}
pointsWin = 6
pointsDraw = 3
pointsLose = 0

lose = [("B","X"), ("C", "Y"), ("A", "Z")]
win = [("C","X"), ("A","Y"), ("B","Z")]
draw = [("A","X"), ("B","Y"), ("C","Z")]

points = 0

"""
Soluzione alla parte 1
"""
for line in lines:
    opponent, me = line.split()
    points += pointsFigure[me]
    if (opponent,me) in lose : points += pointsLose
    if (opponent,me) in win : points += pointsWin
    if (opponent,me) in draw : points += pointsDraw
    
print(f'Solution 1: {points}')

