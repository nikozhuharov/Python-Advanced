from collections import deque
robots = []


def time_to_second(time):
    t = time.split(":")
    seconds = int(t[0]) * 3600 + int(t[1])*60 + int(t[2])
    return seconds


def seconds_to_time(seconds):
    if seconds >= 24*60*60:
        seconds %= 24*60*60
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds - h*3600 - m*60
    return f"{h:02d}:{m:02d}:{s:02d}"


class Robot():
    def __init__(self, robot_name, robot_time):
        self.name = robot_name
        self.time = int(robot_time)
        self.finish = 0


text = input().split(";")
for t in text:
    robot_name, robot_time = t.split("-")
    robots.append(Robot(robot_name, robot_time))

start_time = input()
seconds = time_to_second(start_time)
products = deque()
count = 0

command = input()
while command != "End":
    products.append(command)
    command = input()


while products:

    seconds += 1
    product = products.popleft()
    taken = False

    for robot in robots:
        if robot.finish == 0 and not taken:
            robot.finish = robot.time - 1
            print(f"{robot.name} - {product} [{seconds_to_time(seconds)}]")
            taken = True
        elif robot.finish != 0:
            robot.finish -= 1
    if not taken:
        products.append(product)






