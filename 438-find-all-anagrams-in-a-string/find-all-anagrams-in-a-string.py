class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        target = collections.Counter(p)
        len_p = len(p)
        len_s = len(s)
        window_s = s[:len_p]
        window = collections.Counter(window_s)
        if window == target:
            res.append(0)
        for r in range(len_p, len_s):
            window[s[r]] += 1
            window[s[r - len_p]] -= 1
            if window[s[r - len_p]] == 0:
                del window[s[r - len_p]]
            if window == target:
                res.append(r - len_p + 1)
        return res