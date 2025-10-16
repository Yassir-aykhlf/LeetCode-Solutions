class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target =collections.Counter(p)
        k = len(p)
        n = len(s)
        window = collections.Counter(s[:k])
        result = []
        if window == target:
            result.append(0)
        for r in range(k, n):
            window[s[r]] += 1
            window[s[r - k]] -= 1
            if window[s[r - k]] == 0:
                del window[s[r - k]]
            if window == target:
                result.append(r - k + 1)
        return result