from collections import deque
green_duration1 = int(input())
free_window_duration1 = int(input())
cars = deque()
command = input()
count = 0
is_crash = False
while command != "END":
    if command == "green":
        green_duration = green_duration1
        free_window_duration = free_window_duration1
        while green_duration > 0 and cars:
            if len(cars[0]) <= green_duration + free_window_duration:
                car = cars.popleft()
                count += 1
                if len(car) <= green_duration:
                    green_duration -= len(car)
                else:
                    green_duration = 0
                    free_window_duration -= len(car)-green_duration
            else:
                print("A crash happened!")
                print(f"{cars[0]} was hit at {cars[0][green_duration+free_window_duration]}.")
                is_crash = True
                break
        if is_crash:
            break
    else:
        cars.append(command)
    command = input()

if not is_crash:
    print("Everyone is safe.")
    print(f"{count} total cars passed the crossroads.")