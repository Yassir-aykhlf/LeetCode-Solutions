import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        # l, r = 0, len(nums) - 1
        # target_idx = len(nums) - k
        # while l <= r:
        #     pivot_idx = random.randint(l, r)
        #     nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx] 
        #     pivot = nums[r]
        #     cursor = l
        #     for i in range(l, r):
        #         if nums[i] < pivot:
        #             nums[cursor], nums[i] = nums[i], nums[cursor]
        #             cursor += 1
        #     nums[cursor], nums[r] = nums[r], nums[cursor]
        #     if cursor == target_idx:
        #         return nums[cursor]
        #     elif cursor < target_idx:
        #         l = cursor + 1
        #     else:
        #         r = cursor - 1
        # return -1