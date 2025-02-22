import unittest
from linkedlist import solution, node, linkedlist



class linkedlistcyclictest(unittest.TestCase):
    def setUp(self):
        self.solution = solution()
	    
    def test_llc1(self):
        ll = linkedlist(1)
        expected_output = False
        self.assertEqual(self.solution.findCycleInLL(ll), expected_output)

    def test_llc2(self):
        ll = linkedlist(1)
        n2 = node(2)
        n3 = node(3)
        n4 = node(4)
        ll.head.next = n2
        n2.next = n3
        n3.next = n4
        expected_output = False
        self.assertEqual(self.solution.findCycleInLL(ll), expected_output)
    
    def test_llc3(self):
        ll = linkedlist(1)
        n2 = node(2)
        n3 = node(3)
        n4 = node(4)
        ll.head.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n2
        expected_output = True
        self.assertEqual(self.solution.findCycleInLL(ll), expected_output)

if __name__ == "__main__":
    # unittest.main()
    unittest.main(argv=['first-arg-is-ignored', '-k', 'test_llc1'])
