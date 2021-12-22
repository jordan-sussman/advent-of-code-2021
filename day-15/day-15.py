from collections import defaultdict
import heapq

data = [[int(y) for y in x] for x in open("day-15/data.txt").read().strip().split("\n")]
size_y, size_x = len(data), len(data[0])

def solve(risk):
    rows, cols = size_y * risk, size_x * risk
    costs = defaultdict(int)
    pqueue = [(0, 0, 0)]
    visited = set()
    heapq.heapify(pqueue)
    while len(pqueue) > 0:
        cost, row, col = heapq.heappop(pqueue)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        costs[(row, col)] = cost
        if row == rows - 1 and col == cols - 1:
            break

        for move_y, move_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + move_y
            new_col = col + move_x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            new_cost = (
                (
                    data[new_row % size_y][new_col % size_x]
                    + (new_row // size_y)
                    + (new_col // size_x)
                )
                - 1
            ) % 9 + 1
            heapq.heappush(pqueue, (cost + new_cost, new_row, new_col))
    return costs[(rows - 1, cols - 1)]

prt1 = solve(1)
print("Part 1 Answer:", prt1)
# Part 1 Answer: 527

prt2 = solve(5)
print("Part 2 Answer:", prt2)
# Part 2 Answer: 2887
