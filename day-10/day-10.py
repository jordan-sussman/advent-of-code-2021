data = open("day-10/data.txt").read().strip().split("\n")
pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
errorPoints = {")": 3, "]": 57, "}": 1197, ">": 25137}
messagePoints = {")": 1, "]": 2, "}": 3, ">": 4}
errorScores = []
messageScores = []

for chunk in data:
    score = 0
    found = []
    for c in chunk:
        if c not in [")", "]", "}", ">"]:
            found.append(c)
        else:
            if c == pairs[found[-1]]:
                found.pop()
            else:
                errorScores.append(errorPoints[c])
                found = []
                break
    if found:
        for m in [pairs[x] for x in found[::-1]]:
            score = (score * 5) + messagePoints[m]
        messageScores.append(score)

part1 = sum(errorScores)
part2 = sorted(messageScores)[len(messageScores)//2]

print("Part 1 Answer:", part1)
# Part 1 Answer: 215229
print("Part 2 Answer:", part2)
# Part 2 Answer: 1105996483
