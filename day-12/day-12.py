from collections import defaultdict, deque

data = open("day-12/data.txt").read().strip().split("\n")
map = defaultdict(list)

def path(map, dbls):
    cnt = 0
    tracker = deque([("start", set(["start"]), False)])
    while tracker:
        p, seen, visited = tracker.popleft()
        if p == "end":
            cnt += 1
            continue
        for c in map[p]:
            if c not in seen:
                seen_cp = set(seen)
                if c.islower():
                    seen_cp.add(c)
                tracker.append((c, seen_cp, visited))
            elif c in seen and not visited and c not in ["start", "end"] and dbls:
                tracker.append((c, seen, c))
    return cnt

for line in data:
    p, c = line.split("-")
    map[p].append(c)
    map[c].append(p)

prt1 = path(map, False)
prt2 = path(map, True)


print("Part 1 Answer:", prt1)
# Part 1 Answer: 3410
print("Part 2 Answer:", prt2)
# Part 2 Answer: 98796
