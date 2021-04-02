import unittest
from algorithm.stack import (Stack, check_parentheses, base_convert,
    inorder_to_postorder, calculate_postorder)

CHECK_PARENTHESES_TEST_CASES = [
    ('', True),
    ('()', True),
    ('[]', True),
    ('{}', True),
    ('{[()]}', True),
    ('{{}}', True),
    ('()()', True),
    ('{[}]', False),
    ('({[}])', False),
    ('{{{{{}}{}}{}}}', True),
    ('}{}{', False),
    ('(){[]}', True),
    ('()()(', False),
    ('(((((', False),
    ('({[', False),
    ('(', False),
    ('{', False),
    ('[', False),
    (')', False),
    ('}', False),
    (']', False),

]

BASE_CONVERT_TEST_CASES = [
    ((10, 2), '1010'),
    ((1, 2), '1'),
    ((2, 2), '10'),
    ((5, 2), '101'),
    ((0, 3), '0'),
    ((3, 3), '10'),
    ((100, 3), '10201'),
    ((127, 4), '1333')
]

INORDER_TO_POSTORDER_TEST_CASES = [
    ('1 + 2 * 3 + 4', '1 2 3 * + 4 +'),
    ('1 - 2 * 3 + 11', '1 2 3 * - 11 +'),
    ('( 1 + 2 ) * 3 + 4', '1 2 + 3 * 4 +'),
    ('( 1 + 2 ) * ( 3 + 4 )', '1 2 + 3 4 + *'),
    ('1 + 2 + 3 + 4', '1 2 + 3 + 4 +'),
    ('( ( ( 1 + 2 ) + 3 ) * 4 ) * 5', '1 2 + 3 + 4 * 5 *'),
    ('( ( ( 10 * 2 ) - 3 ) / 4 ) * 125', '10 2 * 3 - 4 / 125 *')
]

CALCULATE_POSTORDER_TEST_CASES = [
    ('1 2 3 * + 4 +', 11),
    ('1 2 3 * - 11 +', 6),
    ('1 2 + 3 * 4 +', 13),
    ('1 2 + 3 4 + *', 21),
    ('1 2 + 3 + 4 +', 10),
    ('1 2 + 3 + 4 * 5 *', 120),
    ('10 2 * 3 - 4 / 125 *', 531.25)
]


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack(self):
        # stack should be empty
        self.assertTrue(self.stack.is_empty())

        # stack should raise error
        with self.assertRaises(ValueError):
            self.stack.peek()
            self.stack.pop()

        # push elements
        self.stack.push(4)
        self.stack.push('dog')
        self.assertEqual(self.stack.peek(), 'dog')
        self.assertFalse(self.stack.is_empty())

        # pop elements
        val = self.stack.pop()
        self.assertEqual(val, 'dog')
        self.assertEqual(self.stack.peek(), 4)
        self.assertEqual(self.stack.size(), 1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.pop(), 4)
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

        with self.assertRaises(ValueError):
            self.stack.peek()
            self.stack.pop()
    
    def test_check_parentheses(self):
        for test_case in CHECK_PARENTHESES_TEST_CASES:
            self.assertEqual(check_parentheses(test_case[0]), test_case[1])

    def test_base_convert(self):
        for test_case in BASE_CONVERT_TEST_CASES:
            self.assertEqual(base_convert(*test_case[0]), test_case[1])
    
    def test_inorder_to_postorder(self):
        for test_case in INORDER_TO_POSTORDER_TEST_CASES:
            self.assertEqual(inorder_to_postorder(test_case[0]), test_case[1])
    
    def test_calculate_postorder(self):
        for test_case in CALCULATE_POSTORDER_TEST_CASES:
            self.assertEqual(calculate_postorder(test_case[0]), test_case[1])

if __name__ == '__main__':
    unittest.main()