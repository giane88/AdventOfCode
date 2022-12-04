import requests
import os
import sys
from pathlib import Path

if len(sys.argv) != 4:
    print('Wrong number of arguments')
    exit(0)

day, year, cookie = int(sys.argv[1]),int(sys.argv[2]), sys.argv[3]

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path = Path(location)
print (f'Working path: {path.parent.absolute()}')
print(f'Creating path for day {day:02} and year {year} ')
os.makedirs(f'{path.parent.absolute()}/aoc{year}/{day:02}')
print('Path created')

print('Retrieving file...')
headers = {'session': cookie}
url = f'https://adventofcode.com/{year}/day/{day}/input'
session = requests.Session()
resp = session.get(url,cookies=headers)

inputFile = f'{path.parent.absolute()}/aoc2022/{day:02}/day{day:02}.txt'
print(f'File saved in {inputFile}')
in_file = open(inputFile,'w')
in_file.write(resp.text)
in_file.close()

testFile = f'{path.parent.absolute()}/aoc2022/{day:02}/test.txt'
rulesFile = f'{path.parent.absolute()}/aoc2022/{day:02}/rules.md'
pyFile = f'{path.parent.absolute()}/aoc2022/{day:02}/day{day:02}.py'

open(testFile, 'x')
open(rulesFile,'x')
open(pyFile,'x')

print('File correctly saved')