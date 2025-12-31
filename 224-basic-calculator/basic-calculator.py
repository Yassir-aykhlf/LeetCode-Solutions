class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        res = 0
        sign = 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+' or c == '-':
                res += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                num = 0
                sign = 1
            elif c == ')':
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign