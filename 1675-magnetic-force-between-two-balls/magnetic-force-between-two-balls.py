class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(dis):
            balls_placed = 1
            last_p = position[0]
            for p in position[1:]:
                if p - last_p >= dis:
                    balls_placed += 1
                    last_p = p
            return balls_placed >= m
        position.sort()
        lo, hi = 1, position[-1]
        ans = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans