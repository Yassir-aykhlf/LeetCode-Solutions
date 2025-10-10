class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        k, n = len(s1), len(s2)
        state = collections.Counter(s2[:k])
        if state == target:
            return True
        l = 0
        for r in range(k, n):
            state[s2[r]] += 1
            state[s2[l]] -= 1
            if state[s2[l]] == 0:
                del state[s2[l]]
            l += 1
            if state == target:
                return True
        return False