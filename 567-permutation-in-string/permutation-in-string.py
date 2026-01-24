class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        target = Counter(s1)
        window = Counter(s2[:s1_len])
        if window == target:
            return True
        for r in range(s1_len, len(s2)):
            window[s2[r]] += 1
            window[s2[r - s1_len]] -= 1
            if window[s2[r - s1_len]] == 0:
                del window[s2[r - s1_len]]
            if window == target:
                return True
        return False