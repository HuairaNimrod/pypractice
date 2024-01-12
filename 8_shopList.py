#shop list

shoppingList = []

def showMenu():
    print("--------------------------------")
    print("a. Show List")
    print("b. Add element")
    print("c. Delete element")
    print("d. Exit")
    option = input("enter option: ")
    return option

def showList():
    print(shoppingList)

def addElement():
    element = input('enter the item to add: ')
    shoppingList.append(element)

def deleteElement():
    element = input('enter the item to delete: ')
    shoppingList.remove(element)

def main():
    
    option= "e"
    while(option!="d"):
        option = showMenu()
        if (option== "a"):
            showList()
        elif (option== "b"):
            addElement()
        elif (option== "c"):
            deleteElement()


        


main()

