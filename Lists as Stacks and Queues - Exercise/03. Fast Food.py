from collections import deque
food = int(input())
is_completed = True
queue = deque([int(x) for x in input().split()])

print(max(queue))

while queue:
    order = queue[0]
    if food - order >= 0:
        food -= order
        queue.popleft()
    else:
        is_completed = False
        break

if is_completed:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, queue))}")

