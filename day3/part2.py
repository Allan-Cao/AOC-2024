import re

with open("day3.txt", "r") as f:
    data = f.read().splitlines()

pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

sum = 0
current = 1
for row in data:
    match = re.finditer(
        pattern,
        row,
    )
    for mul in match:
        command = mul.group(0)
        if command == "do()":
            current = 1
        elif command == "don't()":
            current = 0
        else:
            sum += int(mul.group(1)) * int(mul.group(2)) * current

print(sum)
