class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = []
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = []
            elif c == ')':
                curr.reverse()
                curr = stack.pop() + curr
            else:
                curr.append(c)
        return ''.join(curr)