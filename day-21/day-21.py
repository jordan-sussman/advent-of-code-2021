import functools
import itertools

data = open("day-21/data.txt").read().strip().split("\n")

# PART 1
player1, player2 = int(data[0][-1]), int(data[1][-1])
start1 = start2 = 0
die = rolls = 0
while True:
    die = die % 100 + 1
    if die % 2:  # PLAYER 1
        player1 += sum([die, die + 1, die + 2])
        start1 += player1 % 10 if player1 % 10 else 10
    else:  # PLAYER 2
        player2 += sum([die, die + 1, die + 2])
        start2 += player2 % 10 if player2 % 10 else 10
    die += 2
    rolls += 3
    if start1 >= 1000 or start2 >= 1000:
        break
    # PART 1 ANSWER
    prt1 = min(start1, start2) * rolls

# PART 2
player1, player2 = int(data[0][-1]), int(data[1][-1])
start1 = start2 = 0
@functools.lru_cache(maxsize=None)
def play_out(player1, start1, player2, start2):
    win1 = win2 = 0
    for move1, move2, move3 in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3)):
        player1_copy = (player1 + move1 + move2 + move3) % 10 if (player1 + move1 + move2 + move3) % 10 else 10
        start1_copy = start1 + player1_copy
        if start1_copy >= 21:
            win1 += 1
        else:
            win2_copy, win1_copy = play_out(player2, start2, player1_copy, start1_copy)
            win1 += win1_copy
            win2 += win2_copy
    return win1, win2
# PART 2 ANSWER
prt2 = max(play_out(player1,start1,player2,start2))

print("Part 1 Answer:", prt1)
# Part 1 Answer: 503478
print("Part 2 Answer:", prt2)
# Part 2 Answer: 716241959649754
