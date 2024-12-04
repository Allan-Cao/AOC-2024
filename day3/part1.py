import re

with open("day3.txt", "r") as f:
    data = f.read().splitlines()

pattern = r"mul\((\d+),(\d+)\)"


sum = 0
for row in data:
    match = re.findall(
        pattern,
        row,
    )
    for mul in match:
        sum += int(mul[0]) * int(mul[1])

print(sum)
