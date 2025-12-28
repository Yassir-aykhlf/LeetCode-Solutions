class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        opening = set("({[")
        closing = set(")}]")
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in opening:
                stack.append(c)
            elif stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0