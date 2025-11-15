class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(q):
            index = 0
            for c in q:
                if index < len(pattern) and c == pattern[index]:
                    index += 1
                elif c.isupper():
                    return False
            return index == len(pattern)
        return[isMatch(q) for q in queries]