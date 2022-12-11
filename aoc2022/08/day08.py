import os

def is_top_visible(i,j,matrix) -> bool:
    for k in range(0,i):
        if matrix[k][j]>= matrix[i][j]:
            return False
    return True

def is_bottom_visible(i,j,matrix) -> bool:
    for k in range(i+1, len(matrix)):
        if matrix[k][j]>= matrix[i][j]:
            return False
    return True

def is_left_visible(i,j,matrix) -> bool:
    for k in range(0,j):
        if matrix[i][k]>= matrix[i][j]:
            return False
    return True

def is_right_visible(i,j,matrix) -> bool:
    for k in range(j+1, len(matrix)):
        if matrix[i][k]>= matrix[i][j]:
            return False
    return True

def is_visible(i, j , matrix) -> bool:
    if i == 0 or j == 0 or i == row_number-1 or j == col_number-1:
        return True
    if is_top_visible(i,j,matrix) or is_bottom_visible(i,j,matrix) or is_right_visible(i,j,matrix) or is_left_visible(i,j,matrix):
        return True
    return False

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day08.txt') as f:
    lines = f.readlines()

matrix =[]

for line in lines:
    matrix.append([int(x) for x in list(line.strip())])

num_visible = 0
row_number = len(matrix)
col_number =  len(matrix[0])
for i in range(0, row_number):
    for j in range(0, col_number):
        
        if is_visible(i,j,matrix):
            print(f'matrix[{i}][{j}] -> True')
            num_visible += 1

print(num_visible)