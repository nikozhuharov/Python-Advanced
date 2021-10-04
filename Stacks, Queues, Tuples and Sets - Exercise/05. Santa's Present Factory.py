from collections import deque
materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
toys = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0,
}

while materials and magics:
    total_magic = materials[-1] * magics[0]
    if total_magic == 150:
        toys["Doll"] += 1
        materials.pop()
        magics.popleft()
    elif total_magic == 250:
        toys["Wooden train"] += 1
        materials.pop()
        magics.popleft()
    elif total_magic == 300:
        toys["Teddy bear"] += 1
        materials.pop()
        magics.popleft()
    elif total_magic == 400:
        toys["Bicycle"] += 1
        materials.pop()
        magics.popleft()
    elif total_magic < 0:
        total = materials.pop() + magics.popleft()
        materials.append(total)
    elif total_magic > 0:
        magics.popleft()
        materials[-1] += 15
    elif total_magic == 0:
        if materials[-1] == 0:
            materials.pop()
        if magics[0] == 0:
            magics.popleft()

if (toys["Doll"] > 0 and toys["Wooden train"] > 0) or (toys["Teddy bear"] > 0 and toys["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials.reverse()
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")

for key, value in toys.items():
    if value > 0:
        print(f"{key}: {value}")
