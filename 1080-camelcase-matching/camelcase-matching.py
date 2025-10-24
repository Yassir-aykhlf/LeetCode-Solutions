class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(q):
            idx = 0
            for c in q:
                if idx < len(pattern) and pattern[idx] == c:
                    idx += 1
                elif c.isupper():
                    return False
            return idx == len(pattern)
        return [isMatch(q) for q in queries]