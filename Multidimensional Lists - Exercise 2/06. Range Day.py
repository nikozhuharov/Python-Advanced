matrix = []
hit_positions = []
targets = 0
hit_targets = 0
for r in range(5):
    line = input().split()
    matrix.append(line)
    for c in range(5):
        if line[c] == "A":
            current_row, current_col = r, c
        if line[c] == "x":
            targets += 1

n = int(input())


def is_valid(mat, row, col):
    return 0 <= row < len(mat) and 0 <= col < len(mat)


direction_dict = {
    "up": lambda r, c, s: (r-s, c),
    "down": lambda r, c, s: (r+s, c),
    "left": lambda r, c, s: (r, c-s),
    "right": lambda r, c, s: (r, c+s),
}

for _ in range(n):
    command = input().split()
    if command[0] == "move":
        direction = command[1]
        steps = int(command[2])
        next_row, next_col = direction_dict[direction](current_row, current_col, steps)
        if is_valid(matrix, next_row, next_col) and matrix[next_row][next_col] == ".":
            current_row, current_col = next_row, next_col
    elif command[0] == "shoot":
        direction = command[1]
        bullet_row, bullet_col = current_row, current_col
        while True:
            next_bullet_row, next_bullet_col = direction_dict[direction](bullet_row, bullet_col, 1)
            if is_valid(matrix, next_bullet_row, next_bullet_col):
                bullet_row, bullet_col = next_bullet_row, next_bullet_col
                if matrix[bullet_row][bullet_col] == "x":
                    hit_targets += 1
                    matrix[bullet_row][bullet_col] = "."
                    hit_positions.append([bullet_row, bullet_col])
                    break
            else:
                break

if hit_targets == targets:
    print(f"Training completed! All {targets} targets hit.")
else:
    print(f"Training not completed! {targets - hit_targets} targets left.")
for position in hit_positions:
    print(position)


