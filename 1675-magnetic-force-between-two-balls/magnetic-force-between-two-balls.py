class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        lo, hi = 1, position[-1] - position[0]
        res = hi
        def check(dis):
            placed = 1
            last_pos = position[0]
            for p in position:
                if p - last_pos >= dis:
                    placed += 1
                    last_pos = p
            return placed >= m
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                res= mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res