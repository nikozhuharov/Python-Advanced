from collections import deque
n = int(input())
queue = deque()
index = -1
current_petrol = 0
completed = False

for i in range(n):
    text = input().split()
    queue.append([int(text[0]), int(text[1])])

while not completed:
    index += 1
    completed = True
    for i in range(len(queue)):
        petrol = queue[i][0]
        distance = queue[i][1]
        current_petrol += petrol
        if distance > current_petrol:
            queue.append(queue.popleft())
            completed = False
            break
        current_petrol -= distance
    current_petrol = 0

print(index)


