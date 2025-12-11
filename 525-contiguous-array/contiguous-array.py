class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr = 0
        max_len = 0
        prefix = {0: -1}
        for i, num in enumerate(nums):
            curr += 1 if num else -1
            if curr in prefix:
                max_len = max(max_len, i - prefix[curr])
            else:
                prefix[curr] = i
        return max_len