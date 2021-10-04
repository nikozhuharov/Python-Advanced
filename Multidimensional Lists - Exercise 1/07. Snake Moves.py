n, m = [int(x) for x in input().split()]
text = input()
count = 0
matrix = []
for r in range(n):
    matrix.append([None]*m)

for r in range(n):
    if r % 2 == 0:
        for c in range(m):
            matrix[r][c] = text[count % len(text)]
            count += 1
    else:
        for c in range(m-1, -1, -1):
            matrix[r][c] = text[count % len(text)]
            count += 1

for r in range(n):
    print("".join(str(x) for x in matrix[r]))

