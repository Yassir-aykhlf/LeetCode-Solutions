class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(dist):
            placed = 1
            last_p = position[0]
            for p in position:
                if p - last_p >= dist:
                    placed += 1
                    last_p = p
            return placed >= m
        lo, hi = 1, position[-1] - position[0]
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans