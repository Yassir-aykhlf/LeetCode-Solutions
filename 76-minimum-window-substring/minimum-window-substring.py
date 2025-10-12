class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        we put a target counter, a dict window, and when all chars are in target are satisfied we keep shrinking to find an even smaller solution
        """
        k = len(t)
        n = len(s)
        target = collections.Counter(t)
        window = collections.defaultdict(int)
        full_chars, miss_chars = 0, len(target)
        min_len = float('inf')
        result = ""
        l = 0
        for r in range(n):
            window[s[r]] += 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                full_chars += 1
            while full_chars == miss_chars:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    result = s[l:r+1]
                if s[l] in target and window[s[l]] == target[s[l]]:
                    full_chars -= 1
                window[s[l]] -= 1
                l += 1
        return result