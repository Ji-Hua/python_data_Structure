import unittest
import random

from algorithm.sort import (bubble_sort, selection_sort,
    insertion_sort, shell_sort, merge_sort, merge_sort_iteration,
    quick_sort)


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
    [0] * 100,
    [-1, 1] * 100,
]

class SortTestCase(unittest.TestCase):
    def test_bubble_sort(self):
        self._test_sort(bubble_sort)

    def test_selection_sort(self):
        self._test_sort(selection_sort)

    def test_insertion_sort(self):
        self._test_sort(insertion_sort)

    def test_shell_sort(self):
        self._test_sort(shell_sort)

    def test_merge_sort(self):
        self._test_sort(merge_sort)
    
    def test_merge_sort_iteration(self):
        self._test_sort(merge_sort_iteration)
    
    def test_quick_sort(self):
        self._test_sort(quick_sort)

    def _test_sort(self, sort_func):
        with self.assertRaises(ValueError):
            sort_func(None)
            sort_func('1,2,3')

        for test_case in TESTCASES:
            self.assertEqual(sort_func(test_case), sorted(test_case))

if __name__ == '__main__':
    unittest.main()