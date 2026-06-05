class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_count = max(candies)
        return [c + extraCandies >= max_count for c in candies]