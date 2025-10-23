class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(str):
            dq = collections.deque()
            for c in str:
                if c != "#":
                    dq.append(c)
                elif dq:
                    dq.pop()
            return ''.join(dq)
        return build(s) == build(t)