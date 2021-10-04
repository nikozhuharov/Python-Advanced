clothes = [int(x) for x in input().split()]
capacity = int(input())
count = 1
current_capacity = capacity

while clothes:
    cloth = clothes[-1]
    if current_capacity < cloth:
        count += 1
        current_capacity = capacity
    else:
        clothes.pop()
        current_capacity -= cloth

print(count)




