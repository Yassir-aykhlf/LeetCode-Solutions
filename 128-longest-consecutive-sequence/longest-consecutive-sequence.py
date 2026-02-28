class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ = set(nums)
        res = 0
        for n in nums_:
            if n - 1 not in nums_:
                curr = 1
                while n + curr in nums_:
                    curr += 1
                res = max(res, curr)
        return res