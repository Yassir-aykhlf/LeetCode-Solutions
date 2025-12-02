class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isIso(word):
            if len(word) != len(pattern):
                return False
            w_t = {}
            t_w = {}
            for w, t in zip(word, pattern):
                if w in w_t and w_t[w] != t:
                    return False
                if t in t_w and t_w[t] != w:
                    return False
                w_t[w] = t
                t_w[t] = w
            return True
        return [word for word in words if isIso(word)]