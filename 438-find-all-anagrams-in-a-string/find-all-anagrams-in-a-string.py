class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l_p = len(p)
        l_s = len(s)
        target = collections.Counter(p)
        window = collections.Counter(s[:l_p])
        res = [0] if target == window else []
        l = 0
        for r in range(l_p, l_s):
            window[s[r]] += 1
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            if window == target:
                res.append(l + 1)
            l += 1
        return res