class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += num
            comp = cur_sum - k
            count += prefix_sums.get(comp, 0)
            prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
        return count 