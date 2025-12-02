class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        cur_sum = 0
        count = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            prev_slice = cur_sum - k
            if prev_slice in prefix:
                count += prefix[prev_slice]
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1
        return count