with open('day-2/data.txt', 'r') as data:
    lines = data.readlines()

movements = [a.strip().split() for a in lines]

# Part 1
horizontal, depth = 0, 0
for command,value in movements:
    if command == "forward":
        horizontal += int(value)
    elif command == "down":
        depth += int(value)
    elif command == "up":
        depth -= int(value)

# final horizontal = 1996
# final depth = 1022
part1Answer = horizontal*depth
# 1996 x 1022 = 2039912
print("Part 1 Answer:", part1Answer)
# Part 1 Answer: 2039912


# Part 2
aim = 0
horizontal, depth = 0, 0
for command,value in movements:
    if command == "forward":
        horizontal += int(value)
        depth += aim * int(value)
    elif command == "down":
        aim += int(value)
    elif command == "up":
        aim -= int(value)

# final horizontal = 1996
# final depth = 972980
part2Answer = horizontal*depth
print("Part 2 Answer:", part2Answer)
# Part 2 Answer: 1942068080
