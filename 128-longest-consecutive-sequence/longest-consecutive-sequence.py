class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        res = 0
        for num in nums_s:
            if num - 1 not in nums_s:
                count = 1
                while num + count in nums_s:
                    count += 1
                res = max(res, count)
        return res