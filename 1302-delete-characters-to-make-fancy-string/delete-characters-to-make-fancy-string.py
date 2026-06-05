class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            count = 0
            while i < len(s) and s[i] == c:
                i += 1
                count += 1
                if count < 3:
                    res.append(c)
        return ''.join(res)