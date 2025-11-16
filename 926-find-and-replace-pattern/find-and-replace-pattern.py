class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isIsomorphic(word):
            if len(word) != len(pattern):
                return False
            w_p = {}
            p_w = {}
            for w, p in zip(word, pattern):
                if w in w_p and w_p[w] != p:
                    return False
                if p in p_w and p_w[p] != w:
                    return False
                w_p[w] = p
                p_w[p] = w
            return True
        return [word for word in words if isIsomorphic(word)]