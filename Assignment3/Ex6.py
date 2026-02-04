def middle_character(text):
    length = len(text)

    if length % 2 == 0:
        return text[length // 2 - 1] + text[length // 2]
    else:
        return text[length // 2]
word = input("Enter a word: ")
print(middle_character(word))
