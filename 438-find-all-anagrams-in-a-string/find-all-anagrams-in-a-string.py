class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        ref = Counter(p)
        window = Counter(s[:k])
        res = [0] if window == ref else []
        l = 0
        for r in range(k, n):
            window[s[r]] += 1
            window[s[r - k]] -= 1
            if window[s[r - k]] == 0:
                del window[s[r - k]]
            if window == ref:
                res.append(r - k + 1)
        return res