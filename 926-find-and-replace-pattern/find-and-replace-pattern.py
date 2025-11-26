class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isIso(w1, w2):
            if len(w1) != len(w2): return False
            w1_w2 = {}
            w2_w1 = {}
            for c1, c2 in zip(w1, w2):
                if c1 in w1_w2 and w1_w2[c1] != c2:
                    return False
                if c2 in w2_w1 and w2_w1[c2] != c1:
                    return False
                w1_w2[c1] = c2
                w2_w1[c2] = c1
            return True
        return [word for word in words if isIso(word, pattern)]