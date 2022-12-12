import os 

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{location}/day09.txt') as f:
    lines = f.readlines()


def get_vector_change(direction: str):
    match direction:
        case 'L':
            return [-1, 0]
        case 'U':
            return [0, 1]
        case 'R':
            return [1, 0]
        case 'D':
            return [0, -1]
        case _:
            print("Invalid direction argument")
            exit(-1)
def move_tail(head: list[int], tail: list[int]) -> None:
    Δ = [x - y for x, y in zip(head, tail)]

    if abs(Δ[0]) > 1 or abs(Δ[1]) > 1:
        tail[:] = [n + (1 if Δn >= 1 else -1 if Δn <= -1 else 0) for n, Δn in zip(tail, Δ)]


"""
Posizioni iniziali
"""
head = [0,0]
tail = [0,0]

visited_p1 = set()
visited_p2 = set()
tail_parts = [[0, 0] for _ in range(9)]

for line in lines:
    direction, count = line.strip().split()[0],int(line.strip().split()[1])

    for i in range(count):
        head = [x + y for x, y in zip(head, get_vector_change(direction))]

        move_tail(head, tail)
        visited_p1.add(tuple(tail))

        for i in range(len(tail_parts)):
            move_tail(head if i == 0 else tail_parts[i - 1], tail_parts[i])

            if i == 8:
                visited_p2.add(tuple(tail_parts[i]))

print(f"Part 1: {len(visited_p1)}")
print(f"Part 2: {len(visited_p2)}")