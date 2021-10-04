n = int(input())
elements = set()
for _ in range(n):
    line = set(input().split())
    elements.update(line)

[print(el) for el in elements]