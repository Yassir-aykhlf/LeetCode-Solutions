class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_p = len(p)
        pattern = collections.Counter(p)
        state = collections.Counter(s[:len_p])
        res = []
        if pattern == state:
            res += [0]
        for r in range(len_p, len(s)):
            state[s[r]] += 1
            state[s[r - len_p]] -= 1
            if state[s[r - len_p]] == 0:
                del state[s[r - len_p]]
            if state == pattern:
                res.append(r - len_p + 1)
        return res