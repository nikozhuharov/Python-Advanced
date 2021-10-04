def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    l = []
    for arg in args:
        f = arg[0]
        t = arg[1]
        l.append(f(*t))
    return l


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))