import requests
import os
import sys

if len(sys.argv) != 3:
    print('Wrong number of arguments')
    exit(0)

day, cookie = int(sys.argv[1]),sys.argv[2]
headers = {'session': cookie}
url = f'https://adventofcode.com/2022/day/{day}/input'

session = requests.Session()
resp = session.get(url,cookies=headers)

path = os.getcwd()

print ("current directory is %s" % path)

os.makedirs(f'{path}/aoc2022/{day:02}',)


in_file = open(f'{path}/aoc2022/{day:02}/day{day:02}.txt','w')
in_file.write(resp.text)
in_file.close()