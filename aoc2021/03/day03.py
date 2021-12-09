from utils import files
import itertools

def most_frequent(List):
    return max(set(List), key = List.count)

def to_int_from_list(List):
    return int("".join(str(x) for x in List), 2)

#Transform lines in a matrix
def matrix_extractor(lines):
    matrix = []
    for line in lines:
        arr = list(line.strip())
        matrix.append(arr)
    return matrix

def transpose_matrix(matrix):
    return list(map(list, itertools.zip_longest(*matrix, fillvalue=None)))

def filter_list(List,position, control):
    print("Position %d Contorl: %s" % (position, control))
    print(List)
    if(len(List)==1): 
        return List
    temp = []
    for elem in List:
        print("Element %s Contorl: %s" % (elem[position], control))
        if (elem[position] == control):
           temp.append(elem)
    print(temp)
    return temp


lines = files.readInput('day03.txt')
matrix = matrix_extractor(lines)
transposed = transpose_matrix(matrix)


gamma= []
epsilon= []

for row in transposed:
    mf = most_frequent(row)
    if mf=='1':
        gamma.append(1);
        epsilon.append(0);
    else:
        gamma.append(0);
        epsilon.append(1);

print(to_int_from_list(gamma)*to_int_from_list(epsilon))

oxigen = matrix
co2 = matrix


transposed = transpose_matrix(oxigen)
for x in range(len(matrix[0])):
    mf = most_frequent(transposed[x])
    if mf=='0':
        oxigen = filter_list(oxigen,x, '0')
    else:
        oxigen = filter_list(oxigen,x, '1')
    transposed = transpose_matrix(oxigen)

transposed = transpose_matrix(co2)
for x in range(len(matrix[0])):
    mf = most_frequent(transposed[x])
    if mf=='0':
        co2 = filter_list(co2,x, '1')
    else:
        co2 = filter_list(co2,x, '0')
    transposed = transpose_matrix(co2)

print(oxigen)
print(co2)
print(to_int_from_list(oxigen[0])*to_int_from_list(co2[0]))