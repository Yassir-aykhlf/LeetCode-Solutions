class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for c in t:
            if index < len(s) and c == s[index]:
                index += 1
        return index == len(s)