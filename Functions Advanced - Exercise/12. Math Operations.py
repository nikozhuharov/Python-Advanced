from collections import deque


def math_operations(*args, **kwargs):
    finished = False
    queue = deque(args)
    while True:
        for key, value in kwargs.items():
            if queue:
                if key == "a":
                    kwargs[key] += queue.popleft()
                elif key == "s":
                    kwargs[key] -= queue.popleft()
                elif key == "d":
                    de = queue.popleft()
                    if de == 0:
                        continue
                    kwargs[key] /= de
                elif key == "m":
                    kwargs[key] *= queue.popleft()
            else:
                finished = True
                break
        if finished:
            break
    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
