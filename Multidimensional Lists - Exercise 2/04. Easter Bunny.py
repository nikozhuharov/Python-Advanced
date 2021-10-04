n = int(input())
matrix = []
for r in range(n):
    line = input().split()
    matrix.append(line)
    for c in range(len(line)):
        if line[c] == "B":
            bunny_row, bunny_col = r, c


def is_valid(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


max_eggs = float('-inf')
i = 1
path_up = []
total_eggs_up = 0
while True:
    current_row = bunny_row - i
    current_col = bunny_col
    if is_valid(matrix, current_row, current_col):
        if matrix[current_row][current_col] == "X":
            break
        else:
            total_eggs_up += int(matrix[current_row][current_col])
            path_up.append([current_row, current_col])
    else:
        break
    i += 1

max_eggs = float('-inf')
i = 1
path_down = []
total_eggs_down = 0
while True:
    current_row = bunny_row + i
    current_col = bunny_col
    if is_valid(matrix, current_row, current_col):
        if matrix[current_row][current_col] == "X":
            break
        else:
            total_eggs_down += int(matrix[current_row][current_col])
            path_down.append([current_row, current_col])
    else:
        break
    i += 1

max_eggs = float('-inf')
i = 1
path_right = []
total_eggs_right = 0
while True:
    current_row = bunny_row
    current_col = bunny_col + i
    if is_valid(matrix, current_row, current_col):
        if matrix[current_row][current_col] == "X":
            break
        else:
            total_eggs_right += int(matrix[current_row][current_col])
            path_right.append([current_row, current_col])
    else:
        break
    i += 1

max_eggs = float('-inf')
i = 1
path_left = []
total_eggs_left = 0
while True:
    current_row = bunny_row
    current_col = bunny_col - i
    if is_valid(matrix, current_row, current_col):
        if matrix[current_row][current_col] == "X":
            break
        else:
            total_eggs_left += int(matrix[current_row][current_col])
            path_left.append([current_row, current_col])
    else:
        break
    i += 1

most_eggs = max(total_eggs_up, total_eggs_down, total_eggs_left, total_eggs_right)
if most_eggs == total_eggs_up:
    print("up")
    [print(x) for x in path_up]
    print(total_eggs_up)
if most_eggs == total_eggs_down:
    print("down")
    [print(x) for x in path_down]
    print(total_eggs_down)
if most_eggs == total_eggs_left:
    print("left")
    [print(x) for x in path_left]
    print(total_eggs_left)
if most_eggs == total_eggs_right:
    print("right")
    [print(x) for x in path_right]
    print(total_eggs_right)