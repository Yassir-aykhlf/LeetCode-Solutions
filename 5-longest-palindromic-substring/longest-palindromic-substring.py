class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(i, j):
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i + 1: j]
        for i in range(len(s)):
            odd = expand(i, i)
            if len(odd) > len(res):
                res = odd
            even = expand(i, i + 1)
            if len(even) > len(res):
                res = even
        return res