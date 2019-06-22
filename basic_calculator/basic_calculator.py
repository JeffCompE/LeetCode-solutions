from collections import deque
from typing import Tuple

class Solution:

    @staticmethod
    def read(exp: str, index: int) -> Tuple[str, int, bool]:
        while index < len(exp) and exp[index] == ' ':
            index += 1
        if index == len(exp):
            return '', -1, False
        if exp[index].isdigit():
            nums = deque()
            while index < len(exp) and exp[index].isdigit():
                nums.append(exp[index])
                index += 1
            return ''.join(nums), index, True
        else:
            return exp[index], index + 1, False

    @classmethod
    def infix_to_postfix(cls, exp: str) -> List[str]:
        """Convert an infix expression to a postfix expression
        """
        stack = deque()  # priority of symbols in stack is monotone increasing
        postfix_exp = []
        index = 0
        while index < len(exp):
            symbol, index, isdigit = cls.read(exp, index)
            if symbol == '':
                break
            if isdigit:
                postfix_exp.append(symbol)
            else:
                if symbol == ')':
                    while stack and stack[-1] != '(':
                        postfix_exp.append(stack.pop())
                    stack.pop()
                elif symbol == '(':
                    stack.append(symbol)
                else:
                    while stack and stack[-1] != '(':
                        postfix_exp.append(stack.pop())
                    stack.append(symbol)
        while stack:
            postfix_exp.append(stack.pop())
        return postfix_exp

    @staticmethod
    def evaluate_postfix(exp: List[str]) -> int:
        """Evaluate the given postfix expression
        """
        stack = deque()
        for symbol in exp:
            if symbol.isdigit():
                stack.append(int(symbol))
            else:
                if symbol == '+':
                    num_2 = stack.pop()
                    num_1 = stack.pop()
                    stack.append(num_1 + num_2)
                else:  # symbol is '-'
                    num_2 = stack.pop()
                    num_1 = stack.pop()
                    stack.append(num_1 - num_2)
        return stack.pop()

    def calculate(self, s: str) -> int:
        return self.evaluate_postfix(self.infix_to_postfix(s))
