import unittest
from linkedlistcyclictest import linkedlistcyclictest

def suite():
    suite1 = unittest.TestSuite()
    suite1.addTest(linkedlistcyclictest('test_llc1'))
    suite1.addTest(linkedlistcyclictest('test_llc2'))
    suite1.addTest(linkedlistcyclictest('test_llc3'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())