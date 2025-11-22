class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # target_idx = n - k
        # def partition(l, r):
        #     pivot = nums[r]
        #     i = l
        #     for cur in range(l, r + 1):
        #         if nums[cur] < pivot:
        #             nums[i], nums[cur] = nums[cur], nums[i]
        #             i += 1
        #     nums[i], nums[r] = nums[r], nums[i]
        #     if i == target_idx:
        #         return nums[i]
        #     elif i < target_idx:
        #         return partition(i + 1, r)
        #     else:
        #         return partition(l, i - 1)
        # return partition(0, n - 1)
        return heapq.nlargest(k, nums)[-1]