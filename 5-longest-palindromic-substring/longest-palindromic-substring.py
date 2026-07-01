class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            a, b = i, i
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            if len(s[a+1:b]) > len(res):
                res = s[a+1:b]
            a, b = i, i + 1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            if len(s[a+1:b]) > len(res):
                res = s[a+1:b]
        return res