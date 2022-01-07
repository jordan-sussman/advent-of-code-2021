from collections import defaultdict
data = open("day-22/data.txt").read().strip().split("\n")

def cube_volume(b):
    x1, x2 = b[0]
    y1, y2 = b[1]
    z1, z2 = b[2]
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) * (abs(z2 - z1) + 1)

def overlaps(b1, b2):
    ans = []
    for n1, n2 in zip(b1, b2):
        if n1[1] < n2[0] or n2[1] < n1[0]:
            return None
        bounds = (max(n1[0], n2[0]), min(n1[1], n2[1]))
        ans.append(bounds)
    return tuple(ans)

def wrangle(data, ignore=False):
    steps = []
    for line in data:
        switch, coords = line.split(" ")
        bounds = tuple(tuple(int(p) for p in l[2:].split("..")) for l in coords.split(","))
        x, y, z = bounds
        if ignore:
            if (
                -ignore <= int(x[0]) <= ignore
                and -ignore <= int(x[1]) <= ignore
                and -ignore <= int(y[0]) <= ignore
                and -ignore <= int(y[1]) <= ignore
                and -ignore <= int(z[0]) <= ignore
                and -ignore <= int(z[1]) <= ignore
            ):
                steps.append((switch == "on", bounds))
        else:
            steps.append((switch == "on", bounds))
    return steps

def count(steps):
    counts = defaultdict(int)
    for i in range(len(steps)):
        switch, bounds = steps[i]
        updates = defaultdict(int)
        keys = set(counts.keys())
        for cube in keys:
            overlapping = overlaps(bounds, cube)
            if not overlapping:
                continue
            updates[overlapping] -= counts[cube]
        if switch:
            updates[bounds] += 1
        for x in updates:
            counts[x] += updates[x]
    return counts

# PART 1
steps = wrangle(data, 50)
counts = count(steps)
prt1 = 0
for cube in counts:
    prt1 += cube_volume(cube) * counts[cube]
print("Part 1 Answer:", prt1)
# Part 1 Answer: 588200

# PART 2
steps = wrangle(data)
counts = count(steps)
prt2 = 0
for cube in counts:
    prt2 += cube_volume(cube) * counts[cube]
print("Part 1 Answer:", prt2)
# Part 2 Answer: 1207167990362099