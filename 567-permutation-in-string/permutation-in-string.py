class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = collections.Counter(s1)
        k = len(s1)
        window = s2[:k]
        window_state = collections.Counter(window)
        if window_state == pattern:
            return True
        for r in range(k, len(s2)):
            window_state[s2[r]] += 1
            window_state[s2[r - k]] -= 1
            if window_state[s2[r - k]] == 0:
                del window_state[s2[r - k]]
            if window_state == pattern:
                return True
        return False