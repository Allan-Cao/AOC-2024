from collections import Counter

with open("day1.txt", "r") as f:
    data = f.read().splitlines()
l1 = [int(_.split()[0]) for _ in data]
l2 = [int(_.split()[1]) for _ in data]

l1 = set(l1)
l2_counts = Counter(l2)

sum = 0
for i in l1:
    sum += i * l2_counts[i]
print(sum)
