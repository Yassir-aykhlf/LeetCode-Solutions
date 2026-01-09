class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            while stack and stack[-3:] == ['a', 'b', 'c']:
                stack = stack[:-3]
        return not stack