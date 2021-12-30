import re
import numpy as np
from itertools import repeat
from typing import Tuple

with open("day-17/data.txt", "rt") as file:
    text_regex = re.compile(r"x=(-*\d+)\.\.(-*\d+), y=(-*\d+)\.\.(-*\d+)")
    raw_text = file.read()
    coordinates = text_regex.search(raw_text).groups()
    x_min, x_max, y_min, y_max = (int(coord) for coord in coordinates)

def collision(x, y, x1=x_min, x2=x_max, y1=y_min, y2=y_max) -> bool:
    within_x = (x >= x1) and (x <= x2)
    within_y = (y >= y1) and (y <= y2)

    if within_x and within_y: 
        return True
    else: 
        return False

def trajectory(x_speed, y_speed, x=0, y=0, x_max=x_max, y_min=y_min) -> Tuple[Tuple[int,int]]:
    x_coord = [x]
    y_coord = [y]

    while x <= x_max and y >= y_min:
        x += x_speed
        y += y_speed
        x_coord += [x]
        y_coord += [y]
        x_speed = max(0, x_speed-1)
        y_speed -= 1 
    return (x_coord, y_coord)

def check(x_speed, y_speed, x=0, y=0, x1=x_min, x2=x_max, y1=y_min, y2=y_max) -> bool:
    x_path, y_path = trajectory(x_speed, y_speed, x, y, x2, y1)

    target = any(
        map(
            collision,
            x_path,
            y_path,
            repeat(x1),
            repeat(x2),
            repeat(y1),
            repeat(y2)
        )
    )
    
    if target:
        return (x_speed, y_speed)
    else:
        return None

x_range = np.arange(0, 250)
y_range = np.arange(-250, 250)
x_mesh, y_mesh = np.meshgrid(x_range, y_range)
launch_tests = map(check, x_mesh.ravel(), y_mesh.ravel())
successes = [hit for hit in launch_tests if hit]
max_x_speed, max_y_speed = max(successes, key = lambda f: f[1])
x_path, y_path = trajectory(max_x_speed, max_y_speed)

prt1 = max(y_path)
prt2 = len(successes)

print("Part 1 Answer:", prt1)
# Part 1 Answer: 17766
print("Part 2 Answer:", prt2)
# Part 2 1733
