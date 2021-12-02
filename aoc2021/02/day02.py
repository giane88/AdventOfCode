from utils import files

lines = files.readInput('day02.txt')
coordinate = [0,0]
aim = [0]

def commandDecoder(command):
    arr = command.split()
    cmd= arr[0]
    val = int(arr[1])
    if (cmd == 'forward') :
        coordinate[0] += val
    elif (cmd == 'down'):
        coordinate[1] += val
    elif (cmd == 'up'):
        coordinate[1] -= val
    else:
        print("invalid")

def commandDecoder2(command):
    arr = command.split()
    cmd= arr[0]
    val = int(arr[1])
    if (cmd == 'forward') :
        coordinate[0] += val
        coordinate[1] += val*aim[0]
    elif (cmd == 'down'):
        aim[0] += val
    elif (cmd == 'up'):
        aim[0] -= val
    else:
        print("invalid")

for line in lines:
    commandDecoder(line)

answer = coordinate[0]*coordinate[1]

print("Position: %d" % answer)

coordinate = [0,0]
for line in lines:
    commandDecoder2(line)
    
answer = coordinate[0]*coordinate[1]
print("Position: %d" % answer)