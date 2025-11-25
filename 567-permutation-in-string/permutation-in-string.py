class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        window = collections.Counter(s2[:len(s1)])
        if target == window:
            return True
        k = len(s1)
        n = len(s2)
        for r in range(k, n):
            window[s2[r]] += 1
            window[s2[r - k]] -= 1
            if window[s2[r - k]] == 0:
                del window[s2[r - k]]
            if window == target:
                return True
        return False