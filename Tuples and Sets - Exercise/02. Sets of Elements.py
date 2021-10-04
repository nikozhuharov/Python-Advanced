n, m = [int(x) for x in input().split()]
first = set()
second = set()
for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))

inter = first.intersection(second)

for el in inter:
    print(el)
