from collections import deque


def fill_the_box(*args):
    queue = deque(args)
    total = 0
    bulk = queue.popleft()*queue.popleft()*queue.popleft()
    for num in queue:
        if num == "Finish":
            break
        total += num
    if total > bulk:
        return f"No more free space! You have {total-bulk} more cubes."
    elif bulk > total:
        return f"There is free space in the box. You could put {bulk-total} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))