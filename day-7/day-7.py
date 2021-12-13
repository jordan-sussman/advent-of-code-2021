data = [int(x) for x in open("day-7/data.txt").read().strip().split(",")]

part1 = {x: sum([abs(x - z) for z in data]) for x in range(0, max(data) + 1)}
print("Part 1 Answer:", min(part1.values()))
# Part 1 Answer: 355989

part2 = {x: sum([abs(x - z) / 2 * (2 + (abs(x - z) - 1)) for z in data]) for x in range(0, max(data) + 1)}
print("Part 2 Answer:", int(min(part2.values())))
# Part 2 Answer: 102245489
