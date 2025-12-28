class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = {0: 1}
        count = 0
        curr = 0
        for num in nums:
            curr += num
            tar = curr - goal
            if tar in prefix:
                count += prefix[tar]
            prefix[curr] = prefix.get(curr, 0) + 1
        return count