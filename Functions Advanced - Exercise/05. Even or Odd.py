def even_odd(*args):
    stack = list(args)
    command = stack.pop()
    parity = 0 if command == "even" else 1
    result = list(filter(lambda x: x % 2 == parity, [int(x) for x in stack]))
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "odd"))