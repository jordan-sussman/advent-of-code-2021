from collections import Counter

data = open("day-5/data.txt").read().strip().split("\n")
prt1 = []
prt2 = []

for line in data:
    x1, y1 = tuple(int(x) for x in line.split(" -> ")[0].split(","))
    x2, y2 = tuple(int(x) for x in line.split(" -> ")[1].split(","))

    # Part 1
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                prt1.append((x, y))
                prt2.append((x, y))
    # Part 2
    else:
        xinc = 1 if x1 < x2 else -1
        yinc = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1, x2 + xinc, xinc):
            prt2.append((x, y))
            y += yinc

p1_dupes = [pt for pt in Counter(prt1).values() if pt > 1]
print("Part 1:", len(p1_dupes))
# Part 1 Answer: 5835

p2_dupes = [pt for pt in Counter(prt2).values() if pt > 1]
print("Part 2:", len(p2_dupes))
# Part 2 Answer: 17013
