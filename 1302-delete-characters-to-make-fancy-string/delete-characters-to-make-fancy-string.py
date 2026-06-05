class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        count = 0
        for i, c in enumerate(s):
            if i > 0 and s[i - 1] == c:
                count += 1
            else:
                count = 1
            if count < 3:
                res.append(c)
        return ''.join(res)