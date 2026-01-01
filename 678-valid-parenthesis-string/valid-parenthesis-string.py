class Solution:
    def checkValidString(self, s: str) -> bool:
        p_stack = []
        s_stack = []
        for i, c in enumerate(s):
            if c == '(':
                p_stack.append(i)
            elif c == ')':
                if p_stack and s[p_stack[-1]] == '(':
                    p_stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
            elif c == '*':
                s_stack.append(i)
        while p_stack and s_stack:
            if p_stack[-1] > s_stack[-1]:
                return False
            p_stack.pop()
            s_stack.pop()
        return not p_stack