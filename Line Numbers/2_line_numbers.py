file = open("text.txt", "r")
file2 = open("output.txt", "w")
lines_count = 0
punctuation_marks = [".", "?", "!", ",", ";", "'", "-", ":", "(", ")", "[", "]", "{", "}", '"', "..."]

for line in file:
    line = line[:-1]
    letters_count = 0
    punctuations_count = 0
    lines_count += 1
    for ch in line:
        if 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            letters_count += 1
        elif ch in punctuation_marks:
            punctuations_count += 1
    final_line = f"Line {lines_count} " + line + f" ({letters_count})({punctuations_count})\n"
    file2.writelines(final_line)

file.close()
file2.close()
