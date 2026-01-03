class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "-+*/":
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                prev_op = c
        return sum(stack)