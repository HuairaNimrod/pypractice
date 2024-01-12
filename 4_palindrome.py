# guess if a word is palindrome

word = input("enter word to verify: ")


def invertWord(word):
    back = ""
    for letter in word:
        back = letter + back

    return(back)

inverted = invertWord(word)
print(f"inverted word: {inverted}")

if(inverted == word):
    print("It's a palindrome!!")
else:
    print("It is NOT a palindrome")