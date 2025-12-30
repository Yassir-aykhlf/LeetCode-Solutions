class Solution:
    def calculate(self, s: str) -> int:
        _s = [c for c in s if c != ' ']
        n = len(_s)
        stack = []
        op = '+'
        num = 0
        for i, c in enumerate(_s):
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-*/" or i == n -1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
        return sum(stack)