class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if stack and stack[-3:] == ['a', 'b', 'c']:
                stack = stack[:-3]
        return not stack