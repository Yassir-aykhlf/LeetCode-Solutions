class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        last_sign = '+'
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if last_sign == '+':
                    stack.append(num)
                elif last_sign == '-':
                    stack.append(-num)
                elif last_sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                last_sign = c
                num = 0
        return sum(stack)