input = open("day-13/data.txt").read()
data = [part.splitlines() for part in input.split("\n\n")]
dots = set([tuple(map(int, line.split(","))) for line in data[0]])
fold_instructions = data[1]

for a, fold_instruction in enumerate(fold_instructions):
    x_fold = fold_instruction.split("fold along x=")[-1]
    y_fold = fold_instruction.split("fold along y=")[-1]
    if x_fold.isnumeric():
        x = int(x_fold)
        dots = set([(dot[0] - 2 * max(0, dot[0] - x), dot[1]) for dot in dots])
    if y_fold.isnumeric():
        y = int(y_fold)
        dots = set([(dot[0], dot[1] - 2 * max(0, dot[1] - y)) for dot in dots])

    if a == 0:
        print("Part 1 Answer:", len(dots))
        # Part 1 Answer: 675

print("Part 2 Answer:")
x_max, y_max = max([c[0] for c in dots]), max([c[1] for c in dots])
for y in range(y_max + 1):
    for x in range(x_max + 1):
        print("█", end="") if (x, y) in dots else print(" ", end="")
    print()
# Part 2 Answer: HZKHFEJZ
