class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isIso(word, pattern):
            if len(word) != len(pattern):
                return False
            w_p = {}
            p_w = {}
            for p, w in zip(pattern, word):
                if (p in p_w and p_w[p] != w) or (w in w_p and w_p[w] != p):
                    return False
                w_p[w] = p
                p_w[p] = w
            return True
        return [word for word in words if isIso(word, pattern)]