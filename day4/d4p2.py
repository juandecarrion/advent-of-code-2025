import copy

lines = []

with open("d4p1.txt") as f:
    for l in f:
        lines.append(l.strip())



old_grid = []

i = 0
for l in lines:
    old_grid.append([])
    j = 0
    for c in l:
        old_grid[i].append(c)
        j += 1
    i += 1


pass

height = i
width = j

new_grid = copy.deepcopy(old_grid)

first = True
p2_counter = 0
while old_grid != new_grid or first == True:
    first = False
    for i in range(height):
        for j in range(width):
            tp_around = 0
            if old_grid[i][j] == "@":
                adjacents_pos = []
                for k in [
                    (i - 1, j - 1),
                    (i - 1, j),
                    (i - 1, j + 1),

                    (i, j - 1),

                    (i, j + 1),

                    (i + 1, j - 1),
                    (i + 1, j),
                    (i + 1, j + 1),
                ]:
                    adjacents_pos.append((k[0], k[1]))

                for a_pos in adjacents_pos:
                    if -1 < a_pos[0] < height and -1 < a_pos[1] < width:
                        if old_grid[a_pos[0]][a_pos[1]] == '@':
                            tp_around += 1
                if tp_around < 4:
                    p2_counter += 1
                    new_grid[i][j] = '.'
    old_grid = copy.deepcopy(new_grid)


p1_counter = 0
for i in range(height):
    for j in range(width):
        tp_around = 0
        if old_grid[i][j] == "@":
            adjacents_pos = []
            for k in [
                (i - 1, j - 1),
                (i - 1, j    ),
                (i - 1, j + 1),

                (i    , j - 1),

                (i    , j + 1),

                (i + 1, j - 1),
                (i + 1, j    ),
                (i + 1, j + 1),
            ]:
                adjacents_pos.append((k[0], k[1]))

            for a_pos in adjacents_pos:
                if -1 < a_pos[0] < height and -1 < a_pos[1] < width:
                    if old_grid[a_pos[0]][a_pos[1]] == '@':
                        tp_around += 1
            if tp_around < 4:
                p1_counter += 1

print(p1_counter)
print(p2_counter)


test_case_input = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
]

test_case_output = [
    '..xx.xx@x.',
    'x@@.@.@.@@',
    '@@@@@.x.@@',
    '@.@@@@..@.',
    'x@.@@@@.@x',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    'x.@@@.@@@@',
    '.@@@@@@@@.',
    'x.x.@@@.x.',
]

pass
