n = int(input())
longest_set = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(x) for x in first_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]
    current_set = set(range(first_start, first_end+1)).intersection(set(range(second_start, second_end+1)))
    if len(current_set) > len(longest_set):
        longest_set = current_set

print(f"Longest intersection is [{', '.join([str(x) for x in longest_set])}] with length {len(longest_set)}")
