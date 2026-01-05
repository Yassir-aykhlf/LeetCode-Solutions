class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0: -1}
        max_len = 0
        cur = 0
        for r in range(len(nums)):
            cur += 1 if nums[r] == 1 else -1
            if cur in prefix:
                max_len = max(max_len, r - prefix[cur])
            else:
                prefix[cur] = r
        return max_len