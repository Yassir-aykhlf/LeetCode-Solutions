class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cur = 0
        prefix_sum = {0:1}
        count = 0
        for num in nums:
            cur += num
            tar = cur - goal
            if tar in prefix_sum:
                count += prefix_sum[tar]
            prefix_sum[cur] = prefix_sum.get(cur, 0) + 1
        return count