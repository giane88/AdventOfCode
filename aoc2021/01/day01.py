import utils.files

def countIncrement (lines) :
    count = 0
    prev = int(lines[0]);

    for line in lines:
        if (int(line) > prev):
            count += 1
        prev = int(line)
    return count

lines = utils.files.readInput('day01.txt')


#print("Number of increment %d" % countIncrement(lines));

three_sum =[]

for x in range(len(lines)-2):
    sublist = lines[x:x+3]
    print(sublist)
    summ = 0
    for elem in sublist:
        summ += int(elem)
    three_sum.append(summ)

print(three_sum)

print("Number of increment %d" % countIncrement(three_sum));
    

