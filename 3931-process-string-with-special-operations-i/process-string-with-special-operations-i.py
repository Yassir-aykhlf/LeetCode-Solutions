class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c.isalnum():
                res.append(c)
            elif c == '#':
                res += res
            elif c == '*':
                if res:
                    res.pop()
            elif c == '%':
                res = res[::-1]
        return ''.join(res)