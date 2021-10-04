rows, cols = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == "END":
        break
    com_arg = command.split()
    if com_arg[0] != "swap" or len(com_arg) != 5:
        print("Invalid input!")
        continue
    if not(0 <= int(com_arg[1]) < rows and 0 <= int(com_arg[2]) < cols and 0 <= int(com_arg[3]) < rows and 0 <= int(com_arg[4]) < cols):
        print("Invalid input!")
        continue
    matrix[int(com_arg[1])][int(com_arg[2])], matrix[int(com_arg[3])][int(com_arg[4])] = matrix[int(com_arg[3])][int(com_arg[4])], matrix[int(com_arg[1])][int(com_arg[2])]
    for r in range(rows):
        print(" ".join(matrix[r]))

