with open("day4.txt", "r") as f:
    data = f.read().splitlines()

# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
max_col = len(data[0])
max_row = len(data)
cols = [[] for _ in range(max_col)]
rows = [[] for _ in range(max_row)]
fdiag = [[] for _ in range(max_row + max_col - 1)]
bdiag = [[] for _ in range(len(fdiag))]
min_bdiag = -max_row + 1

for x in range(max_col):
    for y in range(max_row):
        cols[x].append(data[y][x])
        rows[y].append(data[y][x])
        fdiag[x + y].append(data[y][x])
        bdiag[x - y - min_bdiag].append(data[y][x])

test_values = []
test_values.extend(rows)
test_values.extend(cols)
test_values.extend(fdiag)
test_values.extend(bdiag)

sum = 0
for row in test_values:
    sum += "".join(row).count("XMAS")
    sum += "".join(row).count("SAMX")

print(sum)
