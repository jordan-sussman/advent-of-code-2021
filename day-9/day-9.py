import math

data = open("day-9/data.txt").read().strip().split("\n")
lows = []
basins = []

def follow(row, col, z):
    for y, x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if (row + y, col + x) not in z:
            if row + y >= 0 and row + y < len(data):
                if col + x < len(data[0]) and col + x >= 0:
                    if data[row + y][col + x] != "9":
                        z.add((row + y, col + x))
                        follow(row + y, col + x, z)
    return z

for row in range(len(data)):
    for col in range(len(data[0])):
        cur = int(data[row][col])
        a = int(data[row - 1][col]) if row > 0 else 9999
        b = int(data[row + 1][col]) if row < len(data) - 1 else 9999
        c = int(data[row][col + 1]) if col < len(data[0]) - 1 else 9999
        d = int(data[row][col - 1]) if col > 0 else 9999
        if cur < min([a, b, c, d]):
            lows.append(cur)
            basins.append(len(follow(row, col, {(row, col)})))

prt1 = sum([x + 1 for x in lows])
prt2 = math.prod(sorted(list(basins), reverse=True)[:3])

print("Part 1 Answer:", prt1)
# Part 1 Answer: 508
print("Part 2 Answer:", prt2)
# Part 2 Answer: 1564640
