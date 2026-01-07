class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        las_sig = '+'
        s += '+'
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if las_sig == '+':
                    stack.append(num)
                elif las_sig == '-':
                    stack.append(-num)
                elif las_sig == '*':
                    stack.append(stack.pop() * num)
                elif las_sig == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                las_sig = c
        return sum(stack)