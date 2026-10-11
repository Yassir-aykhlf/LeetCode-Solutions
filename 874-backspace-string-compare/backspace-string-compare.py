class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(s):
            stack = []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack
        return solve(s) == solve(t)