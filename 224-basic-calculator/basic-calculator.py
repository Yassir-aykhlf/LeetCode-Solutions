class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num = 0
        sign = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == ')':
                res += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + res * prev_sign
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
        return res + num * sign