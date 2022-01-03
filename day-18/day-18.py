import itertools
import math
import re

data = open("day-18/data.txt").read().strip().split("\n")
sum = ""
final_sum = ""
magnitudes = set()
prt1 = list(data)
prt2 = list(itertools.permutations(prt1, 2))

def add(data):
    if " + " in data:
        data = f"[{data.split(' + ')[0]},{data.split(' + ')[1]}]"
    return data

def explode(data):
    offset = 0
    for x in re.findall("\[\d+,\d+\]", data):
        pair = re.search(re.escape(x), data[offset:])
        left_brackets = data[: pair.start() + offset].count("[")
        right_brackets = data[: pair.start() + offset].count("]")
        if left_brackets - right_brackets >= 4:
            x, y = pair.group()[1:-1].split(",")
            left = data[: pair.start() + offset][::-1]
            right = data[pair.end() + offset :]
            look_left = re.search("\d+", left)
            if look_left:
                amt = int(left[look_left.start() : look_left.end()][::-1]) + int(x)
                left = f"{left[:look_left.start()]}{str(amt)[::-1]}{left[look_left.end():]}"
            look_right = re.search("\d+", right)
            if look_right:
                amt = int(right[look_right.start() : look_right.end()]) + int(y)
                right = (f"{right[:look_right.start()]}{amt}{right[look_right.end():]}")
            data = f"{left[::-1]}0{right}"
            break
        else:
            offset = pair.end() + offset
    return data

def split(data):
    dd = re.search("\d\d", data)
    if dd:
        left = data[: dd.start()]
        right = data[dd.end() :]
        left_digit = int(math.floor(int(dd.group()) / 2))
        right_digit = int(math.ceil(int(dd.group()) / 2))
        data = f"{left}[{left_digit},{right_digit}]{right}"
    return data

def reduce(data):
    exploded = explode(data)
    if exploded != data:
        return reduce(exploded)
    else:
        split_data = split(data)
        if split_data != data:
            return reduce(split_data)
        else:
            return split_data

def magnitude(data):
    while data.count(",") > 1:
        for x in re.findall("\[\d+,\d+\]", data):
            pair = re.search(re.escape(x), data)
            left_digit, right_digit = x[1:-1].split(",")
            data = f"{data[: pair.start()]}{int(left_digit) * 3 + int(right_digit) * 2}{data[pair.end() :]}"
    left_digit, right_digit = data[1:-1].split(",")
    return int(left_digit) * 3 + int(right_digit) * 2

# SOLVE FOR PART 1
while prt1:
    line1 = prt1.pop(0)
    if not final_sum:
        line2 = prt1.pop(0)
        final_sum = f"{line1} + {line2}"
    else:
        final_sum = f"{final_sum} + {line1}"
    final_sum = reduce(add(final_sum))
oneAnswer = magnitude(final_sum)
print("Part 1 Answer:", oneAnswer)
# Part 1 Answer: 4323

# SOLVE FOR PART 2
for pair in prt2:
    final_sum = reduce(add(f"{pair[0]} + {pair[1]}"))
    magnitudes.add(magnitude(final_sum))
twoAnswer = max(magnitudes)
print("Part 2 Answer:", twoAnswer)
# Part 2 Answer: 4749
