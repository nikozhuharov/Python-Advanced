n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n+1):
    name = input()
    sum_name = 0
    for letter in name:
        sum_name += ord(letter)
    number = sum_name // i
    if number % 2 == 0:
        even_set.add(number)
    else:
        odd_set.add(number)

if sum(odd_set) == sum(even_set):
    final_set = odd_set.intersection(even_set)
elif sum(odd_set) > sum(even_set):
    final_set = odd_set.difference(even_set)
else:
    final_set = odd_set.symmetric_difference(even_set)

print(", ".join([str(x) for x in final_set]))


