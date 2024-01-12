#program that check if a word is inside a list

word = input("enter the word: ")
wordList = ["car","snow", "mountain dew", "summer"]

def checkWord(word, list):
    message = ""
    for element in list:
        if(element==word):
            message = "word found"
            break
    
    if(message==""):
        message="word not found!!"

    return message
   



print(checkWord(word, wordList))