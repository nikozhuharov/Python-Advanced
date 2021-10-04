from collections import deque

line = deque(input().split())
numbers = deque()
result = int(line.popleft())

while line:
    if line[0] not in "+-/*":
        numbers.append(int(line[0]))
        line.popleft()
    else:
        sign = line.popleft()
        if sign == "+":
            for num in numbers:
                result += num
        elif sign == "-":
            for num in numbers:
                result -= num
        elif sign == "/":
            for num in numbers:
                result //= num
        elif sign == "*":
            for num in numbers:
                result *= num
        numbers.clear()

print(result)