class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sums = {0: -1}
        max_len = 0
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += 1 if num == 1 else -1
            if cur_sum in prefix_sums:
                max_len = max(max_len, i - prefix_sums[cur_sum])
            else:
                prefix_sums[cur_sum] = i
        return max_len