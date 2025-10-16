class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k - 1]
        # n = len(nums)
        # target_index = n - k
        # def quickSelect(l, r):
        #     pivot = nums[r]
        #     i = l
        #     for j in range(l, r):
        #         if nums[j] < pivot:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #     nums[i], nums[r] = nums[r], nums[i]
        #     if i == target_index:
        #         return nums[i]
        #     elif i < target_index:
        #         return quickSelect(i + 1, r)
        #     else:
        #         return quickSelect(l, i - 1)
        # return quickSelect(0, n - 1)