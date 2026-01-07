class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = 1
        res = 0
        num = 0
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                if c == '+':
                    res += num * sign
                    sign = 1
                    num = 0
                elif c == '-':
                    res += num * sign
                    sign = -1
                    num = 0
                elif c == '(':
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif c == ')':
                    res += num * sign
                    num = 0
                    pre_sig = stack.pop()
                    pre_res = stack.pop()
                    res = pre_res + res * pre_sig
        return res + num * sign