class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [i, seen[comp]]
            seen[n] = i
        return []