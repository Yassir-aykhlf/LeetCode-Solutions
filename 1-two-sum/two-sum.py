class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in pairs:
                return [i, pairs[comp]]
            pairs[num] = i
        return []