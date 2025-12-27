class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for r in range(len(s) - 9):
            if s[r : r+10] in seen:
                res.add(s[r:r+10])
            else:
                seen.add(s[r:r+10])
        return list(res)