from collections import Counter

data = open("day-14/data.txt").read().strip().split("\n\n")
tmpl = data[0]
pairs = Counter()
rules = {}

def solve(pairs, tmpl, steps):
    for step in range(steps + 1):
        if step == steps:
            letters = Counter()
            for pair in pairs:
                letters[pair[0]] += pairs[pair]
            letters[tmpl[-1]] += 1
            return max(letters.values()) - min(letters.values())
        new_pairs = Counter()
        for pair in pairs:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs

for i in range(len(tmpl) - 1):
    pairs[tmpl[i] + tmpl[i + 1]] += 1

for line in data[1].split("\n"):
    pair, elem = line.split(" -> ")
    rules[pair] = elem

prt1 = solve(pairs, tmpl, 10)
print("Part 1 Answer:", prt1)
# Part 1 Answer: 2740

prt2 = solve(pairs, tmpl, 40)
print("Part 2 Answer:", prt2)
# Part 2 Answer: 2959788056211
