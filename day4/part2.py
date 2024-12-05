with open("day4.txt", "r") as f:
    data = f.read().splitlines()

max_col = len(data[0])
max_row = len(data)

sum = 0

for row in range(0, max_row - 2):
    for col in range(0, max_col - 2):
        diag1 = data[row][col] + data[row + 1][col + 1] + data[row + 2][col + 2]
        diag2 = data[row + 2][col] + data[row + 1][col + 1] + data[row][col + 2]
        sum += (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM")

print(sum)
