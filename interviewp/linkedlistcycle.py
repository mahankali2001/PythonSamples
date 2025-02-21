# detect a cycle in a linked list.
class node:    
    def __init__(self, value: int):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __init__(self, value=None):
        if value is not None:
            nnode = node(value)
            self.head = nnode
            self.tail = nnode
        else:
            self.head = None
            self.tail = None

class solution:
    def findCycleInLL(self, ll : linkedlist):
        slow = ll.head
        fast = ll.head
        if fast.next == None:
            return False
        
        while(fast != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    s = solution()
    ll = linkedlist(1)
    print(s.findCycleInLL(ll))
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)
    ll.head.next = n2
    n2.next = n3
    n3.next = n4
    print(s.findCycleInLL(ll))
    n4.next = n2
    print(s.findCycleInLL(ll))