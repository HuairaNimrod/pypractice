# A single linked list a list where the element are linked xD
#   Head            Tail
#     a-> b-> c-> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Llist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data) # the new node will have a "value" of data and "next" = None
        if self.head == None:
            self.head = new_node #if the LL is empty the value of the head will be the new node
        else:
            curr_node = self.head #curr = a
            while curr_node.next: # a.next = b 
                curr_node = curr_node.next 
            curr_node.next = new_node  # a.next = b

    def printLinkList(self):
        curr_node =  self.head
        while curr_node:
            print(f"{curr_node.value} ->", end =" ")
            curr_node = curr_node.next
        print("None")

   
   

    def printLinkListBackward(self):
        self.printBackward(self.head) 
        print("None")

    def printBackward(self, node):
        if node is None:
            return
        self.printBackward(node.next)
        print(node.value, end =" -> ")


            

# Instance of class LList

LinkedList = Llist()

#append items to the list
LinkedList.append("a")
LinkedList.append("b")
LinkedList.append("c")

#print linked list
LinkedList.printLinkList()

#print linked list
LinkedList.printLinkListBackward()


