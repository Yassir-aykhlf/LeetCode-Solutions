class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3:
            return False
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack = stack[:-3]
        return not stack