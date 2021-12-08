def calc_board(board, num):
    return num * sum([item for sublist in board for item in sublist if item != "X"])

data = open("day-4/data.txt").read().strip().split("\n\n")
numbers = [int(x) for x in data.pop(0).split(",")]
rows = []
for i in data:
    for row in i.split("\n"):
        rows.append([int(x) for x in row.split(" ") if x])

part1 = part2 = 0
for num in numbers:
    for row_num, row in enumerate(rows):
        if num in row:
            row[row.index(num)] = "X"
            # check row
            if row == ["X"] * 5:
                board = rows[row_num // 5 * 5 : row_num // 5 * 5 + 5]
                del rows[row_num // 5 * 5 : row_num // 5 * 5 + 5]
                if not part1:
                    part1 = calc_board(board, num)
                part2 = calc_board(board, num)

    for i in range(len(rows) // 5):
        board = rows[i * 5 : i * 5 + 5]
        for n in range(5):
            col = [x[n] for x in board]
            if col == ["X"] * 5:
                del rows[i * 5 : i * 5 + 5]
                if not part1:
                    part1 = calc_board(board, num)
                part2 = calc_board(board, num)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
