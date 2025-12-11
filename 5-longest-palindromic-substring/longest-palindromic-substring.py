class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        def isPal(i, j):
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i+1:j]
        for i in range(len(s)):
            odd = isPal(i, i)
            if len(odd) > len(longest):
                longest = odd
            even = isPal(i, i + 1)
            if len(even) > len(longest):
                longest = even
        return longest