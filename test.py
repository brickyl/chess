import unittest
# import expecttest
from board import Board

class Testing(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(1, 1)
    
    def test_bool(self):
        self.assertTrue(True)

    # def test_expect(self):
    #     self.assertExpectedInline(print(), "")

if __name__ == '__main__':
    unittest.main()