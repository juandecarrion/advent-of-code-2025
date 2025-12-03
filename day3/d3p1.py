lines = []

with open("d3p1.txt") as f:
    for l in f:
        lines.append(l.strip())


def max_jolt(line):
    max_ten = max(line[:-1])
    first_max_ten = line.find(max_ten)
    second_digit = max(max(line[first_max_ten + 1:]))
    return int(max_ten + second_digit)


for t in ['987654321111111',
          '811111111111119',
          '234234234234278',
          '818181911112111']:
    print(t, max_jolt(t))

sol = 0
for l in lines:
    sol += max_jolt(l)

print(sol)
pass
