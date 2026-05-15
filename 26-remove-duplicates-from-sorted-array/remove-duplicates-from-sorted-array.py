class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_ = sorted(list(set(nums)))
        for i in range(len(nums_)):
            nums[i] = nums_[i]
        return len(nums_)