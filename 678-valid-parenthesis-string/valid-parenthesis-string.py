class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        s_stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
            elif c == '*':
                s_stack.append(i)
        while stack and s_stack:
            if stack[-1] < s_stack[-1]:
                stack.pop()
                s_stack.pop()
            else:
                return False
        return not stack