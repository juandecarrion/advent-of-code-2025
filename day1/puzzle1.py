

pos = 50
rotations = []
positions = []

with open("data/puzzle1_input.txt") as f:
    for line in f:
        direction = -1 if line.startswith("L") else 1
        rotation = direction * int(line[1:])
        rotations.append(rotation)

for r in rotations:
    pos = pos + r
    pos %= 100
    positions.append(pos)

print(positions.count(0))
