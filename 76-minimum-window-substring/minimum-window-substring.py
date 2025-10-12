class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = collections.Counter(t)
        window = collections.Counter()
        min_len = float('inf')
        required = len(target)
        formed = 0
        ans = (0, 0)
        l = 0
        for r, char in enumerate(s):
            window[char] += 1
            if char in target and window[char] == target[char]:
                formed += 1

            while formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = (l, r + 1)
                if s[l] in target and window[s[l]] == target[s[l]]:
                    formed -= 1
                window[s[l]] -= 1
                l += 1
        return s[ans[0]:ans[1]] if min_len != float('inf') else ""