class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        target = collections.Counter(p)
        window = collections.Counter(s[:k])
        res = [0] if target == window else []
        for r in range(k, n):
            window[s[r]] += 1
            window[s[r - k]] -= 1
            if window[s[r - k]] == 0:
                del window[s[r - k]]
            if window == target:
                res.append(r - k + 1)
        return res