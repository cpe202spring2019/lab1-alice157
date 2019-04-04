import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Check that max_list_iter works in a 'typical' case"""
        tlist = [5, 6, 0, 1]
        self.assertEqual(max_list_iter(tlist), 6)

    def test_max_list_iter_empty(self):
        """Ensure that max_list_iter returns None for an empty list"""
        tlist = []
        self.assertIsNone(max_list_iter(tlist))

    def test_max_list_iter_exception(self):
        """Ensure that max_list_iter raises an exception on None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        """Ensure that reverse_rec works in a 'typical' case"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_empty(self):
        """Ensures that reverse_rec properly handles empty lists"""
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec_exception(self):
        """Ensure that reverse_rec raises an exception on None"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search(self):
        """Checks that bin_search works on a sorted list"""
        list_val = [0, 1, 2, 3, 4]
        low = 0
        high = len(list_val) - 1
        for i in range(low, high + 1):
            self.assertEqual(bin_search(i, low, high, list_val), i)

    def test_bin_search_fail(self):
        """Ensures that bin_search returns None if the value isn't found"""
        list_val = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertIsNone(bin_search(7, low, high, list_val))

    def test_bin_search_exception(self):
        """Ensures that bin_search raises an exception on None"""
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, list_val)

if __name__ == "__main__":
        unittest.main()
