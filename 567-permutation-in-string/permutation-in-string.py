class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        window_str = s2[:k]
        target = collections.Counter(s1)
        window = collections.Counter(window_str)
        if window == target:
            return True
        for r in range(k, n):
            window[s2[r]] += 1
            window[s2[r - k]] -= 1
            if window[s2[r - k]] == 0:
                del window[s2[r - k]]
            if window == target:
                return True
        return False