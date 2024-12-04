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


print(sum([is_safe(list(map(int, row.split()))) for row in data]))
