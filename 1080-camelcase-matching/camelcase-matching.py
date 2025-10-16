class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(query):
            index = 0
            for c in query:
                if index < len(pattern) and pattern[index] == c:
                    index += 1
                elif c.isupper():
                    return False
            return index == len(pattern)
        return [isMatch(query) for query in queries]