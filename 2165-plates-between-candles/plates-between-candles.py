class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if s[i] == '*' else 0)
        # what we have now: ...
        nearest_left = [-1] * n
        curr = -1
        for i in range(n):
            if s[i] == '|':
                curr = i
            nearest_left[i] = curr
        nearest_right = [-1] * n
        curr = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                curr = i
            nearest_right[i] = curr
        # what we have now: ...
        ans = []
        for s, e in queries:
            L, R = nearest_right[s], nearest_left[e]
            if L != -1 and R != -1 and L < R:
                ans.append(prefix[R] - prefix[L])
            else:
                ans.append(0)
        return ans