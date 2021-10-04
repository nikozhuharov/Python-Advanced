text = input()

count = {}
for t in text:
    if t in count:
        count[t] += 1
    else:
        count[t] = 1

for key, value in sorted(count.items()):
    print(f"{key}: {value} time/s")