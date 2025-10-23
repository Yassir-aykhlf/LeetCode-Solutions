class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]
        # target = len(nums) - k
        # def quickSelect(l, r):
        #     pivot = nums[r]
        #     i = l
        #     for j in range(l, r):
        #         if nums[j] <= pivot:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #     nums[i], nums[r] = nums[r], nums[i]
        #     if i == target:
        #         return nums[i]
        #     elif i < target:
        #         return quickSelect(i + 1, r)
        #     else:
        #         return quickSelect(l, i - 1)
        # return quickSelect(0, len(nums) - 1)