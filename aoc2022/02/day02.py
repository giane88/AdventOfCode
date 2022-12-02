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


"""
Soluzione alla parte 2
"""
points=0
for line in lines:
    opponent, result = line.split()

    if result == "X":
        points += pointsLose
        for (opMove, myMove) in lose:
            if opponent == opMove : points += pointsFigure[myMove]
    if result == "Y":
        points += pointsDraw
        for (opMove, myMove) in draw:
            if opponent == opMove : points += pointsFigure[myMove]
    if result == "Z":
        points += pointsWin
        for (opMove, myMove) in win:
            if opponent == opMove : points += pointsFigure[myMove]

print(f'Solution 2: {points}')