numbers = [int(x) for x in input().split()]


def calc(args):
    sum_negative = 0
    sum_positive =0
    for arg in args:
        if arg > 0:
            sum_positive += arg
        elif arg < 0:
            sum_negative += arg
    print(sum_negative)
    print(sum_positive)
    if abs(sum_negative) > abs(sum_positive):
        print('The negatives are stronger than the positives')
    elif abs(sum_positive) > abs(sum_negative):
        print('The positives are stronger than the negatives')


calc(numbers)
