class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        # n = len(nums)
        # target_index = n - k
        # l = 0
        # r = n - 1
        # while l <= r:
        #     pivot = nums[r]
        #     cursor = l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[cursor], nums[i] = nums[i], nums[cursor]
        #             cursor += 1
        #     nums[cursor], nums[r] = nums[r], nums[cursor]
        #     if cursor == target_index:
        #         return nums[cursor]
        #     elif cursor < target_index:
        #         l = cursor + 1
        #     else:
        #         r = cursor - 1