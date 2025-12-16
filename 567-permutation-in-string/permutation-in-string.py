class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)
        target = Counter(s1)
        window = Counter(s2[:k])
        if window == target:
            return True
        l = 0
        for r in range(k, n):
            window[s2[r]] += 1
            window[s2[r - k]] -= 1
            if window[s2[r - k]] == 0:
                del window[s2[r - k]]
            if window == target:
                return True
        return False