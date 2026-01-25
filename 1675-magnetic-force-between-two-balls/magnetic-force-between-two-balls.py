class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(dist):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= dist:
                    count += 1
                    last_position = position[i]
            return count >= m
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