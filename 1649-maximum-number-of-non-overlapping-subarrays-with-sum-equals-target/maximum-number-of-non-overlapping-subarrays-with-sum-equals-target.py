class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        count = 0
        curr_sum = 0
        sum_to_index = {0: -1}
        for i, num in enumerate(nums):
            curr_sum += num
            prev_sum = curr_sum - target
            if prev_sum in sum_to_index:
                count += 1
                sum_to_index = {}
            sum_to_index[curr_sum] = i
        return count