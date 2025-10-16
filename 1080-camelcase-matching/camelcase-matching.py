class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(query):
            idx = 0
            for c in query:
                if idx < len(pattern) and c == pattern[idx]:
                    idx += 1
                elif c.isupper():
                    return False
            return len(pattern) == idx
        return [isMatch(query) for query in queries]