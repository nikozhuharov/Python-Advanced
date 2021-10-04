n = int(input())
matrix = []
for r in range(n):
    line = input().split()
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "A":
            alice_row, alice_col = r, c


def is_valid(mat, row, col):
    return 0 <= row < len(mat) and 0 <= col < len(mat)


direction = {
    "up": lambda r, c: (r-1, c),
    "down": lambda r, c: (r+1, c),
    "left": lambda r, c: (r, c-1),
    "right": lambda r, c: (r, c+1),
}

current_row = alice_row
current_col = alice_col
total_tea = 0

while True:
    matrix[current_row][current_col] = "*"
    command = input()
    current_row, current_col = direction[command](current_row, current_col)
    if not is_valid(matrix, current_row, current_col):
        print("Alice didn't make it to the tea party.")
        break
    if matrix[current_row][current_col] == "R":
        print("Alice didn't make it to the tea party.")
        matrix[current_row][current_col] = "*"
        break
    if matrix[current_row][current_col].isdigit():
        total_tea += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = "*"
    if total_tea >= 10:
        print("She did it! She went to the party.")
        break

for row in matrix:
    print(" ".join(row))
