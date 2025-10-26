class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        res = []
        window_str = s[:k]
        target = collections.Counter(p)
        window = collections.Counter(window_str)
        if target == window:
            res.append(0)
        for r in range(k, n):
            window[s[r]] += 1
            window[s[r - k]] -= 1
            if window[s[r - k]] == 0:
                del window[s[r - k]]
            if window == target:
                res.append(r - k + 1)
        return res