class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        k = len(s1)
        ref = Counter(s1)
        window = Counter(s2[:k])
        if window == ref:
            return True
        for r in range(k, len(s2)):
            window[s2[r]] += 1
            window[s2[r - k]] -= 1
            if window[s2[r - k]] == 0:
                del window[s2[r - k]]
            if window == ref:
                return True
        return False