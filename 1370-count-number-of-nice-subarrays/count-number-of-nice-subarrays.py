class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: 1}
        curr = 0
        count = 0
        for i, num in enumerate(nums):
            curr += 1 if num % 2 == 1 else 0
            target = curr - k
            if target in prefix_sum:
                count += prefix_sum[target]
            prefix_sum[curr] = prefix_sum.get(curr, 0) + 1
        return count