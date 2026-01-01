class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c != '(' and c != ')':
                continue
            if c == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    continue
            stack.append(i)
        unmatched = set(stack)
        return ''.join([c for i, c in enumerate(s) if i not in unmatched])