stack = input().split()
reversed_stack = []

for i in range(len(stack)):
    reversed_stack.append(stack.pop())

print(" ".join(reversed_stack))