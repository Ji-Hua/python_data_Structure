from typing import Union


class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        text = [str(s) for s in self.stack]
        return f"[{', '.join(text)}]"

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Problem1
# check if parentheses match
def check_parentheses(text:str) -> bool:
    """Check if the (), [], {} match in the text

        Input:
            text: text with parentheses

        Return:
            boolean, True if match, otherwise False
    """
    left_pars = ['(', '[', '{']
    matches = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for t in text:
        if t in left_pars:
            stack.push(t)
        elif t in matches:
            if stack.is_empty():
                return False
            left = stack.pop()
            if left != matches[t]:
                return False

    if not stack.is_empty():
        return False

    return True


# Problem2
# change 10-based numbers to certain base
def base_convert(number:int, base:int=2) -> str:
    """Convert 10-based numbers to certain base

        Input:
            number: int, number to convert base 10
            base: int, base to use, default is 2

        Return:
            new number of the base in string format
    """
    if not isinstance(number, int):
        raise ValueError(f"Invalid input number {number}")
    
    if not isinstance(base, int):
        raise ValueError(f"Invalid input base {base}")

    stack = Stack()
    quotient, remainder = number, 0
    while quotient != 0:
        remainder = quotient % base
        quotient = quotient // base
        stack.push(remainder)
    
    if stack.is_empty():
        return '0'
    
    text = ''
    while not stack.is_empty():
        text += str(stack.pop())
    return text


# Problem3
# change inorder expression to postorder expression
def inorder_to_postorder(expression:str) -> str:
    """Convert change inorder expression to postorder expression

        Input:
            expression: string, inorder expression

        Return:
            postorder expression
    """
    if not isinstance(expression, str):
        raise ValueError(f"Invalid input expression {expression}")
    
    priority = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
        ')': 1
    }

    tokens = expression.split(' ')
    stack, results = Stack(), []

    for token in tokens:
        if token not in priority:
            results.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while stack.peek() != '(':
                results.append(stack.pop())
            # postorder doesn't need (), so pop here to discard
            stack.pop()
        else:
            while (not stack.is_empty()) and \
                priority[stack.peek()] >= priority[token]:
                results.append(stack.pop())
            stack.push(token)
    
    while not stack.is_empty():
        results.append(stack.pop())
    
    return ' '.join(results)


# Problem4
# calculate postorder expression
def calculate_postorder(expression:str) -> Union[float, int]:
    """Calculate postorder expression

        Input:
            expression: string, postorder expression

        Return:
            expression result
    """
    if not isinstance(expression, str):
        raise ValueError(f"Invalid input expression {expression}")
    
    tokens = expression.split(' ')
    stack = Stack()

    def calc(op1, op2, op):
        op1 = float(op1)
        op2 = float(op2)
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op1 / op2

    for token in tokens:
        if token not in ('+', '-', '*', '/'):
            stack.push(token)
        else:
            # first in last out
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(calc(op1, op2, token))

    return stack.pop()
