class Solution:
    def compress(self, chars: List[str]) -> int:
        r, c = 0, 0
        res = []
        while r < len(chars) and c < len(chars):
            while c < len(chars) and chars[c] == chars[r]:
                c += 1
            res.append(chars[r])
            if c - r:
                res.append(c - r)
            r = c
        ret = []
        for el in res:
            if el == 1:
                continue
            if type(el) == int:
                el = str(el)
                el = list(el)
                ret += el
            else:
                ret += el
        for i in range(len(ret)):
            if i < len(chars):
                chars[i] = ret[i]
        return len(ret)