def palindrome(text, number):

    if number == len(text)//2:
        return f"{text} is a palindrome"
    if text[number] != text[len(text) - 1 - number]:
        return f"{text} is not a palindrome"
    return palindrome(text, number+1)


print(palindrome("abcda", 0))