class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        def check(c_per_k):
            served = 0
            for c in candies:
                if c >= c_per_k:
                    served += c // c_per_k
            return served >= k
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans