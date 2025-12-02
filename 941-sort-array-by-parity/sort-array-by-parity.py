class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def isPair(i):
            return 0 if i % 2 == 0 else 1
        return sorted(nums, key=isPair)