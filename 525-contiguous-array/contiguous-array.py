class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        # when was the last position we have seen a sum equal to the current sum
        # cuz that means everything in between sums to zero
        sum_to_pos = {0: -1}
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += 1 if num == 1 else -1
            if curr_sum in sum_to_pos:
                max_len = max(max_len, i - sum_to_pos[curr_sum])
            else:
                sum_to_pos[curr_sum] = i
        return max_len