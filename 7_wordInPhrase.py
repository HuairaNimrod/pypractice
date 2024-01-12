# find a word in a phrase

word = input("enter the word to be finded: ")
phrase = "El Peru es libre e independiente por la voluntad general de los pueblos y por la causa que Dios defiende"

def wordLists(phrase):
    words = phrase.split()
    return words

wordsFromList = wordLists(phrase)


if word in wordsFromList:
    print(f"The word '{word}' is present in the phrase")
else:
    print("The word is not present in the phrase :( ")



