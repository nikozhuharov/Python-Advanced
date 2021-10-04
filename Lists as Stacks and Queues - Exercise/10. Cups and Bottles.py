from collections import deque
cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
waste = 0

while cups and bottles:
    cup = cups[0]
    bottle = bottles[-1]
    if bottle >= cup:
        waste += bottle-cup
        cups.popleft()
    else:
        cups[0] -= bottle
    bottles.pop()

if bottles:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
if cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
print(f"Wasted litters of water: {waste}")