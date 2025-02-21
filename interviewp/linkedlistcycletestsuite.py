import unittest
from linkedlistcycletest import linkedlistcycletest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(linkedlistcycletest('test_llc1'))
    suite.addTest(linkedlistcycletest('test_llc2'))
    suite.addTest(linkedlistcycletest('test_llc3'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())