line = input().split('|')

for el in range(len(line)-1, -1, -1):
    [print(x, end=" ") for x in line[el].split()]
