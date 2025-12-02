import re

lines = []

ids = []


with open("d2p1.txt") as f:
    for l in f:
        lines.append(l.strip())

ranges = lines[0].split(',')

for r in ranges:
    start, end = r.split('-')
    start, end = int(start), int(end)
    for id in range(start, end + 1):
        ids.append(id)


r2 = re.compile(r'^(.*)\1+$')


def is_valid(id):
    id = str(id)
    return not r2.match(id)


print(824824824, is_valid(824824824))


print(456, is_valid(456))
print(1059, is_valid(1059))
print(852, is_valid(852))

invalid_ids = 0
for id in ids:
    if not is_valid(id):
        invalid_ids += id

print(invalid_ids)

pass