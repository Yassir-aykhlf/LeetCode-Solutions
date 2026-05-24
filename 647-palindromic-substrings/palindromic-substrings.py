class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def isPal(i, j):
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
            return res
        for i in range(len(s)):
            count += isPal(i, i)
            count += isPal(i, i + 1)
        return count