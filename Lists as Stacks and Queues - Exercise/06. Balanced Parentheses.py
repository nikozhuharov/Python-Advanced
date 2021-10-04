parentheses = input()
open_parentheses = []
balanced = True

for parenthesis in parentheses:
    if parenthesis in "{[(":
        open_parentheses.append(parenthesis)
    else:
        if open_parentheses:
            if (parenthesis == "}" and open_parentheses[-1] != "{") or \
                (parenthesis == "]" and open_parentheses[-1] != "[") or \
                    (parenthesis == ")" and open_parentheses[-1] != "("):
                balanced = False
                break
            else:
                open_parentheses.pop()
        else:
            balanced = False
            break

if not open_parentheses and balanced:
    print("YES")
else:
    print("NO")


