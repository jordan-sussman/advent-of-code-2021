data = open("day-20/data.txt").read().strip().split("\n\n")
alg = data.pop(0)
map = [[0 if i == "." else 1 for i in j] for j in data[0].split("\n")]

def create_map(map, fill):
    w = len(map[0]) + 2
    new_map = []
    new_map.append([fill] * w)
    for line in map:
        new_map.append([fill] + line + [fill])
    new_map.append([fill] * w)
    return new_map

def fetch_neighbors(a, b, map, fill):
    bs = ""
    for am in range(-1, 2):
        for bm in range(-1, 2):
            if a + am < 0 or a + am >= len(map) or b + bm < 0 or b + bm >= len(map[0]):
                bs += str(fill)
            else:
                bs += str(map[a + am][b + bm])
    return 1 if alg[int(bs, 2)] == "#" else 0

for i in range(1, 50 + 1):
    fill = 1 if alg[0] == "#" and alg[-1] == "." and not i % 2 else 0
    map = create_map(map, fill)

    changes = {}
    for a in range(len(map)):
        for b in range(len(map[0])):
            changes[(a, b)] = fetch_neighbors(a, b, map, fill)

    for a, b in changes:
        map[a][b] = changes[(a, b)]
    if i == 2:
        # PART 1
        prt1 = sum([val for sublist in map for val in sublist])
# PART 2
prt2 = sum([val for sublist in map for val in sublist])

print("Part 1 Answer:", prt1)
# Part 1 Answer: 5203
print("Part 2 Answer:", prt2)
# Part 2 Answer: 18806
