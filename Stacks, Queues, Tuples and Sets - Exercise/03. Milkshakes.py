from collections import deque
chocolates = [int(x) for x in input().split(", ")]
milks = deque([int(x) for x in input().split(", ")])
count = 0

while count < 5 and milks and chocolates:
    chocolate = chocolates.pop()
    milk = milks.popleft()
    if chocolate < 1 and milk < 1:
        continue
    if chocolate < 1 or milk < 1:
        if chocolate < 1:
            milks.appendleft(milk)
            continue
        else:
            chocolates.append(chocolate)
            continue
    if chocolate == milk:
        count += 1
    else:
        chocolate -= 5
        chocolates.append(chocolate)
        milks.append(milk)

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if milks:
    print(f"Milk: {', '.join([str(x) for x in milks])}")
else:
    print("Milk: empty")
