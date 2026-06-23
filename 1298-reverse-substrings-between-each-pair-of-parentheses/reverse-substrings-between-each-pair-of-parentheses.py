class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        last_start_stack = []
        res = list(s)
        for i, c in enumerate(s):
            if c == '(':
                last_start_stack.append(i)
            elif c.isalpha():
                pass
            else:
                start = last_start_stack.pop()
                res[start : i] = res[i: start: -1]
        return ''.join(c for c in res if c != '(' and c != ')')