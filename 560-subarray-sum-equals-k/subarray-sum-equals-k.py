class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        cur_sum = 0
        count = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            target_sum = cur_sum - k
            if target_sum in prefix:
                count += prefix[target_sum]
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1
        return count