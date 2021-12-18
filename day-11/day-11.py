data = [[int(f) for f in list(line)] for line in open("day-11/data.txt").read().strip().split("\n")]
step = 0
flashes = 0
prt1 = 0
prt2 = None

def get_nbrs(r, c):
    nbrs = []
    for y,x in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if r + y >= 0 and r + y <= 9 and c + x >= 0 and c + x <= 9:
            nbrs.append((r + y, c + x))
    return nbrs

while True:
    flashed = []
    nbrs = []
    for a in range(len(data)):
        for b in range(len(data[a])):
            if data[a][b] == 9:
                data[a][b] = 0
                flashes += 1
                flashed.append((a, b))
                nbrs.extend(get_nbrs(a, b))
            else:
                data[a][b] += 1

    while nbrs:
        nbr_a, nbr_b = nbrs.pop(0)
        if (nbr_a, nbr_b) not in flashed:
            if data[nbr_a][nbr_b] == 9:
                data[nbr_a][nbr_b] = 0
                flashes += 1
                if (nbr_a, nbr_b) not in flashed:
                    flashed.append((nbr_a, nbr_b))
                nbrs.extend(get_nbrs(nbr_a, nbr_b))
            else:
                data[nbr_a][nbr_b] += 1

    if step + 1 == 100:
        prt1 = int(flashes)
    if len(flashed) == 100:
        prt2 = step + 1
        break
    step += 1

print(f"Part 1 Answer: {prt1}")
# Part 1 Answer: 1683
print(f"Part 2 Answer: {prt2}")
# Part 2 Answer: 788
