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
        if fast == None or fast.next == None:
            return False
        
        while(fast != None):
            try:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            except AttributeError:
                break
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

    # Additional test cases
    # Test case with a single node pointing to itself
    ll_single_cycle = linkedlist(1)
    ll_single_cycle.head.next = ll_single_cycle.head
    print(s.findCycleInLL(ll_single_cycle))  # Should return True

    # Test case with multiple nodes and no cycle
    ll_no_cycle = linkedlist(1)
    n2 = node(2)
    n3 = node(3)
    ll_no_cycle.head.next = n2
    n2.next = n3
    print(s.findCycleInLL(ll_no_cycle))  # Should return False

    # Test case with an empty linked list
    ll_empty = linkedlist()
    print(s.findCycleInLL(ll_empty))  # Should return False