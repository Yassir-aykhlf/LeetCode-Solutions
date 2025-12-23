class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set("aeiouAEIOU")
        l, r = 0, len(s) - 1
        res = [0] * len(s)
        while l <= r:
            if s[l] in v and s[r] in v:
                res[r] = s[l]
                res[l] = s[r]
                r -= 1
                l += 1
            elif s[l] in v:
                res[r] = s[r]
                r -= 1
            elif s[r] in v:
                res[l] = s[l]
                l += 1
            else:
                res[l] = s[l]
                res[r] = s[r]
                r -= 1
                l += 1
        return ''.join(res)