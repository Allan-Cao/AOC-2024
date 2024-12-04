with open("day2.txt", "r") as f:
    data = f.read().splitlines()


def is_safe(line: list[int]) -> bool:
    prev = line[0]
    # Division by zero
    if line[1] == prev:
        return False
    sign = (line[1] - prev) / abs(line[1] - prev)
    for i in line[1:]:
        if abs(prev - i) > 3 or prev == i or (prev + abs(prev - i) * sign) != i:
            return False
        prev = i
    return True


def try_dampener(line: list[int]) -> bool:
    for i in range(len(line)):
        new_line = line.copy()
        new_line.pop(i)
        if is_safe(new_line):
            return True
    return False


safe = 0
for row in data:
    row = list(map(int, row.split()))
    if is_safe(row):
        safe += 1
    else:
        safe += try_dampener(row)

print(safe)
