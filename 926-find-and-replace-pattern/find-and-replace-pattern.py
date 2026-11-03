class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        res = []
        for w in words:
            w_p = {}
            p_w = {}
            for wc, pc in zip(w, pattern):
                if  wc in w_p and w_p[wc] != pc \
                    or pc in p_w and p_w[pc] != wc:
                        break
                w_p[wc] = pc
                p_w[pc] = wc
            else:
                res.append(w)
        return res