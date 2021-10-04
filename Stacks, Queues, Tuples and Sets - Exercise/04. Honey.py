from collections import deque
bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())
total = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if bee <= nectar:
        symbol = symbols.popleft()
        if symbol == "+":
            total += abs(bee + nectar)
        elif symbol == "-":
            total += abs(bee - nectar)
        elif symbol == "*":
            total += abs(bee * nectar)
        elif symbol == "/":
            if nectar > 0:
                total += abs(bee / nectar)
    else:
        bees.appendleft(bee)

print(f"Total honey made: {total}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")


