import unittest
from itemfrequency import solution

class itemfrequencytest(unittest.TestCase):
    def setUp(self):
        self.sol = solution()
    
    def test_itemfrequency(self):
        input = [["apple", "banana", "lemon"], ["banana", "berry", "lemon", "orange"], ["banana", "berry", "lemon"]]
        expected_output = {('apple', 'banana', 'lemon'): 1, ('apple', 'banana'): 1, ('apple', 'lemon'): 1, ('banana', 'lemon'): 3, ('banana', 'berry', 'lemon', 'orange'): 1, ('banana', 'berry'): 2, ('banana', 'orange'): 1, ('berry', 'lemon'): 2, ('berry', 'orange'): 1, ('lemon', 'orange'): 1, ('banana', 'berry', 'lemon'): 2, ('banana', 'berry', 'orange'): 1, ('banana', 'lemon', 'orange'): 1, ('berry', 'lemon', 'orange'): 1}

        result = self.sol.calitemfrequency(input)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()