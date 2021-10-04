n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])


def is_valid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


while True:
    command = input()
    arg = command.split()
    if arg[0] == "END":
        break
    row = int(arg[1])
    col = int(arg[2])
    value = int(arg[3])
    if is_valid(matrix, row, col):
        if arg[0] == "Add":
            matrix[row][col] += value
        if arg[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for r in matrix:
    print(" ".join([str(x) for x in r]))
