import math

data = bin(int('1'+open("day-16/data.txt").read(),16))[3:]

def prt1(startbit):
    x = startbit
    tv = int(data[x:x+3],2)
    ID = int(data[x+3:x+6],2)
    x += 6
    if ID == 4:
        while True:
            x += 5
            if data[x-5] == '0':
                break
    else:
        if data[x] == '0':
            endx = x + 16 + int(data[x+1:x+16],2)
            x += 16
            while x < endx:
                x,v = prt1(x)
                tv += v
        else:
            np = int(data[x+1:x+12],2)
            x += 12
            for _ in range(np):
                x,v = prt1(x)
                tv += v
    return x,tv

op = [sum, math.prod, min, max,
      lambda ls: ls[0],
      lambda ls: 1 if ls[0] > ls[1] else 0,
      lambda ls: 1 if ls[0] < ls[1] else 0,
      lambda ls: 1 if ls[0] == ls[1] else 0]


def prt2(startbit):
    x = startbit
    ID = int(data[x+3:x+6],2)
    x += 6
    if ID == 4:
        vals = [0]
        while True:
            vals[0] = 16*vals[0] + int(data[x+1:x+5],2)
            x += 5
            if data[x-5] == '0':
                break
    else:
        vals = []
        if data[x] == '0':
            endi = x + 16 + int(data[x+1:x+16],2)
            x += 16
            while x < endi:
                x,v = prt2(x)
                vals.append(v)
        else:
            np = int(data[x+1:x+12],2)
            x += 12
            for _ in range(np):
                x,v = prt2(x)
                vals.append(v)
    return x,op[ID](vals)

print("Part 1 Answer:", prt1(0)[1])
# Part 1 Answer: 847
print("Part 2 Answer:", prt2(0)[1])
# Part 2 Answer: 333794664059
