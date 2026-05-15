class Solution:
    def reverseVowels(self, s_: str) -> str:
        vows = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s_)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in vows and s[j] in vows:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
                continue
            if s[i] not in vows:
                i += 1
            if s[j] not in vows:
                j -= 1
        return ''.join(s)