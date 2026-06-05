class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n = len(words)
        ans = float("+inf")
        for i in range(n):
            if words[i] == target:
                direct_dist = abs(i - startIndex)
                wrap_dist = abs(n - direct_dist)
                ans = min(ans, direct_dist, wrap_dist)
        return ans if ans != float("-inf") else -1