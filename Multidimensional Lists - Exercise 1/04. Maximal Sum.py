rows, cols = [int(x) for x in input().split()]
matrix = []
max_sum = -1000000

for r in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows-2):
    for c in range(cols-2):
        if matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] +\
                matrix[r+1][c] + matrix[r+1][c + 1] + matrix[r+1][c + 2] +\
                matrix[r+2][c] + matrix[r+2][c + 1] + matrix[r+2][c + 2] > max_sum:
            max_sum = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] +\
                    matrix[r+1][c] + matrix[r+1][c + 1] + matrix[r+1][c + 2] +\
                    matrix[r+2][c] + matrix[r+2][c + 1] + matrix[r+2][c + 2]
            max_r = r
            max_c = c

print(f"Sum = {max_sum}")
for r in range(max_r, max_r+3):
    for c in range(max_c, max_c+3):
        print(matrix[r][c], end=" ")
    print()

