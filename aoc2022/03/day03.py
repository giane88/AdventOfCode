import os
def calculate_sum(s):
    sum = 0;
    for x in s:
        if x.isupper():
            sum += ord(x)-38
        else:
            sum += ord(x)-96
    return sum


location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day03.txt') as f:
    lines = f.readlines()

exceed =[]

for line in lines:
    length = len(line);
    s1 = line[:length//2];
    s2 = line[length//2:];
    common = set(s1)&set(s2)
    exceed.append(''.join(common))


print(calculate_sum(exceed))

i=0
group= []
while i < len(lines):
    group.append(''.join(set(lines[i].strip())&set(lines[i+1].strip())&set(lines[i+2].strip())))
    i += 3

print(calculate_sum(group))