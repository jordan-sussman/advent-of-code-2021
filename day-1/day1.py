with open('day-1/data.txt', 'r') as data:
    readings = [int(line) for line in data.readlines()]

def count_decreases(depths, neighbor = 1):
    return sum(1 for d1, d2 in zip(depths, depths[neighbor:]) if d1 < d2)

print("Part 1 Answer:", count_decreases(readings))
# Part 1 Answer: 1301
print("Part 2 Answer:", count_decreases(readings, neighbor = 3))
# Part 2 Answer: 1346
