import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day04.txt') as f:
    lines = f.readlines()

countFirst = 0
countSecond = 0

for line in lines:
    x,y = line.split(',')
    a,b = x.split('-')
    c,d = y.split('-')

    """
    Soluzione primo problema
    """
    if (int(a)>=int(c) and int(b)<=int(d)) or (int(a)<=int(c) and int(b)>=int(d)):
        countFirst+=1

    """
    Soluzione secondo problema
    """
    first = [*range(int(a), int(b)+1)]
    second = [*range(int(c), int(d)+1)]

    intersection = []
    for i in set(first) & set(second):
        intersection.append(i)
    
    if intersection !=[]:
        countSecond+=1

print(countFirst)
print(countSecond)