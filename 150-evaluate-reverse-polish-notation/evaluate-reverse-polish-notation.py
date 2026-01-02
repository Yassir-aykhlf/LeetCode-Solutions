class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # LIFO temp register
        for t in tokens:
            if t in "+-/*":
                if t == '+':
                    stack.append(stack.pop() + stack.pop())
                elif t == '-':
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                elif t == '*':
                    stack.append(stack.pop() * stack.pop())
                elif t == '/':
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]