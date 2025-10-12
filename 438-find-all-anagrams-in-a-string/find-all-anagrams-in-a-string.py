class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        k = len(p)
        window = s[:k]
        window_state = collections.Counter(window)
        result = []
        if window_state == target:
            result.append(0)
        for r in range(k, len(s)):
            window_state[s[r]] += 1
            window_state[s[r - k]] -= 1
            if window_state[s[r - k]] == 0:
                del window_state[s[r - k]]
            if window_state == target:
                result.append(r - k + 1)
        return result