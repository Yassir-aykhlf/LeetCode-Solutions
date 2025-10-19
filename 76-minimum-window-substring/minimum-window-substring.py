class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target = collections.Counter(t)
        window = collections.defaultdict(int)
        have = 0
        need = len(target)
        min_len = float('inf')
        result = (0, 0)
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    min_len = r -l + 1
                    result = (l, r + 1)
                if s[l] in target and window[s[l]] == target[s[l]]:
                    have -= 1
                window[s[l]] -= 1
                l += 1
        return s[result[0]: result[1]] if min_len != float('inf') else ""