class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_sign = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if last_sign == '+':
                    stack.append(num)
                if last_sign == '-':
                    stack.append(-num)
                elif last_sign == '*':
                    stack.append(stack.pop() * num)
                elif last_sign == '/':
                    stack.append(int(stack.pop() / num))
                last_sign = c
                num = 0
        return sum(stack)