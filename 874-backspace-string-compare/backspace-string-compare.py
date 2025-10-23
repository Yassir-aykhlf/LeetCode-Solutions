class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(str):
            stack = []
            for c in str:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return build(s) == build(t)