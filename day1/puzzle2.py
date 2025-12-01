

pos = 50
rotations = []
positions = []
zeros = 0

with open("data/puzzle1_input.txt") as f:
    for line in f:
        direction = -1 if line.startswith("L") else 1
        rotation = direction * int(line[1:])
        rotations.append(rotation)

for r in rotations:
    start = pos
    end = pos + r
    step = 1 if r > 0 else -1
    for i in range(start, end, step):
        if i % 100 == 0 and i != start and i != end:
            zeros += 1
    pos = end % 100
    positions.append(pos)

print(positions.count(0) + zeros)
