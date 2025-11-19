class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            subtract_target = cur_sum - k
            if subtract_target in prefix_sum:
                count += prefix_sum[subtract_target]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        return count