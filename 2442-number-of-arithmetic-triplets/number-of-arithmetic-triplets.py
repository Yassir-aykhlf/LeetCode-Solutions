class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_ = set(nums)
        count = 0
        for n in nums:
            if n + diff in nums_ and n + diff * 2 in nums_:
                count += 1
        return count