class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        rep = set()
        for i in range(len(s) - 9):
            if s[i:i+10] in seen:
                rep.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return list(rep)