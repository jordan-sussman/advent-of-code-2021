from collections import Counter

with open("day-6/data.txt") as f:
        fishes = f.read().strip().split(',')
        fishes = list(map(int, fishes))
        
# Part 1
def part1(fishes):
    for day in range(80):
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fishes[idx] = 7
                fishes.append(9)
        fishes = [fish - 1 for fish in fishes]
    return len(fishes)

# Part 2
def part2(fishes):
    timers = Counter({timer: 0 for timer in range(10)})
    fishes = Counter(fishes)
    fishes.update(timers)
    
    for day in range(256):
        fishes[7] += fishes.get(0, 0)
        fishes[9] += fishes.get(0, 0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}      
    return sum(fishes.values())
     
print("Part 1 Answer:", part1(fishes))
# Part 1 Answer: 389726
print("Part 2 Answer:", part2(fishes))
# Part 2 Answer: 1743335992042
