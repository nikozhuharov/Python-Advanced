file = open("text.txt", "r+")
i= 0
for line in file:
    if i % 2 == 0:
        new_line = ""
        for el in line:
            if el != '\n':
                if el in "-,.!?":
                    el = "@"
                new_line += el
        list_line = new_line.split(" ")
        list_line.reverse()
        print(" ".join(list_line))
    i += 1
