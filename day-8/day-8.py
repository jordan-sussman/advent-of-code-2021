data = open("day-8/data.txt").read().strip().split("\n")
prt1 = prt2 = 0

for line in data:
    signals, output = line.strip().split(" | ")

    d = {
        l: set(sets)
        for sets in signals.split()
        if (l := len(sets)) in (2, 4)
    }
    
    n = ""
    for objects in output.split():
        l = len(objects)
        if   l == 2: n += "1"; prt1 += 1
        elif l == 4: n += "4"; prt1 += 1
        elif l == 3: n += "7"; prt1 += 1
        elif l == 7: n += "8"; prt1 += 1
        elif l == 5:
            sets = set(objects)
            if   len(sets & d[2]) == 2: n += "3"
            elif len(sets & d[4]) == 2: n += "2"
            else: n += "5"
        else: # l == 6
            sets = set(objects)
            if   len(sets & d[2]) == 1: n += "6"
            elif len(sets & d[4]) == 4: n += "9"
            else: n += "0"

    prt2 += int(n)

print("Part 1 Answer:", prt1)
# Part 1 Answer: 416
print("Part 2 Answer:", prt2)
# Part 2 Answer: 1043697
