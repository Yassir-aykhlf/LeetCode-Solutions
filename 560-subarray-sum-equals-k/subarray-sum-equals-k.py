class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0:1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            tar_sum = cur_sum - k
            if tar_sum in prefix_sums:
                count += prefix_sums[tar_sum]
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        return count