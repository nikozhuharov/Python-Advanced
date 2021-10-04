first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + " " + line[1]
    if command == "Add First":
        [first.add(int(x)) for x in line[2:]]
    elif command == "Add Second":
        [second.add(int(x)) for x in line[2:]]
    elif command == "Remove First":
        current_set = set([int(x) for x in line[2:]])
        first.difference_update(current_set)
    elif command == "Remove Second":
        current_set = set([int(x) for x in line[2:]])
        second.difference_update(current_set)
    elif command == "Check Subset":
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

print(", ".join([str(x) for x in sorted(first)]))
print(", ".join([str(x) for x in sorted(second)]))