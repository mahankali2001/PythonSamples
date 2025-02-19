class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        nnode = Node(value)
        if self.head == None: 
            self.head = nnode
            self.tail = nnode
        else:
            self.tail.next = nnode
            self.tail = nnode
        self.length += 1


    def prepend(self, value):
        nnode = Node(value)
        nnode.next = self.head
        self.head = nnode

    # def insert(self, value):

    def print(self):
        temp = self.head
        while temp != None :
            print("{} ->".format(temp.value), end=" ")
            temp = temp.next

myLL = LinkedList(4)
myLL.append(3)
myLL.prepend(5)
myLL.print()