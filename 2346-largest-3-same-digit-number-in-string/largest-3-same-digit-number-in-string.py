class Solution:
    def largestGoodInteger(self, s: str) -> str:
        state = defaultdict(int)
        l = 0
        res = -1
        for r in range(len(s)):
            state[s[r]] += 1
            if len(state) > 1 or state[s[r]] > 3:
                state[s[l]] -= 1
                if state[s[l]] == 0:
                    del state[s[l]]
                l += 1
            if state[s[r]] == 3:
                res = max(res, int(s[r] * 3))
        if res == -1: return ""
        if res == 0: return "000"
        return str(res)