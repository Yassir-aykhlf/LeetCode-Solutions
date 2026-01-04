class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0: -1}
        max_len = 0
        curr = 0
        for r in range(len(nums)):
            curr += 1 if nums[r] == 1 else -1
            if curr in prefix:
                max_len = max(max_len, r - prefix[curr])
            else:
                prefix[curr] = r
        return max_len