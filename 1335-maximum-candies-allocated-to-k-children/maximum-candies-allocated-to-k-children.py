# class Solution:
#     def maximumCandies(self, candies: List[int], k: int) -> int:
#         l, r = 0, max(candies)
#         def check(max_per_child):
#             count = 0
#             for c in candies:
#                 if c >= max_per_child:
#                     count += c // max_per_child
#             return count >= k
#         while l < r:
#             mid = (l + r) // 2
#             if check(mid):
#                 l = mid
#             else:
#                 r = mid - 1
#         return l

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        def check(max_per_child):
            count = 0
            for c in candies:
                if c >= max_per_child:
                    count += c // max_per_child
            return count >= k
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans