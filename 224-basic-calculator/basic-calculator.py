class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+' or c == '-':
                res += num * sign
                sign = 1 if c == '+' else -1
                num = 0
            elif c == ')':
                res += num * sign
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + (prev_sign * res)
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
        return res + num * sign