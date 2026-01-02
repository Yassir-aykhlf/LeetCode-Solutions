class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                print(stack[-3:])
                del stack[-3:]
        return not stack