"""class LinkedList:
    Root = None  

    class Element:        
        Next = None
        Prev = None
        Value = None


class Fifo(LinkedList):
    Last = None
    #Insert a new element on top of the stack
    def Insert(self,value):
        elem = LinkedList.Element 
        elem.Value = value
        if LinkedList.Root != None:
            elem.Next = LinkedList.Root
            LinkedList.Root.Prev = elem
        LinkedList.Root = elem
        if LinkedList.Root.Next == None:
            self.Last = LinkedList.Root
    
    #Removing the first element put in the list
    def RemoveFirst(self):
        if self.Last != None:
            value = self.Last.Value
            self.Last = self.Last.Prev
            if self.Last != None:
                self.Last.Next = None
            else:
                LinkedList.Root = None
            return value
        else:
            return None




class Lifo(LinkedList):
    pass

mylist = [1,2,3,4,5,6,7,8,9,10]
list_fifo = Fifo()
for x in range(len(mylist)):
    list_fifo.Insert(mylist[x])

while list_fifo.Last != None:
    print(list_fifo.RemoveFirst())"""


#Creating the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
#Creating the Doubly linked list
class Double_Linked_List:
    def __init__(self):
        self.head = None

    #Define the push method to add elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    #Define the method for printing the linked list
    def listprint(self,node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

mylist = Double_Linked_List()
list = [1,2,3,4,5,6,7,8,9,10]
for x in range(len(list)):
    mylist.push(list[x])

mylist.listprint(mylist.head)