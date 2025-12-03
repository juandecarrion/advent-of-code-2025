lines = []

with open("d3p1.txt") as f:
    for l in f:
        lines.append(l.strip())


def max_jolt(line, digit_len=12):
    digits = []
    digits_pos = []
    l_len = len(line)

    search_start = 0
    search_end = l_len - digit_len + 1
    digits.append(max(line[search_start:search_end]))
    digits_pos.append(line.find(digits[0]))
    for i in range(1, digit_len):
        search_start = digits_pos[i - 1] + 1
        search_end = l_len - digit_len + i + 1
        digits.append(max(line[search_start:search_end]))
        digits_pos.append(line[digits_pos[i - 1] + 1:].find(digits[i]) + digits_pos[i - 1] + 1)

    return int("".join(digits))


for t in [
    # '987654321111111',
    # '811111111111119',
    # '234234234234278',
    # '818181911112111',
    # '2113214222323223222322333121232313223422322533222223225133222221223333233322423133313222233222213732',
    # '987654321111111',
    # '811111111111119',
    '234234234234278',
    '818181911112111',
]:
    print(t, max_jolt(t))

sol = 0
for l in lines:
    print(l, max_jolt(l))
    sol += max_jolt(l)

print(sol)
