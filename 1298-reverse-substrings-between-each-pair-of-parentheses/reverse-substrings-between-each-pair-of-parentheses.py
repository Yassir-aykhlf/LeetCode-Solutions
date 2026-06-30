class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = []
        for c in s:
            if c.isalpha():
                curr.append(c)
            elif c == '(':
                stack.append(curr)
                curr = []
            elif c == ')':
                curr.reverse()
                curr = stack.pop() + curr
        return ''.join(curr)