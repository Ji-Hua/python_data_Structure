import unittest
import random

from algorithm.sort import (bubble_sort,
    selection_sort, insertion_sort)


large_nums = list(range(10000))
random.shuffle(large_nums)
TESTCASES = [
    [1],
    [],
    [1,2,3],
    [2,1,4],
    [6,2,3,4,1,2,3,1,7],
    list(range(20, 0, -1)),
    large_nums,
    [0] * 1000,
    [-1, 1] * 30,
]

class SortTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        with self.assertRaises(ValueError):
            bubble_sort(None)
            bubble_sort('1,2,3')

        for test_case in TESTCASES:
            self.assertEqual(bubble_sort(test_case), sorted(test_case))

    def test_selection_sort(self):
        with self.assertRaises(ValueError):
            selection_sort(None)
            selection_sort('1,2,3')

        for test_case in TESTCASES:
            self.assertEqual(selection_sort(test_case), sorted(test_case))
    
    def test_insertion_sort(self):
        with self.assertRaises(ValueError):
            insertion_sort(None)
            insertion_sort('1,2,3')

        for test_case in TESTCASES:
            self.assertEqual(insertion_sort(test_case), sorted(test_case))

if __name__ == '__main__':
    unittest.main()