class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        chars = list(pattern)
        if len(chars) != len(words):
            return False
        w_c = {}
        c_w = {}
        for c, w in zip(chars, words):
            if (c in c_w and c_w[c] != w) or (w in w_c and w_c[w] != c):
                return False
            w_c[w] = c
            c_w[c] = w
        return True