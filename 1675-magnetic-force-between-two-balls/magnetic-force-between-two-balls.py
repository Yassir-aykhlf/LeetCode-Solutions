class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def canPlace(force):
            count = 1
            last_pos = position[0]
            for i in range(1, len(position)):
                if position[i] - last_pos >= force:
                    count += 1
                    last_pos = position[i]
                    if count == m:
                        return True
            return False
        lo, hi = 1, position[-1] - position[0]
        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if canPlace(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans