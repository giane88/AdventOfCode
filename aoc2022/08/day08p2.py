import os

def num_top_visible(i,j,matrix) -> int:
    for k in range(1,i):
        if i==78 and j == 53:
            print()
        if matrix[i-k][j]>= matrix[i][j]:
            return k
    return i

def num_bottom_visible(i,j,matrix) -> int:
    for k in range(i+1, len(matrix)):
        if matrix[k][j]>= matrix[i][j]:
            return k-i
    return len(matrix)-i-1

def num_left_visible(i,j,matrix) -> int:
    for k in range(1,j):
        if matrix[i][j-k]>= matrix[i][j]:
            return k
    return j

def num_right_visible(i,j,matrix) -> int:
    for k in range(j+1, len(matrix)):
        if matrix[i][k]>= matrix[i][j]:
            return k-j
    return len(matrix)-j-1

def point_visible(i, j , matrix) -> int:
    if i == 0 or j == 0 or i == row_number-1 or j == col_number-1:
        return 0
    top_point = num_top_visible(i,j,matrix)
    bottom_point = num_bottom_visible(i,j,matrix)
    left_point = num_left_visible(i,j,matrix)
    right_point = num_right_visible(i,j,matrix)
    if i == 78 and j == 53:
        print(f'matrix[{i}][{j}] = {top_point}*{bottom_point}*{left_point}*{right_point}')
    return top_point*bottom_point*left_point*right_point

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day08.txt') as f:
    lines = f.readlines()

matrix =[]

for line in lines:
    matrix.append([int(x) for x in list(line.strip())])

max_point = 0
row_number = len(matrix)
col_number =  len(matrix[0])
for i in range(0, row_number):
    for j in range(0, col_number):
        point = point_visible(i,j,matrix)
        
        if (point > max_point): 
            max_point = point
            print(f'matrix[{i}][{j}] = {point}')
        

print(max_point)