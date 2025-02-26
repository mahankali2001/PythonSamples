import unittest
from interviewpb import solution
 
class interviewpbtest(unittest.TestCase):
    def setUp(self):
        self.solution = solution()
    
    def test_ifq(self):
        input = []
        expected_output = {
        }

        result = self.solution.pb1(input)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()