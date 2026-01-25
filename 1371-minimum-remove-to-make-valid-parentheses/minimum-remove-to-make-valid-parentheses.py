class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c.isalpha():
                continue
            if c == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        remove = set(stack)
        return ''.join(c for i, c in enumerate(s) if i not in remove)