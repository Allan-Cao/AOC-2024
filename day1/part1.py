with open("day1.txt", "r") as f:
    data = f.read().splitlines()
l1 = [int(_.split()[0]) for _ in data]
l2 = [int(_.split()[1]) for _ in data]

l1.sort()
l2.sort()

sum = 0
for i, j in zip(l1, l2):
    sum += abs(j - i)
print(sum)
