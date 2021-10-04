n = int(input())
matrix = []
knights = []
my_list = []
count = 0
max_count = -1
total_count = 0


def is_valid (matrix, r, c):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


for r in range(n):
    line = input()
    for c in range(len(line)):
        if line[c] == "K":
            knights.append([r, c])
        my_list.append(line[c])
    matrix.append(my_list.copy())
    my_list.clear()

while True:
    max_count = 0
    for i in range(len(knights)):
        count = 0
        row = knights[i][0]
        col = knights[i][1]
        if is_valid(matrix, row - 2, col + 1):
            if matrix[row-2][col+1] == "K":
                count += 1
        if is_valid(matrix, row - 1, col + 2):
            if matrix[row-1][col+2] == "K":
                count += 1
        if is_valid(matrix, row + 1, col + 2):
            if matrix[row+1][col+2] == "K":
                count += 1
        if is_valid(matrix, row + 2, col + 1):
            if matrix[row+2][col+1] == "K":
                count += 1
        if is_valid(matrix, row + 2, col - 1):
            if matrix[row+2][col-1] == "K":
                count += 1
        if is_valid(matrix, row + 1, col - 2):
            if matrix[row+1][col-2] == "K":
                count += 1
        if is_valid(matrix, row - 1, col - 2 ):
            if matrix[row-1][col-2] == "K":
                count += 1
        if is_valid(matrix, row - 2, col - 1):
            if matrix[row-2][col-1] == "K":
                count += 1
        if count > max_count:
            max_count = count
            max_knight = knights[i]
            max_knight_position = i

    if max_count > 0:
        total_count += 1
        remove_row = int(max_knight[0])
        remove_col = int(max_knight[1])
        matrix[remove_row][remove_col] = "0"
        knights.pop(max_knight_position)
    else:
        break

print(total_count)






