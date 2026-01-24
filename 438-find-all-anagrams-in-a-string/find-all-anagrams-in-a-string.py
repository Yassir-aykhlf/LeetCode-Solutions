class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        target = Counter(p)
        window = Counter(s[:p_len])
        res = [0] if target == window else []
        for r in range(p_len, len(s)):
            window[s[r]] += 1
            window[s[r - p_len]] -= 1
            if window[s[r - p_len]] == 0:
                del window[s[r - p_len]]
            if target == window:
                res.append(r - p_len + 1)
        return res